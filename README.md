# KeyFlip

> Instantly convert text between **English (QWERTY)** and **Persian/Arabic** keyboard layouts with a global hotkey.

KeyFlip is a lightweight Windows utility that fixes text typed with the wrong keyboard layout. Simply select the text, press a hotkey, and KeyFlip replaces it with the correctly mapped version—without switching applications or retyping.

---

## ✨ Features

* 🚀 Instant keyboard layout conversion
* 🔄 Bidirectional conversion (English ⇄ Persian/Arabic)
* 🌍 Works in virtually any Windows application
* ⌨️ Global customizable hotkey
* ⚙️ Editable keyboard mapping via `config.json`
* 📋 Automatic clipboard handling
* 💼 Portable (single executable, no installation required)
* 🪟 Optional Windows startup support
* 🪶 Lightweight and fast

---

## 📸 Example

```text
ghlgh
↓
سلام
```

```text
lk
↓
من
```

```text
سلام
↓
cghl
```

---

## 🚀 Usage

1. Download **KeyFlip.exe** and **config.json** from the latest Release.
2. Place both files in the same folder.
3. Run **KeyFlip.exe**.
4. Select any text in any Windows application.
5. Press the configured hotkey (default: `Ctrl + Shift + ``).
6. The selected text will be instantly replaced with the converted version.

---

## ⚙️ Configuration

KeyFlip stores its settings in `config.json`.

Example:

```json
{
    "hotkey": "ctrl+shift+`",
    "map": {
        "a": "ش",
        "b": "ذ",
        "c": "ز"
    }
}
```

### Available options

| Option   | Description                                |
| -------- | ------------------------------------------ |
| `hotkey` | Global shortcut used to trigger conversion |
| `map`    | Character mapping between keyboard layouts |

You can fully customize the key mappings to support your own layout.

---

## 🛠 Building from Source

### Clone the repository

```bash
git clone https://github.com/yourusername/KeyFlip.git
cd KeyFlip
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Build

```bash
pyinstaller main.spec
```

The executable will be generated in:

```text
dist/
```

---

## 📦 Requirements

* Python 3.10+
* Windows 10 / Windows 11

Python packages:

* keyboard
* pyperclip
* startup-manager
* pyinstaller (for building)

---

## 💡 How It Works

When the hotkey is pressed, KeyFlip:

1. Copies the selected text.
2. Converts every character using the configured keyboard layout map.
3. Copies the converted text back to the clipboard.
4. Pastes it automatically, replacing the original text.

The entire process typically takes only a fraction of a second.

---

## 🗺 Roadmap

* [ ] System tray icon
* [ ] Settings window
* [ ] Multiple keyboard layouts
* [ ] Automatic layout detection
* [ ] Undo last conversion
* [ ] Import / Export configuration
* [ ] Installer
* [ ] Auto update support

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

If you have an idea that could improve KeyFlip, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.
