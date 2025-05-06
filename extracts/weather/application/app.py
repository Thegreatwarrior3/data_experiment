from extracts.weatherstack import WEATHERSTACK


def extract(city):

    weather_stack = WEATHERSTACK()

    current_weather = weather_stack.current_weather(city)

    location = current_weather.get('location', {})
    location_name = location.get('name', {})
    location_country = location.get('country', {})
    location_latitude = location.get('lat', {})
    location_longitude = location.get('lon', {})

    current = current_weather.get('current', {})
    observation_time = current.get('observation_time', {})
    temperature = current.get('temperature', {})
    weather_description = current.get('weather_descriptions', {})
    wind_speed = current.get('wind_speed', {})
    wind_direction = current.get('wind_dir', {})
    precipitation = current.get('precip', {})
    humidity = current.get('humidity', {})
    feels_like = current.get('feelslike', {})

    print(f'location name: {location_name}')
    print(f'location country: {location_country}')
    print(f'latitude: {location_latitude}')
    print(f'longitude: {location_longitude}')
    print(f'observation time: {observation_time}')
    print(f'temperature: {temperature}')
    print(f'weather_description: {weather_description}')
    print(f'wind speed: {wind_speed}')
    print(f'wind direction: {wind_direction}')
    print(f'precipitation: {precipitation}')
    print(f'humidity: {humidity}')
    print(f'feels like: {feels_like}')

