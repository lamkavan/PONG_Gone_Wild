# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features many new features and visuals. This is for non-commercial use only.     #
######################################################################################################################

# GUI will take care of all the visuals from pygame

import pygame
import math

# initiate pygame
pygame.mixer.pre_init(22050, -16, 15, 512)
pygame.init()

# defining all game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
purple = (147, 112, 219)
orchid = (218, 112, 214)
yellow = (255, 255, 0)
skyblue = (135, 206, 235)
teal = (0, 128, 128)


class GUI:

    def __init__(self):
        self.width = 1150
        self.height = 650
        self.game_screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption("PONG Gone Wild")

    def prepare_text(self, text_list):
        prepared_text = []
        for tup in text_list:
            font_galaxy = pygame.font.Font("./font_styles/Galaxy Force.ttf", tup[1])
            prepared_text.append(font_galaxy.render(tup[0], True, tup[2]))
        return prepared_text

    def draw_dashed_line(self, pos1, pos2, color):
        if pos1[0] != pos2[0]:  # if not a vertical line
            slope = (pos2[1] - pos1[1]) / (pos2[0] - pos1[0])
            y_int = pos1[1] - (slope * pos1[0])
            x = min(pos1[0], pos2[0])
            while x <= max(pos1[0], pos2[0]):
                y1 = int((slope * x) + y_int)
                y2 = int((slope * (x + 10)) + y_int)
                pygame.draw.line(self.game_screen, color, [x, y1], [x + 10, y2], 2)
                x += 20
        else:  # if a vertical line
            y = min(pos1[1], pos2[1])
            x = pos1[0]
            while y <= max(pos1[1], pos2[1]):
                pygame.draw.line(self.game_screen, color, [x, y], [x, y + 10], 2)
                y += 20

    def draw_time_ray_icon(self, x, y):
        pygame.draw.line(self.game_screen, purple, [x - 20, y], [x - 10, y - 10], 2)
        pygame.draw.line(self.game_screen, purple, [x - 20, y], [x - 10, y + 10], 2)
        pygame.draw.line(self.game_screen, orchid, [x - 20, y], [x + 19, y], 2)
        pygame.draw.circle(self.game_screen, green, [x, y], 20, 2)

    def draw_time_ray_use(self, p_use_num, p_use):
        x = p_use.pad_x
        y = p_use.pad_y
        if p_use_num == 1:
            f = -1
        else:
            f = 1
        pygame.draw.line(self.game_screen, purple, [x, y], [x - (70 * f), y - 30], 2)
        pygame.draw.line(self.game_screen, purple, [x, y], [x - (70 * f), y + 30], 2)
        pygame.draw.line(self.game_screen, orchid, [x, y], [x - (1090 * f), y], 2)

    def draw_afterburner_icon(self, x, y):
        pygame.draw.line(self.game_screen, yellow, [x, y - 10], [x, y + 10], 2)
        pygame.draw.line(self.game_screen, yellow, [x, y - 10], [x - 7, y - 5], 2)
        pygame.draw.line(self.game_screen, yellow, [x, y - 10], [x + 7, y - 5], 2)
        pygame.draw.circle(self.game_screen, green, [x, y], 20, 2)

    def draw_afterburner_use(self, p_use_num, p_use):
        x = p_use.pad_x
        y = p_use.pad_y
        rec = (x - 30, y - 50, 60, 100)
        if p_use_num == 1:
            pygame.draw.arc(self.game_screen, yellow, rec, math.radians(90), math.radians(270), 2)
            pygame.draw.arc(self.game_screen, orange, rec, math.radians(45), math.radians(90), 2)
            pygame.draw.arc(self.game_screen, orange, rec, math.radians(270), math.radians(315), 2)
            pygame.draw.arc(self.game_screen, red, rec, math.radians(315), math.radians(405), 2)
        else:
            pygame.draw.arc(self.game_screen, yellow, rec, math.radians(270), math.radians(450), 2)
            pygame.draw.arc(self.game_screen, orange, rec, math.radians(90), math.radians(135), 2)
            pygame.draw.arc(self.game_screen, orange, rec, math.radians(225), math.radians(270), 2)
            pygame.draw.arc(self.game_screen, red, rec, math.radians(135), math.radians(225), 2)

    def draw_quantum_icon(self, x, y, fac):
        pygame.draw.line(self.game_screen, skyblue, [x - (1 * fac), y - (5 * fac)], [x - (1 * fac), y - (15 * fac)], 2)
        pygame.draw.line(self.game_screen, skyblue, [x - (1 * fac), y + (5 * fac)], [x - (1 * fac), y + (15 * fac)], 2)
        pygame.draw.line(self.game_screen, skyblue, [x - (5 * fac), y], [x - (15 * fac), y], 2)
        pygame.draw.line(self.game_screen, skyblue, [x + (5 * fac), y], [x + (15 * fac), y], 2)
        pygame.draw.line(self.game_screen, skyblue, [x + (6 * fac), y + (6 * fac)], [x - (6 * fac), y - (6 * fac)], 1)
        pygame.draw.line(self.game_screen, skyblue, [x + (6 * fac), y - (6 * fac)], [x - (6 * fac), y + (6 * fac)], 1)
        pygame.draw.circle(self.game_screen, teal, [x, y], 3, 0)
        if fac == 1:  # if fac is one then we are only drawing the icon so include this circle
            pygame.draw.circle(self.game_screen, green, [x, y], 20, 2)

    def draw_quantum_use(self, p_use):
        self.draw_quantum_icon(int(p_use.pad_x), int(p_use.pad_y), 5)

    def clear_screen(self):
        self.game_screen.fill(black)

    def draw_game_menu(self):
        # prepare text to be displayed
        text = [("PONG Gone Wild", 100, green), ("Play", 100, green), ("Instructions", 40, green),
                ("Credits", 60, green), ("A", 60, green), ("B", 60, green), ("C", 60, green)]
        menu_text = self.prepare_text(text)

        # displaying all main menu visuals #
        # title
        pygame.draw.line(self.game_screen, green, [240, 110], [910, 110], 2)
        self.game_screen.blit(menu_text[0], (self.width // 4.5, 0))
        # play button
        pygame.draw.rect(self.game_screen, blue, [170, 400, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [270, 400], [270, 310], 2)
        pygame.draw.line(self.game_screen, red, [270, 310], [210, 310], 2)
        pygame.draw.circle(self.game_screen, red, [180, 310], 30, 2)
        self.game_screen.blit(menu_text[1], (190, 385))
        self.game_screen.blit(menu_text[4], (166, 275))
        # instruction button
        pygame.draw.rect(self.game_screen, blue, [470, 400, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [570, 400], [570, 340], 2)
        pygame.draw.circle(self.game_screen, red, [570, 310], 30, 2)
        self.game_screen.blit(menu_text[2], (479, 415))
        self.game_screen.blit(menu_text[5], (560, 275))
        # credits button
        pygame.draw.rect(self.game_screen, blue, [770, 400, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [870, 400], [870, 310], 2)
        pygame.draw.line(self.game_screen, red, [870, 310], [930, 310], 2)
        pygame.draw.circle(self.game_screen, red, [960, 310], 30, 2)
        self.game_screen.blit(menu_text[3], (793, 405))
        self.game_screen.blit(menu_text[6], (949, 275))

    def draw_game_play(self, p1, p2, ball):
        # prepare text to be displayed
        text = [("Player 1", 30, orange), ("Player 2", 30, blue), (str(p1.score), 50, orange),
                (str(p2.score), 50, blue)]
        play_text = self.prepare_text(text)

        # display all the game play visuals
        # border --- The exact dimensions are 15 <= x <= 1135 and 2 <= y <= 580
        pygame.draw.line(self.game_screen, red, [0, 2], [1150, 2], 3)
        pygame.draw.line(self.game_screen, red, [0, 582], [1150, 582], 3)
        pygame.draw.line(self.game_screen, red, [2, 0], [2, 580], 3)
        pygame.draw.line(self.game_screen, red, [1148, 0], [1148, 580], 3)
        pygame.draw.line(self.game_screen, red, [575, 0], [575, 580], 3)
        # player 1
        pygame.draw.line(self.game_screen, p1.color, [round(p1.pad_x), round(p1.pad_y) - 30], [round(p1.pad_x),
                                                                                               round(p1.pad_y) + 30], 4)
        self.game_screen.blit(play_text[0], (15, 600))
        self.game_screen.blit(play_text[2], (500, 585))
        self.draw_dashed_line([15, 10], [15, 570], orange)
        if p1.powers[0] == 1:
            self.draw_time_ray_icon(200, 615)
        if p1.powers[1] == 1:
            self.draw_afterburner_icon(270, 615)
        if p1.powers[2] == 1:
            self.draw_quantum_icon(340, 615, 1)
        # player 2
        pygame.draw.line(self.game_screen, p2.color, [round(p2.pad_x), round(p2.pad_y) - 30], [round(p2.pad_x),
                                                                                               round(p2.pad_y) + 30], 4)
        self.game_screen.blit(play_text[1], (1035, 600))
        self.game_screen.blit(play_text[3], (630, 585))
        self.draw_dashed_line([1135, 10], [1135, 570], blue)
        if p2.powers[0] == 1:
            self.draw_time_ray_icon(800, 615)
        if p2.powers[1] == 1:
            self.draw_afterburner_icon(870, 615)
        if p2.powers[2] == 1:
            self.draw_quantum_icon(940, 615, 1)
        # ball
        pygame.draw.circle(self.game_screen, ball.color, [round(ball.ball_x), round(ball.ball_y)], ball.ball_radius, 0)

    def draw_game_instructions(self):
        # prepare text to be displayed
        text = [("Instructions", 100, green), ("Back", 70, green), ("A", 60, green), ("Movement", 40, green),
                ("Player1 (Left)", 30, orange), ("Player2 (Right)", 30, blue), ("Up = W", 26, orange),
                ("Down = S", 26, orange), ("Up = up arrow key ", 26, blue), ("Down = down arrow key", 26, blue),
                ("Powers", 40, green), ("Time Ray = C", 26, orange), ("Afterburner = V", 26, orange),
                ("Quantum Repulser = B", 26, orange), ("Time Ray = 1", 26, blue), ("Afterburner = 2", 26, blue),
                ("Quantum Repulser = 3", 26, blue),
                ("Time Ray: Shoot a high power laser at your foe to slow their movement", 26, green),
                ("Afterburner: Temporarily increases your movement speed", 26, green),
                ("Quantum Repulser: Emit a shock wave to vigorously knock the ball back towards your foe ", 26, green),
                ("To return to main menu when playing press ESC key", 26, green)]
        instruction_text = self.prepare_text(text)

        # displaying all instruction visuals #
        # title
        pygame.draw.line(self.game_screen, green, [345, 110], [820, 110], 2)
        self.game_screen.blit(instruction_text[0], (self.width // 3.2, 0))
        # movement instructions
        pygame.draw.line(self.game_screen, red, [100, 160], [100, 190], 2)
        pygame.draw.line(self.game_screen, red, [100, 190], [260, 190], 2)
        pygame.draw.line(self.game_screen, red, [450, 190], [600, 190], 2)
        self.game_screen.blit(instruction_text[3], (30, 120))
        self.game_screen.blit(instruction_text[4], (273, 175))
        self.game_screen.blit(instruction_text[5], (613, 175))
        self.game_screen.blit(instruction_text[6], (273, 220))
        self.game_screen.blit(instruction_text[7], (273, 250))
        self.game_screen.blit(instruction_text[8], (613, 220))
        self.game_screen.blit(instruction_text[9], (613, 250))
        # powers instructions
        pygame.draw.line(self.game_screen, red, [100, 310], [100, 340], 2)
        pygame.draw.line(self.game_screen, red, [100, 340], [260, 340], 2)
        pygame.draw.line(self.game_screen, red, [450, 340], [600, 340], 2)
        self.game_screen.blit(instruction_text[10], (30, 270))
        self.game_screen.blit(instruction_text[4], (273, 325))
        self.game_screen.blit(instruction_text[5], (613, 325))
        self.game_screen.blit(instruction_text[11], (273, 370))
        self.game_screen.blit(instruction_text[12], (273, 400))
        self.game_screen.blit(instruction_text[13], (273, 430))
        self.game_screen.blit(instruction_text[14], (613, 370))
        self.game_screen.blit(instruction_text[15], (613, 400))
        self.game_screen.blit(instruction_text[16], (613, 430))
        # powers descriptions
        self.draw_time_ray_icon(50, 497)
        self.draw_afterburner_icon(50, 540)
        self.draw_quantum_icon(50, 583, 1)
        self.game_screen.blit(instruction_text[17], (90, 480))
        self.game_screen.blit(instruction_text[18], (90, 523))
        self.game_screen.blit(instruction_text[19], (90, 566))
        # exit game instruction
        self.game_screen.blit(instruction_text[20], (90, 610))
        # back button
        pygame.draw.rect(self.game_screen, blue, [930, 20, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [1030, 110], [1030, 180], 2)
        pygame.draw.circle(self.game_screen, red, [1030, 210], 30, 2)
        self.game_screen.blit(instruction_text[1], (970, 23))
        self.game_screen.blit(instruction_text[2], (1016, 173))

    def draw_game_credits(self):
        # prepare text to be displayed
        text = [("Credits", 100, green), ("Back", 70, green), ("A", 60, green), ("Programming", 40, green),
                ("Kavan Lam (Using Python and Pygame)", 30, green), ("Visuals", 40, green),
                ("Galaxy Force by Pixel Sagas (font style)", 30, green), ("Kavan Lam (Using Pygame)", 30, green),
                ("Sounds", 40, green), ("Epic Night (Main Menu) by Kavan Lam (Using GarageBand)", 30, green),
                ("In game sound effects by Kavan Lam (Using GarageBand)", 30, green),
                ("End Game (Win Screen) by Kavan Lam (Using GarageBand)", 30, green),
                ("Deep Logic (In game) by Kavan Lam (Using GarageBand)", 30, green)]

        credits_text = self.prepare_text(text)

        # displaying all credit visuals #
        # title
        pygame.draw.line(self.game_screen, green, [440, 110], [710, 110], 2)
        self.game_screen.blit(credits_text[0], (self.width // 2.55, 0))
        # back button
        pygame.draw.rect(self.game_screen, blue, [930, 20, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [1030, 110], [1030, 180], 2)
        pygame.draw.circle(self.game_screen, red, [1030, 210], 30, 2)
        self.game_screen.blit(credits_text[1], (970, 23))
        self.game_screen.blit(credits_text[2], (1016, 173))
        # programming section
        pygame.draw.line(self.game_screen, red, [120, 160], [120, 190], 2)
        pygame.draw.line(self.game_screen, red, [120, 190], [240, 190], 2)
        self.game_screen.blit(credits_text[3], (30, 120))
        self.game_screen.blit(credits_text[4], (250, 170))
        # visuals section
        pygame.draw.line(self.game_screen, red, [120, 260], [120, 290], 2)
        pygame.draw.line(self.game_screen, red, [120, 290], [240, 290], 2)
        self.game_screen.blit(credits_text[5], (65, 220))
        self.game_screen.blit(credits_text[6], (250, 270))
        self.game_screen.blit(credits_text[7], (250, 310))
        # Sounds section
        pygame.draw.line(self.game_screen, red, [120, 360], [120, 390], 2)
        pygame.draw.line(self.game_screen, red, [120, 390], [240, 390], 2)
        self.game_screen.blit(credits_text[8], (65, 320))
        self.game_screen.blit(credits_text[9], (250, 370))
        self.game_screen.blit(credits_text[11], (250, 400))
        self.game_screen.blit(credits_text[12], (250, 430))
        self.game_screen.blit(credits_text[10], (250, 460))

    def draw_game_end(self, message):
        # prepare text to be displayed
        text = [(message[0], 100, green), (message[1], 70, green), ("Back", 70, green), ("A", 60, green)]
        end_text = self.prepare_text(text)

        # displaying all credit visuals #
        # winner
        self.game_screen.blit(end_text[0], (300, 50))
        self.game_screen.blit(end_text[1], (300, 200))
        # back button
        pygame.draw.rect(self.game_screen, blue, [930, 20, 200, 90], 0)
        pygame.draw.line(self.game_screen, red, [1030, 110], [1030, 180], 2)
        pygame.draw.circle(self.game_screen, red, [1030, 210], 30, 2)
        self.game_screen.blit(end_text[2], (970, 23))
        self.game_screen.blit(end_text[3], (1016, 173))
