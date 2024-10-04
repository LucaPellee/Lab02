class Dictionary:
    def __init__(self, dict = {}):
        self._dict = dict

    def addWord(self, key_value):

        pass

    def translate(self):
        pass

    def loadDictionary(self):
        with open('dictionary.txt', 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dict[key_value[0]] = key_value[1]

    def translateWordWildCard(self):
        pass

