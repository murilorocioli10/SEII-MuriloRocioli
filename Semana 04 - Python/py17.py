import datetime
import pytz

# Naive dates and times are easier to work, but doesn't provide much information

# Code 01
d = datetime.date(2021, 12, 27) #year/month/day
print(d)
tday = datetime.date.today()    #current local date
print(tday) #full date
print(tday.weekday()) #day of the week -> 0 to 6
print(tday.isoweekday) #day of the week -> 1 to 7

# Code 02 - Time Deltas
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
#date2 = date1 + timedelta
#timedelta = date1 + date2

# Code 03
tday = datetime.date.today()
bday = datetime.date(2022, 3, 9)
till_bday = bday - tday
print(till_bday.total_seconds())

# Code 04 - Working with 'date' and'time'
#dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
#tdelta = datetime.timedelta(days=7)
#print(dt + tdelta)

t = datetime.time(9, 30, 45, 100000)
dt = datetime.time(2021, 3, 15, 16, 33, 20, 100000)
tdelta = datetime.timedelta(hour=12)
print(t.hour)
print(dt+tdelta)

# Code 05
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)


dt = datetime.datetime(2021, 3, 15, 16, 33, 20, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'March 15, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime -> datetime to string
# strptime -> string to datetime
