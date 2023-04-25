import json
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
        print( self.title_color("\n\n Inscrire des joueur, "
                                "consulter la liste des joueurs inscrit au tournois,"
                                " Lancer le Tournois, consulter la liste des precedent tournois\n\n"))

        start_input = input(self.question_color("que voulez vous faire ?\n1 pour inscrire des joueur \n"
                                                "2 pour consulter la liste de joueurs\n3 pour lancer le tournois\n4 pour consulter la liste des precedent tournois : \n"))
        return start_input
       

    def add_players_to_tournament_list_prompt(self):
        prenom = input(self.title_color("tapez le prenom du joueur : "))
        while not prenom:
            print(self.error_color("champs vide"))
            prenom = input(self.title_color("tapez le prenom du joueur : "))
        nom = input(self.title_color("tapez le nom du joueur : "))
        while not nom:
            print(self.error_color("champs vide"))
            nom = input(self.title_color("tapez le nom du joueur : "))
        date_de_naissance = input(self.title_color("tapez la date de naissance (au format jjmmaaaa) : "))
        while not date_de_naissance:
            print(self.error_color("champs vide"))
            date_de_naissance = input(self.title_color("tapez la date de naissance (au format jjmmaaaa) : "))
        return nom, prenom, date_de_naissance

    def show_players_list_prompt(self, player_list):
        
        print("\n_________________ liste des joueurs _________________\n")

        for player in player_list:
            date_obj = datetime.strptime(player.birth_date, "%d%m%Y")
            date_formatted = date_obj.strftime("%d-%m-%Y")

            print("        ", player.first_name, "  |   ", player.last_name, "  |   ", date_formatted)
            print("_____________________________________________________\n")

        ask_to_continue = input("\n\nPour revenir au menu principal appuyer sur n'importe quelle touche\n")

        return ask_to_continue
    
    def show_tournaments_list_prompt(self, tournament_list):
        
        print("\n_________________ liste des joueurs _________________\n")

        for tournament in tournament_list:
            print("_____________________________________________________\n")

        ask_to_continue = input("\n\nPour revenir au menu principal appuyer sur n'importe quelle touche\n")

        return ask_to_continue

    def start_tournament_prompt(self):

        name = input(self.title_color("tapez le nom du tournois : \n"))
        while not name:
            print(self.error_color("champs vide\n"))
            name = input(self.title_color("tapez le nom du tournois : \n"))
        locale = input(self.title_color("tapez le lieu : \n"))
        while not locale:
            print(self.error_color("champs vide\n"))
            locale = input(self.title_color("tapez le lieu : \n"))
        tournament_begin_date = input(self.title_color("tapez la date du debut du tournois (au format jjmmaaaa) : \n"))
        while not tournament_begin_date:
            print(self.error_color("champs vide\n"))
            tournament_begin_date = input(self.title_color("tapez la date du debut du tournois (au format jjmmaaaa) : \n"))
        tournament_end_date = input(self.title_color("tapez la date de fin du tournois (au format jjmmaaaa) : \n"))
        while not tournament_end_date:
            print(self.error_color("champs vide\n"))
            tournament_end_date = input(self.title_color("tapez la date de fin du tournois (au format jjmmaaaa) : \n"))
        description = input(self.title_color("tapez la decription : \n"))
        while not description:
            print(self.error_color("champs vide\n"))
            description = input(self.title_color("tapez la decription : \n"))
        
        return name, locale, tournament_begin_date, tournament_end_date, description

    def question_color(self, question):
        return self.color_yellow + question + self.color_reset
    
    def title_color(self, title):
        return self.color_cyan + title + self.color_reset
    
    def error_color(self, error):
        return self.color_red + error + self.color_reset
