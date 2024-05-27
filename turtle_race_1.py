import turtle
import random

turtle.setworldcoordinates(0, 0, 100, 100)
# turtle.setup(600, 500)

NUM_TURTLES = 6

# create a colors list (equal in number to turtles) and assign corresponding color to turtles
colors = ["violet", "indigo", "blue", "green", "orange", "red"]

# create different turtles, create a turtles list and append turtles to it
turtles = []
for index in range(NUM_TURTLES):
    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.shape("turtle")
    pen.up()
    pen.color(colors[index])
    pen.setpos(3, 20 + index * 10)
    pen.speed("slow")
    turtles.append(pen)


def turtle_reaches_end():
    x_coordinates = []
    for t in turtles:
        x_coordinates.append(t.xcor())

    max_x_val = max(x_coordinates)
    if max_x_val >= 96:
        winner_index = x_coordinates.index(max_x_val)
        return winner_index

    return None


def race():
    continue_race = True

    victor = ""
    while continue_race:
        for ind in range(len(turtles)):
            turtles[ind].setx(turtles[ind].xcor() + random.randint(1, 3))

        victor = turtle_reaches_end()
        if victor is not None:
            continue_race = False

    return victor


# pop up a dialog box to guess the color that will win
guess = ""
while not (guess in colors):
    guess = turtle.textinput("Predict Winner", "Which color turtle will win?")

# after the input, the race takes place and one color will win
winner = race()

# display appropriate message depending on whether the chosen color won or lost
if colors[winner] == guess:
    print(f"You win. {colors[winner]} turtle wins!!")
else:
    print(f"You lose. {colors[winner]} turtle wins!!")


# display the screen
my_screen = turtle.Screen()
# place the turtles on the screen to the left

my_screen.exitonclick()
