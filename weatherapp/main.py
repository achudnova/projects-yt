import rumps
import requests
import tempfile

API_KEY = 'YOURAPIKEYHERE'
UNITS = 'metric'

""" Function to fetch weather information for a given city
1. Construct the URL for the API request
2. Send a GET request to the API
3. Parse the response as JSON
"""
def get_weather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units={UNITS}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract weather data from the JSON response
        weather = data['weather'][0]
        temperature = round(data['main']['temp'])
        description = weather['description'].capitalize()

        icon_url = f'https://openweathermap.org/img/wn/{weather["icon"]}.png'
        return f'{city_name}: {temperature}°C, {description}', icon_url
    return f'Error fetching weather data for {city_name}: {data["message"]}', None

class WeatherApp(rumps.App):
    def __init__(self):
        super(WeatherApp, self).__init__(' ')
        self.icon = 'icon.png'

    # Method called when the "Search" option is clicked
    @rumps.clicked('Search')
    def search_weather(self, _):
        city_name = rumps.Window("Enter city name:").run().text
        if city_name:
            weather_info, icon_url = get_weather(city_name)
            if icon_url:
                # Create a temporary file and write the icon data to it
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                    tmp_file.write(requests.get(icon_url).content)
                    self.icon = tmp_file.name
            self.title = weather_info
        else:
            self.title = 'Invalid city name'
    
    # Method to automatically refresh weather information every 30 min
    @rumps.timer(1800)
    def auto_refresh(self, _):
        if self.title and ':' in self.title:
            city_name = self.title.split(':')[0].strip()
            weather_info, icon_url = get_weather(city_name)
            if icon_url:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                    tmp_file.write(requests.get(icon_url).content)
                    self.icon = tmp_file.name
            self.title = weather_info

if __name__ == '__main__':
    app = WeatherApp()
    app.run()
