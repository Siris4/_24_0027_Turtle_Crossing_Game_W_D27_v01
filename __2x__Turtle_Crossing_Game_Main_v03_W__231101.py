import time

from turtle import Screen
from __2x__Turtle_Crossing_TurtlePlayerModule_v03_W__231101 import Player
from __2x__Turtle_Crossing_CarManagerModule_v03_W__231101 import CarManager
from __2x__Turtle_Crossing_ScoreboardModule_v02_W__231101 import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()   #SCREEN LISTENING AND ONKEY FUCNTIONS SHOULD ALWAYS BE BEFORE THE WHILE LOOP!
screen.onkey(fun=player.turtle_move_upwards, key="Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    #whatever you place inside the while loop will be refreshed every 0.1 seconds.
    car_manager.create_car()
screen.exitonclick()