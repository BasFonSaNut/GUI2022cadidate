from datetime import datetime,timedelta

#Today= datetime.today()
# date_list = [Today + timedelta(minutes=15*x) for x in range(0, 1000)]
# datetext=[x.strftime('%Y-%m-%d T%H:%M Z') for x in date_list]
#print(Today) 

# x = datetime.today()
# #datetime.datetime(2018, 6, 1)
# print(x.strftime("%d-%b-%Y"))
# print(x.strftime("%H:%M"))


# a= '3900080009999'
# print(len(a))
# print(a[13:-4]) //not work in python

# s = "3900080009999"
# res = s.partition('9999')[0]
# print(res)



date_1 = '27-Feb-2022 00:37'
date_2 = '28-Feb-2022 00:21'
date_format_str = '%d-%b-%Y %H:%M'
start = datetime.strptime(date_1, date_format_str)
end =   datetime.strptime(date_2, date_format_str)
# Get interval between two timstamps as timedelta object
diff = end - start
# Get interval between two timstamps in hours
diff_in_hours = diff.total_seconds() / 3600
print('Difference between two datetimes in hours:')
print(diff_in_hours)
