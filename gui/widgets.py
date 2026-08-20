# -*- coding: utf-8 -*-
"""Reusable widgets: the task card and the live console."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qfluentwidgets import (
    CardWidget, PushButton, CheckBox,
    StrongBodyLabel, CaptionLabel, TextEdit, IndeterminateProgressBar,
    MessageBox,
)

from core.tasks import Task
from core.i18n import t
from gui.bus import BUS, RUNNER


class TaskCard(CardWidget):
    """A row like Windows Settings: title, description and a button."""

    def __init__(self, task: Task, checkbox: bool = False, parent=None):
        super().__init__(parent)
        self.task = task
        self.setBorderRadius(8)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(12)

        if checkbox:
            self.check = CheckBox()
            self.check.setChecked(True)
            layout.addWidget(self.check)
        else:
            self.check = None

        texts = QVBoxLayout()
        texts.setSpacing(2)
        title = StrongBodyLabel(task.title)
        desc = CaptionLabel(task.description)
        desc.setTextColor("#606060", "#c0c0c0")
        texts.addWidget(title)
        texts.addWidget(desc)
        layout.addLayout(texts, 1)

        self.button = PushButton(t("button.run"))
        self.button.setMinimumWidth(110)
        self.button.clicked.connect(self._on_click)
        layout.addWidget(self.button, 0, Qt.AlignRight)

        RUNNER.busy_changed.connect(lambda busy: self.button.setEnabled(not busy))

    def _on_click(self):
        if self.task.requires_confirmation:
            box = MessageBox(
                t("confirm.title"), self.task.confirmation_text, self.window()
            )
            if not box.exec():
                return
        RUNNER.run([self.task])

    def is_selected(self) -> bool:
        return self.check.isChecked() if self.check else True


class LiveConsole(QWidget):
    """Read-only console + indeterminate progress bar."""

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        header = QHBoxLayout()
        header.addWidget(StrongBodyLabel(t("console.live_log")))
        header.addStretch(1)
        self.status = CaptionLabel(t("console.idle"))
        header.addWidget(self.status)
        layout.addLayout(header)

        self.progress = IndeterminateProgressBar(self)
        self.progress.setFixedHeight(4)
        self.progress.stop()
        layout.addWidget(self.progress)

        self.text = TextEdit(self)
        self.text.setReadOnly(True)
        self.text.setPlainText("\n".join(BUS.history))
        self.text.setMinimumHeight(220)
        layout.addWidget(self.text)

        BUS.line.connect(self._append_line)
        BUS.task_started.connect(self._task_started)
        BUS.task_finished.connect(self._task_finished)
        BUS.all_finished.connect(self._all_finished)

    def _append_line(self, text):
        self.text.append(text)
        bar = self.text.verticalScrollBar()
        bar.setValue(bar.maximum())

    def _task_started(self, title):
        self.status.setText(t("console.running", title=title))
        self.progress.start()

    def _task_finished(self, title, success):
        mark = t("console.ok") if success else t("console.error")
        self.status.setText(f"[{mark}] {title}")

    def _all_finished(self):
        self.status.setText(t("console.done"))
        self.progress.stop()
