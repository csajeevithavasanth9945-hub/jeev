stock_prices=[9,6,1,2,5,4]
min_price=stock_prices[0]
max_prices=0
for prices in stock_prices:
    if prices<min_prices:
        min_prices=prices
    elif prices-min_prices>max_prices:       
        max_profit=prices-min_prices