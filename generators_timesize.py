'''
A program that shows Performance and Memory utilization of Genrators over List
------------
Python 3.7.0
------------

SCOPE :
Will repeat the below steps for both List and Generator
1. Store the time before initialization of a List/Generator
2. Initialize a List/Generator with 1 million data using List/Generator comprehension
3. Store the time after initializtion is complete
4. Print the time and memory size to initialize the List/Generator

'''

import time
import sys

start_time = time.time()
# Creating a list with 1 million data using List comprehension
gen_list = [i for i in range(100000000)]
end_time = time.time()
# Print the time and memory size to initialize the List
print(f"Total time to generate list : {end_time-start_time}")
print(f"Size of list : {sys.getsizeof(gen_list)/(1024*1024)} MB")

start_time = time.time()
# Creating a list with 1 million data using Generator comprehension
gen_gen = (i for i in range(100000000))
end_time = time.time()
# Print the time and memory size to initialize the Generator
print(f"Total time to generate generator : {end_time-start_time}")
print(f"Size of generator : {sys.getsizeof(gen_gen)} Bytes")

# Clearing the memory
del gen_list
del gen_gen

