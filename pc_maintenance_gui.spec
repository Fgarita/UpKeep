# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller build spec for PC Maintenance.

This file must be run on Windows (PyInstaller does not cross-compile):

    pyinstaller pc_maintenance_gui.spec

The resulting executable is written to dist/PC Maintenance/PC Maintenance.exe
(or a single dist/PC Maintenance.exe if ONEFILE below is set to True).
"""

from PyInstaller.utils.hooks import collect_all

block_cipher = None

# PySide6 and qfluentwidgets both rely on dynamic imports / Qt plugins that
# PyInstaller's static analysis can miss, so we pull in everything from both
# rather than hand-listing hidden imports.
datas = [("assets", "assets")]
binaries = []
hiddenimports = []

for package in ("PySide6", "qfluentwidgets"):
    pkg_datas, pkg_binaries, pkg_hiddenimports = collect_all(package)
    datas += pkg_datas
    binaries += pkg_binaries
    hiddenimports += pkg_hiddenimports

# Set to True for a single .exe file (slower to start, easier to distribute).
# Set to False for a folder build (faster startup, what the installer expects).
ONEFILE = False

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

if ONEFILE:
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name="PC Maintenance",
        icon="assets/app.ico",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        # Embeds a manifest that makes Windows show the UAC prompt on launch,
        # instead of relying on the app relaunching itself.
        uac_admin=True,
        uac_uiaccess=False,
    )
else:
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name="PC Maintenance",
        icon="assets/app.ico",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
        disable_windowed_traceback=False,
        uac_admin=True,
        uac_uiaccess=False,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name="PC Maintenance",
    )
