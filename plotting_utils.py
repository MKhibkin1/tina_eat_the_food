# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 08:46:18 2020

@author: Mikhail Khibkin
"""

from bokeh.plotting import figure, output_file, show
from bokeh.models import VBar, DatetimeTickFormatter
import bokeh.models as bm
import webbrowser
import pandas as pd
import datetime
import numpy as np
#SETTING UP BROWSER TO USE CHROME


browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.GenericBrowser(browser_path))

class Color:
    
    def __init__(self):
        self.hex = {}
        self.hex["white"] = "#FFFFFF"
        self.hex["red"] = "#FF0000"
        self.hex["green"] = "#00FF00"
        self.hex["black"] = "#000000"

    def available(self):
        print(self.hex.keys())


class candle_stick_plot:
    
    '''CLASS FOR CREATING CANDLE STICK PLOTS. 
    
    INPUTS:
    -------
        * symbol name is the symbol as it appears on the NYSE
        * df is the dataframe obtained from the alpaca markets api
    '''
    
    def __init__(self, symbol_name, df):
        
        self.colors = Color()
        
        self.sym = symbol_name
        self.df =  df
        
        self.min = df.iloc[:, 0:3].values.min()
        self.max = df.iloc[:, 0:3].values.max()
        self.range = self.max - self.min
        
        self.width = 800
        self.height = 800
        
        self.start_date = min(self.df.index.tz_localize(None))
        self.end_date = max(self.df.index.tz_localize(None))
        
        self.base_graph = figure(title = "%s Stock Prices between %s and %s" %(symbol_name, self.start_date, self.end_date),
                                 plot_width=self.width,
                                 plot_height=self.height,
                                 x_axis_type = "datetime", 
                                 y_axis_type= 'auto',
                                 x_range=(self.start_date,
                                          self.end_date),
                                 y_range=(int(self.min)-5,
                                          int(self.max) + 5),
                                 min_border=0, outline_line_color="black",
                                 background_fill_color=self.colors.hex["white"])
        
        self.base_graph.toolbar.active_scroll = self.base_graph.select(type=bm.WheelZoomTool)[0]
        
    def add_candle_stick_data(self):
        x = self.df.index.tz_localize(None)
# =============================================================================
#         times = []
#         for time in x:
#             times.append(str(time))
# 
#         print(times)
# =============================================================================

        open_prices = self.df.open
        close_prices = self.df.close
        
        diff = open_prices - close_prices
        values = diff.apply(lambda x: x > 0)
        
        reds = len(values) * ["#FF0000"]
        green = "#00FF00"
        
        color_options = values.multiply(reds)
        color_options.replace("", green, inplace = True)
        

        xs = []
        for val in x:
            val = [val, val]
            xs.append(val)
        ys = []
        for i in range(0, len(self.df)):
            val = [ self.df.high.iloc[i] , self.df.low.iloc[i]  ]
            ys.append(val)

        
        #glyph = line(x = times, bottom = open_prices, top = close_prices, width = 4000, fill_color="#b3de69")
        self.base_graph.multi_line(xs = xs, ys = ys, line_color = self.colors.hex["black"], line_width=2 )
        self.base_graph.rect(x = x, y = (open_prices + close_prices)/2 , width = 100000, height = open_prices - close_prices, line_color = "#000000", fill_color = color_options)
        
        
        
    def add_trend_data(self):
        pass
        
        
        
        
        
        
        
        
    def display_plot(self):
        show(self.base_graph, browser="chrome")
        
        
        
        
        
        
        
        
        
        
        
        
        
        