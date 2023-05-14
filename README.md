# Python_P4_Supligeon_29032023

##logiciel de gestion de tournoi
### permet d'inscrire des joueurs, gerer des tournois, sauvegarder les donnée et les charger


## Comment utiliser/lancer le logiciel ?

### Etape 1 : ouvrir le repertoire du projet dans un terminal

### Etape 2 : cree l'environement dans le repertoire du projet
        " $ python -m venv env"

### Etape 3 : lancer L'environement Python
        "$ source env/bin/activate" ou "$ env/Scripts/activate.bat" (sur windows)

### Etape 4 : Insataller les package grace au fichier requirements.txt
        "$ pip install -r requirements.txt"

### Etape 5 : lancer le Script
        "$ python main.py"

## Comment faire un rapport Flake8-html
### Etape 1 : Si ce n'est pas déja fait installé flake8-html
        "$ pip install flake8-html"
### Si vous n'avez pas de fichier setup.cfg, créez en un et collé ce texte a l'interieur
        "[flake8]
        max-line-length = 120
        exclude = .git,__pycache__,docs/source/conf.py,old,build,dist,env"
### Pour faire une rapport lancer la commande suivante sur votre terminal
        "$ python -m flake8 --format=html --htmldir=flake-report"
### Et le rapport apparaittra dans un dossier nommé /flake-report 

