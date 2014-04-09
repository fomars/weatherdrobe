__author__ = 'Arseniy'

from pprint import pprint
from datetime import datetime
import urllib2

API_KEY = '0516b41d47c715f30d1318bbfffd3ab5'


def get_today_forecast(lat=55.75, lng=37.617):
    localtime = datetime.today()
    time_str = '{:%Y-%m-%dT12:00:00}'.format(localtime)
    #time_str = "{0[0]}-{0[1]}-{0[2]}T12:00:00".format(localtime)
    url = "https://api.forecast.io/forecast/%s/%.3f,%.3f,%s?units=si" %(API_KEY, lat, lng, time_str)
    try:
        result = urllib2.urlopen(url)
        return (result.read())
    except urllib2.URLError, e:
        pass

    return


if __name__ == "__main__":
    print "Enter latitude: "
    latitude = float(raw_input())

    print "Enter longitude: "
    longitude = float(raw_input())

    conditions = get_today_forecast(latitude, longitude)

    print conditions
