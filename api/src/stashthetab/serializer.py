'''
Created on Nov 16, 2010

@author: Tim Eggert <tim@elbart.com>
'''

class StringSerializer():
    def serialize(self, string):
        return str(string)
    
class DateSerializer():
    def __init__(self, format = '%d.%m.%Y %H:%M:%S'):
        self.format = format
    
    def serialize(self, date):
        return date.strftime(self.format)