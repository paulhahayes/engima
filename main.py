
import pygame

from keyboard import Keyboard
from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector
from enigma import Enigma
from draw import draw
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma siulator")

MONO = pygame.font.SysFont("BlexMono Nerd Font", 25)
BOLD = pygame.font.SysFont("BlexMono Nerd Font", 25, bold=True)

WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS = {"top": 100, "bottom": 100, "left": 100, "right": 100}
GAP = 100

INPUT = ""
OUTPUT = ""
PATH = []

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO ", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK ", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

enigma = Enigma(B,I,II,III,PB,KB)
enigma.set_rings((1,1,1))
enigma.set_key("CAT")


anitmating = True
while anitmating:
    SCREEN.fill("#333333")

    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/2 - 40))
    SCREEN.blit(text, text_box)

    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/2 -20))
    SCREEN.blit(text, text_box)

    draw(enigma, SCREEN, PATH, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    pygame.display.flip()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            anitmating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
            else:
                key = event.unicode
                if key.isalnum():
                    letter = key.upper()
                    INPUT += letter
                    PATH, cipher = enigma.encipher(letter)
                    OUTPUT += cipher
