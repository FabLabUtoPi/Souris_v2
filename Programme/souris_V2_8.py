# Souris pilotee par joystick
# MIT License
# Version 2 avec joystick analogique
# 2 vitesses de déplacement en fonction de la position du joystick
# Avertissement sonore quand deux directions sont activées (diagonale)


# Copyright (c) 2024 FabLabUtoPi

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Licence MIT

# Copyright (c) 2024 FabLabUtoPi

# L autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce
# logiciel et des fichiers de documentation associés (le "Logiciel"), de l'utiliser
# sans restriction, y compris sans limitation d'utilisation, de copie, de modification, de fusion, 
# de publication, de distribution, d'accorder des sous-licences et/ou de vendre des copies du logiciel.
# et/ou de vendre des copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni
# de le faire, sous réserve des conditions suivantes :

# La licence ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les
# copies ou parties substantielles du logiciel.

# LE LOGICIEL EST FOURNI "EN L'ETAT", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU
# EXPLICITE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE,
# D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON. EN AUCUN CAS LES AUTEURS OU
# LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS POUR
# RESPONSABLES D'UNE RÉCLAMATION, D'UN DOMMAGE OU D'UNE AUTRE RESPONSABILITÉ, 
# QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE,
# PROVENANT DE OU EN RELATION AVEC LE LOGICIEL OU AVEC SON UTILISATION 
# OU D'AUTRES TRANSACTIONS LIEES AU LOGICIEL.


# Références
# Source https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/mouse.html
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.mouse.Mouse
#
# Créé par le FabLab UtoPi Le Creusot
# Contact : contact@fablab-utopi.org 
# La position x=0, y=0 pour la souris est en haut à gauche de l'écran
#
# COnnexion des potentiomètres
# Horizontal           Déplacement droite-gauche     A1
# Vertical             Déplacement Haut-Bas          A0

# Connexion des switchs
# Peut se modifier en fonction de vos connexions

# GAUCHE               Appui bouton gauche souris    GP5
# DROITE               Appui bouton droit souris     GP6

# PROG                 Lancement programme           GP7

# Wheel UP             Roulette vers le haut         GP8
# Wheel DOWN           Roulette vers le bas          GP9

# Connexion des LEDs
# DROITE               LED Bouton droit              GP0
# GAUCHE               LED Bouton gauche             GP1
# PROG                 LED Lancement programme       GP2
# Wheel UP             LED Roulette vers le haut     GP3
# Wheel DOWN           LED Roulette vers le bas      GP4

# Vibreur  NON CONNECTE                              GP14
# Buzzer                                             GP15

# Importation des bibliotheques utilisées
import time
import analogio
import board
import digitalio
import usb_hid
import array
import pulseio
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)

kbd = Keyboard(usb_hid.devices)

x_axis = analogio.AnalogIn(board.A1)
y_axis = analogio.AnalogIn(board.A0)

pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def steps(axis):
    return round((axis - pot_min) / step)

# Définir la LED interne au Raspberry Pi PICO
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
# Eteindre la LED du Raspberry Pi PICO
led.value = 0

# Définir les LED des boutons poussoir
led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT

led1.value = 0

led2 = digitalio.DigitalInOut(board.GP1)
led2.direction = digitalio.Direction.OUTPUT
# Eteindre la LED2
led2.value = 0

led3 = digitalio.DigitalInOut(board.GP2)
led3.direction = digitalio.Direction.OUTPUT
# Eteindre la LED3
led3.value = 0

led4 = digitalio.DigitalInOut(board.GP3)
led4.direction = digitalio.Direction.OUTPUT
# Eteindre la LED4
led4.value = 0

led5 = digitalio.DigitalInOut(board.GP4)
led5.direction = digitalio.Direction.OUTPUT
# Eteindre la LED5
led5.value = 0

# Definir les boutons poussoirs de la souris
# De gauche à droite :
# Clic gauche, clic droit, programme, roulette up, roulette down
# Clic gauche / Appui sur Joystick
LEFT_BUTTON = digitalio.DigitalInOut(board.GP9)
LEFT_BUTTON.direction = digitalio.Direction.INPUT
LEFT_BUTTON.pull = digitalio.Pull.UP

# Clic droit
RIGHT_BUTTON = digitalio.DigitalInOut(board.GP8)
RIGHT_BUTTON.direction = digitalio.Direction.INPUT
RIGHT_BUTTON.pull = digitalio.Pull.UP
# 
# Bouton PROG
PROG_BUTTON = digitalio.DigitalInOut(board.GP7)
PROG_BUTTON.direction = digitalio.Direction.INPUT
PROG_BUTTON.pull = digitalio.Pull.UP

# Roulette UP
up = digitalio.DigitalInOut(board.GP6)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

# Roulette DOWN
down = digitalio.DigitalInOut(board.GP5)
down.direction = digitalio.Direction.INPUT
down.pull = digitalio.Pull.UP

# Définir les directions du joystick
dir_G = False
dir_D = False
dir_H = False
dir_B = False

# Faire Flasher la LED de la carte PICO
def blink():
    led.value = 1
    time.sleep(0.05)
    led.value = 0

# Clignoter pour montrer que le programme demarre
# vu uniquement sur le Raspberry Pi PICO
for i in range(0, 5):
    blink()
    time.sleep(0.02)

# Declarer le Vibreur - Inutilise en V2
# vibreur = digitalio.DigitalInOut(board.GP14)
# vibreur.direction = digitalio.Direction.OUTPUT

# Declarer le Buzzer
buzzer = pulseio.PulseOut(board.GP15, frequency=3000, duty_cycle=32768)
pulses = array.array('H', [65000, 1000, 65000, 65000, 1000])


# Chenillard des LEDs avant de démarrer
# Utile pour la mise au point
#   et la verification du bon fonctionnement du programme
led1.value = True
time.sleep(0.05)
led2.value = True
time.sleep(0.05)
led3.value = True
time.sleep(0.05)
led4.value = True
time.sleep(0.05)
led5.value = True
time.sleep(0.4)
led5.value = False
time.sleep(0.05)
led4.value = False
time.sleep(0.05)
led3.value = False
time.sleep(0.05)
led2.value = False
time.sleep(0.05)
led1.value = False
time.sleep(0.05)

# Définir les valeurs de déplacement du curseur sur l'écran
# Nombre de pixels dont le curseur se déplace
v_lent = 8
v_rapide = 16

# Définir la durée de la temporisation de boucle principale
# 0,05 seconde par défaut
tempo_boucle = 0.05

# Définir l'intervalle de temps entre les bips quand on déplace en diagonale
# 1 seconde par défaut
tempo_bip = 1

# Démarrer le chronométrage pour le BIP
# Le bip est activé toutes les secondes si le curseur se déplace en diagonale
t_debut = time.monotonic()

# Mettre le flag du BIP à 0
flag_BIP = 0

# Test vibreur - Pas utilise dans cette version
# vibreur.value = True
# time.sleep(0.1)
# vibreur.value = False
# time.sleep(0.5)

# Test buzzer
buzzer.send(pulses)

# Allumer LED 1 utilisé pour les test
def led1_on():
    led1.value = 1
    time.sleep(0.05)
    led1.value = 0

# Fermer la fenetre CIRCUITPI qui s ouvre a  la connexion
# Mettre en commentaire pendant les essais sinon l editeur se ferme !
# kbd.send(Keycode.LEFT_ALT, Keycode.F4)

# BOUCLE PRINCIPALE DU PROGRAMME ===============
while True:
    try:
        # Déplacer le curseur en fonction de la positions du joystick
        x = get_voltage(x_axis)
        y = get_voltage(y_axis)
        print(steps(x))
        print(steps(y))

        if steps(x) > 12.0:
            dir_D = True
            # print(steps(x))
            mouse.move(x = v_lent)
        if steps(x) < 8.0:
            dir_G = True
            # print(steps(x))
            mouse.move(x = -v_lent)

        if steps(x) > 16.0:
            dir_D = True
            # print(steps(x))
            mouse.move(x = v_rapide)
        if steps(x) < 4.0:
            dir_G = True
            # print(steps(x))
            mouse.move(x = -v_rapide)

        if steps(y) > 12.0:
            dir_H = True
            # print(steps(y))
            mouse.move(y = -v_lent)
        if steps(y) < 8.0:
            dir_B = True
            # print(steps(y))
            mouse.move(y = v_lent)

        if steps(y) > 16.0:
            dir_H = True
            # print(steps(y))
            mouse.move(y = -v_rapide)
        if steps(y) < 4.0:
            dir_B = True
            # print(steps(y))
            mouse.move(y = v_rapide)

        # Si on active 2 directions simultanement
        # Actionner le buzzer au maxi une fois par seconde
        if ((dir_G and dir_H) or (dir_D and dir_H) or (dir_G and dir_B) or (dir_D and dir_B)) == True :
            # On est en diagonale mettre le flag_BIP à 1
            flag_BIP = 1
            # Si le flag est à 0, on n'a pas encore bippé
            if flag_BIP == 1:
                # Est ce qu'il s'est écoulé une seconde depuis le dernier bip ?
                if (time.monotonic() - t_debut) > tempo_bip:
                    print("BIP ! Flag à 1 Temps = ", time.monotonic())
                    buzzer.send(pulses)
                    led1_on()
                    t_debut = time.monotonic()
                else:
                    # Le flag est à 0 et on est passé en diagonale = on bippe
                    flag_BIP = 1
        else:
            # On n'est plus en diagonale : enlever le flag
            flag_BIP = 0
        
        # Remettre la direction au centre pour la prochaine lecture
        dir_G = False
        dir_D = False
        dir_H = False
        dir_B = False
        

        # Bouton gauche de la souris
        if (LEFT_BUTTON.value is False):
            # Si un bouton est appuye on positionne le flag
            flag = 1
            print("BOUTON GAUCHE valeur = ", LEFT_BUTTON.value)
            mouse.click(Mouse.LEFT_BUTTON)
            led1.value = True
        else:
            led1.value = False

        # Bouton droit de la souris
        if (RIGHT_BUTTON.value is False):
            # Si un bouton est appuye on positionne le flag
            flag = 1
            print("BOUTON DROIT valeur = ", RIGHT_BUTTON.value)
            mouse.click(Mouse.RIGHT_BUTTON)
            led2.value = True
        else:
            led2.value = False

        # Bouton PROGRAMMABLE de la souris
        if (PROG_BUTTON.value is False):
            # Si un bouton est appuye on positionne le flag
            flag = 1
            print("BOUTON CENTRAL valeur = ", PROG_BUTTON.value)
            buzzer.send(pulses)
            # Envoyer code clavier
            kbd.press(Keycode.WINDOWS)
            time.sleep(.09)
            kbd.release(Keycode.WINDOWS)
            led3.value = True
        else:
            led3.value = False

        # Roulette haut
        if (up.value is False):
            # Si un bouton est appuye on positionne le flag
            flag = 1
            print("Roulette UP valeur = ", up.value)
            mouse.move(wheel=1)
            led4.value = True
        else:
            led4.value = False

        # Roulette bas
        if (down.value is False):
            # Si un bouton est appuyé on positionne le flag
            flag = 1
            print("Roulette DOWN valeur = ", down.value)
            mouse.move(wheel=-1)
            led5.value = True
        else:
            led5.value = False

        # Tempo de la boucle de lecture des boutons
        time.sleep(tempo_boucle)
    except KeyboardInterrupt:
        raise Exception("Arrete par l utilisateur")



