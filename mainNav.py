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
		domain = "abc"#"www.srescoe.sresgurukul.appspot.com"#os.environ['HTTP_HOST']
		pat='([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)\.([\w.-]+)'
		match = re.search(pat, domain)
		if match:
			#query_result = db.GqlQuery("SELECT * "
            #               "FROM validDomain")
			flag = 0 # 1
			#if query_result:
			#	for query_result_loop in query_result:
			#		if query_result_loop.validDomains == match.group(2):
			#			flag = 1
			#			break
			if flag	== 1:
				self.session = Session()
				self.session['college']=match.group(2)
				user = users.get_current_user()
				path = os.path.join(os.path.dirname(__file__), 'template/collegeHome.html')
				logoimg = "logo1.gif"
				if user:
					url = users.create_logout_url(self.request.uri)
					url_linktext = 'Logout'
					self.response.out.write(template.render(path,{'person':user.nickname(),'url':url,'url_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'nogurukul','collegeCode':self.session['college']}))
				else:
					url = users.create_login_url(self.request.uri)
					url_linktext = 'Login'
					self.response.out.write(template.render(path,{'lurl':url,'lurl_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'nogurukul','collegeCode':self.session['college']}))
			else:
				user = users.get_current_user()
				path = os.path.join(os.path.dirname(__file__), 'template/newSubdomain.html')
				logoimg = "gurukullogo.gif"
				if user:
					url = users.create_logout_url(self.request.uri)
					url_linktext = 'Logout'
					self.response.out.write(template.render(path,{'person':user.nickname(),'url':url,'url_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))
				else:
					url = users.create_login_url(self.request.uri)
					url_linktext = 'Login'
					self.response.out.write(template.render(path,{'lurl':url,'lurl_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))
		else:
			user = users.get_current_user()
			path = os.path.join(os.path.dirname(__file__), 'template/gurukulHome.html')
			logoimg = "gurukullogo.gif"
			if user:
				url = users.create_logout_url(self.request.uri)
				url_linktext = 'Logout'
				self.response.out.write(template.render(path,{'person':user.nickname(),'url':url,'url_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))
			else:
				url = users.create_login_url(self.request.uri)
				url_linktext = 'Login'
				self.response.out.write(template.render(path,{'lurl':url,'lurl_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))

class indexPage(webapp.RequestHandler):
	def get(self):
		self.session = Session()
		if 'college' in self.session:
			del self.session['college']
		user = users.get_current_user()
		path = os.path.join(os.path.dirname(__file__), 'template/gurukulHome.html')
		logoimg = "gurukullogo.gif"
		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			self.response.out.write(template.render(path,{'person':user.nickname(),'url':url,'url_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			self.response.out.write(template.render(path,{'lurl':url,'lurl_linktext':url_linktext,'logoimg':logoimg,'gurukulDisp':'gurukul'}))

applications = webapp.WSGIApplication([	('/', mainPage),
										('/gurukulHome.html', indexPage)
									  ],debug=True)

def main():
  run_wsgi_app(applications)

if __name__ == '__main__':
  main()