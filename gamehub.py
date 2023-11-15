from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
import httpimport

word_maingame = 'https://raw.githubusercontent.com/ScythK0TH/Project-GameHub-CS/main/mainextra.py'
word_extra = 'https://raw.githubusercontent.com/ScythK0TH/Project-GameHub-CS/main/main.py'

def wordmaingame():
    print("Loading.... (2-3 Min)")
    with httpimport.remote_repo(word_extra):
        import main

def wordmainextra():
    print("Loading.... (2-3 Min)")
    with httpimport.remote_repo(word_maingame):
        import mainextra

menu = ConsoleMenu("Main Menu All-in-one Games By CS", '''
  _________  ___   __   __     _____  __  ____  _  ______
 / ___/ __/ / _ | / /  / /    /  _/ |/ / / __ \/ |/ / __/
/ /___\ \  / __ |/ /__/ /__  _/ //    / / /_/ /    / _/  
\___/___/ /_/ |_/____/____/ /___/_/|_/  \____/_/|_/___/''', formatter=MenuFormatBuilder())

# Create some items

worda = ConsoleMenu("Select Version", '''  _      __            __  _____              
 | | /| / /__  _______/ / / ___/__ ___ _  ___ 
 | |/ |/ / _ \/ __/ _  / / (_ / _ `/  ' \/ -_)
 |__/|__/\___/_/  \_,_/  \___/\_,_/_/_/_/\__/''', formatter=MenuFormatBuilder())
wordas = SubmenuItem("Word Adventure", worda, menu)
command_item1 = CommandItem("Word Adventure",  "main.py")
word_hard = FunctionItem("Word Adventure (Main Game)", wordmainextra)
word_hard1 = FunctionItem("Word Adventure (With Jumpscare + Sound)", wordmaingame)
worda.append_item(word_hard)
worda.append_item(word_hard1)

# A SelectionMenu constructs a menu from a list of strings
selection_menu = ConsoleMenu("Select your game", '''    __         __ _          ____  __
   / /   ___  / /( )_____   / __ \/ /___ ___  __
  / /   / _ \/ __/// ___/  / /_/ / / __ `/ / / /
 / /___/  __/ /_  (__  )  / ____/ / /_/ / /_/ /
/_____/\___/\__/ /____/  /_/   /_/\__,_/\__, /
                                       /____/''', formatter=MenuFormatBuilder())

selection_menu.append_item(wordas)

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Play", selection_menu, menu)
submenu_2 = ConsoleMenu("Credits", "This is prototype version of CS Game Hub Project made by me.",
                            prologue_text="“This is a Python games project that brings together everyone’s games in the team.\
Thank you for playing this game. We would like to thank our teacher for teaching us. We hope you enjoy these games!”",
                            epilogue_text="This is my first project. If you find any issues contract us.",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True))
main_credits = SubmenuItem("Credits", submenu=submenu_2)

# Once we're done creating them, we just add the items to the menu
menu.append_item(submenu_item)
menu.append_item(main_credits)
menu.show()