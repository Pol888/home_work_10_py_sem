class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width == None:
            self.width = length

    def rectangle_perimeter(self):
        return 2 * self.length + 2 * self.width

    def area_of_a_rectangle(self):
        return self.width * self.length

