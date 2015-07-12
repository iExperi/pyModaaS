__author__="shpant"

import os, web,sys
import ConfigParser
import schedule,time
import thread
import serviceManager

config = ConfigParser.ConfigParser()
config.read('config.ini')
deployedPath = config.get('ServiceConfig','serviceBasePath')

def loadServices(serviceDir,pathName):
	global serviceManager
	for serviceModules in os.listdir(serviceDir):
		module_name, ext = os.path.splitext(serviceModules)
		if module_name.startswith('service_') and ext == '.py':
			moduleName=pathName+'.'+module_name
			if moduleName in sys.modules:
				reload(sys.modules[moduleName])
			else:
				module = __import__(moduleName)


def masterServiceLoader(deployedBasePath):
	loadServices(deployedBasePath+"/utils",'utils')
	loadServices(deployedBasePath+"/devs",'devs')
	loadServices(deployedBasePath+"/ops",'ops')

def reoadApplication():
	global app,deployedPath,serviceManager
	print("Stopping server if already running")
	app.stop()
	serviceManager.urls = [ ]
	masterServiceLoader(deployedPath)
	app = web.application(serviceManager.urls,globals())
	print("Loading Service Modules")
	thread.start_new_thread(loadApplication,())
	print("Server Started")

def loadApplication():
	global app
	app.run()


masterServiceLoader(deployedPath)
app = web.application(serviceManager.urls,globals())

if __name__ == "__main__":	
	schedule.every(10).seconds.do(reoadApplication)
	while 1:
		schedule.run_pending()
		time.sleep(15)