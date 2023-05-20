#10.2 Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

fname = input("Enter file name: ")
fh = open(fname)

count = 0

dictionary_hours = dict()
lst = list()
for line in fh:
    if line.startswith('From '):
        parts = line.rstrip().split()
        time = parts[5]
        hour = time[0:2]
        if hour not in dictionary_hours:
            dictionary_hours[hour] = 1
        else:
            dictionary_hours[hour] += 1
        count += 1
for key, val in list(dictionary_hours.items()):
    lst.append((key, val))

lst.sort()
for key, val in lst:
    print(key, val)
