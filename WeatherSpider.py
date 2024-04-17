import bs4
import matplotlib
import matplotlib.pyplot as plt
import requests as req
import re
import pandas as pd
import time

ls = ['101240101', '101210101', '101020100']
City = ['BEIJING', 'SHANGHAI', 'HANGZHOU']
WEATHER = ['BeijingWeather.csv', 'ShanghaiWeather.csv', 'HangzhouWeather.csv']
condition = ['北京近6天天气情况', '上海近6天天气情况', '杭州近6天天气情况']
url1 = 'http://www.weather.com.cn/weather/'
url2 = '.shtml'
header = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)'
                        'AppleWebKit/537.36(KHTML,like Gecko)'
                        'Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115'}
matplotlib.rcParams['font.family'] = 'SimHei'
for z in range(3):
    url = url1 + ls[z] + url2
    r = req.get(url, headers=header)
    print(r.status_code)
    r.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    Date = soup.find_all('li')  # date
    date = []
    for Date1 in Date:
        date1 = Date1.find_all('h1')
        for a in date1:
            date.append(a.text)
    del (date[0])
    Max = soup.find_all('p', 'tem')  # max
    max = []
    min = []
    for Max1 in Max:
        max1 = Max1.find_all('span')
        for b in max1:
            max.append(b.text)
    for Min1 in Max:  # min
        min1 = Min1.find_all('i')
        for c in min1:
            min.append(c.text)
    del (min[0])
    Weather = re.compile('<p title="(.*?)" class="wea"')  # weather
    pt = re.findall(Weather, r.text)
    weather = []
    for e in pt:
        weather.append(e)
    del (weather[0])
    Wind = soup.find_all('p', 'win')
    wind = []
    for Wind1 in Wind:
        wind1 = Wind1.find_all('i')
        for i in wind1:
            wind.append(i.text)
    del (wind[0])
    print(City[z])
    print(weather)
    print(date)
    print(max)
    print(min)
    print(wind)
    time.sleep(5)

    fr1 = {'日期': date, '天气': weather, '风力': wind, '最高温': max, "最低温": min}
    print(fr1)
    Forecastweather = pd.DataFrame(fr1)
    print(Forecastweather)
    Forecastweather.to_csv(WEATHER[z], index=False, encoding='utf_8_sig')

    temperature = ['Highest temperature', 'Lowest temperature']
    MAX = []
    MIN = []
    x = date
    for g in max:
        MAX.append(eval(g.replace('℃', ' ')))
    for h in min:
        MIN.append(eval(h.replace('℃', ' ')))
    y1 = MAX
    y2 = MIN
    plt.figure(z + 1, figsize=(6, 4))
    plt.plot(x, y1, x, y2)
    plt.figtext(0.52, 0.9, condition[z], ha='center', size=20)
    legend = plt.legend(temperature, loc=(0.78, 0.80), labelspacing=0.1)
plt.show()