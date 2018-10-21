# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features many new features and visuals. This is for non-commercial use only.     #
######################################################################################################################

# Backend will take care of the game logic and hold/modify player data

import pygame
import math
from random import randint

# constants to be used for power-ups
TIME_RAY_SPEED = 0.5
TIME_RAY_COOLDOWN = 600
AFTERBURNER_SPEED = 4
AFTERBURNER_COOLDOWN = 900
NORMAL_SPEED = 2
BALL_SPEED_INCREASE = 7


class Backend:

    def process_game_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 1  # play game
                elif event.key == pygame.K_b:
                    return 2  # instructions
                elif event.key == pygame.K_c:
                    return 3  # credits
            elif event.type == pygame.QUIT:
                return -1
        return 0  # stay on main menu

    def process_game_play(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0  # main menu
            elif event.type == pygame.QUIT:
                return -1
        return 1  # stay on game play screen

    def process_power_cooldown(self, p1, p2):
        self.check_time_ray_cooldown(p1)
        self.check_time_ray_cooldown(p2)
        self.check_afterburner_cooldown(p1)
        self.check_afterburner_cooldown(p2)

    def check_time_ray_cooldown(self, player):
        if player.time_ray_hit_cooldown != 0:
            player.time_ray_hit_cooldown -= 1
            if player.time_ray_hit_cooldown == 0:
                if player.afterburner_cooldown != 0:
                    player.speed = AFTERBURNER_SPEED
                else:
                    player.speed = NORMAL_SPEED

    def check_afterburner_cooldown(self, player):
        if player.afterburner_cooldown != 0:
            player.afterburner_cooldown -= 1
            if player.afterburner_cooldown == 0:
                if player.time_ray_hit_cooldown != 0:
                    player.speed = TIME_RAY_SPEED
                else:
                    player.speed = NORMAL_SPEED

    def process_player_controls(self, p1, p2, ball):
        all_key_presses = pygame.key.get_pressed()
        result = []  # will tell main controller if powers are used. [1,2] means player 1 used afterburner

        # player 1
        # powers
        if all_key_presses[pygame.K_c] and p1.powers[0] == 1:  # time ray
            self.process_time_ray_use(p1, p2)
            result.append([1, 1])
        elif all_key_presses[pygame.K_v] and p1.powers[1] == 1:  # afterburner
            self.process_afterburner_use(p1)
            result.append([1, 2])
        elif all_key_presses[pygame.K_b] and p1.powers[2] == 1:  # quantum repulser
            self.process_quantum_use(p1, 1, ball)
            result.append([1, 3])
        # movement
        if all_key_presses[pygame.K_w]:
            if (p1.pad_y - 30 - p1.speed) >= 2:
                p1.pad_y -= p1.speed
            else:
                p1.pad_y = 32
        if all_key_presses[pygame.K_s]:
            if (p1.pad_y + 30 + p1.speed) <= 580:
                p1.pad_y += p1.speed
            else:
                p1.pad_y = 550

        # player 2
        # powers
        if all_key_presses[pygame.K_KP1] and p2.powers[0] == 1:  # time ray
            self.process_time_ray_use(p2, p1)
            result.append([2, 1])
        elif all_key_presses[pygame.K_KP2] and p2.powers[1] == 1:  # afterburner
            self.process_afterburner_use(p2)
            result.append([2, 2])
        elif all_key_presses[pygame.K_KP3] and p2.powers[2] == 1:  # quantum repulser
            self.process_quantum_use(p2, 2, ball)
            result.append([2, 3])
        # movement
        if all_key_presses[pygame.K_UP]:
            if (p2.pad_y - 30 - p2.speed) >= 2:
                p2.pad_y -= p2.speed
            else:
                p2.pad_y = 32
        if all_key_presses[pygame.K_DOWN]:
            if (p2.pad_y + 30 + p2.speed) <= 580:
                p2.pad_y += p2.speed
            else:
                p2.pad_y = 550

        return result  # so we can let the main controller know if any powers were used

    def process_time_ray_use(self, p_use, p_hit):
        p_use.powers[0] = 0
        if p_hit.pad_y - 30 <= p_use.pad_y <= p_hit.pad_y + 30:
            p_hit.speed = TIME_RAY_SPEED
            p_hit.time_ray_hit_cooldown = TIME_RAY_COOLDOWN

    def process_afterburner_use(self, p_use):
        p_use.powers[1] = 0
        p_use.speed = AFTERBURNER_SPEED
        p_use.afterburner_cooldown = AFTERBURNER_COOLDOWN

    def process_quantum_use(self, p_use, p_num, ball):
        p_use.powers[2] = 0
        ball.speed += BALL_SPEED_INCREASE
        if p_num == 1:
            ball.angle_of_move = 0
        else:
            ball.angle_of_move = 180

    def process_ball_movement(self, ball):
        dir_of_move = [math.cos(math.radians(ball.angle_of_move)) * ball.speed,
                       math.sin(math.radians(ball.angle_of_move)) * ball.speed]
        # move the ball
        # deal with vertical movement
        if dir_of_move[1] < 0:  # move up
            if (ball.ball_y + dir_of_move[1]) >= 10:
                ball.ball_y += dir_of_move[1]
            else:
                ball.ball_y = 10
        elif dir_of_move[1] > 0:  # move down
            if (ball.ball_y + dir_of_move[1]) <= 573:
                ball.ball_y += dir_of_move[1]
            else:
                ball.ball_y = 573
        # deal with horizontal movement
        if dir_of_move[0] < 0:  # move left
            if (ball.ball_x + dir_of_move[0]) >= 5:
                ball.ball_x += dir_of_move[0]
            else:
                ball.ball_x = 5
        elif dir_of_move[0] > 0:  # move right
            if (ball.ball_x + dir_of_move[0]) <= 1145:
                ball.ball_x += dir_of_move[0]
            else:
                ball.ball_x = 1145

    def check_ball_collisions(self, ball, p1, p2):
        change_in_speed = 0.1
        dir_vector = [math.cos(math.radians(ball.angle_of_move)), math.sin(math.radians(ball.angle_of_move))]
        # check for collisions with player 1 (left player)
        if 25 <= ball.ball_x <= 38 and p1.pad_y - 30 <= ball.ball_y <= p1.pad_y + 30:
            ball.angle_of_move = randint(-50, 50)
            ball.speed += change_in_speed
            return 1  # 1 = there is a collision
        # check for collisions with player 2 (right player)
        elif 1112 <= ball.ball_x <= 1125 and p2.pad_y - 30 <= ball.ball_y <= p2.pad_y + 30:
            ball.angle_of_move = randint(130, 230)
            ball.speed += change_in_speed
            return 1
        # check for collision with top wall
        elif ball.ball_y == 10:
            if dir_vector[0] > 0 and dir_vector[1] < 0:  # going right
                ball.angle_of_move = randint(0, 50)
                ball.speed += change_in_speed
            elif dir_vector[0] < 0 and dir_vector[1] < 0:  # going left
                ball.angle_of_move = randint(91, 130)
                ball.speed += change_in_speed
            else:
                ball.angle_of_move = randint(0, 360)
                ball.speed += change_in_speed
            return 1
        # check for collision with bottom wall
        elif ball.ball_y == 573:
            if dir_vector[0] > 0 and dir_vector[1] > 0:  # going right
                ball.angle_of_move = randint(-50, 0)
                ball.speed += change_in_speed
            elif dir_vector[0] < 0 and dir_vector[1] > 0:  # going left
                ball.angle_of_move = randint(180, 230)
                ball.speed += change_in_speed
            else:
                ball.angle_of_move = randint(0, 360)
                ball.speed += change_in_speed
            return 1
        return 0  # 0 = no collision

    def check_goal(self, ball, p1, p2):
        if ball.ball_x < 25:  # player 2 has scored
            p2.increase_score()
            ball.ball_x = 575
            ball.ball_y = 291
            ball.speed = 1
            ball.angle_of_move = 180
            return 1  # 1 = yes goal
        elif ball.ball_x > 1125:  # player 1 has scored
            p1.increase_score()
            ball.ball_x = 575
            ball.ball_y = 291
            ball.speed = 1
            ball.angle_of_move = 0
            return 1
        return 0  # 0 = no goal

    def check_for_winner(self, p1, p2):
        if p1.score == 7:
            return ["Player 1 Wins", "Final Score : " + str(p1.score) + " - " + str(p2.score)]
        if p2.score == 7:
            return ["Player 2 Wins", "Final Score : " + str(p1.score) + " - " + str(p2.score)]
        return []  # return nothing if no one has won yet

    def process_game_instructions(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 0  # go back to main menu
            elif event.type == pygame.QUIT:
                return -1
        return 2  # stay on instructions

    def process_game_credits(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 0  # go back to main menu
            elif event.type == pygame.QUIT:
                return -1
        return 3  # stay on credits

    def process_game_end(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return 0  # go back to main menu
            elif event.type == pygame.QUIT:
                return -1
        return 4  # stay on end game
