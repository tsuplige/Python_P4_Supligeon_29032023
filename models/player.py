
class Player:
    """
    Class Players.
    
    has name, last name, birth date and cans have national chess id
    """
    def __init__(self, LAST_NAME, NAME, BIRTH_DATE, NATIONNAL_CHESS_ID = 0):
        self.LAST_NAME = LAST_NAME
        self.NAME = NAME
        self.BIRTH_DATE = BIRTH_DATE

class PlayersList:
    """
    class PlayersListe

    has list of players
    """
    def __init__(self, plauers):
        self.players = plauers

    def add_player(self, player):
        self.players.append(player)


    
timote = Player("CHALUMO", "TIMOTE", "12021998")
bertrand = Player("CELO", "Bertrand", "24041973")
lisa = Player("fruit", "Lisa", "24111994")

Tournament2023_playerlist = PlayersList([timote, bertrand])

Tournament2023_playerlist.add_player(lisa)
list = []
for player in Tournament2023_playerlist.players:
    list.append(vars(player))

print(list)