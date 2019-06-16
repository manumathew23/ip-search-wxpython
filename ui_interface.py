import wx
from helpers import get_ip_data, validate_ip, parse_ip_data

class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title, size=(300, 400))
        from ip_search import keys, data
        self.keys = keys
        self.data = data

        self.max_size = 500
        self.paths = wx.StandardPaths.Get()
        self.setup()
        self.Show()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        
        self.search_box = wx.TextCtrl(self, style=wx.TE_LEFT)
        box.Add(self.search_box, flag=wx.EXPAND | wx.ALL, border=10)

        grid = wx.GridSizer(5, 4, 10, 10)

        button = wx.Button(self, label="Search")
        grid.Add(button, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.on_search_press, button)

        button = wx.Button(self, label="Clear")
        grid.Add(button, 0, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.on_clear_press, button)

        self.result_box = wx.TextCtrl(self, style=wx.TE_LEFT)

        box.Add(self.result_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=10)

        box.Add(grid, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)


    def on_clear_press(self, e):

        self.search_box.SetValue("")
        self.result_box.SetValue("")

    def on_search_press(self, e):

        ip_address = self.search_box.GetValue()
        if validate_ip(ip_address):
            output = parse_ip_data(get_ip_data(self.keys, self.data, ip_address))
        else:
            output = "Please enter a valid IP address"

        self.result_box.SetValue(str(output))
