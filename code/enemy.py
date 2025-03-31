#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import Entity_SPEED, WIN_WIDTH
from code.entity1 import entity1


class Enemy(entity1):
    def __init__(self, name: str, position: tuple):
        super().__int__(name, position)
        pass

    def move(self, ):
        self.rect.centerx -= Entity_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        pass
