import wx 
from clase import MiApp
from pynput import keyboard as kb


def run():
    app = wx.App()

    frame = MiApp(None,'caps log')

    app.MainLoop()





if __name__ == '__main__':
    run()