import pydirectinput
import time
import random

def press_e_in_game():
    try:
        while True:
            a = random.uniform(3.0,3.4)
            b = random.uniform(0.1,0.3)
            pydirectinput.keyDown('e')  # Appuie sur la touche 'e'
            time.sleep(a)               # Maintient la touche pendant 3 secondes
            pydirectinput.keyUp('e')    # Relâche la touche 'eeeee'
            time.sleep(b)             # Petit délai avant la prochaine pression
    except KeyboardInterrupt:
        print("Programme arrêté manuellement.")

if __name__ == "__main__":
    press_e_in_game()
