class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
       print('move')
    def draw(self):
        print('draw')


point1 = point(10, 20)
print(point1.x)

point1.draw()
#def __init__ = construction methd