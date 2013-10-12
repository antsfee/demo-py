import tornado.ioloop
import tornado.web
import os

class ProfileHandler(tornado.web.RequestHandler):
        
    def initialize(self,database):
            self.database = database
            print self.database
    
    def get(self,username):
        
        self.write('box profileHandler man'+username)
##path pei zhi 
app = tornado.web.Application([(r'/user/(.*)',ProfileHandler,dict(database='2bchina'))])

if __name__ == "__main__":
    ## print os.getpid()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()