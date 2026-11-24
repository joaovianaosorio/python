# Áudio: Music by AudioAtlant from Pixabay
import pygame
pygame.init() # Primeiro, você deve iniciar o uso do Pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

input("Pressione ENTER para parar a música...")
pygame.mixer.music.stop()