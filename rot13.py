import webapp2
import string
import cgi

form = """
<form method="post">
	<textarea name="text"></textarea>
	<input type="submit">
</form>
"""

def rot13_string(s):
	return s.encode("rot13")

class Rot13Handler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
    def post(self):
    	rot13d = rot13_string(self.request.get("text"))
    	encoded = cgi.escape(rot13d)
    	self.response.out.write(encoded)

app = webapp2.WSGIApplication([('/rot13', Rot13Handler)],
                              debug=True)
