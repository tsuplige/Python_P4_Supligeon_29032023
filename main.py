from models.player import Player
from models.round import Round
from models.tournaments import Tournament
from typing import List
import json
import os


if os.path.exists("data") and os.path.isdir("data"):
    print("Le dossier 'data' existe.")
else:
    os.makedirs('data')

class Controllers:
    """
        class Controllers

        Attb :

            attribut_1 -- la Vue

    """
    def __init__(self,  view):
        
        
        self.players: List[Player] = []
        self.more_player = True
        self.view = view
        self.tournament_list = []

        if os.path.exists("data/players.json"):
            with open('data/players.json', 'r') as f:
                datas = f.read()
                for data in json.loads(datas):
                    self.players.append(Player(data["first_name"], data["last_name"], data["birth_date"]))

    def main_menu(self):
        """

        Méthode main_menu


        """

        menu_input = self.view.main_menu_prompt()

        if menu_input == '1':
            self.get_players()
        elif menu_input == '2':
            ask_to_continue = self.view.show_players_list_prompt(self.players)
            self.main_menu()
        elif menu_input == '3':
            self.start_tournament()
        elif menu_input == '4':
            pass
        else:
            self.main_menu()
    
    def start_tournament(self):
        
        name, locale, tournament_begin_date, tournament_end_date, description = self.view.start_tournament_prompt()

        new_tournament = Tournament(name, locale, tournament_begin_date, tournament_end_date, description, self.players)

        while new_tournament.current_round < new_tournament.number_of_round:
            new_tournament.current_round += 1
            self.view.title_prompt("Round " + str(new_tournament.current_round))
            new_tournament.start_round()

            self.view.title_prompt("Resultat")
            for player in self.players:
                result = self.view.ask_for_result_prompt(player.first_name, player.last_name)
                player.add_point(result)
            
            new_tournament.end_round()



    def get_players(self):
        """
        
        Méthode get_players

        permets d'ajouter des joueurs a la liste de joueurs et appelle la methode save_player_data()
        pour ajouter les donnée créé dans le fichier de saugdarde data/players.json

        """
        
        
        if self.more_player == False:
            self.more_player = True
        while self.more_player == True:
            
            nom, prenom, date_de_naissance = self.view.add_players_to_tournament_list_prompt()
            if not (nom, prenom, date_de_naissance):
                return 
            self.players.append(Player(nom, prenom, date_de_naissance))
            
            
            """
            permets de mettre fin à la boucle si l'utilisateurs a finis d'ajouter des joueurs
            """
            ask_to_continue = input(self.view.question_color("voulez vous ajouter d'autre joueur ? \n o pour oui\n n pour non\n"))
            if ask_to_continue == "o" or ask_to_continue == "O":
                self.more_player = True
            elif ask_to_continue == "n" or ask_to_continue == "N":
                self.more_player = False
        
        self.save_player_data()
        self.main_menu()
    
    def save_player_data(self):
        data = []

        for player in self.players:
            data.append({
                "first_name": player.first_name,
                "last_name": player.last_name,
                "birth_date": player.birth_date
            })

        with open('data/players.json', 'w') as f:
                json.dump(data, f)
        

from views.base import View

vue = View()
    
test = Controllers(vue)

test.start_tournament()