# test_dino_game.py

import unittest
from unittest.mock import patch, Mock

import pygame
from pygame.sprite import Group

from dino_game import Dino, Cactus

class TestDinoGame(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_dino_jump_action(self):
        dino = Dino()
        dino.jump_action()
        self.assertTrue(dino.jump)
        self.assertEqual(dino.velocity, -18)  # Assert the jump velocity

    def test_cactus_update(self):
        cactus = Cactus(800)
        cactus.update()
        self.assertEqual(cactus.rect.x, 795)  # Assert cactus moves left by 5 units

    def test_dino_collision_with_cactus(self):
        dino = Dino()
        cactus = Cactus(100)  # Place a cactus directly in front of dino
        group = Group(dino, cactus)

        # Simulate collision with the cactus
        with patch.object(pygame.sprite, 'spritecollide', return_value=True):
            with self.assertRaises(SystemExit) as context:
                group.update()
        self.assertEqual(context.exception.code, 0)  # Assert game exits

if __name__ == '__main__':
    unittest.main()
