from google.appengine.ext import webapp
import pprint
from django.utils import simplejson as json
import datetime

import helpers
import models

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        
class ListHandler(webapp.RequestHandler):
    @helpers.auth
    def get(self, *args, **kwargs):
        query = models.StashItem.all();
        items = query.fetch(limit = 10)
        
        result = []
        
        for item in items:
            result.append(item.to_json())
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(result)
        
    
    @helpers.auth
    def put(self, *args, **kwargs):
        try:
            params = json.loads(self.request.body)
        except:
            self.error(400)
        
        if params.has_key('url') and params.has_key('title'):
            item = models.StashItem(
                url = params['url'],
                title = params['title'],
                created = datetime.datetime.now(),
                owner = self.user
            )
            
            item.put()

class AuthHandler(webapp.RequestHandler):
    def get(self):
        pass
    
    