import logging
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.log import enable_pretty_logging


logger = logging.getLogger(__name__)


class RelayHandler(tornado.web.RequestHandler):

    def post(self):
        logger.info(self.request.body)
        # print(self.request.body)
        # logger.debug(self.request.body)
        # data = tornado.escape.json_decode(self.request.body)
        # print(data)


if __name__ == '__main__':
    enable_pretty_logging()
    app = tornado.web.Application([
        (r'/relay', RelayHandler),
    ])
    server = HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
