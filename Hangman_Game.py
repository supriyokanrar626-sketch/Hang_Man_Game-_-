#          HANG_MAN  GAME


import random

words = ("apple", "orange", "banana", "coconut", "pineapple", "watermelon")
#  dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   ",),

               1: (" o ",
                   "   ",
                   "   ",),

               2: (" o ",
                   " | ",
                   "   ",), 

               3: (" o ",
                   "/| ",
                   "   ",),

               4: (" o ",
                   "/|\\",
                   "   ",),

               5: (" o ",
                   "/|\\",
                   "/  ",),

               6: (" o ",
                   "/|\\",
                   "/ \\",)}

def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")    

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_runnrig = True

    while is_runnrig:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter your girlfriend name as fruit : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("This is not your girlfriend....")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed..")
            continue

        guessed_letters.add(guess)

        if guess in answer:
          for i in range(len(answer)) :
              if answer[i] == guess:
                  hint[i] = guess
        else :
            wrong_guesses += 1 

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WINNN!!! YOU OWN YOUR GIRLFRIEND..")
            is_runnrig = False
        elif wrong_guesses >= len(hangman_art)-1 :
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU FUCKERRR!!!  YOU LOST YOUR GF< SHE IS MINE>>HAHA..") 
            is_runnrig = False  


if __name__=="__main__":
    main()