class Match:
    def __init__(self, player1, score1, player2, score2):
        self.players = ([player1, score1], [player2, score2])
        self.result = None

    def __str__(self):
        return f"Match: {self.players[0][0].first_name} vs. {self.players[1][0].first_name}"

    # Fonction qui inscrit le score du match en cours et met à jour le score du joueur
    def record_result(self):
        while True:
            self.result = input(
                f"Enter the result for {self.players[0][0].first_name} {self.players[0][0].last_name} vs."
                f" {self.players[1][0].first_name} {self.players[1][0].last_name} \n"
                f"The winner is: 1 for {self.players[0][0].first_name}, 2 for {self.players[1][0].first_name}, "
                f"0 for a draw: ")

            if self.result in ('1', '2', '0'):
                if self.result == '1':
                    self.players[0][0].is_winner()
                elif self.result == '2':
                    self.players[1][0].is_winner()
                elif self.result == '0':
                    self.players[0][0].is_draw()
                    self.players[1][0].is_draw()

                for player, score in self.players:
                    player.score += score

                break
            else:
                print("Invalid input. Please enter 1, 2, or 0.")
