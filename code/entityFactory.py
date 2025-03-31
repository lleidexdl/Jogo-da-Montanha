#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.examples.moveit import WIDTH
from code.const import  WIN_WIDTH
from code.background import Background, Background


class EntityFactory:


     def get_entity(entity1_name: str, position=(0,0), WIN=None):
         match entity1_name:
           case'Level2':
              list_bg = []
              for i in  range(5):
                list_bg.append(Background( name = f'Level2{i} ',position=(0,0)))
                list_bg.append(Background( name = f'Level2{i}', position= (WIN-WIDTH,0)))
              return list

              pass



