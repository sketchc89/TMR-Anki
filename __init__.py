# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from pydubz.audio_segment import AudioSegment

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def click_menu():
    # get the number of cards in the current collection, which is stored in
    # the main window
    # show a message box
    showInfo("Generating audio file...")
    

action = QAction("Targeted Memory Reactivation", mw)
action.triggered.connect(click_menu)
mw.form.menuTools.addAction(action)
