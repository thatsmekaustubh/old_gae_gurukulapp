import os
import re
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from util.sessions import Session

class validDomain(db.Model):
  validDomains = db.StringProperty()  
  
class mainPage(webapp.RequestHandler):
	def get(self):
		#self.response.out.write("Hello mainPage")
		domain = "www.srescoe.sresgurukul.appspot.com"#os.environ['HTTP_HOST']
		pat='([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)'
		match = re.search(pat, domain)
		self.session = Session()
		if match:
			#self.response.out.write(match.group(2))
			query_result = db.GqlQuery("SELECT * "
                           "FROM validDomain")
			flag = 0
			for query_result_loop in query_result:
				if query_result_loop.validDomains == match.group(2):
					flag = 1
					break
			if flag	== 1:
				self.session['portal']==match.group(2)
				path = "%s/index.html" % os.environ['HTTP_HOST']
				self.redirect(path)
			else:
				self.session['portal']=="newcollege"
				path = "%s/index.html" % os.environ['HTTP_HOST']
				self.redirect(path)
		else:
			self.session['portal']=="gurukul"
			path = "%s/index.html" % os.environ['HTTP_HOST']
			self.redirect(path)
		
applications = webapp.WSGIApplication([	('/', mainPage)],debug=True)

def main():
  run_wsgi_app(applications)

if __name__ == '__main__':
  main()