# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features new features, visuals and audio. This is for non-commercial use only.   #
# EXECUTION OF THE GAME BEGINS IN THIS FILE                                                                          #
######################################################################################################################

######################################################################################################################
#                                   Below are credits for assets not made by me                                      #
# Galaxy Force by Pixel Sagas, Retrieved from http://www.fontspace.com/category/cyber                                #
# GarageBand Loops by Apple used in the making of ---                                                                #
#                                                    "Epic Night" (main menu soundtrack)                             #
#                                                    "End Game" (Winner screen soundtrack)                           #
#                                                    "Deep Logic" (In game soundtrack)                               #
######################################################################################################################

# Main_Controller will help blend the backend to to the GUI and be the backbone for the program

# Below is a state table
# -1 = quit game
# 0 = main menu
# 1 = play game
# 2 = instructions
# 3 = credits
# 4 = end game

import pygame
from GUI import GUI
from Backend import Backend
from Sounds import Sounds
from Player import Player
from Ball import Ball


class MainController:

    def __init__(self, cur_state):
        self.cur_state = cur_state  # will help keep track of which screen the game is in
        self.message = []  # will allow us to carry information to next game state if needed

    def game_menu(self):
        game_sounds.play_main_menu()
        while True:
            game_gui.clear_screen()
            game_gui.draw_game_menu()
            temp = game_backend.process_game_menu()
            if temp != 0:
                self.cur_state = temp
                if temp != -1:
                    game_sounds.forwards()
                return None
            pygame.display.update()

    def game_play(self):
        game_sounds.stop_game_music()
        game_sounds.play_in_game_music()
        players = [Player((255, 165, 0), 1), Player((0, 0, 255), 2)]
        ball = Ball((255, 255, 255))
        while True:
            game_gui.clear_screen()
            game_gui.draw_game_play(players[0], players[1], ball)
            temp = game_backend.process_game_play()
            if temp != 1:
                self.cur_state = temp
                if temp != -1:
                    game_sounds.backwards()
                game_sounds.stop_game_music()
                return None
            # update all player's cooldown counters
            game_backend.process_power_cooldown(players[0], players[1])
            # process both player's controls (movement and power-up use)
            result = game_backend.process_player_controls(players[0], players[1], ball)
            for thing in result:  # here we go through the list of all power-ups used
                if thing[1] == 1:
                    game_gui.draw_time_ray_use(thing[0], players[thing[0] - 1])
                    pygame.display.update()
                    game_sounds.time_ray()
                elif thing[1] == 2:
                    game_gui.draw_afterburner_use(thing[0], players[thing[0] - 1])
                    pygame.display.update()
                    game_sounds.afterburner()
                else:
                    game_gui.draw_quantum_use(players[thing[0] - 1])
                    pygame.display.update()
                    game_sounds.quantum()
            if len(result) > 0:
                pygame.time.wait(250)
            # check to see if the is to bounce on something ie/ wall or player
            result = game_backend.check_ball_collisions(ball, players[0], players[1])
            if result == 1:
                game_sounds.bounce()
            # move the ball
            game_backend.process_ball_movement(ball)
            # see if someone has scored and if so update the scores
            result = game_backend.check_goal(ball, players[0], players[1])
            if result == 1:
                game_sounds.score()
            # check to see if anyone has won yet. If yes then stop the game and move to next game screen
            result = game_backend.check_for_winner(players[0], players[1])
            if result != []:
                self.message = result
                self.cur_state = 4  # end game
                return None
            pygame.display.update()

    def game_instructions(self):
        while True:
            game_gui.clear_screen()
            game_gui.draw_game_instructions()
            temp = game_backend.process_game_instructions()
            if temp != 2:
                self.cur_state = temp
                if temp != -1:
                    game_sounds.backwards()
                return None
            pygame.display.update()

    def game_credits(self):
        while True:
            game_gui.clear_screen()
            game_gui.draw_game_credits()
            temp = game_backend.process_game_credits()
            if temp != 3:
                self.cur_state = temp
                if temp != -1:
                    game_sounds.backwards()
                return None
            pygame.display.update()

    def game_end(self):
        game_sounds.stop_game_music()
        game_sounds.play_end_game_music()
        while True:
            game_gui.clear_screen()
            game_gui.draw_game_end(self.message)
            temp = game_backend.process_game_end()
            if temp != 4:
                self.cur_state = temp
                if temp != -1:
                    game_sounds.backwards()
                game_sounds.stop_game_music()
                return None
            pygame.display.update()


if __name__ == "__main__":
    # create elementary game objects
    game_controller = MainController(0)
    game_gui = GUI()
    game_backend = Backend()
    game_sounds = Sounds()
    # main loop for main controller
    while game_controller.cur_state != -1:
        if game_controller.cur_state == 0:
            game_controller.game_menu()
        elif game_controller.cur_state == 1:
            game_controller.game_play()
        elif game_controller.cur_state == 2:
            game_controller.game_instructions()
        elif game_controller.cur_state == 3:
            game_controller.game_credits()
        elif game_controller.cur_state == 4:
            game_controller.game_end()
