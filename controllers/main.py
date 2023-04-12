from models.player import Player

rangei = input("noter un chiffre")

list_of_player = []

class Controller:
    pass

for n in range(int(rangei)):
    n = Player(input("nom de famille : "), input("prenom : "), input("date naissance au format jjmmaaaa : "))
    list_of_player.append(n)

for player in list_of_player:
    print(player.nom," ",player.point, " \n")
    ask = "vouley vous ajouter un resultat pour ", player.nom," ",player.point, "  (o pour oui, n pour non) \n"
    ask_for_point = input(ask)

    if ask_for_point == "o":
        equal_or_vic = input("est ce un victoire,une defaite ou une egalité ? ")
        if equal_or_vic == "v":
            player.add_point(equal_or_vic)
        elif equal_or_vic == "e":
            player.add_point(equal_or_vic)
        elif equal_or_vic == "d":
            player.add_point(equal_or_vic)
        else:
            pass
    elif ask_for_point == "n":
        pass
    else:
        pass

    print(player.nom," ",player.point, " \n")



