# KeyFlip

A keyboard-level transliterator for Persian/Arabic text. Press a hotkey to instantly translate selected text from English QWERTY layout to Persian/Arabic characters.

## Features

- **Instant translation** — select text, press hotkey, translated text is pasted automatically
- **Customizable hotkey** — default is `Ctrl+Shift+``
- **Editable character map** — configure via `config.json`
- **Windows startup support** — optionally auto-start with Windows
- **Lightweight** — single executable, no installation required

## Usage

1. Download `KeyFlip.exe` and `config.json` from [Releases](../../releases)
2. Place both files in the same folder
3. Run `KeyFlip.exe`
4. Select text in any application and press `Ctrl+Shift+`` to translate

## Configuration

Edit `config.json` to customize the hotkey and character mappings:

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

## Building from Source

```bash
pip install -r requirements.txt
pyinstaller main.spec
```

The output executable will be in the `dist/` folder.

## License

MIT
