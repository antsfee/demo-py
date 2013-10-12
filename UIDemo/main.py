from  tornado.options import options , define
import tornado.web
import tornado.ioloop
import tornado.auth
import tornado.escape
import tornado.httpserver
import os.path

define('port',default=8000,help='run the given port',type=int)

########################################################################
class AppDD(tornado.web.Application):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        handlers=[
        (r"/",MainHandler),
        (r"/recommended",RecommendedHandler),
        (r"/dicussion",DiscussionHandler)
        ]
        settings={"gzip":True,
                  "template_path":os.path.join(os.path.dirname(__file__),"templates"),
                  "static_path":os.path.join(os.path.dirname(__file__),"static"),
                  "debug":True,
                  "ui_modules":{"book":BookModel}
                  }
        tornado.web.Application.__init__(self,handlers,**settings)
    
########################################################################
class RecommendedHandler(tornado.web.RequestHandler):

    def get(self):
        
        self.render("recommended.html",page_title="Recommended page")
        
class DiscussionHandler(tornado.web.RequestHandler):
    
    def get(self):

        self.render()

class BookModel(tornado.web.UIModule):
    
    def render(self,book):
        """Constructor"""
        return self.render_string("modules/book.html",book=book)
    def javascript_files(self):
        return "static/js/book.js"
    
    def css_files(self):
        return "static/css/book.css"
    
########################################################################
class MainHandler(tornado.web.RequestHandler):
    """"""

    def  get(self):
        self.render("index.html",page_title="home page")
        
    
    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(AppDD())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
if __name__ == "__main__":
    main()
        
    
    
    
    