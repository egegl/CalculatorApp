# Tkinter Calculator App

## Features
- Basic arithmetic: addition, subtraction, multiplication, division
- Clickable buttons and keyboard input support
- Clear (C) and Backspace (⌫) functionality
- Error handling (e.g., division by zero)
- Cross-platform (Windows executable, also runs on macOS/Linux with Python)

## Installation
> Python 3.6+ is required. Tkinter is included in most Python distributions.

### Run from Source
> ```bash
> python main.py
> ```

### Use the Windows Executable
> Simply double-click `Calculator.exe` or run:
> ```bash
> ./Calculator.exe
> ```

## Usage
> - Click buttons or type numbers/operators on your keyboard.
> - Press `=` or `Enter` to evaluate.
> - Press `C` to clear all input.
> - Press `Backspace` (⌫) to delete the last character.

## Keyboard Shortcuts
>| Key         | Action                       |
>|-------------|------------------------------|
>| 0–9         | Enter digits                 |
>| `+`, `-`, `*`, `/` | Enter operators           |
>| `Enter`, `=`| Evaluate expression          |
>| `Backspace` | Delete last character        |
>| `C`, `c`    | Clear input                  |

## Building from Source
> This executable was created using [PyInstaller](https://www.pyinstaller.org/).
>
> ```bash
> pip install pyinstaller
> pyinstaller --onefile --windowed --icon=icon.ico main.py
> ```
>
> The standalone executable will be in the `dist/` folder.
