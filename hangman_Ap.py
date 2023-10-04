from words import words
import random
import string
# print(words)


def validWord(words):
    ourWord = random.choice(words)
    while (" " in ourWord or "-" in ourWord):
        ourWord = random.choice(words)
    return ourWord


def hangman():

    ourWord = validWord(words)
    print(ourWord)
    # set of all used words
    # set of all letter in the word

    allWords = set(string.ascii_lowercase)
    lettersInWord = set(list(ourWord))
    wordsUsed = set()
    lives = 7

    print(lettersInWord)

    # while (len(lettersInWord - wordsUsed) != 0):
    while (len(lettersInWord) != 0 and lives > 0):
        currentGuess = [
            letter if letter in wordsUsed else "-" for letter in ourWord]
        newLetter = input(f"Input the new letter : {currentGuess}").lower()
        if (newLetter in allWords):
            if (newLetter in lettersInWord):
                lettersInWord.remove(newLetter)
            elif (newLetter in wordsUsed):
                print("You have already used this letter, try again!!")
            else:
                lives -= 1

            wordsUsed.add(newLetter)
            print(wordsUsed)
            print(lettersInWord)
            print(lives)
        else:
            print("Invalid input, please try again!!")

    if (lives == 0):
        print("Sry!! you lost")
    else:
        print(f"Yeyy!! You won, the word is {ourWord}")


hangman()
