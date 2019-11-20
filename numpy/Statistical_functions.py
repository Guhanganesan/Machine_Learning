"""
1. mean() :- This function returns the mean or average of the data passed in its arguments. 
If passed argument is empty, StatisticsError is raised.
"""
import statistics 
 
li = [1, 2, 3, 3, 2, 2, 2, 1] 
print ("The average of list values is : ",end="") 
print (statistics.mean(li))

"""
2. mode() :- This function returns the number with maximum number of occurrences. 
If passed argument is empty, StatisticsError is raised.
"""

print ("The maximum occurring element is  : ",end="") 
print (statistics.mode(li))


"""
3. median() :- This function is used to calculate the median, i.e middle element of data. 
If passed argument is empty, StatisticsError is raised.
"""

print ("The median of list element is : ",end="") 
print (statistics.median(li)) 
  

"""
4. median_low() :- This function returns the median of data in case of odd number of elements, but in case of even number of elements, returns the lower of two middle elements.
If passed argument is empty, StatisticsError is raised.
"""
print ("The lower median of list element is : ",end="") 
print (statistics.median_low(li)) 

"""
5. median_high() :- This function returns the median of data in case of odd number of elements,
but in case of even number of elements, returns the higher of two middle elements. 
If passed argument is empty, StatisticsError is raised.
""""
print ("The higher median of list element is : ",end="") 
print (statistics.median_high(li))

"""
median_grouped() :- This function is used to compute group median, 
i.e 50th percentile of the data. If passed argument is empty, StatisticsError is raised.

value=percentile/100 * (n+1)
if it is not value in the given range take avg 

value=50/100 * (6+1)= 1/2 * 7 =3.5 

there is no value of 3.5 in list

avg =4th and 5th/2 = 3+2 /2 =2.5

"""
print ("The 50th percentile of data is : ",end="") 
print (statistics.median_grouped(li)) 



"""
import numpy as np
normal_array = np.random.normal(5, 0.5, 6) #ValueError: scale < 0
print(normal_array)	

print(np.min(normal_array))

print(np.max(normal_array))

print(np.mean(normal_array))

print(np.median(normal_array))

print(np.std(normal_array))

"""
