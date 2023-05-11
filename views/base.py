from datetime import datetime


class View:
    def __init__(self):
        pass
        self.color_red = "\033[31m"
        self.color_green = "\033[32m"
        self.color_yellow = "\033[33m"
        self.color_blue = "\033[34m"
        self.color_magenta = "\033[35m"
        self.color_cyan = "\033[36m"
        self.color_white = "\033[37m"
        self.color_reset = "\033[0m"

    def main_menu_prompt(self):
        print(
            self.exemple_color(
                "\n\n Inscrire des joueur, "
                "consulter la liste des joueurs inscrit au tournois,"
                " Lancer le Tournois, consulter"
                " la liste des precedent tournois\n\n"
            )
        )

        start_input = input(
            self.question_color(
                "que voulez vous faire ?\n1 pour inscrire des joueur \n"
                "2 pour consulter la liste de joueurs\n"
                "3 pour lancer le tournois\n"
                "4 Charger les Tournois enregistré : \n"
            )
        )
        return start_input

    def add_players_to_tournament_list_prompt(self):
        prenom = input(self.exemple_color("tapez le prenom du joueur : "))
        while not prenom:
            print(self.error_color("champs vide"))
            prenom = input(self.exemple_color("tapez le prenom du joueur : "))
        nom = input(self.exemple_color("tapez le nom du joueur : "))
        while not nom:
            print(self.error_color("champs vide"))
            nom = input(self.exemple_color("tapez le nom du joueur : "))
        date_de_naissance = input(
            self.exemple_color("tapez la date de naissance "
                               "(au format jjmmaaaa) : ")
        )
        while not date_de_naissance:
            print(self.error_color("champs vide"))
            date_de_naissance = input(
                self.exemple_color("tapez la date de naissance"
                                   " (au format jjmmaaaa) : ")
            )
        return nom, prenom, date_de_naissance

    def show_players_list_prompt(self, player_list):
        for player in player_list:
            player.last_name = player.last_name.lower().title()

        self.title_prompt("liste des joueurs")

        sorted_players = sorted(player_list, key=lambda x: x.last_name)

        for player in sorted_players:
            format_birth_date = self.format_date(player.birth_date)

            print(
                "        ",
                player.first_name,
                "  |   ",
                player.last_name,
                "  |   ",
                format_birth_date,
            )
            print("   _____________________________________________________\n")

        ask_to_continue = input(
            "\n\nPour revenir au menu principal "
            "appuyer sur n'importe quelle touche\n"
        )

        return ask_to_continue

    def tournament_menu_prompt(self, current_round, tournament_name):
        print(
            self.title_color(
                "Tournois : " + tournament_name + "\nRound "
                + current_round + " Menu :"
            )
        )

        start_input = input(
            self.question_color(
                "\n 1 pour afficher les matchs du Round \n"
                " 2 pour consulter le Classement Actuelle\n"
                " 3 pour sauvegarder les donnée du tournois\n"
                " 4 pour Finir le round, Attribuer les Points:\n"
                " 5 pour retourner au menu principal\n"
            )
        )
        return start_input

    def print_match(self, match_list, current_round):
        print(self.title_color("\nMatch Round : " + current_round + "\n"))
        for match in match_list:
            p1 = match[0][0]
            p2 = match[1][0]
            print(
                p1.first_name,
                p1.last_name,
                "    -   ",
                p2.first_name,
                p2.last_name,
                "\n",
            )

    def tournament_end_menu_prompt(
        self, name, locale, tournament_begin_date, tournament_end_date
    ):
        format_begin_date = self.format_date(tournament_begin_date)
        format_end_date = self.format_date(tournament_end_date)

        print(self.title_prompt("Tournois : " + name))
        print(
            self.title_color(
                "\n organisé à "
                + locale
                + "\n du "
                + format_begin_date
                + " au "
                + format_end_date
                + " :\n"
            )
        )

        start_input = input(
            self.question_color(
                "\n 1 pour consulter le Classement Final\n"
                " 2 pour afficher tout les Round du Tournois\n"
                " 3 pour retourner au menu principale\n"
            )
        )
        return start_input

    def load_tournament_menu_prompt(self, tournament_list):
        print(self.title_prompt("Charger un Tournois"))

        print(self.question_color("\n0 pour retourner au menu principal"))
        i = 1
        for tournament in tournament_list:
            print(
                self.question_color(
                    f"{i} pour charger le tournois : {tournament.name}"
                    " au tour {tournament.current_round}"
                )
            )
            i = i + 1

        load_input = input(
            self.question_color("quelle tournois voulez vous charger ?\n")
        )

        return load_input

    def format_date(self, date):
        date_obj = datetime.strptime(date, "%d%m%Y")
        date_formatted = date_obj.strftime("%d-%m-%Y")

        return date_formatted

    def print_players_list_by_point(self, player_list):
        for player in player_list:
            player.last_name = player.last_name.lower().title()

        self.title_prompt("Classement des joueurs")

        sorted_players = sorted(player_list, key=lambda x: x.point, reverse=True)
        i = 0
        for player in sorted_players:
            i += 1

            print(
                "        n°",
                i,
                player.first_name,
                "  |   ",
                player.last_name,
                "  |   point :",
                player.point,
            )
            print("   _____________________________________________________\n")

    def print_round(self, round_list):
        pass

    def print_players_sorted(self, player_list):
        pass

    def start_tournament_prompt(self):
        name = input(self.exemple_color("tapez le nom du tournois : \n"))
        while not name:
            print(self.error_color("champs vide\n"))
            name = input(self.exemple_color("tapez le nom du tournois : \n"))
        locale = input(self.exemple_color("tapez le lieu : \n"))
        while not locale:
            print(self.error_color("champs vide\n"))
            locale = input(self.exemple_color("tapez le lieu : \n"))
        tournament_begin_date = input(
            self.exemple_color(
                "tapez la date du debut du tournois (au format jjmmaaaa) : \n"
            )
        )
        while not tournament_begin_date:
            print(self.error_color("champs vide\n"))
            tournament_begin_date = input(
                self.exemple_color(
                    "tapez la date du debut du tournois"
                    " (au format jjmmaaaa) : \n"
                )
            )
        tournament_end_date = input(
            self.exemple_color(
                "tapez la date de fin du tournois (au format jjmmaaaa) : \n"
            )
        )
        while not tournament_end_date:
            print(self.error_color("champs vide\n"))
            tournament_end_date = input(
                self.exemple_color(
                    "tapez la date de fin du tournois (au format jjmmaaaa) : \n"
                )
            )
        description = input(self.exemple_color("tapez la decription : \n"))
        while not description:
            print(self.error_color("champs vide\n"))
            description = input(self.exemple_color("tapez la decription : \n"))

        return name, locale, tournament_begin_date, tournament_end_date, description

    def ask_for_result_prompt(
        self, p1_first_name, p1_last_name, p2_first_name, p2_last_name
    ):
        print(
            self.question_color(
                f"\npour le match {p1_first_name} {p1_last_name} -"
                " {p2_first_name} {p2_last_name}\n"
            )
        )
        result = input(
            self.exemple_color(
                f"1 si {p1_first_name} {p1_last_name} à gagner,\n"
                "2 si {p2_first_name} {p2_last_name} à gagner,\n3 si il y a eu egalité : \n"
            )
        )

        return result

    def title_prompt(self, title_content):
        print(
            self.title_color(
                "\n______________________"
                f"{title_content}"
                "____________________ \n"
            )
        )

    def question_color(self, question):
        return self.color_yellow + question + self.color_reset

    def exemple_color(self, exemple):
        return self.color_cyan + exemple + self.color_reset

    def title_color(self, title_color):
        return self.color_magenta + title_color + self.color_reset

    def error_color(self, error):
        return self.color_red + error + self.color_reset
