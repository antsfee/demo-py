import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.escape
from tornado.options import define , options
import os.path

define('port',default=8000,help='connect the given port',type=int)
########################################################################
class Application(tornado.web.Application):
    
    def __init__(self):
       
        
        handlers=[
            (r"/",ArticleHandler),
            (r"/article/",ArticleHandler),
        ]
        settings={"template_path":os.path.join(os.path.dirname(__file__),"templates"),
            "static_path":os.path.join(os.path.dirname(__file__),"static"),
            'gzip':True,
            'debug':True
        }
            
        
        
        tornado.web.Application.__init__(self,handlers,**settings)
    
        
        
    
class ArticleHandler(tornado.web.RequestHandler):    
    
    #----------------------------------------------------------------------
    def get(self):
        """"""
        self.render('index.html',title_name="wabger",body_title="shack",header_title="Oh My Tt")
        
 
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
     
if __name__ == "__main__":
    main()
        