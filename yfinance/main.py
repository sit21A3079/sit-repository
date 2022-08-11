import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

days = 20

tickers = {
    'apple' : 'AAPL',
    'facebook' : 'FB',
    'google' : 'GOOGL',
    'microsoft' : 'MSFT',
    'netflix' : 'NFLX',
    'amazon' : 'AMZN'
}

def get_data(days, tickers) :
    df = pd.DataFrame()
    for company in tickers.keys():
    #company = 'facebook'
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period = f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.head()
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    
    return df

apple = yf.Ticker('AAPL')  
apple_info = apple.info                 #会社情報
apple_actions = apple.actions.head()    #配当金

df = get_data(days, tickers)

companies = ['apple', 'facebook']
data = df.loc[companies]
data = data.T.reset_index()
# print(data.head())

data = pd.melt(data, id_vars=['Date']).rename(
    columns = {'value' : 'Stock Prices(USD)'}
)

ymin, ymax = 250, 300
chart = (
    alt.Chart(data)
    .mark_line(opacity = 0.8, clip = True)      #引数clipは範囲外にグラフが表示されるのを防ぐ
    .encode(    #軸の設定
        x = "Date:T",
        y = alt.Y("Stock prices(USD):Q", stack = None, scale = alt.Scale(domain = [ymin, ymax])),
        color = 'Name:N'
    )
)

print(chart)