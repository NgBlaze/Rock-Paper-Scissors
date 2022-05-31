import random

while True:
    print('''Welcome, This game is called Rock, paper, scissors
To begin select the options below''')
    print("")
    print('''"R" for "rock", 
"P" for "paper", 
"S" for "scissors".''')

    cpu_options = ['R', 'P', 'S']

    cpu_choice = random.choice(cpu_options)

    user_choice = input("Select Option: ")
    print("")

    if user_choice not in cpu_options:
        print("Invalid option, please choose again")
        print("")
        continue

    if user_choice == 'R':
        rock = "Rock"
    elif user_choice == 'P':
        paper = "Paper"
    elif user_choice == 'S':

        scissors = "scissors"
    else:
        pass

    if cpu_choice == 'R':
        rocks = "Rock"
    elif cpu_choice == 'P':
        papers = "Paper"
    elif cpu_choice == 'S':
        scissorss = "scissors"
    else:
        pass

    if user_choice == 'R' and cpu_choice == 'S':
        print("Player ({}) : CPU ({})".format(rock, scissorss))
        print("Player is the winner")
        break
    if cpu_choice == 'R' and user_choice == 'S':
        print("Player ({}) : CPU ({})".format(scissors, rocks))
        print("CPU is the winner")
        break
    if user_choice == 'P' and cpu_choice == 'R':
        print("Player ({}) : CPU ({})".format(paper, rocks))
        print("Player is the winner")
        break
    if user_choice == 'R' and cpu_choice == 'P':
        print("Player ({}) : CPU ({})".format(rock, papers))
        print("CPU is the winner")
        break
    if user_choice == 'S' and cpu_choice == 'P':
        print("Player ({}) : CPU ({})".format(scissors, papers))
        print("Player is the winner")
        break
    if user_choice == 'P' and cpu_choice == 'S':
        print("Player ({}) : CPU ({})".format(papers, scissorss))
        print("CPU is the winner")
        break
    if user_choice == 'P' and cpu_choice == 'P':
        print("Player ({}) : CPU ({})".format(paper, papers))
        print("Its a Tie, Choose option again")
        continue
    if user_choice == 'S' and cpu_choice == 'S':
        print("Player ({}) : CPU ({})".format(scissors, scissorss))
        print("Its a Tie, Choose option again")
        continue
    if user_choice == 'R' and cpu_choice == 'R':
        print("Player ({}) : CPU ({})".format(rock, rocks))
        print("Its a Tie, Choose option again")
        print("")
        continue
    else:
        break
