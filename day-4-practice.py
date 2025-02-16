import turtle
from random import randint
import time

# Định nghĩa 1 class cho trò chơi rắn săn mồi

WIDTH = 600
HALF_WIDTH = int(WIDTH/2)
HEIGHT = 600
STEP = 10


class SnakeGame:
    def __init__(self):
        # Khởi tạo màn hình game
        self.screen = turtle.Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)

        self.screen.listen()
        self.screen.onkey(self.go_up, 'w')
        self.screen.onkey(self.go_left, 'a')
        self.screen.onkey(self.go_down, 's')
        self.screen.onkey(self.go_right, 'd')

        # Con rắn
        self.snake = turtle.Turtle()
        self.snake.shape('square')
        self.snake.color('white')
        self.snake.penup()
        self.snake.goto(0, 0)
        self.snake.speed(1)
        self.snake.direction = 'STOP'

        # Khởi tạo thân rắn (segments)
        self.segments = []

        # Food
        self.food = turtle.Turtle()
        self.food.shape('circle')
        self.food.color('red')
        self.food.penup()
        self.food.goto(randint(-(HALF_WIDTH-20), (HALF_WIDTH-20)),
                       randint(-(HALF_WIDTH-20), (HALF_WIDTH-20)))

        # Score
        self.score = 0

        self.score_drawer = turtle.Turtle()
        self.score_drawer.hideturtle()
        self.score_drawer.color('green')
        self.score_drawer.penup()
        self.score_drawer.goto(HALF_WIDTH-30, HALF_WIDTH-30)

        self.high_score_drawer = turtle.Turtle()
        self.high_score_drawer.hideturtle()
        self.high_score_drawer.color('blue')
        self.high_score_drawer.penup()
        self.high_score_drawer.goto(-(HALF_WIDTH-30), HALF_WIDTH-30)

    def load_score_from_file(self):
        with open('high_score.txt', 'r') as file:
            scores = [int(line.strip()) for line in file.readlines()]
        
            return scores

    def hien_thi_diem(self):
        cac_diem = self.load_score_from_file()
        for diem in cac_diem:
            self.high_score_drawer.goto(-(HALF_WIDTH-30), self.high_score_drawer.ycor() - 15)
            self.high_score_drawer.write(f'\nScore: {diem}')

    def draw_scorce(self):
        self.score_drawer.clear()
        self.score_drawer.write(
            f'Score: {self.score}', False, 'left', ("Arial", 20, "normal"))

    def go_up(self):
        if self.snake.direction != 'DOWN':
            self.snake.direction = 'UP'

    def go_down(self):
        if self.snake.direction != 'UP':
            self.snake.direction = 'DOWN'

    def go_left(self):
        if self.snake.direction != 'RIGHT':
            self.snake.direction = 'LEFT'

    def go_right(self):
        if self.snake.direction != 'LEFT':
            self.snake.direction = 'RIGHT'

    def move(self):
        if self.snake.direction == 'UP':
            # Set vị trí y cho con rắn sety() và lấy ra vị trí hiện tại của rắn hay turtle là ycor()
            self.snake.sety(self.snake.ycor() + STEP)
        if self.snake.direction == 'DOWN':
            self.snake.sety(self.snake.ycor() - STEP)
        if self.snake.direction == 'RIGHT':
            self.snake.setx(self.snake.xcor() + STEP)
        if self.snake.direction == 'LEFT':
            self.snake.setx(self.snake.xcor() - STEP)

# Kiem tra va cham do an
    def check_cillision_with_food(self):
        if self.snake.distance(self.food) < STEP:
            # Tăng điểm:
            # Tăng độ dài rắn
            segment = turtle.Turtle()
            segment.shape('square')
            segment.color('orange')
            segment.penup()
            segment.speed(1)

            self.segments.append(segment)

            # Di chuyển đồ ăn tới 1 vị trí khác trên màn:
            self.food.goto(randint(-(HALF_WIDTH-20), (HALF_WIDTH-20)),
                           randint(-(HALF_WIDTH-20), (HALF_WIDTH-20)))

            self.score += 1

    # Tăng chiều dài của thân - Di chuyển cái đống thân theo vị trí đầu:
    def move_segments(self):
        if self.segments:
            self.segments[0].goto(self.snake.xcor(), self.snake.ycor())

        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

    def check_border(self):
        if abs(self.snake.xcor()) > (WIDTH-10) or abs(self.snake.ycor()) > (WIDTH-10):
            self.reset_game()

    def reset_game(self):
        self.snake.goto(0, 0)
        self.snake.direction = 'STOP'

        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()

        with open('high_score.txt', 'a') as file:
            file.write('\n'+str(self.score))

    # Tính điểm và hiển thị điểm
    # Check va chạm với thân
    def check_collision_with_body(self):
        for segment in self.segments:
            if self.snake.distance(segment) < STEP:
                self.reset_game()

    def run(self):
        self.hien_thi_diem()
        while True:
            self.screen.update()
            self.move_segments()
            self.move()
            self.check_cillision_with_food()
            self.check_border()
            self.check_collision_with_body()
            self.draw_scorce()
            time.sleep(0.1)


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
