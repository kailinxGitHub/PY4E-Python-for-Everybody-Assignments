fname = input("Enter file name: ")
fh = open(fname)
count = 0
s=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count=count+1
        a=line.find('0')
        x=line[a:]
        s=s+float(x)
avg=s/count
print("Average spam confidence:",avg)
