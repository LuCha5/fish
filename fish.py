import pyautogui
import time
import keyboard  # Importer le module keyboard

def send_buy_command():
    pyautogui.typewrite('/')  # Taper le slash
    time.sleep(0.2)
    pyautogui.typewrite('buy')  # Taper "buy"
    time.sleep(0.2)
    pyautogui.press('space')  # Appuyer sur Espace
    time.sleep(0.2)
    pyautogui.typewrite('Artifact Magnet')  # Taper "leeches"
    time.sleep(0.2)
    pyautogui.press('right')  # Appuyer sur Flèche droite
    time.sleep(0.2)
    pyautogui.press('tab')  # Appuyer sur Tab
    time.sleep(0.2)
    pyautogui.press('tab')  # Appuyer sur Tab une deuxième fois
    time.sleep(0.2)
    pyautogui.typewrite('50')  # Taper "50"
    time.sleep(0.2)
    pyautogui.press('enter')  # Première validation
    time.sleep(0.2)
    pyautogui.press('enter')  # Deuxième validation

def send_sell_command():
    pyautogui.typewrite('/')  # Taper le slash
    time.sleep(0.2)
    pyautogui.typewrite('sell')  # Taper "sell"
    time.sleep(0.2)
    pyautogui.press('enter')  # Valider "sell"
    time.sleep(0.2)
    pyautogui.typewrite('all')  # Taper "all"
    time.sleep(0.2)
    pyautogui.press('enter')  # Valider "all"
    time.sleep(0.2)
    pyautogui.press('enter')  # Confirmer

def send_fish_command():
    pyautogui.typewrite('/')  # Taper le slash
    time.sleep(0.2)
    pyautogui.typewrite('fish')  # Taper "fish"
    time.sleep(0.2)
    pyautogui.press('enter')  # Valider
    time.sleep(0.2)
    pyautogui.press('enter')  # Confirmer

def main():
    print("Démarrage dans 2 secondes... Prépare-toi à Alt + Tab sur Discord !")
    time.sleep(2)  # Attendre 2 secondes avant de commencer

    fish_interval = 2.2  # Intervalle entre chaque /fish en secondes
    sell_interval = 120  # Intervalle entre chaque /sell en secondes (10 minutes)
    start_time = time.time()
    total_duration = 30 * 60  # Durée totale de 30 minutes en secondes

    fish_count = 0  # Compteur de commandes /fish

    while True:
        if keyboard.is_pressed('e'):  # Vérifier si la touche 'E' est pressée
            print("Script arrêté par l'utilisateur.")
            break

        # Vérifier si la durée totale est atteinte
        if time.time() - start_time >= total_duration:
            print("Script arrêté après 30 minutes.")
            break

        # Envoyer /fish
        send_fish_command()
        fish_count += 1  # Incrémenter le compteur de /fish
        time.sleep(fish_interval)  # Attendre avant de répéter /fish

        # Vérifier si 25 /fish ont été envoyés
        if fish_count % 50 == 0:
            send_buy_command()  # Acheter des leeches
            print(f"Commande /buy item:leeches amount:50 envoyée après {fish_count} /fish.")

        # Vérifier si le délai de 10 minutes pour /sell all est atteint
        if time.time() - start_time >= sell_interval:
            send_sell_command()  # Envoyer /sell all
            print("Commande /sell all envoyée après 10 minutes.")
            start_time = time.time()   # Réinitialiser le timer

if __name__ == '__main__':
    main()