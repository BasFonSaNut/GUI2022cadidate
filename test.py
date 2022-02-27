from datetime import datetime,timedelta


#Today= datetime.today()
# date_list = [Today + timedelta(minutes=15*x) for x in range(0, 1000)]
# datetext=[x.strftime('%Y-%m-%d T%H:%M Z') for x in date_list]
#print(Today) 

x = datetime.today()
#datetime.datetime(2018, 6, 1)
print(x.strftime("%d-%b-%Y"))
print(x.strftime("%H:%M"))

