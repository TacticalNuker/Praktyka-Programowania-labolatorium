class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points < 4 and self.p2points < 4 and (self.p1points + self.p2points < 6):
            SCORES = ["Love", "Fifteen", "Thirty", "Forty"]
            score_player1 = SCORES[self.p1points]
            return score_player1 + "-All" if (self.p1points == self.p2points) else score_player1 + "-" + SCORES[self.p2points]
        else:
            if self.p1points == self.p2points:
                return "Deuce"

            diff = self.p1points - self.p2points
            leader = self.p1_name if diff > 0 else self.p2_name

            if abs(diff) == 1:
                return "Advantage " + leader
            else:
                return "Win for " + leader