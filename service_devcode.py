__author__="shpant"
import web
from serviceManager import ServiceMetaClass

class devcode:
	__metaclass__ = ServiceMetaClass
	url = '/devCode'
	def GET(self):
		return "Dev Code Module Changed Againafasfsadf"
class devcode2:
	__metaclass__ = ServiceMetaClass
	url = '/devCodeNewNew'
	def GET(self):
		return "New Dev Code Module Changed again again again....again testasdkfhaskhfjkdshasdkfjdsalfjdskasdklfjadslkfjasdkljfdskl"