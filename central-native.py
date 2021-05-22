values = [47,95,88,73,88,84]

print ('\n1. The COUNT of values on page 110-111, question 4 =',len(values))

print ('2. The SUM of values on page 110-111, question 4 =',sum(values))

mean = sum(values) / len(values)
print (f'3. The MEAN of values on page 110-111, question 4 = {(mean):.2f}')

sortedlist = sorted(values)
n = len(values)
if n % 2 == 0:
  median1 = sortedlist[n//2]
  median2 = sortedlist[n//2-1]
  median = (median1 + median2)/2
else:
  median = sortedlist_num[n//2]
print ('4. The MEDIAN of values on page 110-11, question 4 =', median)

y = sortedlist
L1 = []
i = 0
while i < len(y):
  l1.append(y.count(y[i])
  i += 1
d1 = dict(zip(y,L1))
d2 = (k for (k,v) in d1.items() if v == max(L1))
print('Mode(s) is/are:', str(d2))





#frequency = {}
#for number in values:
  #frequency.setdefault(number, 0)
  #frequency[number]+=1
#highestfrequency = max(frequency.values())
#print({max(frequency.values())})

#print ('5. The MODE of values on page 110-111, question 4 =', mode(values),'\n')
