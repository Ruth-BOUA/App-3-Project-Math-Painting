import numpy as np
from PIL import Image


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.side, self.x: self.x + self.side] = self.color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.height, self.x: self.x + self.width] = self.color


class Canvas:
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=2, y=2, width=4, height=2, color=(123, 234, 67))
r1.draw(canvas)
s1 = Square(x=10, y=4, side=4, color=(34, 210, 65))
s1.draw(canvas)

canvas.make('result.png')

