# -*- coding: utf-8 -*-
"""Core package: maintenance logic, with no GUI code in it."""

from core.admin import is_admin, relaunch_as_admin
from core.shell import free_space_mb
from core.i18n import I18N, t
from core.tasks import Task, CATEGORIES, category_title, TASKS, TASKS_BY_ID, AUTO_MODE_TASKS

__all__ = [
    "is_admin",
    "relaunch_as_admin",
    "free_space_mb",
    "I18N",
    "t",
    "Task",
    "CATEGORIES",
    "category_title",
    "TASKS",
    "TASKS_BY_ID",
    "AUTO_MODE_TASKS",
]
