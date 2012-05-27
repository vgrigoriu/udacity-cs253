import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	autoescape = True)

class SignupHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('signup.html')
		self.response.write(template.render())

app = webapp2.WSGIApplication([('/unit2/signup', SignupHandler)],
                              debug=True)