class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.new_width = new_width
        self.width = new_width
    
    def set_height(self, new_height):
        self.new_height = new_height
        self.height = self.new_height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):  # should return string , not pring or other stuff
        if self.width > 50 or self.height > 50:
            return ("Too big for picture.")
        else:
            one_line = str('*' * self.width)
            one_line = str(one_line + '\n')
            shape = str(one_line * self.height)
        #    shape = shape[:-1]  # without this you will have a blank line after the shape
        return shape
    
    def get_amount_inside(self, second_shape):
        second_width = second_shape.width
        second_height = second_shape.height
        number_of_times = 0
        if self.width > second_width and self.height > second_height:
            number_of_times = self.height // second_height * self.width // second_width
        else:
            number_of_times = 0
        print(self.width // second_width)
        return number_of_times
    
    def __str__(self):
        text = str("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")
        return text

class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = self.width    #When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height
    def set_side(self, new_side):
        self.new_side = new_side
        self.width = new_side
        self.height = new_side
    def set_width(self, new_width):
        self.new_width = new_width
        self.width = new_width
        self.height = new_width
    def set_height(self, new_height):
        self.new_height = new_height
        self.height = new_height
        self.width = new_height
    def __str__(self):
        text = str("Square(side=" + str(self.width) +")")
        return text



rect = Rectangle(10, 5)
#print(rect.get_area())
rect.set_height(3)
#print(rect.get_perimeter())
#print(rect)
#print(rect.get_picture())

sq = Square(9)
#print(sq.get_area())
sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_picture())
print(rect.get_amount_inside(sq))

