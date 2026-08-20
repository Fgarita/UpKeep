# -*- coding: utf-8 -*-
"""Main window: builds the navigation sidebar and the pages."""

from qfluentwidgets import FluentWindow, NavigationItemPosition, FluentIcon

from core.tasks import CATEGORIES, category_title
from core.i18n import I18N, t
from gui.pages import HomePage, CategoryPage


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(t("app.title"))
        self.resize(980, 720)

        # Mica effect: only has a real effect on Windows 11
        self.setMicaEffectEnabled(True)

        self.home_page = HomePage(self)
        self.addSubInterface(self.home_page, FluentIcon.HOME, category_title("home"))

        icons = {
            "cleanup": FluentIcon.BROOM,
            "system": FluentIcon.DEVELOPER_TOOLS,
            "network_performance": FluentIcon.WIFI,
            "updates": FluentIcon.UPDATE,
            "diagnostics": FluentIcon.CERTIFICATE,
            "external_tools": FluentIcon.APPLICATION,
        }

        for category_id in CATEGORIES:
            if category_id == "home":
                continue
            page = CategoryPage(category_id, self)
            self.addSubInterface(
                page, icons.get(category_id, FluentIcon.SETTING), category_title(category_id)
            )

        # Language toggle: shows the name of the language you'd switch TO.
        self.navigationInterface.addItem(
            routeKey="language",
            icon=FluentIcon.LANGUAGE,
            text=I18N.other_language_name(),
            onClick=I18N.toggle,
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.addItem(
            routeKey="exit",
            icon=FluentIcon.CLOSE if hasattr(FluentIcon, "CLOSE") else FluentIcon.CANCEL,
            text=t("nav.exit"),
            onClick=self.close,
            position=NavigationItemPosition.BOTTOM,
        )
