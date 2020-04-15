#Built in list Methods
list.append(obj)
list.count(obj)
list.extend(obj)
list.index(obj)
list.insert(index, obj)
list.pop(obj = list[-1])
list.remove(obj)
list.reverse(-1)
list.sort([max(list)])

#tuples are read only so no methods can change them

#Built in Dict Methods
dict.clear() #removes all elements of dictionary dict
dict.copy() #returns a shallow copy of dictionary dict
dict.fromkeys() #create new dict with keys from seq and values set to value
dict.get(key, default = none) #for "key" key,returns value or default if key not in dict
dict.has_key(key) #removed, use the in operation instead
dict.items() #returns list of dicts(key, value) tuple pairs
dict.keys() #return list or dictionay dict keys
dict.setdefault(key, default = none) #set dict[key] = default if key is not already in dict
dict.update(dict2) #add dictionary dicts key-value to dict
dict.values() #returns list of dictionary dict values

#Time
time.mktime(tupletime)
time.altzone()
time.asctime([tupletime])
time.clock()
time.gmtime([secs])
time.localtime([secs])
time.tzset()
time.strftime(fmt[ ,tupletime])
time.sleep(secs)

#Calendar
calendar.calendar(year, w=2, i=1, c=6)
calendar.month(year, month; w=2, i=1)
calendar.monthcalendar(year, month)
calendar.monthrange(year, month)
calendar.setfirstweekday(weekday)
calendar.timegm(tupletime)
calendar.weekday(year, month, day)







