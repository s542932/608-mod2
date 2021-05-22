values = [7, 9, 11, 111, 33, 3, 8, 5, 12, 11, 12, 20, 25, 35, 45, 55, 65, 75, 86, 99, 101, 102, 99, 88, 44, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 
          121, 1221, 333, 444, 55, 666, 777, 898, 14, 15, 16, 17, 617, 623, 312, 211, 11, 32, 324, 518, 617, 888, 666, 777, 9, 10, 11, 55, 555, 5555, 111, 1111, 11111, 11, 111, 121, 
          7, 4, 11, 77, 777, 99, 999, 111, 44, 617, 11111, 111111, 99, 100, 101, 111, 121, 122, 155, 165, 175, 185, 195, 205, 204, 66, 91, 911, 101, 102]
import statistics

print ('\nPython Stastics was used to determine the mean, median, and mode in this BONUS example.\n\n1. The COUNT of values for this dataset is =',len(values))

print ('2. The SUM of this dataset is =',sum(values))

print (f'3. The MEAN of this dataset is = {statistics.mean(values):.2f}')

print (f'4. The MEDIAN of this dataset is = {statistics.median(values):.2f}')

print (f'5. The MODE of this dataset is = {statistics.mode(values):.2f} \n')
