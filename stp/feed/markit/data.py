import time
import requests
import xmltodict
from stp import config
from stp.db.connection import get_cursor
from datetime import datetime
URL = "http://dev.markitondemand.com/MODApis/Api/v2/Quote?symbol={}"

def insert_stock(cursor, record):
    id = "{}-{}".format(record["Timestamp"], record["Symbol"])
    cmd = "INSERT INTO stocks "
    cmd += "(quote_id, symbol, last_price, low_price, high_price, changeytd, msdate, "
    cmd += "market_cap, price_open, stock_date, volume, change_percent) "
    cmd += "VALUES "
    cmd += "('{quote_id}', '{symbol}', '{last_price}', '{low_price}', '{high_price}', '{changeytd}', '{msdate}', "
    cmd += "'{market_cap}', '{price_open}', '{stock_date}', '{volume}', '{change_percent}') "
    cmd = cmd.format(quote_id=id,
                     symbol=record["Symbol"],
                     last_price=record["LastPrice"],
                     low_price=record["Low"],
                     high_price=record["High"],
                     changeytd=record["ChangeYTD"],
                     msdate=record["MSDate"],
                     market_cap=record["MarketCap"],
                     price_open=record["Open"],
                     stock_date=record["Timestamp"],
                     volume=record["Volume"],
                     change_percent=record["ChangePercentYTD"])
    try:
        cursor.execute(cmd)
        cursor.connection.commit()
    except Exception as e:
        if not "duplicate" in str(e).lower():
            raise e
    
def get_stocks_to_watch():
    stocks = {}
    for stock in config.stocks_to_watch:
        stocks[stock] = get_stock(stock)
    return stocks

def get_stock(stock, time_sleep=1):
    result = requests.get(URL.format(stock)).text
    try:
        result = xmltodict.parse(result)["StockQuote"]
        return dict(result)
    except Exception as e:
        if "requests/sec limit" in str(result).lower():
            time.sleep(time_sleep)
            time_sleep = time_sleep * 2
            return get_stock(stock, time_sleep=time_sleep)
        else:
            print "ERROR unexpected", result
            
    
if __name__ == "__main__":
    cursor = get_cursor()
    stocks = get_stocks_to_watch()
    for key, value in stocks.iteritems():
        insert_stock(cursor, value)
