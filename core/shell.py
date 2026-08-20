# -*- coding: utf-8 -*-
"""Low-level helpers to run Windows commands (cmd and PowerShell).

Every call passes CREATE_NO_WINDOW so subprocesses never flash their
own console window on top of the GUI.
"""

import os
import shutil
import subprocess

# Only meaningful on Windows; harmless elsewhere since these helpers are
# only ever called on Windows systems.
_NO_WINDOW = subprocess.CREATE_NO_WINDOW if hasattr(subprocess, "CREATE_NO_WINDOW") else 0


def run(cmd, quiet=True):
    """Run a shell command (cmd.exe)."""
    kwargs = {"shell": True, "creationflags": _NO_WINDOW}
    if quiet:
        kwargs["stdout"] = subprocess.DEVNULL
        kwargs["stderr"] = subprocess.DEVNULL
    try:
        subprocess.run(cmd, **kwargs)
    except Exception:
        pass


def ps(cmd, quiet=True):
    """Run a PowerShell command."""
    kwargs = {"creationflags": _NO_WINDOW}
    if quiet:
        kwargs["stdout"] = subprocess.DEVNULL
        kwargs["stderr"] = subprocess.DEVNULL
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", cmd], **kwargs)
    except Exception:
        pass


def ps_output(cmd) -> str:
    """Run PowerShell and return its output as text (to read values)."""
    try:
        r = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd],
            capture_output=True, text=True, creationflags=_NO_WINDOW,
        )
        return r.stdout.strip()
    except Exception:
        return ""


def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)


def free_space_mb() -> int:
    try:
        return shutil.disk_usage("C:\\").free // (1024 * 1024)
    except Exception:
        return 0
