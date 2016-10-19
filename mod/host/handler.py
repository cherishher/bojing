# -*- coding: utf-8 -*-
# @Date    : 2016/10/1  20:51
# @Author  : 490949611@qq.com

import tornado.web
import tornado.web
import tornado.gen
from ..db.publish import News

class HostHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def get(self):
		try:
			data = self.db.query(News).all()
			self.render('../static/index3.html',data=data)
		except Exception,e:
			print str(e)
