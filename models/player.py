
class Player:
    """
    Class Players.
    
    has prenom, last name, birth date and cans have national chess id
    """
    def __init__(self, nom, prenom, birth_date,point = 0, nationnal_chess_id = 0):
        self.nom = nom
        self.prenom = prenom
        self.birth_date = birth_date
        self.point = point
        self.nationnal_chess_id = nationnal_chess_id
    def add_point(self, victoire):
        if victoire == "v":
            self.point += 1
        elif victoire == "e":
            self.point += 0.5
        elif victoire == "d":
            print("dommage,vous aller y arriver !")


    
# timote = Player("CHALUMO", "TIMOTE", "12021998")
# bertrand = Player("CELO", "Bertrand", "24041973")
# lisa = Player("fruit", "Lisa", "24111994")

# Tourprenomnt2023_playerlist = PlayersList([timote, bertrand])

# Tourprenomnt2023_playerlist.add_player(lisa)

# list = []
# for player in Tourprenomnt2023_playerlist.players:
#     list.append(vars(player))

# print(list)