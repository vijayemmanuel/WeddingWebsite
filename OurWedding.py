import cgi
import os
import datetime

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'mainpage.html')
    self.response.out.write(template.render(path, {}))

class AboutUs(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'aboutus.html')
    self.response.out.write(template.render(path, {}))

class TimeTogether(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'timetogether.html')
    self.response.out.write(template.render(path, {}))

class Family(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'family.html')
    self.response.out.write(template.render(path, {}))

class WeddingDetails(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'weddingdetails.html')
    self.response.out.write(template.render(path, {}))

class Service(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'service.html')
    self.response.out.write(template.render(path, {}))

class ReceptionDetails(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'receptiondetails.html')
    self.response.out.write(template.render(path, {}))

class WeddingAlbum(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'weddingalbum.html')
    self.response.out.write(template.render(path, {}))

class HoneyMoonAlbum(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'honeymoonalbum.html')
    self.response.out.write(template.render(path, {}))
##    greetings = db.GqlQuery("SELECT * FROM Greeting ORDER BY date DESC LIMIT 10")
##
##    for greeting in greetings:
##      if greeting.author:
##        self.response.out.write('<b>%s</b> wrote:' % greeting.author.nickname())
##      else:
##        self.response.out.write('An anonymous person wrote:')
##      self.response.out.write('<blockquote>%s</blockquote>' %
##                              cgi.escape(greeting.content))
##
##    # Write the submission form and the footer of the page
##    self.response.out.write(""" </body> </html>""")

class Greeting(db.Model):
  author = db.StringProperty()
  email = db.StringProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class MessageBoard(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(100)

        template_values = {
          'greetings': greetings,
          }

        path = os.path.join(os.path.dirname(__file__), 'guestbook.html')
        self.response.out.write(template.render(path, template_values))


##    def post(self):
##        greeting = Greeting()
##
##        greeting.content = self.request.get('content')
##        greeting.author = self.request.get('author')
##        greeting.email = self.request.get('email')
##        greeting.date = datetime.datetime.now()
##
##        greeting.put()
##        self.get()
##        greeting = Greeting()
##
##        if users.get_current_user():
##          greeting.author = users.get_current_user()
##
##        greeting.content = self.request.get('content')
##        greeting.put()
##        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/aboutus', AboutUs),
                                      ('/timetogether', TimeTogether),
                                      ('/family', Family),
                                      ('/weddingdetails', WeddingDetails),
                                      ('/service', Service),
                                      ('/receptiondetails', ReceptionDetails),
                                      ('/weddingalbum', WeddingAlbum),
                                      ('/honeymoonalbum', HoneyMoonAlbum),
                                      ('/guestbook', MessageBoard)],
                                     debug=False)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()