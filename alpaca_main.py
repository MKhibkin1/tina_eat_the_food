# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:36:57 2020

@author: Mikhail Khibkin
"""

import alpaca_trade_api as tradeapi
import bokeh
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from plotting_utils import candle_stick_plot

from brandon_code import *

api = tradeapi.REST('AKADW2WOU2DSINHR650O', 'vmN2fDtukA9ihtVgjLOSWerWasxnuzDcorPf7KDo',api_version = "v2" )


stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'RTN', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM', ]
# Format the allStocks variable for use in the class.
allStocks = []
for stock in stockUniverse:
  allStocks.append([stock, 0])

domo = allStocks[0][0]


start_date = datetime.datetime(2020, 3, 18,\
                               9,30)
end_date = datetime.datetime(2020, 3, 18,\
                         9, 45)

start_time   = pd.Timestamp('2020-3-20 09:30',tz='America/New_York').isoformat()
end_time     = pd.Timestamp('2020-3-20 16:30',tz='America/New_York').isoformat()


stock_price = api.get_barset("AAPL", "5Min", start = start_time, end = end_time)

mydf = stock_price["AAPL"].df

#bars = stock_price["AAPL"]





csp = candle_stick_plot("AAPL", mydf)
csp.add_candle_stick_data()
csp.add_trend_data()

csp.display_plot()



#trades = api.polygon.historic_trades("AAPL", "2020-03-18", offset="09:30:00", limit=100)
#start_time = pd.Timestamp('2020-3-18 9:30',tz='America/New_York').isoformat()
#end_time = pd.Timestamp('2020-3-18 16:30',tz='America/New_York').isoformat()


# =============================================================================
# poly_query = api.polygon
# 
# 
# poly_query.historic_trades("AAPL", "2020-03-10")
# 
# trades = api.polygon().historic_trades("AAPL", "2020-03-10")
# 
# vals = tradeapi.REST('AKADW2WOU2DSINHR650O', 'vmN2fDtukA9ihtVgjLOSWerWasxnuzDcorPf7KDo', api_version='v2').polygon.historic_trades("DOMO", "2020-03-11")
# 
# =============================================================================


#HISTORIC TRADES
vals = api.polygon.get(path ='/ticks/stocks/trades/AAPL/2018-02-02?limit=100',version = 'v2')




https://api.polygon.io/v2/ticks/stocks/trades/AAPL/2018-02-02?limit=100












