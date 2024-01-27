import random;

print('''
  _______ _             _____                       _   _                 _                  _____                      
 |__   __| |           / ____|                     | \ | |               | |                / ____|                     
    | |  | |__   ___  | |  __ _   _  ___  ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __  __ _ _ __ ___   ___ 
    | |  | '_ \ / _ \ | | |_ | | | |/ _ \/ __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ |/ _` | '_ ` _ \ / _ \
    | |  | | | |  __/ | |__| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |    | |__| | (_| | | | | | |  __/
    |_|  |_| |_|\___|  \_____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|_| |_| |_|\___|
                                                                                                                 
''')

print("Welcome to the guessing number game!");
print("I am thinking of  a number between 0 and 100");
level = input("Choose a difficulty. Type 'easy' or 'hard' :");
easyGuess = 10;
hardGuess = 5;
computer_guessed_nunber = random.randint(0, 100);
if(level == 'easy') :
    print(f"You have ${easyGuess} chances to guess the number. Good luck!");
    while True:
        while easyGuess > 0:
            guess = int(input("Make a guess: "))
            if guess > computer_guessed_nunber:
                print("Too high ");
                easyGuess -= 1;
                print(f"you have ${easyGuess} remaining");
                print("guess again.");
            elif guess < computer_guessed_nunber:
                print("Too low ");
                easyGuess -= 1;
                print(f"you have ${easyGuess} remaining");
                print("guess again.");
            else:
                print("You got it right");
                break;
        if(easyGuess == 0):
            break;
else :
    print(f"You have ${hardGuess} chances to guess the number. Good luck!");
    while True :
        while hardGuess > 0 :
            guess = int(input("Make a guess: "));
            if guess > computer_guessed_nunber :
                print("Too high");
                hardGuess -= 1;
                print(f"You have ${hardGuess} remaining");
                print("guess again.");
            elif guess < computer_guessed_nunber :
                print("Too low");
                hardGuess -= 1;
                print(f"You have ${hardGuess} remaining");
                print("guess again.");
            else :
                print("You got it right");
                break;
        if(hardGuess == 0):
            break;




