file_name = input("What's the name of the file:")
fh = open(file_name)

d = fh.read()
import re
num = re.findall('[0-9]+', d)
sum = 0
for i in range(len(num)):
    c = int(num[i])
    sum += c

print(sum)
