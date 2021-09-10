import sql_data as sq
import random
import psutil
from datetime import datetime
import geocoder

#Imported Variable
now = datetime.now()
current_time = now.strftime("%I:%M %p")
geocode = geocoder.ip('me')
str_g = str(geocode[0])
end = str_g.find(',')
c_location = str_g[1:end]
c_location = c_location.replace(' ','')



#Unknown
def unknown():
        response = ['Could you please re-phrase that?', 
        'I do not understand...',
        'Elaborate',
        'What does that mean?', '???'
        'Eh? I don’t get it', 'I\'m still learning, don\'t understand','I haven’t a clue',
        'I don’t have the foggiest idea.','Your guess is as good as mine.']
        return response[random.randrange(len(response))]


#Questions 
hru = ['how','are','you','doing']
hig = ['hows', 'it', 'going']
wrud = ['what', 'are', 'you', 'doing']
ilib = ['i','love', 'info','bot']
poss_hi = ['hello','sup','heyo','hi','bonjour']
bat_health = ['what', 'is', 'the', 'battery', 'health']
wulte = ['would', 'you', 'like', 'to', 'eat']
w_time = ['what', 'time', 'is', 'it']
h_old = ['how', 'old', 'are', 'you']
w_name = ['what', 'is', 'your', 'name']
c_advice = ['can', 'i', 'have', 'some', 'advice']
w_weather = ['what', 'is', 'the', 'weather', 'today ']
w_temp = ['what', 'is', 'the', 'temperature', 'today']
poss_thats_good = ['fine','good,','well', 'okay','great','fantastic', 'amazing','lovely','alright','wonderful']
poss_bad = ['bad','horriable', 'unwell','sad','depressed']
#Answers
battery = ('Your battery health is '+str(psutil.sensors_battery().percent) + '%')
time = ('The time is currently '+ str(current_time))
birth = ("I do not have an age like humans but my programm was created on August 31, 2020 at 1:00.")
name = ('My name is Info bot :) Thanks for asking.')

#Imported Questions
a1 =['whats', 'up', 'dude']
a2 =['how', 'is', 'the', 'weather', 'outside']
a3 =['what', 'is', 'ur', 'name']
a4 =['do', 'you', 'know', 'how', 'to', 'play', 'baseball']
a5 =['what', 'is', 'your', 'favorite', 'colour']
a6 =['how', 'do', 'you', 'spell']
a7 =['do', 'you', 'like', 'cats']
a8 =['where', 'are', 'you', 'from']
a9 =['what', 'is', 'the', 'weather']

