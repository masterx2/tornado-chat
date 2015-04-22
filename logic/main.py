#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado import ioloop, web, template, websocket

class MainHandler(web.RequestHandler):
    def get(self):
        loader = template.Loader("assets/templates")
        self.write(loader.load("index.tpl").generate())

class Chat(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def get_compression_options(self):
        return {}

    def open(self, *args, **kwargs):
        print "WebSocket opened"
        print self.cookies

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"

if __name__ == "__main__":
    application = web.Application([
        (r"/", MainHandler),
        (r"/ws", Chat),
        (r"/static/js/(.*)", web.StaticFileHandler, {"path": "assets/js"}),
        (r"/static/css/(.*)", web.StaticFileHandler, {"path": "assets/css"}),
    ])
    application.listen(8888)
    ioloop.IOLoop.instance().start()