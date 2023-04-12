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

    def start_menu(self):
        print( self.question_color("\n\nCreer un (N)ouveau tournois, consulter les (R)esultat des precedent tournois\n\n"))

        start_input = input("que voulez vous faire ? n pour lancer un tournois, r pour voir les precedent resultat : ")

        if start_input == "n" or start_input == "N":
            print("\ncommencons le parametrage !\n\n")
        elif start_input == "r" or start_input == "R":
            print("\nFonctionnalité actuellement indisponible\n\n")
            self.return_to_strat_menu()
        else:
            print("\nerreur de frappe\n\n")
            self.return_to_strat_menu()

    def question_color(self, question):
        return self.color_yellow + question + self.color_reset
    def title_color(self, title):
        pass
    def error_color(self, error):
        pass

    def return_to_strat_menu(self):
        print("voulez vous retourner au menu d'accueil ? (O)ui, (N)on\n\n")

        ask_to_continue = input("o pour continuer, n pour fermer l'application\n")

        if ask_to_continue == "o" or ask_to_continue == "O":
            self.start_menu()
        elif ask_to_continue == "n" or ask_to_continue == "N":
            pass
        else:
            print("erreur de frappe\n\n")
            self.return_to_strat_menu()

vue = View()

vue.start_menu()