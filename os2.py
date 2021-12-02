import os
print(dir(os))
from datetime import *

print(os.getcwd())
print(os.chdir('/home/elcot/Documents/python'))
print(os.getcwd())
print(os.chdir('/home/elcot/Documents'))
print(os.getcwd())


print(os.listdir())
print(os.mkdir('course'))
print(os.makedirs('python/firstpro'))


print(os.rmdir('dddd.py'))
print(os.removedirs('python/firstpro'))
print(os.listdir())

print(os.rename('pythoncourse/firstpro','second'))
print(os.rename('employee.db','raja.db'))



for dirpath,dirs,files in os.walk('/home/elcot/Documents/screens'):
	print("dirpath:",dirpath)
	print('---------------------')
	print("directory:",dirs)
	print('----------------------')
	print("dirfile:",files)



print(os.stat('oops.py'))#list out files details
print(os.stat('oops.py').st_ctime)
accesstime=os.stat('oops.py').st_atime
print(datetime.fromtimestamp(accesstime))




