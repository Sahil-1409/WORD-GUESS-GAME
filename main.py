import random



def game():
    print("WELCOME TO THE GAME ......🙏..😊\n\n")
    word = ["communication","suffocation","elimination","aeroplane","python","designing","creative","figmentation","development","investments"]
    target_word=random.choice(word)
    guessed_word=[]
    Attempt_remaining = 6
    while True:
        if Attempt_remaining>0:
            display_word=""
            for letter in target_word:
                if letter in guessed_word:
                    display_word=display_word + letter +""
                else:
                    display_word+= "_ "
            print("WORD : ",display_word)
            print("ATTEMPT LEFT : ",Attempt_remaining)
            print("GUESSED SO FAR : ",",".join(guessed_word))
            if "_" not in display_word:
                print("YEEAAAAhh!!!!!!   CONGRATULATIONS....🎉🎉🎉🎉🎊🥳🥳YOU  GUESSED THE WORD")
                break
            guess=input("ENTER A LETTER THAT YOU GUESSES TO BE IN WORD : ").lower()
            if len(guess)!=1 or not guess.isalpha():
                print("invalid input.... Please Try again !!! ENTER A SINGLE LETTER")
                continue
            if guess in guessed_word:
                print("you guessed",guess,"again !!! TRY AGAIN")
                continue
            guessed_word.append(guess)
            if guess in target_word:
                print(f"GOOD JOB {guess} is in the word")
            else:
                Attempt_remaining -= 1
                print(f"WELL TRIED BUT {guess} IS NOT IN WORD")
            if  Attempt_remaining==0:
                print("\n\n\nBETTER LUCK NEXT TIME\n\n\n")
                print("THE WORD WAS : ",target_word)
                break

            
            
game()