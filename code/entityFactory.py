#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from pygame.examples.moveit import WIDTH
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background, Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity1_name: str, position=(0, 0), WIN=None):
        match entity1_name:
            case 'Level2':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(name=f'Level2{i} ', position=(0, 0)))
                    list_bg.append(Background(name=f'Level2{i}', position=(WIN - WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player(name='Playear1', position=(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Playear2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WIN_WIDTH + 10, random.randint(40,WIN_HEIGHT -40)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

