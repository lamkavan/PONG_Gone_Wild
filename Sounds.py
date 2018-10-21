# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features many new features and visuals. This is for non-commercial use only.     #
######################################################################################################################

# Sounds will take care of the game musics and sounds

import pygame


class Sounds:

    def play_main_menu(self):
        if not(pygame.mixer.music.get_busy()):
            main_menu_music_file = "./game_sounds/Epic Night.wav"
            pygame.mixer.music.load(main_menu_music_file)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)

    def play_in_game_music(self):
        in_game_music_file = "./game_sounds/Deep Logic.wav"
        pygame.mixer.music.load(in_game_music_file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def play_end_game_music(self):
        end_game_music_file = "./game_sounds/End Game.wav"
        pygame.mixer.music.load(end_game_music_file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def stop_game_music(self):
        pygame.mixer.music.stop()

    def forwards(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("./game_sounds/forwards.wav"))

    def backwards(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("./game_sounds/backwards.wav"))

    def score(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("./game_sounds/Score.wav"))

    def bounce(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./game_sounds/Bounce.wav"))

    def time_ray(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./game_sounds/Time Ray.wav"))

    def afterburner(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./game_sounds/Afterburner.wav"))

    def quantum(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./game_sounds/Quantum Repulser.wav"))
