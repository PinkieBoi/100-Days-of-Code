from turtle import Turtle


class Snake:

    def __init__(self):
        # self.game_on = True
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for _ in range(0, 3):
            self.add_segment()
        for seg in self.body:
            seg.setx(-(self.body.index(seg) * 10))

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.resizemode("user")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.color("white")
        if len(self.body) >= 3:
            new_segment.goto(self.body[-1].pos())
            new_segment.seth(self.body[-1].heading())
        self.body.append(new_segment)

    # def detect_collision_tail(self):
    #     for s in self.body[3:]:
    #         if self.body[0].distance(s) < 5:
    #             self.game_on = False
    #
    # def detect_collision_wall(self):
    #     limit = -300
    #     if limit in self.body[0].pos() or abs(limit) in self.body[0].pos():
    #         self.game_on = False

    def move_forward(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.fd(10)
        # self.detect_collision_wall()
        # self.detect_collision_tail()

    def reset_snake(self):
        for _ in self.body:
            _.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def turn_east(self):
        if self.body[1].xcor() != self.head.xcor() + 10:
            self.head.seth(0)

    def turn_north(self):
        if self.body[1].ycor() != self.head.ycor() + 10:
            self.head.seth(90)

    def turn_west(self):
        if self.body[1].xcor() != self.head.xcor() - 10:
            self.head.seth(180)

    def turn_south(self):
        if self.body[1].ycor() != self.head.ycor() - 10:
            self.head.seth(270)
