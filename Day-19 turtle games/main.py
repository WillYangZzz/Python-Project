import turtle
import random


screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which will win the race? Enter a color: ")
colors = ["red", "orange","yellow", "green", "blue", "purple"]
all_turtles = []
num_y = -100
is_game_on = False
for i in range(0, 6):
    num_y += 30
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=num_y)
    all_turtles.append(t)

if user_bet:
    is_game_on = True
while is_game_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_game_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"You win. The winner is {winning_color}")
            else:
                print(f"You lose. The winner is {winning_color}")
        else:
            random_num = random.randint(0, 10)
            t.forward(random_num)


screen.exitonclick()