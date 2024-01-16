import requests


def get_weather():
    api_key = "b28bac52f9bb9f3336e08e625447a4fb"
    lat = "-6.898161107508915"
    lon = "107.63491749929597"
    lang = "id"
    units = "metric"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&lang={lang}&units={units}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        name = data["name"]
        temperatureReal = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return (
            f"Cuaca saat ini di {name} adalah {weather_description} "
            f"Dengan suhu sekitar {temperatureReal:.0f} derajat celsius dan "
            f"Kelembapan {humidity}%"
        )
    else:
        return "Gagal mendapatkan data cuaca."
