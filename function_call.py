import os
import requests
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=252e1b4a4f271712eb978861a56dca5b"
    response = requests.get(url)
    lat = response.json()['coord']['lat']
    lon = response.json()['coord']['lon']
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")

    url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=252e1b4a4f271712eb978861a56dca5b"
    final_response = requests.get(url2)
    weather = final_response.json()['weather'][0]['description']
    print(f"Weather in {city_name}: {weather}")
    return weather

def main():
    client = AzureOpenAI(
        api_version="2024-02-01",
        azure_endpoint="https://debdu-m9cerqxd-swedencentral.cognitiveservices.azure.com/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"]
    )

    function = [
        {
            "name": "get_weather",
            "description": "Get the weather information of a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {
                        "type": "string",
                        "description": "The name of the city to get the weather for"
                    }
                },
                "required": ["city_name"]
            }
        }
    ]

    initial_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant helping people retrieve real-time information."},
            {"role": "user", "content": "How is the weather in Delhi?"}
        ],
        functions=function
    )

    arguments = json.loads(initial_response.choices[0].message.function_call.arguments)
    city_name = arguments['city_name']

    if city_name:
        print(f"City name: {city_name}")
        get_weather(city_name)

if __name__ == "__main__":
    main()
