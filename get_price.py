#code to get a certain stock price
#using Yahoo Finance as the basis for price information

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

get_price=web.DataReader('KO', data_source='yahoo', start="01-01-2021",end="06-21-2021")
display(get_price)
get_price["Adj Close"].plot(figsize=(15,10))
plt.show()
