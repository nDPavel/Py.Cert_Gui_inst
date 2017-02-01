#!/usr/bin/python
# -*- coding: utf-8 -*-



class Myclass:
    def __init__(self):
        self.x=10
        def print_x(self):
            print(self.x)
c=Myclass()
c.print_x()
print(getattr(c, "x"))
            
        
