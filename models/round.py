import datetime
import random

class Round:
    """
    Class Round (Tours)
 
    Attb:
        attribut_1 -- le Numéro du round actuel
        attribut_2 -- le nom du round
        attribut_3 -- la liste des matchs
        attribut_4 -- la date et l'heure de début
        attribut_5 -- la date et l'heure de fin

    """
    def __init__(self, current_round, match_list):
        self.current_round = current_round
        self.round_name = "Round" + str(current_round)
        self.match_list = match_list
        self.round_begin_date = self.get_actual_date()
        self.round_end_date = None

    def get_actual_date(self):
            """
            recupere la date et l'heure
            
            """
            current_date = datetime.datetime.now()

            return current_date.strftime("%Y-%m-%d %H:%M")
    
    def add_end_round_date(self):
         """

         definit l'heure de fin du Tour

         """
         self.round_end_date = self.get_actual_date()

    # def which_player_start(self):
    #      """

    #      definit pour chaque match quel joueur commence
         
    #      """

    #     for match in self.match_list:
	#         chosen_player = random.choice(match)
         
         
    