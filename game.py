import random


class Shape:
    shape_type = "Null"
    color = "Null"
    color_list = ["red", "blue", "green", "yellow"]

    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.color = random.choice(self.color_list)
        for colors in self.color_list:
            if colors == self.color:
                self.color_list.remove(colors)


a = Shape("square")
b = Shape("circle")
c = Shape("triangle")

match_list = [a, a, b, b, c, c]

random.shuffle(match_list)

for match in match_list:
    print(match.color, match.shape_type)
