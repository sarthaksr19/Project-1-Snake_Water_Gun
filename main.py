## Snake Water Gun
import random     #this random module generally select some random integer in a user given integer value

def gameWin(robot,you):
    if robot == you:  # if two values are equals game is tie
        return None

    # check all possiblities of robot when it choses s
    elif robot == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # check all possiblities of robot when it choses w
    elif robot == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # check all possiblities of robot when it choses g
    elif robot == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Robot turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)  #selects random number between 1 to 3 via randint fuction()
if randNo == 1:
    robot = 's'
elif randNo == 2:
    robot = 'w'
elif randNo == 3:
    robot = 'g'
   
you = input("Player's turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(robot,you)

print(f"Robot choose {robot}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie")
elif a:
    print("you win")
else:
    print("Robot win")
