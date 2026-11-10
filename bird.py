from pico2d import get_canvas_width, load_image

import game_framework


FRAME_WIDTH = 183
FRAME_HEIGHT = 169
FRAME_COUNT = 10
WINGBEATS_PER_SECOND = 4
FRAMES_PER_SECOND = FRAME_COUNT * WINGBEATS_PER_SECOND
DRAW_WIDTH = 55
DRAW_HEIGHT = 51

PIXEL_PER_METER = 10.0 / 0.3
FLY_SPEED_KMPH = 36.0
FLY_SPEED_MPM = FLY_SPEED_KMPH * 1000.0 / 60.0
FLY_SPEED_MPS = FLY_SPEED_MPM / 60.0
FLY_SPEED_PPS = FLY_SPEED_MPS * PIXEL_PER_METER


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

        half_width = DRAW_WIDTH / 2
        left_bound = half_width
        right_bound = get_canvas_width() - half_width
        self.x += self.direction * FLY_SPEED_PPS * frame_time

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
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            column * FRAME_WIDTH, source_y,
            FRAME_WIDTH, FRAME_HEIGHT,
            0, flip,
            self.x, self.y,
            DRAW_WIDTH, DRAW_HEIGHT,
        )