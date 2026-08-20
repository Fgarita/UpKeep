@echo off
:: ============================================================
:: Builds PC Maintenance into a Windows executable + installer.
:: Run this on Windows, from the project folder:
::     build.bat
:: ============================================================

echo.
echo [1/3] Installing build dependencies...
pip install -r requirements.txt -r requirements-dev.txt
if errorlevel 1 goto :error

echo.
echo [2/3] Cleaning previous builds...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul

echo.
echo [2/3] Building the executable with PyInstaller...
pyinstaller pc_maintenance_gui.spec
if errorlevel 1 goto :error

echo.
echo [3/3] Done. The app is in: dist\PC Maintenance\PC Maintenance.exe
echo.
echo To also build a Setup.exe installer, install Inno Setup
:: https://jrsoftware.org/isdl.php
echo and then run:
echo     iscc installer.iss
echo (or right-click installer.iss and choose "Compile" in Inno Setup).
echo.
goto :eof

:error
echo.
echo Build failed. Check the messages above.
exit /b 1
