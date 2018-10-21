# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features many new features and visuals. This is for non-commercial use only.     #
######################################################################################################################

# Ball will keep track of the ball moving around the screen


class Ball:

    def __init__(self, ball_color):
        self.ball_x = 575
        self.ball_y = 291
        self.ball_radius = 8
        self.color = ball_color
        self.speed = 1  # must be less than 10
        self.angle_of_move = 0  # angle in standard position
