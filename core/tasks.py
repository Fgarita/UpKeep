# -*- coding: utf-8 -*-
"""
Task catalog: defines WHAT tasks exist, which category/page they belong
to, and which ones are part of the automatic mode. The actual logic of
each one lives in operations.py. Task objects only store an id — their
displayed title/description/confirmation text is looked up through
i18n so it always matches the current language.
"""

from dataclasses import dataclass
from typing import Callable, List

from core import operations as ops
from core.i18n import t
from core.operations import Log


@dataclass
class Task:
    id: str
    category: str          # category key
    function: Callable[[Log], None]
    auto_mode: bool = True
    requires_confirmation: bool = False

    @property
    def title(self) -> str:
        return t(f"task.{self.id}.title")

    @property
    def description(self) -> str:
        return t(f"task.{self.id}.description")

    @property
    def confirmation_text(self) -> str:
        return t(f"task.{self.id}.confirm")


# Category ids, in the order they should appear in the sidebar.
CATEGORIES = [
    "home",
    "cleanup",
    "system",
    "network_performance",
    "updates",
    "diagnostics",
    "external_tools",
]


def category_title(category_id: str) -> str:
    return t(f"category.{category_id}")


TASKS: List[Task] = [
    # --- Cleanup ---
    Task("restore_point", "cleanup", ops.create_restore_point),
    Task("close_browsers", "cleanup", ops.close_browsers),
    Task("browser_cache", "cleanup", ops.clear_browser_cache),
    Task("temp_files", "cleanup", ops.clear_temp_files),
    Task("recycle_bin", "cleanup", ops.empty_recycle_bin),
    Task("update_cache", "cleanup", ops.clear_update_cache),
    Task("font_cache", "cleanup", ops.clear_font_cache),
    Task("store_reset", "cleanup", ops.reset_microsoft_store),
    Task("disk_cleanup", "cleanup", ops.disk_cleanup),
    Task("winsxs", "cleanup", ops.cleanup_winsxs),

    # --- System ---
    Task("repair_files", "system", ops.repair_system_files),
    Task("check_disk", "system", ops.check_disk_errors),
    Task("telemetry", "system", ops.disable_telemetry),
    Task("pending_reboot", "system", ops.check_pending_reboot, auto_mode=False),

    # --- Network & Performance ---
    Task("network_reset", "network_performance", ops.reset_network),
    Task("active_adapter", "network_performance", ops.reset_active_adapter),
    Task("optimize_drives", "network_performance", ops.optimize_drives),
    Task("performance", "network_performance", ops.performance_boost),
    Task("speed_test", "network_performance", ops.speed_test, auto_mode=False),
    Task("cpu_processes", "network_performance", ops.top_cpu_processes, auto_mode=False),

    # --- Updates ---
    Task("update_apps", "updates", ops.update_apps),
    Task("update_windows", "updates", ops.update_windows),
    Task("drivers", "updates", ops.open_driver_update),

    # --- Diagnostics (not part of automatic mode) ---
    Task("disk_space", "diagnostics", ops.disk_space_report, auto_mode=False),
    Task("defender_scan", "diagnostics", ops.defender_quick_scan, auto_mode=False),
    Task("smart", "diagnostics", ops.disk_health_smart, auto_mode=False),
    Task("recent_events", "diagnostics", ops.recent_system_events, auto_mode=False),
    Task("clear_logs", "diagnostics", ops.clear_event_logs, auto_mode=False, requires_confirmation=True),

    # --- External Tools ---
    Task("debloat", "external_tools", ops.run_win11_debloat, auto_mode=False, requires_confirmation=True),
]

TASKS_BY_ID = {t_.id: t_ for t_ in TASKS}
AUTO_MODE_TASKS = [t_ for t_ in TASKS if t_.auto_mode]
