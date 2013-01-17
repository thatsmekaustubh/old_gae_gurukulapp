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
		self.session = Session()
		#to check college from database first
		if 'college' in self.session:
			user = users.get_current_user()
			path = os.path.join(os.path.dirname(__file__), 'template/collegeHome.html')
			#to be fetched from database
			logoimg = "logo1.gif"
			if user:
				url = users.create_logout_url(self.request.uri)
				url_linktext = 'Logout'
				self.response.out.write(template.render(path,{'person':user.nickname(),'url':url,'url_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'nogurukul','collegeCode':self.session['college']}))
			else:
				url = users.create_login_url(self.request.uri)
				url_linktext = 'Login'
				self.response.out.write(template.render(path,{'lurl':url,'lurl_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'nogurukul','collegeCode':self.session['college']}))
		
		
applications = webapp.WSGIApplication([	('/collegeHome.html', mainPage)
									  ],debug=True)

def main():
  run_wsgi_app(applications)

if __name__ == '__main__':
  main()