class Vector:
    ''' Simulates an array of 2D 
    
    Attributes
    ----------
    data : list-like
        The actual data in a list.
    length : int
        Number of elements
    
    Notes
    -------
    Integers and other vectors can be added. 
    Element-wise comparison with other vectors is also supported.
    '''

    def __init__(self, data:list):
        self.data = list(data)
        self.length = len(self.data)

    def __len__(self):
        ''' allows us to call len'''
        return self.length

    def __str__(self):
        return f'{self.data} with {self.length} elements'
    
    def __add__(self, other):
        '''
        allows addition of integers or other vectors
        '''
        if isinstance(other, int):
            self.data = [elem + other for elem in self.data]
            return self
        elif isinstance(other, Vector):
            assert self.length == other.length, 'not same length!'
            new_vec = [el1 + el2 for el1, el2 in zip(self.data, other.data)]
            return Vector(new_vec)
        else:
            raise TypeError(f'Can not add variable of type {type(other)}, expected int or vector')

    
    def __gt__(self, other):
        '''
        Element-wise comparison with other vectors

        Returns a boolean vector
        '''
        if not isinstance(other, Vector):
            raise TypeError(f'Can not compare variable of type {type(other)}, expected vector')

        assert self.length == other.length, 'not same length!'
        gt_data = [el1 > el2 for el1, el2 in zip(self.data, other.data)]
        return Vector(gt_data)

a = Vector([10,2,3,5])
b = Vector([1,6,5,8])
c = 4
x = 'no'
y = Vector([1,1,1])


