import numpy as np

class Structure:
    def __init__(self, name, **kwargs):
        '''name: name of the structure\n
        var1 = val1.\n.\n.\n. so on'''
        self.name = name
        self.items = list(kwargs.items())

    def get(self, *args):
        i = list(args)
        self.getElems = np.array(self.items, dtype=object)
        return self.getElems[args]

# newS = Structure("newS", var1=1, var2=2)
# print(newS.get(0,1))