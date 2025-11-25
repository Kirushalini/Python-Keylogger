 🖥️ Simple Python Keylogger

This is a simple keylogger made using Python and the pynput library.
It can record all keyboard inputs including letters, numbers, symbols, and special keys like Enter, Shift, Backspace, and Arrow keys.

This project is created only for learning and educational purposes to understand how keyboard listeners work in Python.

🚀 Features

Logs every key pressed

Records normal characters and special keys

Saves keystrokes into keyfile.txt

Beginner-friendly and easy to understand

Uses pynput for keyboard event handling

📂 How It Works

The program listens to your keyboard.
Whenever you press a key:

If it's a normal key, it saves the character.

If it's a special key, it saves it in a clear format like:

[Key.enter]
[Key.space]
[Key.backspace]

🧪 Example Log Output

h e l l o [Key.space] w o r l d [Key.enter]

⚙️ Requirements

Python 3

pynput library

📂Install pynput library:

pip install pynput

▶️ How to Run

python keylogger.py


The program will start listening immediately.
All keys will be saved to keyfile.txt in the same folder.

⚠️ Important Disclaimer

This project is made only for study purposes.
Do NOT use this on other people’s devices or any system without permission.
Unauthorized keylogging is illegal.

Use responsibly.
