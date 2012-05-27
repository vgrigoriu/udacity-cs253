# coding: utf8

import webapp2
import jinja2
import os
import re

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape = True)

class SignupHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('signup.html')
        self.response.write(template.render())

    def post(self):
        username = self.request.get('username')

        username_error = ''
        if len(username) == 0:
            username_error = "You must enter a username"
        elif not re.match('^[a-zA-Z0-9_-]{3,20}$', username):
            username_error = "Username must be valid (3-20 digits, letters & _)"

        password = self.request.get('password')
        verify = self.request.get('verify')
        password_error = ''
        if password != verify:
            password_error = "Passwords do not match"
        elif len(password) == 0:
            password_error = "You must enter a password"
        elif not re.match('^.{3,20}$', password):
            password_error = "The password must have between 3 and 20 characters"

        email = self.request.get('email')
        email_error = ''
        if len(email) > 0 and not re.match('^[\S]+@[\S]+\.[\S]+$', email):
            email_error = "You must enter a valid email address"

        if username_error or password_error or email_error:
            template = jinja_environment.get_template('signup.html')
            template_values = {
                'username': username,
                'username_error': username_error,
                'password_error': password_error,
                'email': email,
                'email_error': email_error,
            }
            self.response.write(template.render(template_values))
        else:
            return self.redirect('http://cucu.ro/')


app = webapp2.WSGIApplication([('/unit2/signup', SignupHandler)],
                              debug=True)
