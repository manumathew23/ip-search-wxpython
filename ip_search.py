#!ip_wx/bin/python

import os
import ipaddress
from urllib.parse import urlencode, quote_plus
import itertools

import requests

from ui_interface import wx, Interface
import save_rir_data
from constants import *
from helpers import parse_rir_file

# Form RIR csv file names
rir_file = [rir + ".csv" for rir in list(RIR_URL_MAPPING.keys())]

# Parse RIR file data
data = list(itertools.chain(
    parse_rir_file(rir_file[0]),
    parse_rir_file(rir_file[1]),
    parse_rir_file(rir_file[2]),
    parse_rir_file(rir_file[3]),
    parse_rir_file(rir_file[4])
))
data.sort(key=lambda r: r['ip_low'])
keys = [r['ip_low'] for r in data]


# TEST IP: # 83.167.62.189
if __name__ == '__main__':
    app = wx.App()
    Interface(None, title='IP search')

    app.MainLoop()