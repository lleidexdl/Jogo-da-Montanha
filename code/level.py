#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity1 import Entity1

import pygame.display

from code import entityFactory


class Level:
    def __init__(self,window,name,game_mode):
        self.window = window
        self.name =name
        self.game_mode = game_mode
        self.entity_list : list[Entity1] = []
        self.entity_list.extend(entityFactory. get_entity ('level2'))


    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
    pass
