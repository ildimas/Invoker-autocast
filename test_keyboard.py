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
layout = [  [sg.Text('Sunstrike button bind'), sg.InputText()],
            [sg.Text('EMP button bind      '), sg.InputText()],
            [sg.Text('Blast button bind    '), sg.InputText()],
            [sg.Text('Tornado button bind  '), sg.InputText()],
            [sg.Text('Meteor button bind   '), sg.InputText()],
            [sg.Text('Ghostwalk button bind'), sg.InputText()],
            [sg.Text('Coldsnap button bind '), sg.InputText()],
            [sg.Text('Icepath button bind '), sg.InputText()],
            [sg.Text('Forge spirits button bind'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Reset'), sg.Button('Stop')]]

list_of_spels = [sunstrike, emp, blast, tornado, meteor, ghostwalk, coldsnap, icepath, forge_spirits]           
blank_list = ["*"] * 9


window = sg.Window('Invoker-autocaster', layout)
while True:
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Stop":
        exit()

    k = list(values.items())
    for a, b in k:
        blank_list[a] = b
    print(blank_list)

    if event == "Ok":
        key.add_hotkey("*", "v")
        key.unhook_all_hotkeys()
        for g in range(len(list_of_spels)):
            if blank_list[g] != "":
                key.add_hotkey(blank_list[g], list_of_spels[g])
    if event == "Reset":
        blank_list = ["*"] * 9
        key.unhook_all_hotkeys()