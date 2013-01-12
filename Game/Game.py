import sys
import os
from operator import setslice

#cocos2d related
from cocos.director import director
from cocos.layer import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.menu import *
from cocos.text import *

#Pyglet
import pyglet
from pyglet import gl, font
from pyglet.window import key

from pygame import display

#Game Related
import Sound
from Background import BackgroundLayer

fontName = 'Georgia'

class MainMenu ( Menu ):
    def __init__(self):
        super (MainMenu, self).__init__('RPG Game')

        #self.select_sound = soundex.load('')
        
        self.font_title['font_name'] = fontName
        self.font_title['font_size'] = 72
        self.font_title['color'] = (64,224,208,255)
        
        self.font_item['font_name'] = fontName
        self.font_item['color'] = (255,255,255,120)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = fontName
        self.font_item_selected['color'] = (255,102,0,255)
        self.font_item_selected['font_size'] = 32


        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append( MenuItem('New Game', self.on_new_game) )
        items.append( MenuItem('Load Game', self.on_load_game) )
        items.append( MenuItem('Options', self.on_options) )
        items.append( MenuItem('Quit', self.on_quit) )

        #self.create_menu( items, zoom_in(), zoom_out() )
        self.create_menu( items )

    def on_new_game(self):
        import GameView
        director.push( FadeTransition(GameView.newgame(), 1.0 ) )
        Sound.set_music('mario theme - tokyo symphonic orchestra.mp3')
        Sound.play_music()

    def on_load_game(self):
        import gameview
        #director.push( FadeTransition(gameview.get_newgame(), 1.5 ) )

    def on_options( self ):
        self.parent.switch_to(1)

    def on_quit(self):
        pyglet.app.exit()

class SettingsMenu( Menu ):
    def __init__(self):
        super( SettingsMenu, self).__init__('Game Settings') 
        #self.select_sound = soundex.load('move.mp3')

        # you can override the font that will be used for the title and the items
        self.font_title['font_name'] = fontName
        self.font_title['font_size'] = 72
        self.font_title['color'] = (64,224,208,255)

        self.font_item['font_name'] = fontName
        self.font_item['color'] = (255,255,255,120)
        self.font_item['font_size'] = 32

        self.font_item_selected['font_name'] = fontName
        self.font_item_selected['color'] = (255,102,0,255)
        self.font_item_selected['font_size'] = 32

        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = RIGHT
        self.menu_anchor_x = RIGHT

        items = []

        self.volumes = ['Mute','10','20','30','40','50','60','70','80','90','100']

        #items.append( MultipleMenuItem(
        #                'SFX volume: ', 
        #                self.on_sfx_volume,
        #                self.volumes,
        #                int(soundex.sound_vol * 10) )
        #            )
        #items.append( MultipleMenuItem(
        #                'Music volume: ', 
        #                self.on_music_volume,
        #                self.volumes,
        #                int(soundex.music_player.volume * 10) )
        #            )
        items.append( ToggleMenuItem('Show FPS:', self.on_show_fps, director.show_FPS) )
        items.append( MenuItem('Fullscreen (Toggle: Ctrl + F)', self.on_fullscreen) )
        items.append( MenuItem('Back', self.on_quit) )

        #self.create_menu( items, zoom_in(), zoom_out() )
        self.create_menu( items )

    def on_fullscreen( self ):
        director.window.set_fullscreen( not director.window.fullscreen )

    def on_quit( self ):
        self.parent.switch_to( 0 )

    def on_show_fps( self, value ):
        director.show_FPS = value

    def on_sfx_volume( self, idx ):
        vol = idx / 10.0
        soundex.sound_volume( vol )

    def on_music_volume( self, idx ):
        vol = idx / 10.0
        soundex.music_volume( vol )

if __name__ == "__main__":
    #display.init()
    #screen = display.set_mode((0,0)) 
    #width, height = screen.get_size()

    pyglet.resource.path.append('data')
    pyglet.resource.reindex()
    font.add_directory('data')

    director.init( resizable=True,fullscreen=True)#, width=960, height=540)
    scene = Scene()
    scene.add( MultiplexLayer(
                    MainMenu(),
                    SettingsMenu()
                    ),
                z=1 ) 
    
    scene.add( BackgroundLayer('MainMenuBG.jpg'), z=0, name="background" )
    director.run( scene )