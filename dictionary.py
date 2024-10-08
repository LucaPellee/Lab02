import re


class Dictionary:
    def __init__(self, dict = {}):
        self._dict = dict

    def addWord(self, key_value):
        if len(key_value) == 2:
            if key_value[0] not in self._dict:
                self._dict[key_value[0]] = key_value[1]
            else:
                prev_Val =self._dict.get(key_value[0])
                if isinstance(prev_Val, str):
                    current_Val = []
                    current_Val.append(prev_Val)
                else:
                    current_Val = self._dict.get(key_value[0])
                self._dict[key_value[0]] = [*current_Val, key_value[1]]
                print(self._dict.get(key_value[0]))


    def translate(self, key):
        return self._dict[key]

    def loadDictionary(self):
        with open('dictionary.txt', 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dict[key_value[0]] = key_value[1]

    def translateWordWildCard(self, word):
        word = word.replace("?", ".")
        counter = 0
        sb = []
        for w in self._dict.keys():
            if re.search(word, w):
                counter +=1
                sb.append(self._dict.get(w))

        if counter >= 1:
            return sb
        else:
            return None

    def printAll(self):
        for key, value in self._dict.items():
            alieno = key
            italiano = value
            print(f"Alieno: {alieno}, traduzione: {italiano}\n")
