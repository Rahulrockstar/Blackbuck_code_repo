class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 30
        self.team2_score = 30
        self.team1_overs = 10
        self.team2_overs = 9
        self.nrr1 = 200
        self.nrr2 = 200

def update_scores(self, team, score, overs):
    if team == self.team1:
        self.team1_score += score
        self.team1_overs += overs
        self.nrr1 = (self.team1_score/self.team1_overs) - (self.team2_score/self.team2_overs)
    elif team == self.team2:
        self.team2_score += score
        self.team2_overs += overs
        self.nrr2 = (self.team2_score/self.team2_overs) - (self.team1_score/self.team1_overs)

    def get_scores(self):
        print("{}: {}-{} ({:.1f} overs)".format(self.team1, self.team1_score, self.team2_score, self.team1_overs))
        print("{}: {}-{} ({:.1f} overs)".format(self.team2, self.team2_score, self.team1_score, self.team2_overs))

    def get_nrr(self):
        print("{}: {:.2f}".format(self.team1, self.nrr1))
        print("{}: {:.2f}".format(self.team2, self.nrr2))
        
        
print(Match)