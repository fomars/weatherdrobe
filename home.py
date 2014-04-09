__author__ = 'Arseniy'

import webapp2
import weather


MAIN_PAGE_FILE = open("MAIN_PAGE.html", "r")
MAIN_PAGE = MAIN_PAGE_FILE.read()


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE)


class GetWeather(webapp2.RequestHandler):

    def post(self):
        location = {}
        location['lat'] = float(self.request.get('lat'))
        location['lng'] = float(self.request.get('lng'))
        weather_data = weather.get_today_forecast(location['lat'], location['lng'])
        self.response.write("""<!doctype html>
                                <html>
                                    <body>
                                         %s
                                        <br>
                                        <a href='/'>back</a>
                                    </body>
                                </html>"""
                            % (weather_data)
                            )


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/request_weather', GetWeather)
], debug=True)