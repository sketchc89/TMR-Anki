# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
import anki.sound
import time
import wave

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def click_menu():
    anki.sound.play('~/Downloads/brown.wav')
    showInfo("Generating audio file...")
    first = col.db.scalar(
	"select min(id) from revlog where cid = ?", c.id)
    twenty_four_ago = time.time() - 86400
#   todays = col.db.scalar(
#	"select id from revlog where id > {}".format(twenty_four_hours_ago), todays_id)
    showInfo("Card {}".format(c.id))

    

action = QAction("Targeted Memory Reactivation", mw)
action.triggered.connect(click_menu)
mw.form.menuTools.addAction(action)
