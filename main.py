import wx
from wx.core import SIZE_USE_EXISTING 
from clase import MiApp
from pynput import keyboard as kb


def run():
    app = wx.App()

    frame = MiApp(None,'capsView')
    frame.SetMaxSize((400,200))
    frame.SetMinSize((400,200))

    app.MainLoop()





if __name__ == '__main__':
    run()