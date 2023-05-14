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

    def __init__(
        self,
        name,
        locale,
        tournament_begin_date,
        tournament_end_date,
        description,
        player_list=None,
        number_of_round=4,
    ):
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
        lance un round

        """

        match_list = []
        # melange la list de joueur au premier tour
        if self.current_round == 1:
            random.shuffle(self.player_list)
            # genere les tuples du premier round
            match_list = self.generate_first_pairs()
        else:
            # tri les jueur par point
            self.sort_by_point()
            match_list = self.generate_pair()
        # instancie un objet Round
        self.round_list.append(Round(self.current_round, match_list))

        return match_list

    def end_round(self, match_list_update):
        # met a jour les resultat dans match dans match_list
        self.round_list[self.current_round - 1].match_list = match_list_update
        # ajoute la date de fin de round
        self.round_list[self.current_round - 1].add_end_round_date()

    def sort_by_point(self):
        """
        tri les joueurs par point
        """

        self.player_list = sorted(
            self.player_list, key=lambda player: player.point, reverse=True
        )

    def generate_first_pairs(self):
        """
        genere les tuples du premier round
        """

        pairs = []
        scoreP1 = 0
        scoreP2 = 0
        players = self.player_list

        # verifie si il y a un nombre paire de joueurs
        if len(players) % 2 == 0:
            for i in range(0, len(players), 2):
                # cree les tuples
                pairs.append(([players[i], scoreP1], [players[i + 1], scoreP2]))
        else:
            for i in range(0, len(players) - 1, 2):
                pairs.append(([players[i], scoreP1], [players[i + 1], scoreP2]))
            pairs.append(
                (
                    [players[len(players) - 1], scoreP1],
                    [Player("joueur", "vide", "10012001"), scoreP2],
                )
            )

        return pairs

    def generate_pair(self):
        """
        genere les tuples
        """

        pairs = []
        scoreP1 = 0
        scoreP2 = 0
        players = self.player_list

        for i, player in enumerate(players):
            a = 0
            while True:
                try:
                    player2 = players[i + a]

                except IndexError:
                    # si hors de la list on force la combinaison de joueur
                    a = 0
                    player2 = players[i + a]
                    break

                # verifie si les joueurs on joué ensemble et/ou si il sont dans dans match
                if (
                    self.have_already_play(player, player2)
                    and self.is_not_in_match_list(player, pairs)
                    and self.is_not_in_match_list(player2, pairs)
                ):
                    pairs.append(
                        (
                            [player, scoreP1],
                            [player2, scoreP2],
                        )
                    )
                    break
                # si il reste deux joueur forcé la combinaison
                elif i == len(players) - 1 and self.is_not_in_match_list(player, pairs):
                    for i, player in enumerate(players):
                        if self.is_not_in_match_list(player, pairs):
                            player2 = player
                    pairs.append(
                        (
                            [player, scoreP1],
                            [player2, scoreP2],
                        )
                    )
                    break
                else:
                    a += 1
                    continue
        return pairs

    def is_not_in_match_list(self, player, lmatch_list):
        """
        vérifie si un joueur et dans la list de match
        """
        for match in lmatch_list:
            if (
                player.first_name == match[0][0].first_name
                and player.last_name == match[0][0].last_name
            ):
                return False
            elif (
                player.first_name == match[1][0].first_name
                and player.last_name == match[1][0].last_name
            ):
                return False
        return True

    def have_already_play(self, player, player2):
        """
        vérifie si deux joueur on deja joué l'un contre l'autre
        et si les joueurs ne sont pas la meme personne
        """
        all_match_list = []

        for round in self.round_list:
            for match in round.match_list:
                all_match_list.append(match)
        for match in all_match_list:
            if (
                player.first_name == match[0][0].first_name
                and player.last_name == match[0][0].last_name
            ) and (
                player2.first_name == match[1][0].first_name
                and player2.last_name == match[1][0].last_name
            ):
                return False
            elif (
                player.first_name == match[1][0].first_name
                and player.last_name == match[1][0].last_name
            ) and (
                player2.first_name == match[0][0].first_name
                and player2.last_name == match[0][0].last_name
            ):
                return False
            elif (
                player.first_name == player2.first_name
                and player.last_name == player2.last_name
            ):
                return False
        return True

    def save_tournament_data(self):
        """
        convertie les donnée du tournois et donnée JSON
        """
        player_data = []
        rounds_data = []

        for round in self.round_list:
            rounds_data.append(round.save_round_data())

        for player in self.player_list:
            player_data.append(player.save_player_data())

        tournament_data = {
            "name": self.name,
            "locale": self.locale,
            "tournament_begin_date": self.tournament_begin_date,
            "tournament_end_date": self.tournament_end_date,
            "description": self.description,
            "is_not_finish": self.is_not_finish,
            "number_of_round": self.number_of_round,
            "current_round": self.current_round,
            "round_list": rounds_data,
            "players_list": player_data,
        }

        return tournament_data

    def load_round_data(self, round_data):
        """
        convertie les donnée JSON en objet Round
        et en tuple contenant des objet Player
        """
        for round in round_data:
            match_list = []
            for match in round["match_list"]:
                match_list.append(
                    (
                        [
                            Player(
                                match["joueur_1"]["first_name"],
                                match["joueur_1"]["last_name"],
                                match["joueur_1"]["birth_date"],
                                match["joueur_1"]["point"],
                            ),
                            match["score_J1"],
                        ],
                        [
                            Player(
                                match["joueur_2"]["first_name"],
                                match["joueur_2"]["last_name"],
                                match["joueur_2"]["birth_date"],
                                match["joueur_2"]["point"],
                            ),
                            match["score_J2"],
                        ],
                    )
                )

            self.round_list.append(
                Round(
                    round["current_round"],
                    match_list,
                    round["round_begin_date"],
                    round["round_end_date"],
                )
            )
