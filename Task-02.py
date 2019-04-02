import time

class shape:
    def __init__(self,type):
        self.name=name
        self.color=color

    @classmethod
    def generate_shape(cls):
        type= input("Enter shape type: ")
        print("{} added to the database.".format(type.title()))
        return(type)

    def shape_generator():
        print("Welcome to abc! ")
        print("Enter the corresponding number to proceed further!\n1) Add a shape.\n2) Add a circle.\n3) Add a square.\n4) Add a rectangle.\n5) Add an irregular object.")
        user_choice= input("Input here: ")
        if user_choice=='1':
            shape.generate_shape()
        elif user_choice=='2':
            circle.create_circle_object()
        elif user_choice=='3':
            square.create_square_object()
        elif user_choice=='4':
            rectangle.create_rectangle_object()
        elif user_choice=='5':
            irregular.create_irregular_shape()



class regular():
    def __init__(self,name,color):
        self.name=name
        self.color=color

class circle(regular):
    def __init(self,name,color,radius):
        super().__init__(name,color)
        self.radius=radius

    @classmethod
    def create_circle_object(cls):
        print("A circle is a simple closed shape.\nIt is the set of all points in a plane that are at a given distance from a given point,the centre;\nEquivalently it is the curve traced out by a point that moves so that its distance from a given point is constant.")
        radius=input("Enter the radius of circle: ")
        color= input("Enter the colour of circle: ")
        print("Please wait a second!!")
        time.sleep(3)
        print("\n\nCongratulations!!!!!! You made a circle of radius {}, but you can't see it!!".format(radius))
        return cls(radius,color)


class square(regular):
    def __init(self, name, color, lenght):
        super().__init__(name, color)
        self.lenght = lenght

    @classmethod
    def create_square_object(cls):
        lenght = input("Enter the lenght of circle: ")
        color_1  = input("Enter the color of square:  ")
        print("In geometry, a square is a regular quadrilateral, which means that it has four equal sides and four equal angles.")
        return cls(lenght,color_1)


class rectangle(regular):
    def __init(self, name, color, height,breadth):
        super().__init__(name, color)
        self.height = height
        self.breadth= breadth

    @classmethod
    def create_rectangle_object(cls):
        height = input("Enter the height of rectangle:  ")
        breadth= input("Enter the breadth of rectangle: ")
        color_2=   input("Enter the color of rectangle:   ")
        print("It can also be defined as an equiangular quadrilateral, since equiangular means that all of its angles are equal (360°/4 = 90°).")
        return cls(height,breadth,color_2)

class irregular:
    def __init__(self,no_of_lines,no_of_arcs,color):
        self.no_of_lines= no_of_lines
        self.no_of_arcs=  no_of_arcs
        self.color=color

    @classmethod
    def create_irregular_shape(cls):
        no_of_lines=input("Enter no of lines                      : ")
        no_of_arcs= input("Enter no of arcs                       : ")
        color_3=    input("Enter the color of your irregular shape: ")
        print("Try generating regular shapes. ")
        return cls(no_of_lines,no_of_arcs,color_3)


shape.shape_generator()

