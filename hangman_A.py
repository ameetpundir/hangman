import random
import numpy as np
from wordsSmall import words
from hangman_visual import lives_visual_dict
# print(words)


values = np.array([1, 2, 3, 1, 2, 4, 5, 6, 3, 2, 1])
searchval = 3
ii = np.where(values == searchval)[0]


def findValidWord(words):
    validWord = random.choice(words)

    while " " in validWord or "-" in validWord:
        validWord = random.choice(words)
    
    """while (True):
        if (validWord.find("-") != -1) and (validWord.find(" ") != -1):
            validWord = random.choice(words)
        else:
            break """
            
    return (validWord)


def play():
    ourWord = (findValidWord(words))
    print(ourWord)
    # wordLength = len(ourWord)
    wordList = []
    ourWordList = [*(ourWord)]  # list(ourWord)
    for i in ourWord:
        wordList.append("_")

    print(wordList)
    
    print(ourWordList)
    np_wordList = np.array(ourWordList)
    print(np_wordList)

    wrongTurn = 0
    newLetterList = []
    while (wrongTurn < 7):
        newLetter = input(f"Input the letter : {wordList} : ")
        if len(newLetter)==1 and newLetter.isalpha(): 
            #print(f"Index : {newLetterList.index(newLetter)}")
            if newLetter in newLetterList:
                print("same letter entered again, give a different letter")
            else: # actual logic
                
                newLetterList.append(newLetter) # all the entered letters go in this list to check for duplicates
                foundIx = np.where(np_wordList == newLetter)[0]
                #print(f"The letter is found in indexes {foundIx}")
                if (foundIx.size > 0 ):
                    
                    for a in foundIx:
                        wordList[a]=newLetter
                    
                    if "_" in wordList:
                        print(f"Empty values present {wordList}!")
                    else:
                        return f"You won, final word is {wordList}!!"
                else:
                # if (ourWord.find(newLetter))
                    wrongTurn += 1
                    print(lives_visual_dict[7-wrongTurn])
                    print(f"Wrong letter, chances {wrongTurn}/7 done!!")
        else:
            print("Invalid letter entered")            
            
    return "You lost!!"


result=play()
print(result)
