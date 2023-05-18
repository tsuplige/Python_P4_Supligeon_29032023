from models.player import Player
from models.tournaments import Tournament
from typing import List
import json
import os
import sys


class Controllers:
    """
    class Controllers

    Attb :

        attribut_1 -- la Vue

    """

    def __init__(self, view):
        self.players: List[Player] = []
        self.participant: List[Player] = []
        self.more_player = True
        self.next_round = True
        self.view = view
        self.tournament_list = []

    def launch_app(self):
        # verifie si /data existe et si non le créé
        if os.path.exists("data") and os.path.isdir("data"):
            self.convert_and_load_from_json()
        else:
            os.makedirs("data")
        # lance l'app
        self.main_menu()

    def main_menu(self):
        """

        menu principal


        """

        menu_input = self.view.main_menu_prompt()

        if menu_input == "1":
            self.get_players()
            self.main_menu()
        elif menu_input == "2":
            ask_to_continue = self.view.show_players_list_prompt(self.participant)
            if ask_to_continue:
                self.main_menu()
            else:
                self.main_menu()
        elif menu_input == "3":
            self.start_new_tournament()
        elif menu_input == "4":
            self.load_tournament_menu()
        elif menu_input == "5":
            sys.exit()
        else:
            self.main_menu()

    def manage_tournament(self, tournament):
        """
        gestion d'un tournois
        """

        # tant qu'on n'as pas fais tout les Round
        while tournament.current_round <= tournament.number_of_round:
            self.view.title_prompt("Round " + str(tournament.current_round))
            match_list = tournament.start_round()

            self.next_round = True

            while self.next_round is True:
                self.tournament_menu(
                    str(tournament.current_round), match_list, tournament
                )
                self.view.title_prompt("Resultat du Round")
                match_list = self.add_point_for_match(match_list, tournament)

            tournament.end_round(match_list)
            # incremente current round pour passé au round suivant
            tournament.current_round += 1
        tournament.is_not_finish = False
        # sauvegarde les donnée du tournois fini
        self.save_tournament_data(tournament)
        self.end_tournament_menu(
            tournament,
            tournament.name,
            tournament.locale,
            tournament.tournament_begin_date,
            tournament.tournament_end_date,
            tournament.description,
            tournament.round_list,
        )

    def start_new_tournament(self):
        """
        instancie un objet Tournois et lance le tournois
        """
        (
            name,
            locale,
            tournament_begin_date,
            tournament_end_date,
            description,
        ) = self.view.start_tournament_prompt()

        self.add_player_to_tournament(name)

        new_tournament = Tournament(
            name,
            locale,
            tournament_begin_date,
            tournament_end_date,
            description,
            self.players,
        )

        self.players = []

        self.manage_tournament(new_tournament)

    def add_player_to_tournament(self, tournament_name):
        while True:
            result = self.view.add_player_to_tournament_promp(
                self.participant, tournament_name
            )

            try:
                int_result = int(result)
            except ValueError:
                self.add_player_to_tournament(tournament_name)

            if int_result == 0:
                if len(self.players) < 4:
                    print(
                        self.view.error_color(
                            "il n'y a pas assez de joueurs, veuillez en ajouter"
                        )
                    )
                    continue
                elif len(self.players) % 2 != 0:
                    print(
                        self.view.error_color(
                            "nombres de joueur impaire, veuillez en ajouter"
                        )
                    )
                    continue
                break
            elif int_result == 1:
                print(self.players)
                self.view.show_players_list_prompt(self.players)
                continue
            elif int_result == 2:
                self.get_players()
                self.players.append(self.participant[len(self.participant) - 1])
                continue
            else:
                try:
                    self.players.append(self.participant[int_result - 3])
                    continue
                except IndexError:
                    print(self.view.error_color("aucun joueur a cette index"))
                    continue

    def add_point_for_match(self, match_list, tournament):
        """
        ajoute les point au joueur
        """
        new_match_list = []

        for match in match_list:
            p1 = match[0][0]
            p2 = match[1][0]

            result = self.view.ask_for_result_prompt(
                p1.first_name, p1.last_name, p2.first_name, p2.last_name
            )

            if result != "1" or result != "2" or result != "3":
                print(self.view.error_color("\n" + result + " n'est pas pris en compte, veuillez tapez 1 pour"
                                            " une victoire, 2 pour une défaite ou 3 pour une égalité"))
                result = self.view.ask_for_result_prompt(
                    p1.first_name, p1.last_name, p2.first_name, p2.last_name
                )
            for player in tournament.player_list:
                if (
                    player.first_name == p1.first_name
                    and player.last_name == p1.last_name
                ):
                    if result == "1":
                        player.add_point("1")
                        match[0][1] = 1
                        match[1][1] = 0
                        new_match_list.append(match)
                    elif result == "2":
                        for player2 in tournament.player_list:
                            if (
                                player2.first_name == p2.first_name
                                and player2.last_name == p2.last_name
                            ):
                                player2.add_point("1")
                                match[0][1] = 0
                                match[1][1] = 1
                                new_match_list.append(match)
                                break
                    elif result == "3":
                        player.add_point("2")
                        for player2 in tournament.player_list:
                            if (
                                player2.first_name == p2.first_name
                                and player2.last_name == p2.last_name
                            ):
                                player2.add_point("2")
                                match[0][1] = 0.5
                                match[1][1] = 0.5
                                new_match_list.append(match)
                                break
                    break
        return new_match_list

    def tournament_menu(self, current_round, match_list, tournament):
        """
        Methode : tournament_menu()

        recupere le input de tournament_menu_prompt()

        """
        menu_input = self.view.tournament_menu_prompt(current_round, tournament.name)

        while not menu_input:
            menu_input = self.view.tournament_menu_prompt(
                current_round, tournament.name
            )
        if menu_input == "1":
            self.view.print_match(match_list, current_round)
            self.tournament_menu(current_round, match_list, tournament)
        elif menu_input == "2":
            ask_to_continue = self.view.print_players_list_by_point(
                tournament.player_list
            )
            if ask_to_continue:
                self.tournament_menu(current_round, match_list, tournament)
            else:
                self.tournament_menu(current_round, match_list, tournament)
        elif menu_input == "3":
            self.save_tournament_data(tournament)
            self.tournament_menu(current_round, match_list, tournament)
        elif menu_input == "4":
            self.next_round = False
        elif menu_input == "5":
            self.main_menu()
        else:
            self.tournament_menu(current_round, match_list, tournament)

    def get_players(self):
        """
        permets d'ajouter des joueurs a la liste de joueurs et appelle la
        methode save_player_data() pour ajouter les donnée créé dans
        le fichier de saugdarde data/players.json
        """

        if self.more_player is False:
            self.more_player = True
        while self.more_player is True:
            (
                nom,
                prenom,
                date_de_naissance,
            ) = self.view.add_players_to_tournament_list_prompt()
            if not (nom, prenom, date_de_naissance):
                return
            self.participant.append(Player(nom, prenom, date_de_naissance))

            """
            permets de mettre fin à la boucle si l'utilisateurs a finis
            d'ajouter des joueurs
            """
            ask_to_continue = input(
                self.view.question_color(
                    "voulez vous ajouter d'autre joueur ?"
                    " \n o pour oui\n n pour non\n"
                )
            )
            if ask_to_continue == "o" or ask_to_continue == "O":
                self.more_player = True
            elif ask_to_continue == "n" or ask_to_continue == "N":
                self.more_player = False

        self.save_player_data()

    def get_players_in_tournament(self):
        pass

    def end_tournament_menu(
        self,
        tournament,
        name,
        locale,
        tournament_begin_date,
        tournament_end_date,
        description,
        round_list,
    ):
        """
        menu de fin de tournois
        """
        menu_input = self.view.tournament_end_menu_prompt(
            name, locale, tournament_begin_date, tournament_end_date
        )

        while not menu_input:
            menu_input = self.view.tournament_end_menu_prompt(
                name, locale, tournament_begin_date, tournament_end_date
            )
        if menu_input == "1":
            ask_to_continue = self.view.print_players_list_by_point(
                tournament.player_list
            )
            self.end_tournament_menu(
                tournament,
                name,
                locale,
                tournament_begin_date,
                tournament_end_date,
                description,
                round_list,
            )
        elif menu_input == "2":
            self.view.print_all_round(tournament.round_list)
            self.end_tournament_menu(
                tournament,
                name,
                locale,
                tournament_begin_date,
                tournament_end_date,
                description,
                round_list,
            )
        elif menu_input == "3":
            self.main_menu()
        else:
            self.end_tournament_menu(
                tournament,
                name,
                locale,
                tournament_begin_date,
                tournament_end_date,
                description,
                round_list,
            )
            return ask_to_continue

    def save_player_data(self):
        """
        converti les données Joueur et les sauvgarde dans un fichier Json
        """
        data = []

        for player in self.participant:
            data.append(player.save_participant_data())

        with open("data/players.json", "w") as f:
            json.dump(data, f)

    def save_tournament_data(self, new_tournament):
        """
        convertie les données tournois et le sauvgarde dans le fichier Json
        """
        tournament_data = []
        self.tournament_list.append(new_tournament)

        for tournament in self.tournament_list:
            tournament_data.append(tournament.save_tournament_data())
        with open("data/tournament_data.json", "w") as f:
            json.dump(tournament_data, f)

    def load_tournament_menu(self):
        input_result = self.view.load_tournament_menu_prompt(self.tournament_list)

        try:
            int_input_result = int(input_result)
        except ValueError:
            self.load_tournament_menu()

        if int_input_result == 0:
            self.main_menu()
        elif int_input_result > 0 and (
            int_input_result < len(self.tournament_list)
            or int_input_result == len(self.tournament_list)
        ):
            self.load_tounament(self.tournament_list[int_input_result - 1])
        else:
            self.load_tournament_menu()

    def load_tounament(self, tournament):
        """
        lance un tournois sauvegardé
        """
        if tournament.is_not_finish:
            self.manage_tournament(tournament)
        else:
            self.end_tournament_menu(
                tournament,
                tournament.name,
                tournament.locale,
                tournament.tournament_begin_date,
                tournament.tournament_end_date,
                tournament.description,
                tournament.round_list,
            )

    def convert_and_load_from_json(self):
        "charge toute les donnée json"
        if os.path.exists("data/players.json"):
            with open("data/players.json", "r") as f:
                datas = f.read()
                for data in json.loads(datas):
                    self.participant.append(
                        Player(
                            data["last_name"], data["first_name"], data["birth_date"]
                        )
                    )

        if os.path.exists("data/tournament_data.json"):
            with open("data/tournament_data.json", "r") as f:
                datas = f.read()
                if datas:
                    for data in json.loads(datas):
                        load_player_list = []
                        for player in data["players_list"]:
                            load_player_list.append(
                                Player(
                                    player["last_name"],
                                    player["first_name"],
                                    player["birth_date"],
                                    player["point"],
                                )
                            )
                        load_tournament = Tournament(
                            data["name"],
                            data["locale"],
                            data["tournament_begin_date"],
                            data["tournament_end_date"],
                            data["description"],
                            load_player_list,
                            data["number_of_round"],
                        )
                        load_tournament.current_round = data["current_round"]
                        load_tournament.is_not_finish = data["is_not_finish"]
                        load_tournament.load_round_data(data["round_list"])
                        self.tournament_list.append(load_tournament)
