class WordTree(object):
    def __init__(self, first_letter):
        self.word = first_letter
        self.children = {}
        self.size = 0
        
    def add_word(self, word):
        for letter in word:
            if letter not in self.children.keys():
                self.children[letter] = WordTree(letter)
            self.size += 1
            self = self.children[letter]
        self.size += 1
        finish_word = 'done'
        self.children[finish_word] = WordTree(finish_word)
            
    def search(self, word):
        if word[0] not in self.children.keys():
            return 0
        for letter in word:
            if letter in self.children.keys():
                self = self.children[letter]
            else:
                return 0
        return self.size
