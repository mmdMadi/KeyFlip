import json
import os
import sys
from pathlib import Path
from time import sleep

from keyboard import send, add_hotkey, wait
from pyperclip import copy, paste
from startup_manager import check_startup_status, add_to_startup



# ==================================================
# EXE / SCRIPT PATH HANDLING
# ==================================================

def get_exe_dir():
    """
    Returns the directory of the .exe when frozen,
    or the directory of the .py file when running normally.
    """
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    return Path(__file__).parent


CONFIG_FILE = get_exe_dir() / "config.json"


# ==================================================
# DEFAULT CONFIG
# ==================================================

DEFAULT_MAP = {
    '"': '"', "'": 'گ', ',': 'و', '.': '.',
    '/': '؟', ':': ':', ';': 'ک', '<': '<',
    '>': '>', '?': '؟', '[': 'ج', '\\': 'پ',
    ']': 'چ', '}': '{',
    'A': 'َ', 'B': 'إ', 'C': 'ژ', 'D': 'ِ',
    'E': 'ٍ', 'F': 'ّ', 'G': 'ۀ', 'H': 'آ',
    'I': ']', 'J': 'ـ', 'K': '«', 'L': '»',
    'M': 'ء', 'N': 'أ', 'O': '[', 'P': '\\',
    'Q': 'ً', 'R': 'ريال', 'S': 'ُ', 'T': '،',
    'U': ',', 'V': 'ؤ', 'W': 'ٌ', 'X': 'ي',
    'Y': '؛', 'Z': 'ة',
    'a': 'ش', 'b': 'ذ', 'c': 'ز', 'd': 'ی',
    'e': 'ث', 'f': 'ب', 'g': 'ل', 'h': 'ا',
    'i': 'ه', 'j': 'ت', 'k': 'ن', 'l': 'م',
    'm': 'ئ', 'n': 'د', 'o': 'خ', 'p': 'ح',
    'q': 'ض', 'r': 'ق', 's': 'س', 't': 'ف',
    'u': 'ع', 'v': 'ر', 'w': 'ص', 'x': 'ط',
    'y': 'غ', 'z': 'ظ',
    '|': '|'
}

DEFAULT_CONFIG = {
    "hotkey": "ctrl+shift+`",
    "map": DEFAULT_MAP
}


# ==================================================
# CONFIG LOAD / CREATE
# ==================================================

def load_config():
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # If config is broken, restore defaults
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
        return DEFAULT_CONFIG


config = load_config()

MAP = config.get("map", DEFAULT_MAP)
HOTKEY = config.get("hotkey", "ctrl+shift+`")
REVERSE_MAP = {v: k for k, v in MAP.items()}


# ==================================================
# TRANSLATION LOGIC
# ==================================================

def translate(text: str) -> str:
    result = []
    for c in text:
        lc = c.lower()
        if lc in MAP:
            result.append(MAP[lc])
        elif c in REVERSE_MAP:
            result.append(REVERSE_MAP[c])
        else:
            result.append(c)
    return ''.join(result)


def on_hotkey():
    sleep(0.2)
    send('ctrl+c')
    sleep(0.2)

    text = paste()
    if not text:
        return

    translated = translate(text)
    copy(translated)

    sleep(0.2)
    send('ctrl+v')
    sleep(0.2)
    copy('')


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    # status = check_startup_status()
    # if not status.get("in_startup", False):
    #     add_to_startup()

    add_hotkey(HOTKEY, on_hotkey)

    print(f"Translator running...")
    print(f"Hotkey: {HOTKEY}")
    print(f"Config file: {CONFIG_FILE}")

    wait()
