import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define , options

define("port",default=7888,help="run on  the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    
    #----------------------------------------------------------------------
    def get(self,input):
        self.write("mimisao")
        self.write(111)
        self.write(input[::-1])

########################################################################
class WrapHandler(tornado.web.RequestHandler):
    """"""

    #----------------------------------------------------------------------
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width',40)
        self.write(textwrap.fill(text,int(width)))
        
def main():
    tornado.options.parse_command_line()
    app= tornado.web.Application(handlers=[(r"/reverse/(\w+)",ReverseHandler),(r"/wrap",WrapHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    print options.port
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    main()
    
        
        
    
    
        
        

