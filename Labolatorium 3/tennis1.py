class TennisGame1:

    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def draw(self):
        if self.p1points < 3:
            return self.SCORES[self.p1points] + "-All"
        return "Deuce"
    
    def advantage_or_win(self):
        diff = self.p1points - self.p2points
        if diff == 1:
            return "Advantage " + self.player1_name
        elif diff == -1:
            return "Advantage " + self.player2_name
        elif diff >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def score(self):
        if self.p1points == self.p2points:
            return self.draw()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.advantage_or_win()
        else:
            return self.SCORES[self.p1points] + "-" + self.SCORES[self.p2points]