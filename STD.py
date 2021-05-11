import math
import csv
with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)
d = data[0]
def mean(d):
    n = len(d)
    total = 0
    for x in d:
        total+=int(x)
    mean = total/n
    return mean
squaredList = []
for n in d:
    a = int(n)-mean(d)
    a = a**2
    squaredList.append(a)
sum = 0
for i in squaredList:
    sum = sum+i
result = sum/(len(d)-1)
standDev = math.sqrt(result)
print(standDev)