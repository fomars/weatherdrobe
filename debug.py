__author__ = 'Arseniy'


import webapp2
import pywapi

MAIN_PAGE_FILE = open("MAIN_PAGE.html", "r")
MAIN_PAGE = MAIN_PAGE_FILE.read()


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE)


class GetWeather(webapp2.RequestHandler):

    def post(self):
        location = self.request.get('location')
        location_id = pywapi.get_location_ids(location)
        weather_data = pywapi.get_weather_from_weather_com(location_id)
        self.response.write("""<!doctype html>
                                <html>
                                    <body>
                                        Location: %s
                                        <br>
                                        Current conditions: %s
                                        <br>
                                        <a href='/'>back</a>
                                    </body>
                                </html>"""
                            % (weather_data["loc"]["name"], weather_data["current_conditions"]["text"])
                            )



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/request_weather', GetWeather)
], debug=True)
