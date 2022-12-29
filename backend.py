import requests
import api


def get_data(place, forecast_days=3, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api.key}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    num_values = forecast_days * 8
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data('ahmedabad'))
