from ast import keyword
from tabnanny import check
import pandas as pd   
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US')

all_keywords = ['Pedros','Food','Cycling','Home alone','Crime']

keywords =[]
cat = '0'

timeframes = ['today 5-y', 'today 3-m', 'today 12-m']

geo = ''

# grop is for certain tags like images what google property to filter through
gprop = ''  


def check_trends(keyword):
    pytrends.build_payload(keyword,cat,timeframes[0],geo,gprop)
    data = pytrends.interest_over_time()
    mean = round(data.mean(),2)
    print(keyword[0] + ' : ' + str(mean[keyword[0]]))
    avg = round(data[keyword[0]][-52:].mean(),2)
    avg2 = round(data[keyword[0]][52:].mean(),2)
    trend = round((avg/mean[keyword[0]]-1)*100,2)
    trend = round((avg/avg2-1)*100,2)
    print('The average interest of ' + keyword[0] + ' is ' + str(avg))
    print('The change of interest in ' + keyword[0] + ' is ' + str(trend)+'%')
    #Most Stable
    if mean[keyword[0]] > 75 and abs(trend) <= 5:
        print('The interest for ' + keyword[0] + ' is stable for the last 5 years.')
    elif mean[keyword[0]] > 75 and trend > 5:   
        print('The interest for ' + keyword[0] + ' is stable and increasing the last 5 years.')
    elif mean[keyword[0]] > 75 and trend < -5:   
        print('The interest for ' + keyword[0] + ' is stable and decreasing the last 5 years.')
    #Somewhat Stable
    elif mean[keyword[0]] > 75 and abs(trend) <= 15:   
        print('The interest for ' + keyword[0] + ' is relatively stable for the last 5 years.') 
    elif mean[keyword[0]] > 75 and trend > 15:   
        print('The interest for ' + keyword[0] + ' is relatively stable and increasing the last 5 years.') 
    elif mean[keyword[0]] > 75 and trend < -15:   
        print('The interest for ' + keyword[0] + ' is relatively stable and increasing the last 5 years.')
    #Seasonal
    elif mean[keyword[0]] > 20 and abs(trend) <= 15:   
        print('The interest for ' + keyword[0] + ' is seasonal') 
    elif mean[keyword[0]] > 20 and trend > 30:   
        print('The interest for ' + keyword[0] + ' is trending')
    elif mean[keyword[0]] > 20 and trend < -15:   
        print('The interest for ' + keyword[0] + ' is significantly decreasing')
    #Cyclical
    elif mean[keyword[0]] > 10 and abs(trend) <= 15:   
        print('The interest for ' + keyword[0] + ' is significantly decreasing')  
    else:
        print('Does not fit into a model so far')    



for kw in all_keywords:
    keywords.append(kw)
    check_trends(keywords)
    keywords.pop()