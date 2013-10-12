import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    
    def  get(self):
        
        self.write('helloword')
        
application = tornado.web.Application([(r'/',MainHandler)]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
