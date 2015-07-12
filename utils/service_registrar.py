__author__="shpant"
import web
from serviceManager import ServiceMetaClass

class register_service:
	__metaclass__ = ServiceMetaClass
	url = '/registerServiceModule'
	def POST(self):
		return "Registered the service Module"
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html><head></head><body>Upload your service<br/>
		<form method="POST" enctype="multipart/form-data" action=""><input type="file" name="myfile" /><br/><input type="submit" /></form></body></html>"""

class deregister_service:
	__metaclass__ = ServiceMetaClass
	url = '/deregisterServiceModule'
	def GET(self):
		return "Men At Work!!! Check back l8r"
