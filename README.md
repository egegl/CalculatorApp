# 🧮 Tkinter Calculator App

> A feature-rich, user-friendly calculator built with Python and Tkinter.

---

## Table of Contents
1. [Features](#features)
2. [Screenshots](#screenshots)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Keyboard Shortcuts](#keyboard-shortcuts)
6. [Building from Source](#building-from-source)
7. [Contributing](#contributing)
8. [License](#license)

## Features
- Basic arithmetic: addition, subtraction, multiplication, division
- Clickable buttons and keyboard input support
- Clear (C) and Backspace (⌫) functionality
- Error handling (e.g., division by zero)
- Cross-platform (Windows executable, also runs on macOS/Linux with Python)

## Screenshots
> _Coming soon!_  
> Add your own screenshot or GIF here to showcase the app.

## Installation
> Python 3.6+ is required. Tkinter is included in most Python distributions.

> On Debian/Ubuntu:
> ```bash
> sudo apt-get install python3 python3-tk
> ```
>
> On Fedora:
> ```bash
> sudo dnf install python3 python3-tkinter
> ```
>
> Clone the repo:
> ```bash
> git clone https://github.com/yourusername/tkinter-calculator-app.git
> cd tkinter-calculator-app
> ```

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

## Contributing
> Contributions, issues, and feature requests are welcome!
>
> 1. Fork the repo.
> 2. Create a branch: `git checkout -b feature/YourFeature`.
> 3. Commit your changes: `git commit -m "Add some feature"`.
> 4. Push to your branch: `git push origin feature/YourFeature`.
> 5. Open a Pull Request.

## License
> No license specified. Feel free to add a LICENSE file (e.g., MIT, Apache 2.0).
