'''
Created on Nov 16, 2010

@author: Tim Eggert <tim@elbart.com>
'''

import functools
import models

def auth(f, *args, **kwargs):
    @functools.wraps(f)
    def wrapper(self, *args, **kwargs):
        
        #TODO: use the correct condition here
        if True:
            self.user = models.User(
                                    email = "tim@elbart.com",
                                    pwd = "tester"
                                    )
            if not self.user.is_saved():
                self.user.put()
            
            f(self, *args, **kwargs)
        else:
            self.error(401)
        
    return wrapper