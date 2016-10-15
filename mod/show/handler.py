# -*- coding: utf-8 -*-
# @Date    : 2016/10/13  22:49
# @Author  : 490949611@qq.com

import tornado.web
from ..db.contact import Message
from config import *

class ShowHandler(tornado.web.RequestHandler):

	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get(self):
		if self.current_user != admin_username:
			self.write("您没有权限访问本页面")
		else:
			message = self.db.query(Message).all()
			self.render('message.html',data = message)