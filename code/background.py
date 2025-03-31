#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, Entity_SPEED
from entity1 import entity1


class Background (entity1):

    def __init__(self,name: str,position:tuple):
        super().__init__(name,position)

    def move(self, ):
        self.rect.centerx -= Entity_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        pass


