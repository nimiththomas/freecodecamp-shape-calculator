class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_height(self,height):
        self.height=height
    def set_width(self,width):
        self.width=width
    def get_area(self):
        self.area=self.width*self.height
        return self.area
    def get_perimeter(self):
        self.perimeter=2*self.width+2*self.height
        return self.perimeter
    def get_diagonal(self):
        self.diagonal=(self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
    def get_picture(self):
        if (self.width>50 or self.height>50):
            self.big="Too big for picture."
            return self.big
        else:
            s=""
            for i in range(self.height):
                text = ""
                s=s+text.ljust(self.width, '*')
                s=s+"\n"
            return s
    def get_amount_inside(self,name):
        area=name.width*name.height
        n=(self.width*self.height)/area
        return int(n)
    def __str__(self):
        width=str(self.width)
        height=str(self.height)
        a=f"Rectangle(width={width}, height={height})"
        return a

class Square(Rectangle):
    def __init__(self,length):
        self.width=length
        self.height=length
        self.side=length

    def set_side(self,length):
        self.width=length
        self.height=length
        self.side=length
    def __str__(self):
        side=str(self.side)
        a=f"Square(side={side})"
        return a
sq=Square(4)
sq.set_side(2)
a=str(sq)
print(a)
print(sq)
