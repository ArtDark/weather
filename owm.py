import pyowm

city = input("Какой город вас интересует? ")

owm = pyowm.OWM('5b5fa98f39c880d8be0555412992f8ed')

observation = owm.weather_at_place(city)

w = observation.get_weather()

status = w.get_status()

temp = w.get_temperature('celsius')['temp']

print('Температура в городе ' + str(city) + ' сейчас составляет ' + str(temp) + ' градусов по Цельсию')
print('Небо ' + status)
