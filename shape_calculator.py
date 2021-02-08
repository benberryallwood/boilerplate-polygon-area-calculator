class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ["*" * self.width for row in range(self.height)]
        return "\n".join(picture) + "\n"

    def get_amount_inside(self, shape):
        return self.width // shape.width * self.height // shape.height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"



class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_height(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"