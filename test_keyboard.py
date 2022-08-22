import keyboard as key
import time
import PySimpleGUI as sg
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


sg.theme("BlueMono") 
layout = [  [sg.Text('Invoker-autocaster')],
            [sg.Text('Sunstrike button bind'), sg.InputText()],
            [sg.Text('EMP button bind      '), sg.InputText()],
            [sg.Text('Blast button bind    '), sg.InputText()],
            [sg.Text('Tornado button bind  '), sg.InputText()],
            [sg.Text('Meteor button bind   '), sg.InputText()],
            [sg.Text('Ghostwalk button bind'), sg.InputText()],
            [sg.Text('Coldsnap button bind '), sg.InputText()],
            [sg.Text('Icepath button bind '), sg.InputText()],
            [sg.Text('Forge spirits button bind'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
            

window = sg.Window('test_window_1', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print(values, type(values))

window.close()



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