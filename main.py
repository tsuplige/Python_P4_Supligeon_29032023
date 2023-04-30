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
        self.next_round = True
        self.view = view
        self.tournament_list = []

        if os.path.exists("data/players.json"):
            with open('data/players.json', 'r') as f:
                datas = f.read()
                for data in json.loads(datas):
                    self.players.append(Player(data["last_name"], data["first_name"],  data["birth_date"]))

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

        if new_tournament.is_not_finish :
            while new_tournament.current_round < new_tournament.number_of_round:
                new_tournament.current_round += 1
                self.view.title_prompt("Round " + str(new_tournament.current_round))
                match_list = new_tournament.start_round()

                self.next_round = True 

                while self.next_round == True :
                    self.tournament_menu(str(new_tournament.current_round), match_list)
                    self.view.title_prompt("Resultat du Round")
                    for match in match_list:
                        self.add_point_for_match(match)
                
                new_tournament.end_round()

            self.end_tournament()
            new_tournament.is_not_finish = False
            self.tournament_list.append(new_tournament)
        else :
            pass


    def add_point_for_match(self, match):

        p1 = match[0][0]
        p2 = match[1][0]

        result = self.view.ask_for_result_prompt(p1.first_name, p1.last_name, p2.first_name, p2.last_name)
        for player in self.players:
 
            if player.first_name == p1.first_name and player.last_name == p1.last_name:
                print('Le joueur', player.last_name, player.first_name, 'a été trouvé !')
                if result == '1':
                    player.add_point("1")
                elif result == '2':
                    for player2 in self.players:
                        if player2.first_name == p2.first_name and player2.last_name == p2.last_name:
                            player2.add_point("1")
                            break
                elif result == '3':
                    player.add_point("2")
                    for player2 in self.players:
                        if player2.first_name == p2.first_name and player2.last_name == p2.last_name:
                            player2.add_point("2")
                            break
                break

    def tournament_menu(self,current_round,match_list):
        """
        Methode : tournament_menu()



        """
        menu_input = self.view.tournament_menu_prompt(current_round)

        while not menu_input:
            menu_input = self.view.tournament_menu_prompt(current_round)
        if menu_input == '1':
            self.view.print_match(match_list, current_round)
            self.tournament_menu(current_round,match_list)
        elif menu_input == '2':
            ask_to_continue = self.view.print_players_list_by_point(self.players)
            self.tournament_menu(current_round,match_list)
        elif menu_input == '3':
            self.next_round = False
        else:
            self.tournament_menu(current_round,match_list)

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
    
    def end_tournament(self):
        pass
    
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

    def save_tournament_data(self, tournament):
        player_data = []
        Tournament_data = []
        match_data = []

        for player in self.players:
            player_data.append({
                "first_name": player.first_name,
                "last_name": player.last_name,
                "birth_date": player.birth_date
                "point": player.point
            })
        
        Tournament_data = {
            "name": tournament.name,
            "locale": tournament.locale,
            "tournament_begin_date": tournament.tournament_begin_date,
            "tournament_end_date": tournament.tournament_end_date,
            "description": tournament.description,
            "is_not_finish": self.is_not_finish,
            "number_of_round" : tournament.number_of_round,
            "current_round" : tournament.current_round,
            "round_list": tournament.round_list,
            "tournament_players" : player_data

        }

        with open('data/players.json', 'w') as f:
                json.dump([{}]data, f)
        

from views.base import View

vue = View()
    
test = Controllers(vue)

test.main_menu()