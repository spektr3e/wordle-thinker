def greenLetters(greenInput):
    greenFakeDict = []
    for letter in greenInput:
        if letter == "_":
            pass
        else:
            greenFakeDict.append((letter,[v for v, x in enumerate(greenInput) if x == letter]))
    return greenFakeDict

def greenFilter(greenDict):
    result = []
    with open("prep/backup/wordlelist.txt", "r") as reference:
        for word in reference:
            reformat = word.rstrip()
            listFormat = []
            auth = False
            for char in reformat:
                listFormat.append((char,[v for v, x in enumerate(reformat) if x==char]))
            for letterUnit in greenDict:
                verify = True
                if letterUnit in listFormat:
                    auth = True
                elif letterUnit[0] in reformat:
                    indexList = [v for v, x in enumerate(reformat) if x==letterUnit[0]]
                    for index in letterUnit[1]:
                        if index in indexList:
                            auth = True
                        else:
                            auth = False
                            verify = False
                            break
                    if verify == False:
                        break
                else:
                    auth = False
                    break
            if auth == True:
                result.append(reformat)
    return result

def greenYellow(yellow, green):
    refList = []
    for letter in yellow:
        for char in green:
            if char[0] == letter:
                refList.append(char[0])
            else:
                pass
    return refList

def yellowFilter(yellowInput, greenDict, firstRound):
    yellowList = [letter for letter in yellowInput if letter != "," and letter != " "]
    result = []
    for word in firstRound:
        lettercheck = greenYellow(yellowList, greenDict)
        remaining = [char for char in word]
        auth = True
        offset = 0
        for letter in yellowList:
            if lettercheck != []:
                for char in greenDict:
                    if lettercheck == []:
                        break
                    else:
                        for index in char[1]:
                            if remaining[index - offset] == char[0]:
                                remaining.pop(index)
                                offset += 1
                                lettercheck.remove(char[0])
                                if lettercheck == []:
                                    break
                            else:
                                pass
            if letter not in remaining:
                auth = False
                break
            else:
                remaining.remove(letter)
        if auth == True:
            result.append(word)
    return result

def greyFilter(greyInput, secondRound):
    greyList = [letter for letter in greyInput if letter != "," and letter != " "]
    verify = True
    for word in secondRound:
        for letter in greyList:
            if letter in word:
                verify = False
                break
            else:
                pass
        if verify == False:
            secondRound.remove(word)
    return secondRound

def printer(result):
    if len(result) < 31:
        count = 0
        while count < 29:
            try:
                print(result[count])
                count += 1
            except IndexError:
                if result == []:
                    print("Inga passande ord hittades!")
                count += 100
    else:
        print("Det finns för många alternativ kvar!")

def thinker():
    print("Välkommen till wordle-tänkaren!")
    print("Skriv bokstäverna där de är gröna och sätt '_' på ställen där de inte är")
    greenInput = input("Skriv här: ").lower()
    greenDict = greenLetters(greenInput)
    firstRound = greenFilter(greenDict)
    print("Skriv gula bokstäver här i någon av formaten: x, y, z / xyz")
    print("Om bokstaven förekommer mer än en gång samtidigt som gul skriv den 2 gånger")
    yellowInput = input("Skriv här: ").lower()
    secondRound = yellowFilter(yellowInput, greenDict, firstRound)
    print("Skriv gråa bokstäver här i någon av formaten: x, y, z / xyz")
    greyInput = input("Skriv här: ").lower()
    result = greyFilter(greyInput, secondRound)
    printer(result)

def main():
    thinker()

main()