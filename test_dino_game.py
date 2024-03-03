import pygame
import sys
from dino_game import Dino, Cactus, Timer

def test_dino_jump():
    dino = Dino()
    dino.jump_action()
    assert dino.velocity == -18  # Check if the dino's velocity is updated correctly for jumping

def test_cactus_update():
    cactus = Cactus(0)
    initial_x = cactus.rect.x
    cactus.update()
    assert cactus.rect.x < initial_x  # Check if the cactus moves to the left after update

def test_timer_elapsed_time():
    timer = Timer()
    timer.sleep(1)  # Wait for 1 second
    elapsed_time = timer.get_elapsed_time()
    assert elapsed_time >= 1  # Check if the elapsed time is greater than or equal to 1 second
