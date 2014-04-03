__author__ = 'Arseniy'

import cgi
import webapp2
from google.appengine.ext import ndb

MAIN_PAGE_FILE = open("DB_MAIN_PAGE.html", "r")
MAIN_PAGE = MAIN_PAGE_FILE.read()


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE)

        items = Item.all_query()
        for item in items:
            self.response.write(
                """<tr>
                    <td>%s</td>
                    <td align="right">%i</td>
                    <td align="right">%i</td>
                   </tr>"""
                % (item.name, item.minTemp, item.maxTemp))

        self.response.write("</tbody></table></body></html>")


class Item(ndb.Model):
    """Models new entry for clothes database"""
    name = ndb.StringProperty()
    minTemp = ndb.IntegerProperty()
    maxTemp = ndb.IntegerProperty()

    @classmethod
    def all_query(cls):
        return cls.query()


class AddingItem(webapp2.RequestHandler):

    def post(self):
        item_name = self.request.get('clothes_name')
        item_min_temp = int(self.request.get('min_temp'))
        item_max_temp = int(self.request.get('max_temp'))
        item = Item(parent=ndb.Key('Data Type', 'Clothes'),
                    name=item_name, minTemp=item_min_temp, maxTemp=item_max_temp)
        item.put()
        self.response.write("""<!doctype html>
                                <html>
                                    <body>
                                        You added %s
                                        for %i to %i %s degree
                                        <br>
                                        <a href='/'>back</a>
                                    </body>
                                </html>"""
                            % (item_name,
                            item_min_temp,
                            item_max_temp,
                            cgi.escape(self.request.get('units'))))



application = webapp2.WSGIApplication([
    ('/admin', MainPage),
    ('/add_item', AddingItem)
], debug=True)