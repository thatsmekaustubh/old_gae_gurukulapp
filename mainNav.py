import os
import re
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class validDomain(db.Model):
  validDomains = db.StringProperty()  
  
class mainPage(webapp.RequestHandler):
	def get(self):
		#self.response.out.write("Hello mainPage")
		domain = "www.srescoe.sresgurukul.appspot.com"#os.environ['HTTP_HOST']
		pat='([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)'
		match = re.search(pat, domain)
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
				self.response.out.write("Found in db")
			else:
				path = "%s/index.html" % os.environ['HTTP_HOST']
				self.redirect(path)
			
			
		else:
			path = "%s/index.html" % os.environ['HTTP_HOST']
			self.redirect(path)

class indexPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("Not a valid domain do u wanna register ?")
		

applications = webapp.WSGIApplication([	('/', mainPage),
										('/index.html', indexPage)
									  ],debug=True)

def main():
  run_wsgi_app(applications)

if __name__ == '__main__':
  main()