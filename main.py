import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()


    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Che parola vuoi aggiungere?")
        txtIn = input()
        t.handleAdd(txtIn)
        print("Aggiunta!")
        continue

    if int(txtIn) == 2:
        print("Che parola vuoi tradurre?")
        txtIn = input()
        trad = t.handleTranslate(txtIn)
        print(trad)
        continue

    if int(txtIn) == 3:
        print("Che parola vuoi tradurre?")
        txtIn = input()
        tradWild = t.handleWildCard(txtIn)
        print(tradWild)
        continue

    if int(txtIn) == 4:
        print("Dizionario completo:\n")
        t.printDictionary()
        continue

    if int(txtIn) == 5:
        break
