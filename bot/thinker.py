def greenLetters(greenInput):
    greenFakeDict = []
    for letter in greenInput:
        if letter == "_":
            pass
        else:
            greenFakeDict.append((letter,[v for v, x in enumerate(greenInput) if x == letter]))
    print(greenFakeDict)
    return greenFakeDict

def greenFilter(greenDict):
    result = []
    trash = []
    with open("prep/backup/wordlelist.txt", "r") as reference:
        for word in reference:
            passedLetters = []
            auth = False
            for letter in greenDict:
                if letter[0] in passedLetters:
                    modWord = word.replace(word[word.index(letter[0])], "")
                    print(modWord)
                    modWordIndex = modWord.index(letter[0]) + 1
                    print(modWord)
                    if letter[0] not in modWord:
                        trash.append(word)
                        auth = True
                        break
                    elif letter[1][0] != modWordIndex:
                        trash.append(word)
                        auth = True
                        break
                    else:
                        passedLetters.append(letter[0])
                        pass
                else:
                    if letter[0] not in word:
                        trash.append(word)
                        auth = True
                        break
                    elif letter[1][0] != word.index(letter[0]):
                        trash.append(word)
                        auth = True
                        break
                    else:
                        passedLetters.append(letter[0])
                        pass
            if auth == False:
                result.append(word)
            else:
                pass
    print(result[0])
    return result

def yellowFormat(yellowInput):
    yellowString1 = yellowInput.remove(" ")
    yellowString2 = yellowString1.remove(",")
    yellowList = [letter for letter in yellowString2]

def thinker():
    print("Välkommen till wordle-tänkaren!")
    print("Skriv bokstäverna där de är gröna och sätt '_' på ställen där de inte är")
    greenInput = input("Skriv här: ").lower()
    greenDict = greenLetters(greenInput)
    firstRound = greenFilter(greenDict)

    

def main():
    thinker()

main()

