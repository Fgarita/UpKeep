# -*- coding: utf-8 -*-
"""Window pages: Home (control panel) and one page per category."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame

from qfluentwidgets import (
    TitleLabel, BodyLabel, PushButton, PrimaryPushButton, FluentIcon,
    InfoBar, InfoBarPosition, SmoothScrollArea,
)

from core.tasks import TASKS, AUTO_MODE_TASKS, category_title
from core.i18n import t
from gui.bus import RUNNER
from gui.widgets import TaskCard, LiveConsole


class CategoryPage(SmoothScrollArea):
    """List of task cards for a category (Cleanup, System, etc.)."""

    def __init__(self, category_id: str, parent=None):
        super().__init__(parent)
        self.setObjectName(category_id)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet("QScrollArea{border: none; background: transparent}")

        container = QWidget()
        container.setObjectName("container")
        container.setStyleSheet("#container{background: transparent}")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(10)

        layout.addWidget(TitleLabel(category_title(category_id)))
        layout.addSpacing(4)

        tasks = [task for task in TASKS if task.category == category_id]
        for task in tasks:
            layout.addWidget(TaskCard(task))

        layout.addSpacing(6)
        self.console = LiveConsole()
        layout.addWidget(self.console)

        layout.addStretch(1)
        self.setWidget(container)


class HomePage(SmoothScrollArea):
    """Main screen: run the full maintenance routine + live console."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("home")
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet("QScrollArea{border: none; background: transparent}")

        container = QWidget()
        container.setObjectName("container")
        container.setStyleSheet("#container{background: transparent}")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)

        layout.addWidget(TitleLabel(t("home.title")))
        layout.addWidget(BodyLabel(t("home.subtitle")))

        # Grid of selectable cards (only automatic-mode tasks)
        self.cards = []
        for task in AUTO_MODE_TASKS:
            card = TaskCard(task, checkbox=True)
            card.button.setText(t("button.run_only_this"))
            self.cards.append(card)
            layout.addWidget(card)

        buttons = QHBoxLayout()
        self.run_button = PrimaryPushButton(FluentIcon.PLAY, t("button.run_selected"))
        self.run_button.clicked.connect(self._run_selected)
        buttons.addWidget(self.run_button)

        self.toggle_button = PushButton(FluentIcon.CHECKBOX, t("button.deselect_all"))
        self.toggle_button.clicked.connect(self._toggle_all)
        buttons.addWidget(self.toggle_button)

        buttons.addStretch(1)
        layout.addLayout(buttons)

        layout.addSpacing(6)
        self.console = LiveConsole()
        layout.addWidget(self.console)

        layout.addStretch(1)
        self.setWidget(container)

        RUNNER.busy_changed.connect(lambda busy: self.run_button.setEnabled(not busy))

    def _toggle_all(self):
        select = not all(c.is_selected() for c in self.cards)
        for card in self.cards:
            card.check.setChecked(select)
        self.toggle_button.setText(t("button.deselect_all") if select else t("button.select_all"))

    def _run_selected(self):
        selected = [c.task for c in self.cards if c.is_selected()]
        if not selected:
            InfoBar.warning(
                t("infobar.nothing_selected.title"), t("infobar.nothing_selected.content"),
                position=InfoBarPosition.TOP, duration=2500, parent=self.window(),
            )
            return
        RUNNER.run(selected)
