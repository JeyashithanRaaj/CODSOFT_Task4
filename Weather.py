import tkinter as tk
import requests

def get_weather_data(city):
    api_key = "caab1380d6e6c5d0e6c1e76dfe098452"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return None

def display_weather():
    city = city_entry.get()
    weather_data = get_weather_data(city)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        result_label.config(
            text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description.capitalize()}"
        )
    else:
        result_label.config(text="City not found or an error occurred.")

root = tk.Tk()
root.title("Weather Forecast")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

city_label = tk.Label(frame, text="Enter City or ZIP Code:")
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(frame, text="Get Weather", command=display_weather)
get_weather_button.grid(row=1, columnspan=2, padx=10, pady=20)

result_label = tk.Label(frame, text="Weather information will appear here.")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()

