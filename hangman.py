'''
A envoyer au plus tard dans la nuit de lundi à dimanche prochain sur mon adresse mail
Sujet : créer un fichier .py incluant un mini-projet de votre création, sur le sujet que vous souhaitez (dans les limites du raisonnable) et qui inclura l’utilisation de :
- fonctions
- boucle(s)
- instruction(s) conditionnelle(s)
- gestion des exceptions (try… except)
- liste(s) et/ou dictionnaire(s) et/ou chaîne(s) de caractères
- au moins une utilisation de map ou reduce ou filter

Soyez créatif ! Vous pourrez expliquer ce que fait le programme via des commentaires et en début du fichier ou en ajoutant un fichier texte qui donnera les explications que vous jugez utiles'''
import time

# Début de la fonction
def hangman_game():
    # Demander au joueur 1 d'entrer le mot à deviner
    player1_choice = input('Player1, please choose a word')
    # Convertir le mot entrée en minuscule en cas de majuscule dans le mot
    player1_choice = player1_choice.lower()
    print(player1_choice)
    # Tester si le mot entrer par le joueur 1 est un chiffre
    # Affectation à une variable
    test_player1_choice = player1_choice.isdigit() 
    # Si le mot entré par le joueur 1 est un chiffre alors on rentre dans la condition
    if (test_player1_choice == True): 
        # On propose au joueur 1 de réessayer d'entrée un mot si c'est un chiffre
        try: 
            print('Player1, this was not a word : ' + player1_choice + '. Please try again')
            player1_choice = input ('')
            test_player1_choice = player1_choice.isdigit()
            # Si le joueur rentre encore une fois un nombre, on arrête la fonction avec un message lui disant de re-jouer avec un mot
            if (test_player1_choice == True):
                return print("You didn't choosed a number. If you whant to play, please select a word")
        # Si le try ne fonctionne pas, on lance le Except qui stop le programme et demande de recommencer        
        except : 
            print ('Ok Player1, we have a bug, please try again by rebooting the program')
            return 
    # Affichage du mot choisit
    print('You choosed the word : ' + player1_choice)
    # Donner l'ordinateur au second joueur
    print('Passe the computer to Player2')
    # Temps d'attente
    time.sleep(2)
    n=0
    while(n < 15):
        print('_')
        time.sleep(0.3)
        n+=1
    # Fin du temps d'attente
    # Début du second joueur
    print('Hello Player 2')
    print('Are your ready to play? ')
    time.sleep(1)
    print('Player1 and myself are!')
    time.sleep(1)
    # Indication du nombre de charactère du mot choisit par le joueur 1
    # On convertit l'entier en string
    print('The lenght of the word that Player1 choosed is ' + str(len(player1_choice)))
    # Variable qui représente les tours. Plus bas on laisse 10 tours au joueur 2 pour trouver le mot, dans le cas contraire, il a perdu. Si le joueur 2 à raison, on ne passe pas le round
    rounds = 0
    # Variable qui va ajouter à chaque tour la lettre entré dans le tableau, vide au début
    proposition = []
    print("You have 10 rounds to guess the word")
    # Début des tours pour le joueurs 2
    while(rounds <= 10):
        # Définition d'une variable qui va compter les mauvaises réponses
        wrong = 0
        # Vérification si l'input qui est la lettre, fait partit du mot indiqué par le joueur 1
        for characteres in player1_choice :
            # Si la lettre fait partie du mot 
            if characteres in proposition :
                print(characteres)
            # Si la lettre ne fait pas partie du mot
            else: 
                print('_')
                wrong+=1
        # Si le joueur 2 n'a aucune erreur, il a gagné
        if wrong == 0:
            print('It\'s a won for Player2! Well done')
            return True
        # Important to place the input here to see all the _ for the lenght of the word and the letters already told
        guess = input('Try a charactere')
        # Si le joueur 2 rentre plusieurs valeurs, on ne prend que la première et on la rend en minuscule
        guess = guess[:1]
        guess = guess.lower()
        print(guess)
        # Ajout de la lettre entrée dans le input dans le tableau 
        proposition += guess
        # Affichage des lettres déjà proposé
        print('You already tried those letter :' + str(proposition))
        # Si la lettre n'est pas dans le mot choisit par le joueur 1
        if guess not in player1_choice:
            rounds+=1
            print('Nop, this letter is not in the word that Player1 choosed')
            time.sleep(0.1)
            # Rappel du nombre de round restant
            print('You have '+ str((10 - rounds)) + 'rounds to try')
            # Ici nous avons perdu et donc pas trouvé le mot
            if rounds == 10:
                print('Sorry but you loosed...')
                time.sleep(0.3)
                print('The word was : ' + player1_choice)
                time.sleep(0.3)
                print('Thank you for playing!')
                print('Made by Adley Salabi - P2021 - Maj Tech (la best)')
                return False

# Début de la fonction
hangman_game()

'''
Pour aller plus loin dans ce projet, j'aurai du améliorer la vérification d'entrée de valeurs : nottament si ce n'est pas un chiffre ou que la chaine de charactère ne contient pas de chiffre. 
De plus, je n'ai pas utilisé la dernière règle (Map / Reduce / Filter), j'aurai du dans le cadre de l'exercice. 
Merci pour les cours, nous nous retrouverons aux partiels! Bon courage pour la correction de tous les exercices. 

Adley Salabi
a_salabi@etu-webschoolfactory.fr
P2021
'''