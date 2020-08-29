# %%
import datetime
time = datetime.time(2, 20, 2)


# %%
time.hour
# %%
time.second
# %%
time.minute
print(time)
time.microsecond
type(time)

# %%
today = datetime.date.today()
print(today)
# %%
today.year
today.month
today.day
# %%
today.ctime()
# %%
date_time = datetime.datetime(2021, 10, 3, 14)
dte_time = date_time.replace(year=2020)

# %%
date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)
# %%
result = date1-date2
type(result)
result.days

# %%
datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)
result = datetime1-datetime2
36000/60/60
# %%
result.seconds
result.total_seconds()
# %%
