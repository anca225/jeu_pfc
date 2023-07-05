import random

def get_choices():
    choices_option = ['pierre','feuille', 'ciseaux']
    computer_choice = random.choice(choices_option)
    player_choice = input("entrer votre choix parmis ces trois pierre,feuille, ciseaux : ")
    
    while player_choice not in choices_option:
        player_choice = input("essayer de nouveau, entrer votre choix dans cette liste (pierre,feuille,ciseaux): ")
        if player_choice in choices_option:
            print(player_choice)
    #choices ={'player':player_choice, 'computer':computer_choice}
    return computer_choice, player_choice

def checkwin(computer_choice, player_choice): 
    if computer_choice == player_choice:
        print("il ya égalité")
    elif computer_choice == 'pierre' and player_choice =='ciseaux':
        print(f'{computer_choice} casse {player_choice}, computer win')
    elif computer_choice == 'pierre' and player_choice =='feuille':
        print(f'{player_choice} englouti {computer_choice}, you win')
    elif computer_choice == 'ciseaux' and player_choice =='pierre':
        print(f'{player_choice} casse {computer_choice}, you win')
    elif computer_choice == 'ciseaux' and player_choice =='feuille':
        print(f'{computer_choice} coupe {player_choice}, computer win')
    elif computer_choice == 'feuille' and player_choice =='pierre':
        print(f'{computer_choice} englouti {player_choice}, computer win')
    elif computer_choice == 'feuille' and player_choice =='ciseaux':
        print(f'{player_choice} coupe {computer_choice}, you win')
    else :
        return
    

resultat = get_choices()
checkwin(resultat[0],resultat[1])
