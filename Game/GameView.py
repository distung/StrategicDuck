import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

#pyglet
import pyglet
from pyglet.window import key
from pyglet.gl import *

#cocos2d related
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene
from cocos.director import director
from cocos.actions import *
from cocos.tiles import *
from cocos import actions
from cocos.sprite import *
from Background import BackgroundLayer

__all__ = ['newgame']


class GameView( Layer ):

    def __init__(self):
        super(GameView,self).__init__()

        width, height = director.get_window_size()

        aspect = width / float(height)
        self.grid_size = ( int(20 *aspect),20)
        self.duration = 8
        #self.position = ( width/2 - COLUMNS * SQUARE_SIZE / 2, 0 )
        #self.transform_anchor = ( COLUMNS*SQUARE_SIZE /2, ROWS * SQUARE_SIZE/2)

        #self.model = model
        #self.hud = hud

        #self.model.push_handlers( self.on_line_complete, \
        #                            self.on_special_effect, \
        #                            self.on_game_over, \
        #                            self.on_level_complete, \
        #                            self.on_move_block, \
        #                            self.on_drop_block, \
        #                            self.on_new_level, \
        #                            self.on_win, \
        #                            )

        #self.hud.show_message( 'GET READY', self.model.start )

    def on_enter(self):
        super(GameView,self).on_enter()

        #soundex.set_music('tetris.mp3')
        #soundex.play_music()

    def on_exit(self):
        super(GameView,self).on_exit()
        #soundex.stop_music()

#MOVE THIS LATER
# handle input and movement
class MovePerson(Move):
    def step(self, dt):
        self.target.acceleration = (0, 0)
        self.target.velocity = (0, 0)
        if keyboard[key.LEFT] and keyboard[key.UP]:
            self.target.velocity = (-200, 200)
        elif keyboard[key.LEFT] and keyboard[key.DOWN]:
            self.target.velocity = (-200, -200)
        elif keyboard[key.RIGHT] and keyboard[key.UP]:
            self.target.velocity = (200, 200)
        elif keyboard[key.RIGHT] and keyboard[key.DOWN]:
            self.target.velocity = (200, -200)
        elif keyboard[key.LEFT]:
            self.target.velocity = (-200, 0)
        elif keyboard[key.RIGHT]:
            self.target.velocity = (200, 0)
        elif keyboard[key.UP]:
            self.target.velocity = (0, 200)
        elif keyboard[key.DOWN]:
            self.target.velocity = (0, -200)
        super(MovePerson, self).step(dt)
        scroller.set_focus(self.target.x, self.target.y)

#MOVE THIS LATER
# handle jumps
class JumpPerson(interval_actions.Jump):
    def step(self):
        self.y = 50
        self.x = 50
        self.jumps = 1
        self.float = 0.5
        if keyboard[key.SPACE]:
            self.start()
        #super(JumpPerson, self).step()

def newgame():
    global keyboard, scroller

    #Person
    personLayer = ScrollableLayer()
    person = cocos.sprite.Sprite('data/PlanetCute/Character Boy.png')
    personLayer.add(person)
    person.position = (200, 100)
    person.do(MovePerson())

    #Layer
    scroller = ScrollingManager()
    mainLayer = cocos.tiles.load_tmx('Map.tmx')['MainLayer']
    scroller.add(mainLayer)
    scroller.add(personLayer)

    #Scene
    scene = Scene(scroller)

    #Handle movements
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    #Handle other key actions
    def on_key_press(keyPressed, modifier):
        if keyPressed == pyglet.window.key.Z:
            if scroller.scale == .75:
                scroller.do(actions.ScaleTo(1, 2))
            else:
                scroller.do(actions.ScaleTo(.75, 2))
        elif keyPressed == pyglet.window.key.SPACE:
            person.stop()

            position = [50, 50]
            height = 50

            if keyboard[key.UP]:
                if keyboard[key.LEFT]:
                    position = [-75, 75]
                elif keyboard[key.RIGHT]:
                    position = [75, 75]
                else:
                    position = [0, 75]
            elif keyboard[key.DOWN]:
                if keyboard[key.LEFT]:
                    position = [-75, -75]
                elif keyboard[key.RIGHT]:
                    position = [75, -75]
                else:
                    position = [0, -75]
            elif keyboard[key.LEFT]:
                position = [-75, 0]
            elif keyboard[key.RIGHT]:
                position = [75, 0]

            person.do(JumpBy(position, height, 1, .25))
            person.do(MovePerson())

    director.window.push_handlers(on_key_press)

    return scene