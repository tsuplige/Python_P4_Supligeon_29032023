import random
from models.round import Round
from models.player import Player

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
        self.description = description
        if player_list is None:
            player_list = []
        self.player_list = player_list
        self.number_of_round = number_of_round
        self.current_round = 1
        self.is_not_finish = True
        self.round_list = []

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

        self.round_list.append(Round(self.current_round, match_list))

        return match_list


    def end_round(self, match_list_update):
         self.round_list[self.current_round - 1].match_list = match_list_update
         self.round_list[self.current_round - 1].add_end_round_date()

    # def print_match_list(self, match_list):
         
    #      for match in match_list:
    #         print

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
        if len(players)%2 == 0:
            for i in range(0, len(players), 2):
                pairs.append(([players[i], scoreP1],[players[i+1], scoreP2]))
        else:
            for i in range(0, len(players)- 1, 2):
                pairs.append(([players[i], scoreP1],[players[i+1], scoreP2]))
            pairs.append(([players[len(players) - 1], scoreP1], [Player("joueur","vide","10012001"), scoreP2]))
            

        return pairs
    
    def save_tournament_data(self):
        
        player_data = []
        rounds_data = []

        for round in self.round_list:
            rounds_data.append(round.save_round_data())
            
        for player in self.player_list:
            player_data.append( player.save_player_data())

        tournament_data = {
            "name": self.name,
            "locale": self.locale,
            "tournament_begin_date": self.tournament_begin_date,
            "tournament_end_date": self.tournament_end_date,
            "description": self.description,
            "is_not_finish": self.is_not_finish,
            "number_of_round" : self.number_of_round,
            "current_round" : self.current_round,
            "round_list": rounds_data,
            "players_list" : player_data
        }

        return tournament_data
    def load_round_data(self, round_data):
         
        for round in round_data:
            match_list = []
            for match in round["match_list"]:
                match_list.append(([Player(match["joueur_1"]['first_name'],match["joueur_1"]['last_name'],match["joueur_1"]['birth_date'],match["joueur_1"]['point']), match["score_J1"]],[Player(match["joueur_2"]['first_name'],match["joueur_2"]['last_name'],match["joueur_2"]['birth_date'],match["joueur_2"]['point']), match["score_J2"]]))

            self.round_list.append(Round( round["current_round"], match_list, round["round_begin_date"], round["round_end_date"]))
    

    # def generate_pair(self):

    #     """
        
    #     genere les paire

    #     """

    #     pairs = []
    #     players = self.player_list

    #     if len(players) % 2 == 1:
    #         players = players[:-1]

    #     for i in range(0, len(players), 2):
    #         player1 = players[i]
    #         player2 = players[i + 1]
    #         # pairs.append(([players[i], 0],[players[i+1], 0]))

    #         while self.check_paire(player1, player2):
    #             # Si oui, prendre le joueur suivant dans la liste
    #             i += 2
    #             player1 = players[i]
    #             player2 = players[i + 1]

    #         pairs.append(([player1, 0],[player2, 0]))


    #     return pairs
    
    # def check_paire(self, player1, player2):
    #     # Vérifier si les joueurs ont déjà joué l'un contre l'autre

    #     for round in self.round_list:
    #         for match in round.match_list:
    #             if (match[0][0] == player1 and match[1][0] == player2) or (match[1][0] == player1 and match[0][0] == player2):
    #                 return True
    #         return False