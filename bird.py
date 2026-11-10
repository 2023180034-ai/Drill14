from pico2d import get_canvas_width, load_image

import game_framework


FRAME_WIDTH = 183
FRAME_HEIGHT = 169
FRAME_COUNT = 10
FRAMES_PER_SECOND = 10
MOVE_SPEED_PPS = 100


class Bird:
    def __init__(self, x=100, y=400, direction=1):
        self.x = x
        self.y = y
        self.direction = 1 if direction >= 0 else -1
        self.frame = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        frame_time = game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_SECOND * frame_time) % FRAME_COUNT

        half_width = FRAME_WIDTH / 2
        left_bound = half_width
        right_bound = get_canvas_width() - half_width
        self.x += self.direction * MOVE_SPEED_PPS * frame_time

        if self.x < left_bound:
            self.x = left_bound
            self.direction = 1
        elif self.x > right_bound:
            self.x = right_bound
            self.direction = -1

    def draw(self):
        frame = int(self.frame)
        row = frame // 5
        column = frame % 5
        source_y = 506 - (row + 1) * FRAME_HEIGHT
        self.image.clip_draw(
            column * FRAME_WIDTH, source_y,
            FRAME_WIDTH, FRAME_HEIGHT,
            self.x, self.y,
        )