# PONG Gone Wild
# Date: Aug 30, 2018
# By: Kavan Lam

######################################################################################################################
# The following is an independent game project. The game is called 'PONG Gone Wild' and is a twist to the classic    #
# arcade game, 'PONG'. This version features many new features and visuals. This is for non-commercial use only.     #
######################################################################################################################

# Player will keep track of a single player's information during a single match


class Player:

    def __init__(self, player_color, player_num):
        self.score = 0
        if player_num == 1:
            self.pad_x = 30
        else:
            self.pad_x = 1120
        self.pad_y = 291
        self.color = player_color
        self.powers = [1, 1, 1]
        self.speed = 2
        self.time_ray_hit_cooldown = 0  # how much time this player will be slowed down
        self.afterburner_cooldown = 0  # how much time this player will be moving faster

    def increase_score(self):
        self.score += 1
