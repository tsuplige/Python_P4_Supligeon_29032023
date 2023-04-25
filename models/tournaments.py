import random
from models.round import Round

class Tournament:
    """
    Class Tournament (tournois)


     Attb:
        attribut_1 : name -- le Nom
        attribut_2 : locale  -- le lieu
        attribut_3 : tournament_begin_date -- la date de debut du tournois
        attribut_4 : tournament_end_date -- la date de fin du tournois
        attribut_5 -- la description
        attribut_6 : player_list -- la list de joueurs
        attribut_7 -- le nombre de round

    """
    def __init__(self, name, locale, tournament_begin_date, tournament_end_date, 
                 description, player_list = None, number_of_round = 4):
        self.name = name
        self.locale = locale
        self.tournament_begin_date = tournament_begin_date
        self.tournament_end_date = tournament_end_date
        self.round_list = []
        if player_list is None:
            player_list = []
        self.player_list = player_list
        self.description = description
        self.number_of_round = number_of_round
        self.current_round = 0

    def start_round(self):
        """
        melange la list de joueur au premier tour, et pour les 
        autre tour tri les jueur par point la listinstancie un objet Round

        """

        if self.current_round == 1:
            random.shuffle(self.player_list)
        else:
            self.sort_by_point()

        match_list = self.generate_pair()

        for match in match_list:
            p1 = match[0][0]
            p2 = match[1][0]
            print(p1.first_name, p1.last_name, "    vs   ", p2.first_name, p2.last_name, "\n" )

        self.round_list.append(Round(self.current_round, match_list))

    def print_match_list(self, match_list):
         
         for match in match_list:
              print

    def sort_by_point(self):
        """
       
        tri les joueurs par point

        """

        self.player_list = sorted(self.player_list, key=lambda player: player.point, reverse=True)

    def generate_pair(self):

        """
        
        genere les paire

        """

        pairs = []
        scoreP1 = 0
        scoreP2 = 0
        players = self.player_list
        for i in range(0, len(players), 2):
                    pairs.append(([players[i], scoreP1],[players[i+1], scoreP2]))

        return pairs
