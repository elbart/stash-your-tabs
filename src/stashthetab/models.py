from google.appengine.ext import db
from django.utils import simplejson as json
import serializer

class BaseModel(db.Expando):
    external_properties = []
    
    def to_json(self):
        result = {}
        
        for field, serializer in self.external_properties:
            result[field] = serializer.serialize(self.__dict__['_' + field])
        
        return json.dumps(result)

class User(BaseModel):
    email = db.EmailProperty()
    pwd = db.StringProperty()
    
    external_properties = [
        ('email', serializer.StringSerializer()),
     ]

class StashItem(BaseModel):
    url = db.LinkProperty(required=True)
    title = db.StringProperty(required=False)
    created = db.DateTimeProperty()
    owner = db.ReferenceProperty(User)
    
    external_properties = [
        ('url', serializer.StringSerializer()),
        ('title', serializer.StringSerializer()),
        ('created', serializer.DateSerializer())
     ]

