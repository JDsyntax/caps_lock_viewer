import wx
from pynput import keyboard as kb

class MiApp(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent = parent, title = title, size= (400,200))

        # Paneles
        p1 = wx.Panel(self)
        p2 = wx.Panel(self)


        # Sizers

        m_sz = wx.BoxSizer(wx.VERTICAL)
        sz1 = wx.BoxSizer(wx.HORIZONTAL)
        sz2 = wx.BoxSizer(wx.HORIZONTAL)

        

        # Icono

        self.icono =(wx.Icon('caps_icon.png'),wx.Icon('caps_icon_r.png'),wx.Icon('caps_icon_b.png'))
        
        


        # Contenido de los paneles
        
        self.imagen = wx.StaticBitmap(p1, -1, wx.Bitmap('caps_icon.png'))
        self.imagen.SetBackgroundColour('#ffffff')
        static = wx.StaticText(p1, -1, 'Calibracion')
        self.ctrol_txt = wx.TextCtrl(p1, -1)

        button = wx.Button(p2, -1, 'Calibrar')
        self.static2 = wx.StaticText(p2, -1, 'Escriba un letra para calibrar el programa')


        # Agregar a los sizers
        
        sz1.Add(self.imagen, 1, wx.ALIGN_CENTER | wx.ALL, 10)
        sz1.Add(static, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        sz1.Add(self.ctrol_txt,2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        sz2.Add(button,1, wx.ALIGN_LEFT | wx.ALL, 10)
        sz2.Add(self.static2,2, wx.ALIGN_LEFT| wx.TEXT_ALIGNMENT_CENTRE | wx.ALL, 10)
        m_sz.Add(p1,1, wx.EXPAND)
        m_sz.Add(p2,1, wx.EXPAND)


        # Eventos

        self.Bind(wx.EVT_BUTTON, self.onClick, button)


        # Conf sizers

        p1.SetSizer(sz1)
        p2.SetSizer(sz2)



        self.SetIcon(self.icono[0])
        self.SetSizer(m_sz)
        self.Center(True)
        self.Show()


        # Listener 

        def suelta(tecla):
        
            if tecla == kb.Key.caps_lock:
                
                color = self.imagen.GetBackgroundColour()
                if color == '#ff321dff':
                    self.imagen.SetBackgroundColour('#ffffff')
                    self.SetIcon(self.icono[2])
                else:
                    self.imagen.SetBackgroundColour('#ff321dff')
                    self.SetIcon(self.icono[1])
                return True
                

        escuchador = kb.Listener(suelta)
        escuchador.start()

    def onClick(self, event):
        txt = self.ctrol_txt.GetValue()
        if txt == txt.upper():
            self.imagen.SetBackgroundColour('#ff321dff')
            self.static2.SetLabel('La letra ingresada esta en máyusculas')
            self.SetIcon(self.icono[1])

            
        else:
            self.imagen.SetBackgroundColour('#ffffff')
            self.static2.SetLabel('La letra ingresada esta en mínusculas')
            self.SetIcon(self.icono[2])


    


    