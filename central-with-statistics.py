values = [47,95,88,73,88,84]
import statistics

print ('\nPython Stastics was used to determine the mean, median, and mode in this example.\n\n1. The COUNT of values on page 110-111, question 4 =',len(values))

print ('2. The SUM of values on page 110-111, question 4 =',sum(values))

print (f'3. The MEAN of values on page 110-111, question 4 = {statistics.mean(values):.2f}')

print ('4. The MEDIAN of values on page 110-11, question 4 =',statistics.median(values))

print ('5. The MODE of values on page 110-111, question 4 =', statistics.mode(values),'\n')
