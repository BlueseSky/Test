import datetime
import time
print time.time()
k = "2018-08-11 12:23:19"
l = datetime.datetime.strptime(k,"%Y-%m-%d %H:%M:%S")

print l,type(l)


fmt='%Y-%m-%d %a %H:%M:%S'
Date=time.strftime(fmt,time.localtime(time.time()))
print Date