values = [47,95,88,73,88,84]
import statistics

print ('\nPython Stastics was used to determine the mean, median, and mode in this BONUS example.\n\n1. The COUNT of values for this dataset is =',len(values))

print ('2. The SUM of this dataset is =',sum(values))

print (f'3. The MEAN of this dataset is = {statistics.mean(values):.2f}')

print (f'4. The MEDIAN of this dataset is = {statistics.median(values):.2f}')

print ('5. The MODE of this dataset is = {statistics.mode(values):.2f},'\n')
