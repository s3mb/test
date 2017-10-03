# -*- coding: utf-8 -*-
import krakenex
import re
import sys
import time
from datetime import datetime

#Extracting data from Kraken Exchange API
k = krakenex.API()

while True:
    while True:
        try:
            pBitcoin = k.query_public('Ticker',{'pair': 'XXBTZEUR',});
            break
        except ValueError:
            print("Error : ",pBitcoin['error'])
            #sys.exit("Can't continue with error")
            break

    #askBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['a'][0]),2)
    #bidBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['b'][0]),2)
    lastBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['c'][0]),2)
    #lowBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['l'][1]),2)
    #highBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['h'][1]),2)
    #openBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['o']),2)
    #volumeBitcoin=round(float(pBitcoin['result']['XXBTZEUR']['v'][1]),2)

    #print('Ask :', askBitcoin)
    #print('Bid :', bidBitcoin)
    #print('Last :', lastBitcoin)
    #print('Low :', lowBitcoin)
    #print('High :', highBitcoin)
    #print('Open :', openBitcoin)
    #print('Volume :', volumeBitcoin)

    file = open('out.csv', 'a')
    td = (datetime.now())
    try:
        file.write(str(td.day)+'-'+str(td.month)+'-'+str(td.year)+','+str(td.hour)+':'+str(td.minute)+','+str(lastBitcoin)+'\n')
    finally:
        file.close()
    print(str(td.day)+'-'+str(td.month)+'-'+str(td.year)+','+str(td.hour)+':'+str(td.minute)+','+str(lastBitcoin))
    time.sleep(300)
