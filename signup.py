import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	autoescape = True)

class SignupHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("cucu bau")

app = webapp2.WSGIApplication([('/unit2/signup', SignupHandler)],
                              debug=True)