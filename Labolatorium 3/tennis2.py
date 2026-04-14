class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        result = ""
        score_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

        if self.p1points == self.p2points and self.p1points < 3:
            result = score_map[self.p1points] + "-All"

        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        p1res = ""
        p2res = ""

        if self.p1points > 0 and self.p2points == 0 and self.p1points < 4:
            p1res = score_map[self.p1points]
            p2res = "Love"
            result = p1res + "-" + p2res

        if self.p2points > 0 and self.p1points == 0 and self.p2points < 4:
            p2res = score_map[self.p2points]
            p1res = "Love"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p1points < 4:
            p1res = score_map[self.p1points]
            p2res = score_map.get(self.p2points, "")
            result = p1res + "-" + p2res

        if self.p2points > self.p1points and self.p2points < 4:
            p2res = score_map[self.p2points]
            p1res = score_map.get(self.p1points, "")
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage player1"

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage player2"

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for player1"

        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for player2"

        return result

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1