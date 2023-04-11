class Utils():

    def __init__(self):
        self._name = 'utils'

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError('The input argument should be Integer')
        
        return a+b