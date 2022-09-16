"""Python serial number generator."""

from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''Initialize number generator at start'''
        self.start = self.next = start

    def __repr__(self):
        '''Show representation'''
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        '''Generate next number from start by increment of 1'''
        self.next += 1
        return self.next - 1

    def reset(self):
        '''Reset next number to initialized number from beginning'''
        self.next = self.start


