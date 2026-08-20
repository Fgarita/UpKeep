# -*- coding: utf-8 -*-
"""
Event bus: connects the logic (which runs on a separate thread) with
the GUI (which lives on Qt's main thread).
"""

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication

from qfluentwidgets import InfoBar, InfoBarPosition

from core.i18n import t


class LogBus(QObject):
    line = Signal(str)
    task_started = Signal(str)          # task title
    task_finished = Signal(str, bool)   # title, success
    all_finished = Signal()

    def __init__(self):
        super().__init__()
        self.history = []

    def log(self, text: str):
        for row in str(text).splitlines() or [""]:
            self.history.append(row)
        self.line.emit(str(text))


BUS = LogBus()


class TaskWorker(QObject):
    """Runs a list of tasks, one at a time, on a separate thread."""

    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks

    def run(self):
        for task in self.tasks:
            BUS.task_started.emit(task.title)
            BUS.log(f"\n>> {task.title}")
            success = True
            try:
                task.function(BUS.log)
            except Exception as e:
                success = False
                BUS.log(t("worker.error", title=task.title, error=e))
            BUS.task_finished.emit(task.title, success)
        BUS.all_finished.emit()


class Runner(QObject):
    """Single entry point for launching tasks without blocking the GUI."""

    busy_changed = Signal(bool)

    def __init__(self):
        super().__init__()
        self._thread = None
        self._worker = None
        self.busy = False

    def run(self, tasks):
        if self.busy:
            InfoBar.warning(
                t("infobar.busy.title"),
                t("infobar.busy.content"),
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=QApplication.activeWindow(),
            )
            return

        self.busy = True
        self.busy_changed.emit(True)

        self._thread = QThread()
        self._worker = TaskWorker(tasks)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        BUS.all_finished.connect(self._on_finished)
        self._thread.start()

    def _on_finished(self):
        self.busy = False
        self.busy_changed.emit(False)
        if self._thread:
            self._thread.quit()
            self._thread.wait()
        try:
            BUS.all_finished.disconnect(self._on_finished)
        except (RuntimeError, TypeError):
            pass


RUNNER = Runner()
