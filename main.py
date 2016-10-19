#!/usr/bin/env python
#coding:utf-8

import os.path
import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.simple_httpclient
import tornado.httpclient
import tornado.httpserver
import tornado.options
import tornado.gen
from mod.db.db import engine
from tornado.options import define, options
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.host.handler import HostHandler
from mod.contact.handler import ContactHandler
from mod.publish.handler import PublishHandler
from mod.show.handler import ShowHandler
from mod.login.handler import LoginHandler

define("port", default= 7000, help= "run on the given port", type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/index',HostHandler),
			(r'/contact',ContactHandler),
			(r'/publish',PublishHandler),
			(r'/show',ShowHandler),
			(r'/login',LoginHandler)
		]

		settings = dict (
			template_path= os.path.join(os.path.dirname(__file__), 'templates'),
			static_path= os.path.join(os.path.dirname(__file__), 'static'),
			cookie_secret="MAX90KLP8371B5AEAC5E64C6042415EF",
			debug= True,
			)
		tornado.web.Application.__init__(self,handlers,**settings)
		self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


if __name__ == "__main__":
	tornado.options.parse_command_line()
	Application().listen(options.port)
	tornado.ioloop.IOLoop.instance().start()