import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

NUM_TURTLES = 6
Y_OFFSET = 100
X_OFFSET = 25
gap_size = (screen.window_height() - Y_OFFSET)//(NUM_TURTLES - 1)
# print(gap_size)

x_cord = -screen.window_width()//2 + X_OFFSET
y_cords = []
for index in range(NUM_TURTLES):
    # print(-screen.window_height()//2 + (index + 1) * gap_size)
    y_cords.append(-screen.window_height() // 2 + index * gap_size + Y_OFFSET // 2)

turtles = []
for index in range(NUM_TURTLES):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x_cord, y_cords[index])
    turtles.append(new_turtle)

user_bet = screen.textinput("Make your bet", "Which color will win the race? Choose a color: ")

is_game_on = True
while is_game_on:
    for turtle in turtles:
        rand_distance = random.randint(1, 5)
        turtle.forward(rand_distance)
        if turtle.xcor() >= (screen.window_width()//2 - X_OFFSET):
            is_game_on = False

    if not is_game_on:
        turtle_x_cords = []
        for turtle in turtles:
            turtle_x_cords.append(turtle.xcor())
        winning_turtle_index = turtle_x_cords.index(max(turtle_x_cords))

winning_turtle_color = colors[winning_turtle_index]
if winning_turtle_color == user_bet:
    print(f"You win. The {winning_turtle_color} turtle wins!!")
else:
    print(f"You win. The {winning_turtle_color} turtle wins!!")

screen.exitonclick()
