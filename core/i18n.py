# -*- coding: utf-8 -*-
"""Simple runtime language switch (English / Spanish).

I18N is a global object every part of the app shares. Widgets read
text through `t(key)` at build time; when the language changes the
whole window is rebuilt (see main.py) so every label re-reads its text
in the new language.
"""

from PySide6.QtCore import QObject, Signal

LANGUAGES = ("en", "es")
LANGUAGE_NAMES = {"en": "English", "es": "Español"}


class I18n(QObject):
    language_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._language = "en"

    @property
    def language(self) -> str:
        return self._language

    def set_language(self, language: str):
        if language not in LANGUAGES or language == self._language:
            return
        self._language = language
        self.language_changed.emit(language)

    def toggle(self):
        self.set_language("es" if self._language == "en" else "en")

    def other_language_name(self) -> str:
        """Name of the language you'd switch TO (shown on the toggle button)."""
        other = "es" if self._language == "en" else "en"
        return LANGUAGE_NAMES[other]


I18N = I18n()


def t(key: str, **kwargs) -> str:
    """Translate `key` into the current language, filling in placeholders."""
    from core.strings import STRINGS
    text = STRINGS.get(I18N.language, STRINGS["en"]).get(key)
    if text is None:
        text = STRINGS["en"].get(key, key)
    return text.format(**kwargs) if kwargs else text
