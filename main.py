#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PC Maintenance — entry point.

Checks for Administrator privileges (relaunches elevated if needed)
and starts the Windows 11-style GUI (Fluent Design / Mica).

Requirements (Windows, Python 3.9+):
    pip install -r requirements.txt

Run:
    python main.py
"""

import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, setThemeColor

from core.admin import is_admin, relaunch_as_admin
from core.i18n import I18N
from gui.main_window import MainWindow


def _icon_path() -> str:
    """Resolve assets/app.ico both when run from source and when frozen
    into a PyInstaller executable (where files live next to the .exe,
    or inside sys._MEIPASS for a --onefile build)."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return str(base / "assets" / "app.ico")


def main():
    if sys.platform != "win32":
        print("This GUI is designed for Windows 11 (uses PySide6-Fluent-Widgets).")
        print("You can still develop/preview the layout on other systems, but")
        print("features like the Mica effect and most commands only apply on Windows.")

    if sys.platform == "win32" and not is_admin():
        print("This program needs Administrator privileges. Relaunching...")
        relaunch_as_admin()
        return

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(_icon_path()))
    setTheme(Theme.AUTO)
    setThemeColor("#0078D4")  # Windows 11 blue

    # Kept in a dict so the closure below can swap it out.
    state = {"window": MainWindow()}
    state["window"].show()

    def on_language_changed(_language):
        old_window = state["window"]
        geometry = old_window.geometry()
        old_window.close()

        new_window = MainWindow()
        new_window.setGeometry(geometry)
        new_window.show()
        state["window"] = new_window

    I18N.language_changed.connect(on_language_changed)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
