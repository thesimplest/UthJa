import urllib2,json
def getPNRDetails(pnr):
	url='http://api.railwayapi.com/pnr_status/pnr/'+str(pnr)+'/apikey/3pj8697k/'
	data=urllib2.urlopen(url)
	data=data.read()
	data=json.loads(data)
	train_number=data['train_num']
	d=data['train_start_date']['day']
	c1=''
	c2=''
	if(d<10):
		c1='0'	
	m=data['train_start_date']['month']
	if(m<10):
		c2='0'
	y=data['train_start_date']['year']
	doj=str(y)+c2+str(m)+c1+str(d)
	station_name=data['to_station']['name']
	return train_number,doj,station_name


def getroute(train_number):
	url='http://api.railwayapi.com/route/train/'+str(train_number)+'/apikey/3pj8697k/'
	data=urllib2.urlopen(url)
	data=data.read()
	data=json.loads(data)
	list_of_stations=[]
	for i in range(len(data['route'])):
		list_of_stations.append(data['route'][i]['fullname'])
	return list_of_stations

def getRunningStatus(train_number,doj,station_name):
	url='http://api.railwayapi.com/live/train/'+str(train_number)+'/doj/'+str(doj)+'/apikey/3pj8697k/'
	print url
	data=urllib2.urlopen(url)
	data=data.read()
	data=json.loads(data)
	print data
	for i in range(len(data['route'])):
		if data['route'][i]['station_']['name'] == station_name:
			print data['route'][i]['actarr_date'],data['route'][i]['actarr']
			return data['route'][i]['actarr_date'],data['route'][i]['actarr']
	


