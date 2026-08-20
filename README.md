# PC Maintenance — GUI (Windows 11 / Fluent Design)

A Windows maintenance tool with a Windows 11-style GUI (Fluent Design,
Mica effect), built with [PySide6](https://doc.qt.io/qtforpython/) and
[PySide6-Fluent-Widgets](https://qfluentwidgets.com/). It's the Python
port of the original `.bat` maintenance script.

## Project structure

```
pc_maintenance_gui/
├── .vscode/            # VS Code config (debug + settings)
├── assets/
│   └── app.ico         # app icon (used by the .exe and the installer)
├── core/               # pure logic, no GUI code
│   ├── admin.py        # Administrator privileges (UAC)
│   ├── shell.py        # helpers to run cmd/PowerShell commands
│   ├── operations.py   # the ~27 maintenance tasks
│   ├── tasks.py        # task catalog (what's shown and where)
│   ├── i18n.py         # runtime English/Spanish language switch
│   └── strings.py      # every translatable string, both languages
├── gui/                # graphical interface (PySide6 + Fluent Widgets)
│   ├── bus.py           # event bus + background execution
│   ├── widgets.py        # task card + live console
│   ├── pages.py           # Home page and category pages
│   └── main_window.py      # main window (sidebar + pages)
├── main.py             # entry point
├── pc_maintenance_gui.spec  # PyInstaller build spec
├── installer.iss        # Inno Setup installer script
├── build.bat            # one-command Windows build
├── requirements.txt      # runtime dependencies
├── requirements-dev.txt  # build-time dependencies (PyInstaller)
└── README.md
```

`core/` doesn't import anything from Qt: it can be tested and reused
(for example from a console version) without starting any window.
`gui/` is the only part that knows a GUI exists.

## Requirements

- Windows 10/11
- Python 3.9+

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The program requests Administrator privileges automatically (UAC) if
it doesn't already have them, and relaunches itself with `pythonw.exe`
so no console window appears alongside the GUI.

## What it does

- **Home**: choose which automatic-mode tasks to run (all checked by
  default), run them with one click, and watch progress in a live
  console.
- **Cleanup / System / Network & Performance / Updates / Diagnostics /
  External Tools**: each category has its own tasks, each with its own
  "Run" button and its own live console.
- **Language toggle**: a button at the bottom of the sidebar switches
  the whole app — menus, task titles, buttons and the live log —
  between English and Spanish instantly.
- Tasks that erase data (Event Viewer logs) or open a third-party tool
  (Win11Debloat) ask for confirmation before running.
- Everything runs on a separate thread, so the GUI never freezes while
  SFC, DISM or other long commands are running.

## Notes

- The Mica effect (`setMicaEffectEnabled`) is only visible on Windows
  11; on Windows 10 it falls back to a solid background.
- Win11Debloat (github.com/Raphire/Win11Debloat) is a third-party
  project, not made by Anthropic.

## Building a Windows executable / installer

You need to build on Windows — PyInstaller does not cross-compile, so
this can't be produced from Linux or macOS.

**1. One-command build:**

```bash
build.bat
```

This installs the build tools, cleans old builds, and runs PyInstaller
using `pc_maintenance_gui.spec`. The result is:

```
dist\PC Maintenance\PC Maintenance.exe
```

That folder is a complete, self-contained app — you can zip it and
share it, or double-click the `.exe` directly. No Python install is
required on the machine that runs it.

**2. Optional: a proper Setup.exe installer**

Install [Inno Setup](https://jrsoftware.org/isdl.php) (free), then run:

```bash
iscc installer.iss
```

(or open `installer.iss` in the Inno Setup Compiler and click Build).
This produces `Output\PC-Maintenance-Setup.exe` — a normal Windows
installer with a Start Menu entry, an optional Desktop shortcut, and
an uninstaller, in both English and Spanish.

**Notes on the packaged app:**

- The `.exe` is built with a manifest that requests Administrator
  rights automatically (`uac_admin=True` in the spec), so Windows
  shows the UAC prompt as soon as you launch it — the app doesn't need
  to relaunch itself the way `python main.py` does.
- `dist/`, `build/` and `Output/` are git-ignored; they're generated
  locally and shouldn't be committed.

## Publishing this on GitHub

This is a personal Python project with no Anthropic-specific licensing
attached, so there's nothing stopping you from putting it in a public
or private repo. A few practical notes:

- `.gitignore` already excludes `__pycache__/`, `dist/`, `build/` and
  `Output/` — don't commit the compiled `.exe` or installer; those are
  build artifacts, not source. If you want to distribute the binary,
  attach it to a [GitHub Release](https://docs.github.com/en/repositories/releasing-projects-on-github)
  instead of committing it to the repo.
- Consider adding a `LICENSE` file (MIT is a common default for a
  portfolio project like this) so it's clear how others can use it.
- `PySide6` is LGPL-licensed and `PySide6-Fluent-Widgets` is GPLv3 —
  both fine to depend on via `pip`/`requirements.txt` in your own
  project; just don't vendor their source code directly into the repo.
