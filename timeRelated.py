import time
from datetime import datetime
def getDiff(s1,s2):
	FMT = '%Y:%m:%d:%H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
	d=tdelta.days
	h=(tdelta.seconds//3600)%24
	m=(tdelta.seconds//60)%60
	s=tdelta.seconds%60
	return d,h,m,s
	
def getDates(actarr_date,actarr):
	date,month,year=actarr_date.split()
	mon={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
	h,m=actarr.split(':')
	s='00'
	s2=year+':'+mon[month]+':'+date+':'+h+':'+m+':'+s
	return s2

def getcurtime():
	s1=time.strftime("%Y:%m:%d:%H:%M:%S")
	return s1




