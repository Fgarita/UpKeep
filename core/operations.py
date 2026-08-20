# -*- coding: utf-8 -*-
"""
All maintenance tasks. Each function takes a `log(text)` callback to
report progress, instead of printing directly, so it can be wired to
either a console or a graphical interface. Every message goes through
t() so it comes out in whichever language is currently active.
"""

import glob
import os
import shutil
import time
import urllib.request
import winreg
from typing import Callable

from core import shell
from core.i18n import t

Log = Callable[[str], None]


def create_restore_point(log: Log):
    log(t("op.restore_point.start"))
    shell.ps(
        "Checkpoint-Computer -Description 'Before PC Maintenance' "
        "-RestorePointType 'MODIFY_SETTINGS'"
    )
    log(t("op.restore_point.done"))


def close_browsers(log: Log):
    log(t("op.close_browsers.start"))
    for proc in ("chrome.exe", "msedge.exe", "firefox.exe", "brave.exe"):
        shell.run(f"taskkill /IM {proc} /F")
    time.sleep(1)
    log(t("op.close_browsers.done"))


def reset_network(log: Log):
    log(t("op.network_reset.start"))
    shell.run("ipconfig /flushdns")
    shell.run("ipconfig /release")
    shell.run("ipconfig /renew")
    shell.run("netsh winsock reset")
    shell.run("netsh int ip reset")
    shell.run("netsh advfirewall reset")
    shell.run("netsh interface ipv4 reset")
    shell.run("netsh interface ipv6 reset")
    log(t("op.network_reset.done"))


def clear_browser_cache(log: Log):
    log(t("op.browser_cache.start"))
    close_browsers(log)
    local = os.environ.get("LOCALAPPDATA", "")
    shell.remove_dir(os.path.join(local, "Google", "Chrome", "User Data", "Default", "Cache"))
    shell.remove_dir(os.path.join(local, "Google", "Chrome", "User Data", "Default", "Code Cache"))
    shell.remove_dir(os.path.join(local, "Microsoft", "Edge", "User Data", "Default", "Cache"))
    for profile in glob.glob(os.path.join(local, "Mozilla", "Firefox", "Profiles", "*")):
        shell.remove_dir(os.path.join(profile, "cache2"))
    log(t("op.browser_cache.done"))


def clear_temp_files(log: Log):
    log(t("op.temp_files.start"))
    for folder in (os.environ.get("TEMP", ""), r"C:\Windows\Temp", r"C:\Windows\Prefetch"):
        if not folder or not os.path.isdir(folder):
            continue
        for name in os.listdir(folder):
            path = os.path.join(folder, name)
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path, ignore_errors=True)
                else:
                    os.remove(path)
            except Exception:
                pass
    log(t("op.temp_files.done"))


def empty_recycle_bin(log: Log):
    log(t("op.recycle_bin.start"))
    shell.ps("Clear-RecycleBin -Force -ErrorAction SilentlyContinue")
    log(t("op.recycle_bin.done"))


def clear_update_cache(log: Log):
    log(t("op.update_cache.start"))
    shell.run("net stop wuauserv")
    shell.run("net stop bits")
    shell.remove_dir(r"C:\Windows\SoftwareDistribution\Download")
    shell.run("net start wuauserv")
    shell.run("net start bits")
    log(t("op.update_cache.done"))


def disk_cleanup(log: Log):
    log(t("op.disk_cleanup.start"))
    shell.run("cleanmgr /sagerun:1")
    log(t("op.disk_cleanup.done"))


def repair_system_files(log: Log):
    log(t("op.repair_files.start"))
    shell.run("DISM /Online /Cleanup-Image /RestoreHealth", quiet=False)
    shell.run("sfc /scannow", quiet=False)
    log(t("op.repair_files.done"))


def disable_telemetry(log: Log):
    log(t("op.telemetry.start"))
    tasks = [
        r"Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
        r"Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
        r"Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
        r"Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
    ]
    for task in tasks:
        shell.run(f'schtasks /Change /TN "{task}" /Disable')
    log(t("op.telemetry.done"))


def optimize_drives(log: Log):
    log(t("op.optimize_drives.start"))
    shell.run("defrag C: /O")
    log(t("op.optimize_drives.done"))


def update_apps(log: Log):
    log(t("op.update_apps.start"))
    if shutil.which("winget"):
        shell.run(
            "winget upgrade --all --silent --accept-source-agreements "
            "--accept-package-agreements",
            quiet=False,
        )
    else:
        log(t("op.update_apps.missing"))


def update_windows(log: Log):
    log(t("op.update_windows.start"))
    shell.ps(
        "if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) { "
        "Install-PackageProvider -Name NuGet -Force -ErrorAction SilentlyContinue | Out-Null; "
        "Install-Module PSWindowsUpdate -Force -Confirm:$false -ErrorAction SilentlyContinue }"
    )
    shell.ps(
        "Import-Module PSWindowsUpdate -ErrorAction SilentlyContinue; "
        "Get-WindowsUpdate -AcceptAll -Install -AutoReboot:$false -ErrorAction SilentlyContinue"
    )
    log(t("op.update_windows.done"))


def open_driver_update(log: Log):
    log(t("op.drivers.start"))
    shell.run("start ms-settings:windowsupdate")
    log(t("op.drivers.done"))


def performance_boost(log: Log):
    log(t("op.performance.start"))
    shell.run("powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
    shell.run("taskkill /f /im explorer.exe")
    shell.run("start explorer.exe")
    top = shell.ps_output(
        "Get-Process | Where-Object {$_.WorkingSet -gt 200MB} | "
        "Select-Object Name, @{Name='RAM_MB';Expression={[math]::round($_.WorkingSet/1MB,2)}} | "
        "Sort-Object RAM_MB -Descending | Select-Object -First 10 | Format-Table -AutoSize | Out-String"
    )
    if top:
        log(t("op.performance.top_ram", table=top))
    log(t("op.performance.done"))


def disk_space_report(log: Log):
    log(t("op.disk_space.start"))
    report = shell.ps_output(
        "Get-Volume | Where-Object {$_.DriveLetter -ne $null} | "
        "Select-Object DriveLetter, "
        "@{Name='FreeGB';Expression={[math]::Round($_.SizeRemaining/1GB,2)}}, "
        "@{Name='TotalGB';Expression={[math]::Round($_.Size/1GB,2)}} | "
        "Format-Table -AutoSize | Out-String"
    )
    log(report or t("op.disk_space.failed"))


def defender_quick_scan(log: Log):
    log(t("op.defender_scan.start"))
    exe = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"),
                        "Windows Defender", "MpCmdRun.exe")
    if os.path.exists(exe):
        shell.run(f'"{exe}" -Scan -ScanType 1', quiet=False)
        log(t("op.defender_scan.done"))
    else:
        log(t("op.defender_scan.missing"))


def disk_health_smart(log: Log):
    log(t("op.smart.start"))
    health = shell.ps_output(
        "Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, "
        "OperationalStatus | Format-Table -AutoSize | Out-String"
    )
    log(health or t("op.smart.failed"))
    log(t("op.smart.note"))


def _registry_key_exists(hive, subkey):
    try:
        winreg.OpenKey(hive, subkey)
        return True
    except OSError:
        return False


def check_pending_reboot(log: Log):
    log(t("op.pending_reboot.start"))
    pending = False
    if _registry_key_exists(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending",
    ):
        pending = True
    if _registry_key_exists(
        winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired",
    ):
        pending = True
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager"
        ) as k:
            winreg.QueryValueEx(k, "PendingFileRenameOperations")
            pending = True
    except OSError:
        pass
    log(t("op.pending_reboot.yes") if pending else t("op.pending_reboot.no"))


def clear_font_cache(log: Log):
    log(t("op.font_cache.start"))
    shell.run("net stop FontCache")
    windir = os.environ.get("WINDIR", r"C:\Windows")
    fontcache_dir = os.path.join(
        windir, "ServiceProfiles", "LocalService", "AppData", "Local", "FontCache"
    )
    if os.path.isdir(fontcache_dir):
        for name in os.listdir(fontcache_dir):
            try:
                os.remove(os.path.join(fontcache_dir, name))
            except Exception:
                pass
    fntcache = os.path.join(windir, "System32", "FNTCACHE.DAT")
    if os.path.exists(fntcache):
        try:
            os.remove(fntcache)
        except Exception:
            pass
    shell.run("net start FontCache")
    log(t("op.font_cache.done"))


def clear_event_logs(log: Log):
    log(t("op.clear_logs.start"))
    output = shell.ps_output("wevtutil el")
    for channel in output.splitlines():
        channel = channel.strip()
        if channel:
            shell.run(f'wevtutil cl "{channel}"')
    log(t("op.clear_logs.done"))


def speed_test(log: Log):
    log(t("op.speed_test.start"))
    if shutil.which("speedtest"):
        shell.run("speedtest", quiet=False)
        return
    log(t("op.speed_test.fallback"))
    url = "http://speedtest.tele2.net/10MB.zip"
    tmp = os.path.join(os.environ.get("TEMP", "."), "speedtest_pc.tmp")
    try:
        start = time.perf_counter()
        urllib.request.urlretrieve(url, tmp)
        elapsed = time.perf_counter() - start
        size = os.path.getsize(tmp)
        os.remove(tmp)
        mbps = round((size * 8 / (1024 * 1024)) / elapsed, 2)
        log(t("op.speed_test.result", mbps=mbps))
    except Exception:
        log(t("op.speed_test.failed"))


def reset_active_adapter(log: Log):
    log(t("op.active_adapter.start"))
    table = shell.ps_output(
        "Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | "
        "Format-Table Name, InterfaceDescription, LinkSpeed -AutoSize | Out-String"
    )
    if table:
        log(table)
    name = shell.ps_output(
        "(Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | "
        "Select-Object -First 1 -ExpandProperty Name)"
    )
    if name:
        log(t("op.active_adapter.renewing", name=name))
        shell.run(f'ipconfig /release "{name}"')
        shell.run(f'ipconfig /renew "{name}"')
        shell.run("ipconfig /flushdns")
        log(t("op.active_adapter.done", name=name))
    else:
        log(t("op.active_adapter.none"))


def check_disk_errors(log: Log):
    log(t("op.check_disk.start"))
    shell.run("chkdsk C: /scan", quiet=False)
    log(t("op.check_disk.done"))


def reset_microsoft_store(log: Log):
    log(t("op.store_reset.start"))
    shell.run("start /wait wsreset.exe")
    log(t("op.store_reset.done"))


def cleanup_winsxs(log: Log):
    log(t("op.winsxs.start"))
    shell.run("Dism /Online /Cleanup-Image /StartComponentCleanup", quiet=False)
    log(t("op.winsxs.done"))


def recent_system_events(log: Log):
    log(t("op.recent_events.system_start"))
    system = shell.ps_output(
        "Get-EventLog -LogName System -Newest 20 -EntryType Error,Warning "
        "-ErrorAction SilentlyContinue | Format-Table TimeGenerated, EntryType, "
        "Source, Message -AutoSize -Wrap | Out-String"
    )
    log(system or t("op.recent_events.system_empty"))
    log(t("op.recent_events.app_start"))
    application = shell.ps_output(
        "Get-EventLog -LogName Application -Newest 20 -EntryType Error,Warning "
        "-ErrorAction SilentlyContinue | Format-Table TimeGenerated, EntryType, "
        "Source, Message -AutoSize -Wrap | Out-String"
    )
    log(application or t("op.recent_events.app_empty"))


def top_cpu_processes(log: Log):
    log(t("op.cpu_processes.start"))
    table = shell.ps_output(
        "Get-Process | Sort-Object CPU -Descending | Select-Object -First 15 "
        "Name, Id, @{Name='CPU_s';Expression={[math]::Round($_.CPU,2)}}, "
        "@{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet/1MB,2)}} | "
        "Format-Table -AutoSize | Out-String"
    )
    log(table or t("op.cpu_processes.failed"))


def run_win11_debloat(log: Log):
    log(t("op.debloat.start"))
    shell.ps("& ([scriptblock]::Create((irm 'https://debloat.raphi.re/')))", quiet=False)
    log(t("op.debloat.done"))
