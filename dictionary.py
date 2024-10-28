from PyDictionary import PyDictionary

class Dictionary:
    def __init__(self):
        self.dictionary = PyDictionary()

    def get_meaning(self, word):
        meaning = self.dictionary.meaning(word)
        if meaning:
            # Format meaning for display
            formatted_meaning = "\n".join([f"{key}: {value}" for key, value in meaning.items()])
            return formatted_meaning
        return None
