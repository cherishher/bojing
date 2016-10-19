# -*- coding: utf-8 -*-
# @Date    : 2016/5/22  15:02
# @Author  : 490949611@qq.com

import json
import random
import traceback
from sqlalchemy.orm.exc import NoResultFound

import tornado.web

from config import *
from tornado.httpclient import HTTPRequest,HTTPClient,HTTPError
import tornado.web
import tornado.gen
import json

class LoginHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get(self):
		self.render('login.html')

	def post(self):

		#验证用户身份
		retjson={
				'code':200,
				'text':"管理员登陆"
				}
		studentnum = self.get_argument('studentnum',default=None)
		password = self.get_argument('password',default=None)

		result = self.auth(studentnum,password)

		if result['code']==200:
			try:
				self.set_secure_cookie("admin_username",studentnum,expires_days=2)
			except:
				traceback.print_exc()
				retjson['code'] = 500
				retjson['text'] = u'数据库链接异常，请联系后台管理员'
		elif result['code'] == 400:
			retjson['code'] = 400
			retjson['text'] = u'密码错误或网络故障，请稍后再试'
		else:
			retjson['code'] = 500
			retjson['text'] = u'系统错误，请联系后台管理员'
		print retjson
		self.write(json.dumps(retjson))

	def auth(self,username,password):
		result = {
			'code':0
		}
		if username == admin_username:
			if password == admin_password:
				result['code'] = 200
			else:
				result['code'] = 400
		else:
			result['code'] = 400
		return result