'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-04-02 17:33:38
LastEditors: TianyuYuan
LastEditTime: 2021-04-03 01:07:25
'''
from tykit import pb_range
from time import sleep

# use pb_range just like range()
for i in pb_range(50):
   sleep(0.001)

from tykit import pb_iter
some_task = lambda x: x*x
iterable_file = [x for x in range(100)]

for i in pb_iter(iterable_file):
    some_task(i)


from tykit import pb_multi_thread as pbmt

# Firstly, define your task func
task_func = lambda x: x*x*x
# Put your jobs in a iterable data structure
jobs = [x for x in range(1000)]
# run multi-threading with pb(ProgressBar)
# and save the result in a list
max_workers = 20
result = pbmt(max_workers,task_func,jobs)
print(result[:10])

from tykit import pb_multi_thread_partial as pbmtp

# define a task func with multi params
def task(x,a,b,c):
    return x+a+b+c
# Put your jobs in a iterable data structure
jobs = [x for x in range(1000)]
# run multi-threading with partial
max_workers = 20

result = pbmtp(max_workers,task,jobs,a=10,b=100,c=-20)
print(result[:10])