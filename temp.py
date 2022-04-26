# link: https://medium.com/financial-data-analysis/web-scraping-cryptocurrency-1-minute-price-data-python-471dd165d934

# Import Libraries

import requests
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta# The CoinDesk 20
import time
from datetime import datetime, timedelta
import win32api



def trend_finder():
    
    win32api.Beep(500,100)
    print("Initiating")
    coindesk_list = ['BTC', 'ETH', 'XRP', 'ADA', 'USDT', 'DOGE', 'XLM', 'DOT', 'UNI', 'LINK', 'USDC', 'BCH', 'LTC', 
                     'GRT', 'ETC', 'FIL', 'AAVE', 'ALGO', 'EOS', 'AVAX', 'SHIB','MATIC','WBTC','UNI','TRX','ALGO',
                     'AAVE','CELO','XTZ','BTT','KSM','DASH','YFI','REN','ANT']

    
    while True:
        print(datetime.now().replace(second=0, microsecond=0))
        
        end_datetime = datetime.now().replace(second=0, microsecond=0) - timedelta(hours=2)
        start_datetime = end_datetime - relativedelta(minutes = 30)
        
        for coin in coindesk_list:
            df = pd.DataFrame(index=[0])
            
            # Define the Start Date and End Date

            url = 'https://production.api.coindesk.com/v2/price/values/' + coin + '?start_date=' + start_datetime.strftime("%Y-%m-%dT%H:%M") + '&end_date=' + end_datetime.strftime("%Y-%m-%dT%H:%M") + '&ohlc=true'
            temp_data_json = requests.get(url)
            temp_data = temp_data_json.json()
            df = pd.DataFrame(temp_data['data']['entries'])
            df.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
            
            jump = (df.Close.iat[-1] - df.Close.iat[0])/df.Close.iat[0]
            if jump > 0.025:
                win32api.Beep(1000,100)
                print(coin,":",round(jump,3),"Time: ",datetime.now().replace(second=0, microsecond=0))
            #else: print("No jump for: ",coin)
            

            
        time.sleep(180)
#end of function
        
# RUN

trend_finder()
