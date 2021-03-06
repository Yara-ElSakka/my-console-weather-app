# console app to get temperature of a city.
# By Yara ElSakka.
# 20.12.21
# https://planningclasses.notion.site/Class-20-12-2021-b520ff3d833d4db383bd9b311d35be90
# https://codefile.io/f/4BfjySsT3Ai05dygyUyh
# added other information API on 27.12.21
#


from requests import *
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def getWeatherMethod(cityTemp):
    tempDB = get(f'https://www.google.com/search?q={cityTemp}&oq={cityTemp}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(tempDB.text, 'html.parser')

    # API to get the weather temparature:
    weatherID = soup.select('#wob_tm')[0].get_text().strip()
    print(weatherID+" C")

    print("\n..working out other information..\n")
    # additional information as per 27.12.21 updates:

    # API to get the location information:
    location = soup.select('#wob_loc')[0].getText().strip()
    print(f"Location information: {location}\n")

    # API to get the time information:
    time = soup.select('#wob_dts')[0].getText().strip()
    print(f"Time information: {time}\n")

    # API to get other info:
    info = soup.select('#wob_dc')[0].getText().strip()
    print(f"Other information: {info}\n")

    precipitation = soup.select_one('#wob_pp').text
    print(f"precipitation: {precipitation}\n")

    humidity = soup.select_one('#wob_hm').text
    print(f"humidity: {humidity}\n")

    wind = soup.select_one('#wob_ws').text
    print(f"wind: {wind}\n")

    #return weatherID // "no need for return command as per the teacher"

cityName = input("The city temperature: ")
cityName = cityName + " weather now is" # weather will be replaced with the actual weather in Celsius
print(cityName)
getWeatherMethod(cityName)
# end of code
# yara elsakka