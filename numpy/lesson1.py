#leanring numpy right now 
#numpy is used in AI, MAchine Learning applications 
#pytohn is really slow 
#under teh hood it's written in C 
#Number crunching 
#10x faster, perform vectorized operotnr 
#massive datasets, 
import numpy as np 
print(np.__version__)
#sewucne of data->tuple, 
my_list = [1,2,3,4]
print(my_list)
print(type(my_list))
my_list = my_list * 2 
print(my_list)

# 3creatin array in numpy 
array = np.array([1,2,3])
print(type(array))
print(array)
array = array * 2 
print(array)


#practing array 
array2 = np.array([
    [123,343,45], 
    [1,2,34]])
print(array2)
print(array2.ndim)