score = 0
name = input('Enter your name')
import random
def main():   # main function to wrap up th two functions
    print(name, 'You are welcome to my guessing game!')
    guessing_game()    

def guessing_game():
    the_number = random.randint(1,20)
    print(the_number)
    while True:        
        guess = int(input("Guess a number between 1 and 20:"))
        if guess !=the_number: 
            if guess>the_number:
                print(guess,'was too high. Try again.')
            elif guess<the_number:
                print(guess,'was too low. Try again.')            
        else:
            print(guess,'was the right number! You win!')
            print('it took you',1,'attempt!')
            play_again()
            break
        guess = int(input("Guess a number between 1 and 20:"))
        if guess !=the_number: 
            if guess>the_number:
                print(guess,'was too high. Try again.')
            elif guess<the_number:
                print(guess,'was too low. Try again.')   
        else:
            print(guess,'was the right number! You win!')
            print('it took you',2,'attempts!')
            play_again()
            break
        guess = int(input("Guess a number between 1 and 20:"))
        if guess !=the_number: 
            if guess>the_number:
                print(guess,'was too high. Try again.')
            elif guess<the_number:
                print(guess,'was too low. Try again.')   
        else:
            print(guess,'was the right number! You win!')
            print('it took you',3,'attempts!')
            play_again()
            break
        guess = int(input("Guess a number between 1 and 20:"))
        if guess !=the_number: 
            if guess>the_number:
                print(guess,'was too high. Try again.')
            elif guess<the_number:
                print(guess,'was too low. Try again.')   
        else:
            print(guess,'was the right number! You win!')
            print('it took you',4,'attempts!')
            play_again()
            break
        guess = int(input("Guess a number between 1 and 20:"))
        if guess !=the_number: 
            print('game over')
            print(name, 'your total score is:',score)
            break
        else:
            print(guess,'was the right number! You win!')
            print('it took you',5,'attempts!')
            play_again()
            break

    
def play_again():
    global score
    score += 50
    another_game = input('do you want to play again (Y/N?)')
    if another_game.lower() =='y':
        guessing_game()
    elif another_game.lower() == 'N':
        print(name, 'Bye for now')
        print(name, 'your total score is:',score)
    else:
        print('You have selected no option')
        print(name,'you are logged out')
        print(name, 'your total score is:',score)
 
        
main()   