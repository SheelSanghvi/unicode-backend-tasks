import json
import requests
#requesting data from api
r=requests.get('https://api.spacexdata.com/v3/launches')
data=r.json()
l=len(data)
out={}
#accessing data required
for index in range(0,l):
	out['flight number']=data[index]['flight_number']
	datestr=data[index]['launch_date_local']
	year=datestr[0:4]
	month=datestr[5:7]
	date=datestr[8:10]
	out['launch date']=(date+'-'+month+'-'+year)
	out['mission name']=data[index]['mission_name']
	out['mission patch link']=data[index]['links']['mission_patch']
	print(out) #displaying output