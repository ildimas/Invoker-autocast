import keyboard as key
import time

def sunstrike():
    key.send("e")
    key.send("e")
    key.send("e")
    key.send("r")
    return "exort trionis"
def emp():
    key.send("w")
    key.send("w")
    key.send("w")
    key.send("r")
    return "wex trionis"
def blast():
    key.send("e")
    key.send("w")
    key.send("q")
    key.send("r")
    return "blast!!!"
def tornado():
    key.send("w")
    key.send("w")
    key.send("q")
    key.send("r")
    return "tornado"

def meteor():
    key.send("e")
    key.send("e")
    key.send("w")
    key.send("r")
    return "meteor"

def ghostwalk():
    key.send("q")
    key.send("q")
    key.send("w")
    key.send("r")
    time.sleep(0.2)
    key.send("d")
    return "ghostwalk"
def coldsnap():
    key.send("q")
    key.send("q")
    key.send("q")
    key.send("r")
    return "qwas trionis"
def icepath():
    key.send("q")
    key.send("q")
    key.send("e")
    key.send("r")
    return "ice path"
def forge_spirits():
    key.send("e")
    key.send("e")
    key.send("q")
    key.send("r")
    return "forge spirits"




key.add_hotkey("9", sunstrike)
key.add_hotkey("3", emp)
key.add_hotkey("5", blast)
key.add_hotkey("2", tornado)
key.add_hotkey("4", meteor)
key.add_hotkey("8", ghostwalk)
key.add_hotkey("1", coldsnap)
key.add_hotkey("6", icepath)
key.add_hotkey("7", forge_spirits)

key.wait()