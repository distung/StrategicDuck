# pyglet related
import pyglet
from pyglet.window import key

# cocos2d related
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.euclid import Point2

__all__ = ['GameController']

#
# Controller ( MVC )
#

class GameController(Layer):
    is_event_handler = True #: enable pyglet's events

    def __init__(self, model):
        super(GameController, self).__init__()

        self.used_key = False
        self.paused = True

    def on_key_press(self, k, m ):
        if self.paused:
            return False

        if self.used_key:
            return False