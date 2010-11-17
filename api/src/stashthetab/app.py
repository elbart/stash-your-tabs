'''
Created on Nov 16, 2010

@author: Tim Eggert <tim@elbart.com>
'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import handlers

def configure():
    urlmap = [
              ('/user/([^/]+)/list', handlers.ListHandler),
              ('/user/([^/]+)/auth', handlers.AuthHandler)
              ]
    
    config = {}
    
    return [urlmap, config]

def main():
    urlmap, config = configure()
    application = webapp.WSGIApplication(urlmap, debug=False)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()