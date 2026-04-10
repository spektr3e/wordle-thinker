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
    with open("prep/backup/wordlelist.txt", "r") as reference:
        for word in reference:
            listFormat = []
            auth = True
            for char in word:
                listFormat.append((char,[v for v, x in enumerate(word) if x==char]))
            for letterUnit in greenDict:
                if letterUnit not in listFormat:
                    auth = False
                    break
                else:
                    pass
            if auth == True:
                result.append(word)
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

