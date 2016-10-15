# -*- coding: utf-8 -*-
# @Date    : 2016/10/1  20:51
# @Author  : 490949611@qq.com


import tornado.web
from ..db.publish import News
import json
import time
from config import *

class PublishHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get_current_user(self):
		return self.get_secure_cookie("admin")

	def get(self):
		if self.current_user != admin_username:
			self.write("您没有权限访问本页面")
		else:
			news = self.db.query(News).all()
			self.render('publish.html',data = news)

	def post(self):
		retjson={
			'code':200,
			'content':''
		}

		id = self.get_argument('id',default=None)
		title = self.get_argument('title',default=None)
		profile = self.get_argument('profile',default=None)
		delete = self.get_argument('dlt',default=0)

		if int(delete) == 1:
			try:
				news = self.db.query(News).filter(News.id == id).one()
				self.db.delete(news)
				self.db.commit()
				retjson['content'] = u'删除成功！'
			except Exception,e:
				retjson['content'] = u'删除失败,请重新尝试'
		else:
			try:
				print 'enter'
				localtime = time.strftime("%Y-%m-%d")
				news = News(title = title,time = localtime,profile = profile)
				self.db.add(news)
				self.db.commit()
				retjson['content'] = u'发布成功！'
			except Exception,e:
				retjson['code'] = 400
				retjson['content'] = u'发布失败'
		self.write(json.dumps(retjson))
		self.finish()

	def remove(self,id,retjson):
		try:
			print 'try to remove'
			news = self.db.query(News).filter(News.id == id).one()
			self.db.delete(news)
			self.db.commit()
			retjson['content'] = u'删除成功！'
		except Exception,e:
			retjson['content'] = u'删除失败,请重新尝试'


