values = [47,95,88,73,88,84]

print('\nHere are my answers using native Python for the Module 2 Project. \n')
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

mode = max(values, key= values.count)
print ('5. The MODE of values on page 110-111, question 4 =', mode,'\n')
