import datetime


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
    def __init__(
        self, current_round, match_list,
        round_begin_date=None, round_end_date=None
    ):
        self.current_round = current_round
        self.round_name = "Round" + str(current_round)
        self.match_list = match_list
        self.round_begin_date = round_begin_date
        if self.round_begin_date is None:
            self.round_begin_date = self.get_actual_date()
        self.round_end_date = round_end_date

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

    def save_round_data(self):
        matchs_datas = []
        if self.match_list:
            for match in self.match_list:
                print(match)
                matchs_datas.append(
                    {
                        "joueur_1": match[0][0].save_player_data(),
                        "score_J1": match[0][1],
                        "joueur_2": match[1][0].save_player_data(),
                        "score_J2": match[1][1],
                    }
                )

        round_data = {
            "round_name": self.round_name,
            "current_round": self.current_round,
            "match_list": matchs_datas,
            "round_begin_date": self.round_begin_date,
            "round_end_date": self.round_end_date,
        }
        return round_data
