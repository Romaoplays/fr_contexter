# Control C -> Copy word
# Control V -> Pastes phrase
# Control T -> Writes definition


import keyboard
import time

import pyperclip
import pyautogui

from larrouse_module import get_example_phrase
from larrouse_module import get_monolingual_translation


while True:
    if keyboard.is_pressed("ctrl+c"):
        time.sleep(0.3)
        palavra_original = pyperclip.paste()
        example_phrase = get_example_phrase(palavra_original)

        if get_example_phrase is not None:
            pyperclip.copy(example_phrase)
            print("Frase copiada!!")
            monolingual_translation = get_monolingual_translation(palavra_original)
            while True:
                if keyboard.is_pressed("ctrl+t"):
                    if monolingual_translation is not None:
                        time.sleep(0.3)
                        pyperclip.copy(
                            f" {palavra_original.title()} - {monolingual_translation[0][3:]}"
                        )
                        pyautogui.hotkey("ctrl", "v")
                        print("Definição Colada!!")
                        break
                    else:
                        time.sleep(0.3)
                        pyperclip.copy("Fail")
                        pyperclip.paste()

        else:
            print("\n!!! Palavra não encontrada!!!")

    elif keyboard.is_pressed("ctrl+p"):
        time.sleep(0.3)
        print("Contexter pausado!")

        while True:
            if keyboard.is_pressed("ctrl+p"):
                time.sleep(0.3)
                print("Contexter despausado!")
                break
