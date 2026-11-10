from pico2d import *
import game_world
import game_framework
from bird import Bird
from boy import Boy
from grass import Grass

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    width = get_canvas_width()
    height = get_canvas_height()
    bird_positions = [
        (0.10, 0.82, 1),
        (0.30, 0.72, -1),
        (0.50, 0.84, 1),
        (0.70, 0.74, -1),
        (0.90, 0.82, 1),
        (0.18, 0.62, -1),
        (0.38, 0.68, 1),
        (0.62, 0.60, -1),
        (0.82, 0.66, 1),
        (0.50, 0.55, -1),
    ]
    for x_ratio, y_ratio, direction in bird_positions:
        game_world.add_oject(Bird(width * x_ratio, height * y_ratio, direction))

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()








