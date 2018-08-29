import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.redirect('/ja/')


app = webapp2.WSGIApplication([
    ('/ja', MainPage),
])
