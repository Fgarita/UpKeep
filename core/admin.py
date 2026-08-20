# -*- coding: utf-8 -*-
"""Administrator privileges: check for them and relaunch elevated (UAC)."""

import ctypes
import os
import sys


def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def _windowless_python() -> str:
    """Return pythonw.exe next to the current interpreter if it exists.

    Relaunching with python.exe (a console subsystem executable) makes
    Windows pop up a new console window for the elevated process, since
    it can't attach to the parent's terminal. pythonw.exe is the same
    interpreter built without a console, so the elevated app starts
    silently instead of flashing a cmd window behind the GUI.
    """
    candidate = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    return candidate if os.path.exists(candidate) else sys.executable


def relaunch_as_admin():
    """Relaunch this same program, requesting elevation (UAC)."""
    params = " ".join(f'"{a}"' for a in sys.argv)
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", _windowless_python(), f'"{sys.argv[0]}" {params}', None, 1
    )
    sys.exit(0)
