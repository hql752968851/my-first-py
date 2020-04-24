import  requests

class HeFeng():
    def __init__(self):
        self.url = "https://cdn.heweather.com/china-city-list.txt"

    def get_weather(self,city_code):
        url="https://free-api.heweather.com/s6/weather/now?location="+city_code+&key=7449d0b69a2347ce9feb00a53a61da77
        info=requests.get(url)
        info.encoding='utf8'
        print(info.text)

    def get_city_code(self):
        cities=self.get_citys()
        for each in cities:
            print(each[2:13])



    def get_citys(self):
        html = requests.get(self.url)
        html.encoding = 'utf8'
        cities=html.text.split('\n')
        yield cities[6:]



if __name__ == '__main__':
    hefeng = HeFeng()
    codes=hefeng.get_city_code()
    hefeng.