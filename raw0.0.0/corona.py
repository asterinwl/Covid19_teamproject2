import requests
import xmltodict
import time
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

url_decide_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
url_decide_serviceKey = "S8%2Ftx%2BhEP7bZDZI%2By0P1ZKvPuHpx%2BVUKpt6ay8faxnxR%2FTRO9M5UAy8%2BafhJBNVzQG%2Fgwoym2S4Xbe1dUXivUw%3D%3D"
url_pages = "1000" #페이지당열갯수
url_start_date = "20200303" #시작날짜
url_end_date = datetime.today().strftime("%Y%m%d%H%M%S")[:8] #끝날짜
url_decide = url_decide_base + "?serviceKey=" + url_decide_serviceKey + "&pageNo=1&numOfRows=" + url_pages + "&startCreateDt="+ url_start_date + "&endCreateDt=" + url_end_date

req = requests.get(url).content

xmlObject = xmltodict.parse(req)
dict_data = xmlObject['response']['body']['items']['item']

dfDecide = pd.DataFrame(dict_data)

dfDecide.drop(['createDt', 'seq', 'stateTime', 'updateDt'], axis=1, inplace=True)

dfDecide['newDecideCnt'] = 0

for i in range(len(dfDecide)-1):
    dfDecide['newDecideCnt'][i] = int(dfDecide.iloc[i]['decideCnt']) - int(dfDecide.iloc[i+1]['decideCnt'])
    


dfDecide.to_csv('dfDecide.csv', index=False)
    



