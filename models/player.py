class Player:
    """
    Class Players.

     Attb:
        attribut_1 -- nom
        attribut_2 -- prenom
        attribut_3 -- date de naissance
        attribut_4 -- point
        attribut_5 -- numero d'identifiant nationnal

    """

    def __init__(
        self, last_name, first_name, birth_date,
        point=0, nationnal_chess_id="0000000"
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.point = point
        self.nationnal_chess_id = nationnal_chess_id

    def add_point(self, result):
        """
        Ajout ou non un point

        Args:
        first -- self
        second -- le resultat du match
        """
        if result == "1":
            self.point += 1
        elif result == "2":
            self.point += 0.5
        elif result == "3":
            pass

    def save_participant_data(self):
        """
        convertie les donnée du Player en donnée JSON
        """
        participant_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
        }
        return participant_data

    def save_player_data(self):
        """
        convertie les donnée du Player (avec les points) en donnée JSON
        """
        player_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "point": self.point,
        }
        return player_data
