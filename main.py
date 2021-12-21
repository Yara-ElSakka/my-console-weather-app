# console app to get temperature of a city.
# By Yara ElSakka.
# 20.12.21
# https://planningclasses.notion.site/Class-20-12-2021-b520ff3d833d4db383bd9b311d35be90
# https://codefile.io/f/4BfjySsT3Ai05dygyUyh


from requests import *
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def getWeatherMethod(cityTemp):
    tempDB = get(f'https://www.google.com/search?q={cityTemp}&oq={cityTemp}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(tempDB.text, 'html.parser')
    weatherID = soup.select('#wob_tm')[0].get_text()
    print(weatherID+" C")
    #return weatherID

cityName = input("City Temperature: ")
cityName = cityName + " weather now is" # weather will be replaced with the actual weather in Celsius
print(cityName)
getWeatherMethod(cityName)
# end of code 
