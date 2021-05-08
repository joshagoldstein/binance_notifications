from binance.client import Client
import time 
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


client = Client('3wfiKJWWSW42XSsSw0Y4fxm9iVHMaZeQFSyIMqn6RzAG8s33CpXW8rrr1J4TzC5m', 'o8BfTLXoa1evd5FpLn1TD1WqpRg3bGfvKSzwmta7a9T0afHe1SrEYJyb8qqSLw9w')

#Get current price of each coin


# info = client.get_all_tickers()
# symbol=[]
# for dictionaries in info:
#     ticker_price= list(dictionaries.values())
#     if ticker_price[0][-4:]=='USDT':
#         new_val=ticker_price[0][0:-4]+'/'+'USDT'
#         ticker_price[0]=new_val
#         symbol.append(ticker_price)
# symbol_sort=sorted(symbol, key=lambda x: float(x[1]), reverse=True)
#for pair in symbol_sort:
    #print('The coin {} is currently valued at ${}'.format(pair[0],pair[1]))
# print(symbol[0][0][:3])

info = client.get_ticker()
tick_change={}
for ind in info:
    if ind['symbol'][-4:]=='USDT':
        sym=ind['symbol'][0:-4]+'/'+'USDT'
        percent_change=float(ind['priceChangePercent'])
        tick_change[sym]=percent_change
        price=ind['lastPrice']
        if percent_change < -5.0 or percent_change > 5.0:
            print("The coin {} has changed {}% over the past 24 hours and is currently ${} as of {}".format(sym,percent_change,price,current_time))
sorted_tick_change=sorted(tick_change.items(), key=lambda x: x[1], reverse=True) 
biggest_win=sorted_tick_change[0]
biggest_loser=sorted_tick_change[-1]
print('-'*100)
print('The winner of the day is {} with a massive growth of {}%!'.format(biggest_win[0],biggest_win[1]))
print('The WOAT of the day is {} with a piss poor performance of {}%!'.format(biggest_loser[0],biggest_loser[1]))

    #print(ind.keys())
    #val=list(ind.values())
    #print(val)

    #symbol, priceChange, priceChangePercent, lastPrice, 
