import datetime

now = datetime.datetime.now()
# returns date as locale has it
print(now.strftime("%x"))