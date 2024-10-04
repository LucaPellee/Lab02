from dictionary import Dictionary
class Translator:

    def __init__(self, dict = Dictionary()):
        self._dict = dict

    def printMenu(self):
        print("______________________________\n" +
              "   Translator Alien-Italian\n" +
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n" +
              "______________________________\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self._dict.loadDictionary()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass