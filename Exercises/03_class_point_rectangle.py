class Point:
    """A 2D point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def transpose(self):
        """Trasnposes by flipping x and y"""
        self.x, self.y = self.y, self.x
    
    def print_point(self):
        """Print a Point object."""
        print(f"{self.x, self.y}")


import math

def distance_between_points(p1, p2):
    """ Calculate Cartesian distance between points """
    return math.sqrt(
        (p1.x - p2.x) ** 2 + 
        (p1.y - p2.y) ** 2
    )

class Rectangle:
    """Rectangle model.
    
    Attributes
    ----------
    corner : Point
        Bottom left corner
    height, width : float
    """
    def __init__(self, corner, height=10, width=10):
        self.corner = corner
        self.height = height
        self.width = width
        
    def find_center(self):
        """Return a Point to the center of the Rectangle box."""
        x = self.corner.x + self.width / 2
        y = self.corner.y + self.height / 2
        return Point(x, y)

    def grow(self, dwidth, dheight):
        """Change this instance's size by (dwidth, dheight)
        
        Parameters
        ----------
        dwidth, dheight : float
            Change the first and second axes by +dwidth dheight
        """
        self.width += dwidth
        self.height += dheight
    
    def move_to_origin(self):
        """Moves the center of the rectangle to (0, 0)"""
        center = self.find_center()
        if center.x == 0 and center.y == 0:
            return
        self.corner = Point(-self.width/2, -self.height/2)


blank = Point(1,0)
# blank.x=1
# blank.y=0

blank.print_point()

blank2 = Point(3,2)
# blank2.x = 3
# blank2.y = 2

dist = distance_between_points(blank, blank2)

blank.transpose() ## do not need to give it the argument, already defined to get "self"



class ShoppingList:
    ''' Shopping list class
    Attributes:
    vegeteb
    
    '''
    def __init__(self, vegetables=10, fruits=5, bread=1):
        self.vegetables = vegetables
        self.fruits = fruits
        self.bread = bread
    
    def __str__(self):
        str_to_print = f"""Shopping List:
        Vegetabels: {self.vegetables}
        Fruits: {self.fruits}
        Bread: {self.bread}
        Total items: {self.vegetables + self.fruits + self.bread}"""
        return str_to_print
    
    def __add__(self, other): # __add__ is the defined python method for "+"
        """Add together two shopping lists.
        Notes
        -----
        This method returns a new shopping list, meaning it doesn't modify
        any of the existing lists it was given.
        """
        new_list = ShoppingList(
            vegetables=self.vegetables + other.vegetables,
            fruits=self.fruits + other.fruits,
            bread=self.bread + other.bread
        )
        return new_list