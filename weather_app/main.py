import requests
api_key = '52798eb2079ffbc6fee6068aba6c60c5'
user_input = input("Enter City Name : ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?&q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404' :
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round((weather_data.json()['main']['temp'] - 32) * (5 / 9))
    print(f"The Weather in {user_input} is : {weather}")
    print(f"The Temperature in {user_input} is : {temp}°C")