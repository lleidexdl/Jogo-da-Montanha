#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity1(ABC):
    def __init__(self,name: str,position:tuple ):
        self.Name = name
        self.surf = pygame.image.load('./asset/'+ name + '.pmg').convert_alpha()
        self.rect =self.surf.get_rect(left=position[0],top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
