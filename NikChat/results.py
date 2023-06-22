import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import geocoder
#import openai



def ctime():
    if 1 == 1: #time
        from datetime import datetime
        now = datetime.now()
        timePre = str(now.time()).split(":")
        datePre = str(now.date()).split("-")
        #timePre = timePre1.split(":")
        #datePre = datePre1.split("-")
        suffix = "AM"
        if int(timePre[0]) > 12:
            suffix = "PM"
            timePre[0] = int(timePre[0]) - 12
        elif int(timePre[0]) == 12:
            suffix = "PM"
        monthdict = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }
        

        # enter city name
        city = "union city".replace(" ", "+")

        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str1 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str1.split('\n')
        time1111 = data[0]
        sky = data[1]

        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        # printing all data
        day = time1111.split(" ")[0]
        ending = ''
        if str(datePre[2])[-1] == "1":
            ending = 'st'
        elif str(datePre[2])[-1] == "2":
            ending = 'nd'
        elif str(datePre[2])[-1] == "3":
            ending = 'rd'
        else:
            ending = 'th'

        timestr = "The time is " + str(timePre[0]) + ":" + timePre[1] + suffix + ". The date is " + day + ", " + monthdict[datePre[1]] + " " + datePre[2] + ending + " " + datePre[0]
        return timestr
    
def weather():
    if 1 == 1: #weather and stuff
        from datetime import datetime
        g = geocoder.ip('me')
        geoLoc = Nominatim(user_agent="GetLoc")
        locname = geoLoc.reverse("{}, {}".format(g.latlng[0], g.latlng[1]))
        city = locname.address.split(", ")[3].replace(" ", "+")
        city1 = locname.address.split(", ")[3]

        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str1231231 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # formatting data
        data = str1231231.split('\n')
        sky = data[1]

        # getting all div tag

        str1 = "The temperature in {} is currently {}. The sky is {}. ".format(city1, temp.replace("°F"," degrees fahrenheit"), sky)
        return str1
def internet(term):
    if 1 == 1:
        try:
            query = term.split(' is ')[1].replace(' ', "")
            # importing the module
            import wikipedia
            search = ""
            if str(term.split(' is ')[0]) == "where":
                a = query.capitalize()
                search = "where" + a
            elif str(term.split(' is ')[0]) == "what":
                search = "what" + query
            elif str(term.split(' is ')[0]) == "when":
                search = "when" + query
            else:
                search = query
            result = wikipedia.summary(search, sentences = 1)
            return result
        except:
            query = term.split(' is ')[1].replace(' ', "")
            # importing the module
            import wikipedia
            search = ""
            if str(term.split(' is ')[0]) == "where":
                a = query.capitalize()
                search = "where" + a
            elif str(term.split(' is ')[0]) == "what":
                search = "what" + query
            elif str(term.split(' is ')[0]) == "when":
                search = "when" + query
            else:
                search = query
            result = wikipedia.summary(search, sentences = 1)
            return result
