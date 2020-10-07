import random
Board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


def timedelay():

    for i in range(60000000):
        continue
            

            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'],"\t\t\t  7|8|9 ")
    print('-+-+-',"\t\t\t  -+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'],"\t positions =>\t  4|5|6 ")
    print('-+-+-',"\t\t\t  -+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'],"\t\t\t  1|2|3 ")

def game():

    turn = input("enter your choice (X/O): ")
    turn=turn.upper()
    choice=turn
    count = 0
    
    for i in range(10):
        printBoard(Board)
        print("\n")
        if choice==turn:
            move = input("It's your turn, " + turn + ". where to place the mark? : ")        

            if Board[move] == ' ':
                Board[move] = turn
                count += 1
            else:
                print("That place is already filled.\nWhere else to place? : ")
                continue
            
        elif choice!=turn:
            lst=[]
            print("It's now "+turn+"'s turn: let "+turn+" think....\n")
            timedelay()
            for i in range(1,10):
                i=str(i)
                if Board[i] == " ":
                    lst.append(i)
                else:
                    continue
            move=str(random.choice(lst))
            print(turn+" chose to place the mark at "+move," ")
            Board[move] = turn
            count +=1

        
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ':
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': 
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    restart = input("Do want to play Again?(y/n): ")
    if restart == "y" or restart == "Y":  
        for key in range(10):
            key=str(key)
            Board[key] = " "
        game()

print("welcome to tik-tac-toe....\n(user Vs. Computer)\n")
game()
