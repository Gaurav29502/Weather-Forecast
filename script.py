#import the necessary package!
import requests

#input the city name
city = 'Thane'
print(city)


#Display the message!
print('Displaying Weater report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)
