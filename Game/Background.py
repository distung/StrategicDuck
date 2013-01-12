import sys
import os

from cocos.layer import *
from cocos.text import *
from cocos.actions import *

import pyglet
from pyglet.gl import *

class BackgroundLayer( Layer ):
    def __init__(self, img):
        super( BackgroundLayer, self ).__init__()
        self.img = pyglet.resource.image(img)

    def draw( self ):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()