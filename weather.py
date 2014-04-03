__author__ = 'Arseniy'

from pprint import pprint
import forecastio
from datetime import datetime

API_KEY = '0516b41d47c715f30d1318bbfffd3ab5'


def get_today_forecast(lat=55.75, lng=37.617):
    forecast = forecastio.load_forecast(API_KEY, lat, lng, units='si', time=datetime.now())
    return forecast.daily().data[0]


if __name__ == "__main__":
    print "Enter latitude: "
    latitude = float(raw_input())

    print "Enter longitude: "
    longitude = float(raw_input())

    conditions = get_today_forecast(latitude, longitude)

    pprint (vars(conditions))