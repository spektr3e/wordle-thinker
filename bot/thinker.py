def greenLetters(greenInput):
    greenFakeDict = []
    for letter in greenInput:
        if letter == "_":
            pass
        else:
            greenFakeDict.append((letter,[v for v, x in enumerate(greenInput) if x == letter]))
    return greenFakeDict

# problem med ord som "dread" pga index systemet
# jämför längd mellan input index lista och ord index lista? å om ordets e längre granska då att de i input versionen stämmer?
def greenFilter(greenDict):
    result = []
    with open("prep/backup/wordlelist.txt", "r") as reference:
        for word in reference:
            reformat = word.rstrip()
            listFormat = []
            auth = True
            for char in reformat:
                listFormat.append((char,[v for v, x in enumerate(word) if x==char]))
            for letterUnit in greenDict:
                if letterUnit not in listFormat:
                    auth = False
                    break
                else:
                    pass
            if auth == True:
                result.append(reformat)
    print(result[0])
    return result


# måste fixas senare
def greenYellow(yellow, green):
    refList = []
    for letter in yellow:
        for char in green:
            if char[0] == letter:
                refList.append(char[0])
            else:
                pass
    return refList

# samma här
def yellowFilter(yellowInput, greenDict, firstRound):
    yellowList = [letter for letter in yellowInput if letter != "," and letter != " "]
    result = []
    for word in firstRound:
        lettercheck = greenYellow(yellowList, greenDict)
        print(word)
        print(lettercheck)
        remaining = [char for char in word]
        print(remaining)
        auth = True
        offset = 0
        for letter in yellowList:
            if lettercheck != []:
                for char in greenDict:
                    if lettercheck == []:
                        break
                    for index in char[1]:
                        if remaining[index - offset] == char[0]:
                            remaining.pop(index)
                            offset += 1
                            lettercheck.remove(char[0])
                            print(remaining)
                            print(lettercheck)
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
    print(result)
    return result


    

def thinker():
    print("Välkommen till wordle-tänkaren!")
    print("Skriv bokstäverna där de är gröna och sätt '_' på ställen där de inte är")
    greenInput = input("Skriv här: ").lower()
    greenDict = greenLetters(greenInput)
    print(greenDict)
    firstRound = greenFilter(greenDict)
    print("Skriv gula bokstäver här i formatet: x, y, z")
    print("Om bokstaven förekommer mer än en gång samtidigt som gul skriv den 2 gånger")
    yellowInput = input("Skriv här: ").lower()
    secondRound = yellowFilter(yellowInput, greenDict, firstRound)

    

def main():
    thinker()

main()

