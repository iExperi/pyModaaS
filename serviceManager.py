__author__="shpant"

urls = [ ]

class ServiceMetaClass(type):
	def __init__(klass, name, bases, attrs):
		urls.append(attrs["url"])
		urls.append("%s.%s" % (klass.__module__, name))
		print urls
