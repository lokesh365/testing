import datetime as dt
import time
from datetime import timedelta

times=dt.datetime.now()
dates = (times.strftime("%I:%M")) 
print dates

nine_hours_from_now=dt.datetime.now() + dt.timedelta(minutes=1)
plus= '{:%I:%M}'.format(nine_hours_from_now)


def dat():
	curnt = dt.datetime.now()
	tym = (curnt.strftime("%I:%M")) 
	print "tym",tym
	print "plus",plus
	if tym==plus:
		print "true"
	else:
		time.sleep(5)
		dat()	
			
dat()


'''
import datetime as dt
mytime = dt.datetime.strptime('0130','%H%M').time()
mydatetime = dt.datetime.combine(dt.date.today(), mytime)
print "mydatetime	:",mydatetime

datetime = (time.strftime("%I:%M"))
print "time",datetime
thousandDays = datetime.timedelta(minutes=10)
print str(thousandDays)

datim=dat+thousandDays
print "final :",datim
'''
