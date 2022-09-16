
import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...

    '''
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

>>> wf.random()
    1. instantiation
        1A. reads file
        1B. creates list of words
        1C. prints number of words read
    2. method: return random word from list
    
    '''

    def __init__(self, txtdoc):
        '''
        Read text document, create list of words from dictionary
        and return word count from list
        '''
        self.txtdoc = self.wordfile = txtdoc
        self.wordfile = wordfile = open(self.txtdoc, "r").read().splitlines()
        self.lst = []
        for word in wordfile:
            self.lst.append(word)
        self.count = len(self.lst)
        print(f"{self.count} words read")
    
    def __repr__(self):
        return f"<WordFinder number of words in file={self.count}"
        
    def random(self):
        '''Return a random word from list'''
        return random.choice(self.lst)


class SpecialWordFinder(WordFinder):
    def parse(self, wordfile):
        for word in wordfile:
            if word.strip() and not word.startswith("#"):
                self.lst.append(word)
        print(self.lst)


