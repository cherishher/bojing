# -*- coding: utf-8 -*-
# @Date    : 2016/10/1  20:51
# @Author  : 490949611@qq.com
import json

import tornado.web
from ..db.contact import Message
import traceback

class ContactHandler(tornado.web.RequestHandler):

	@property
	def db(self):
		return self.application.db

	def on_finish(self):
		self.db.close()

	def get(self):
		self.write('hello profth!')

	def post(self):
		name = self.get_argument('name')
		email = self.get_argument('email')
		phonenum = self.get_argument('phonenum')
		message = self.get_argument('message')
		retjson = {
			'code':200,
			'text':''
		}

		if not (name and email and phonenum and message):
			retjson['code'] = 401
			retjson['text'] = u'请输入完整信息后发送'
		else:
			try:
				message = Message(name = name,email = email,phonenum = phonenum , message = message)
				self.db.add(message)
				self.db.commit()
				retjson['text'] = u'提交成功！'
			except Exception,e:
				traceback.print_exc()
				retjson['code'] = 500
				retjson['text'] = u'系统故障请联系系统开发人员'
		self.write(json.dumps(retjson))

