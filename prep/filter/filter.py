line1 = 0
line2 = 9

def getcontent():
    with open("filter/words_alpha.txt", "r") as english:
        content = english.readlines()
        return content

def hepa(word):
    word.rstrip()
    if len(word) == 6:
        return True
    else:
        return 0

def write(word):
    with open("txt_dump/wordlelist.txt", "a") as wordleList:
        wordleList.writelines(word)

def loop():
    global line1
    filtering = True
    content = getcontent()
    try:
        while filtering:
            word = content[line1]
            print(f"{line1} {word}")
            line1 += 1
            # continue up
            value = hepa(word)
            if value == True:
                write(word)
            else:
                pass
    except IndexError:
        print("done")



def main():
    loop()

main()