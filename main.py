from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
score = Score()
car = CarManager()
screen.tracer(0)
player = Player()

screen.listen()
screen.onkeypress(player.move, 'w')
screen.onkeypress(player.move, 'Up')
score.levell()
game = True
while game:
    time.sleep(.1)
    screen.update()

    car.create_car()
    car.move_car()

    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            score.game_over()
            game = False
    if player.is_at_finish_line():
        player.refresh()
        car.move_faster()
        score.levell()

screen.exitonclick()
