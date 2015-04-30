''' Teach how mixin classes work, what inheritanc is really all about,
    and how to ABCs (abstract base classes) to impose discipline on mixins.

    It is all about code organize and reuse.
'''

class DoubleSeq(object):
    #"wrap an existing sequence to only access every other"

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 1) // 2

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Out of Range')
        return self.seq[index // 2]

    d = DoubleSeq('The Tale of Two Cities')

