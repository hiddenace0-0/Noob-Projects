from re import I
import requests

#API

#Advice
slip = requests.get('https://api.adviceslip.com/advice')
adv = slip.json() 
advice = adv['slip']['advice']


#Weather
def weather(city):
    w = 'https://goweather.herokuapp.com/weather/%7B'+city+'%7D'
    w_slip = requests.get(w)
    w_wea = w_slip.json()
    if len(w_wea)>1:
        weather_temp = w_wea['temperature']
        weather_desc = w_wea['description']
        return weather_desc, weather_temp
    elif len(w_wea) == 1:
        return w_wea['message']


