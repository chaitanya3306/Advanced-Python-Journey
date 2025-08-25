#1
from typing import Optional
import time

class Timer():
    def __init__(self,label:str):
        self.label=label
        self.start:Optional[float]=None
        self.elapsed:Optional[float]=None
        
    def __enter__(self):
        self.start=time.perf_counter()
        print("execition started")
        return self
        
    def __exit__(self,exc_type,exc_val,traceback):
        end_time=time.perf_counter()
        elapsed_time=end_time-self.start
        print(f"time required {elapsed_time:.2f} Sec ")
        if exc_type:
            print(f"Exception occured {exc_val} ")
        print("Ended")
        
        
        

with Timer("data"):
    sum(range(56_000_000))


#2
# from contextlib import contextmanager

# @contextmanager
# def tempfile(filename,mode):
#     file=open(filename,mode)
#     try:
#         yield file
#     finally:
#         file.close()
#     print(f"{filename} Closed ")

# with tempfile('Temp.txt','w') as f:
#     f.write("IMP noted")




#3
# # this is the way to open the file in the traditional way lets open more than one files at a time 
# # in a dynamic memory

# from contextlib import ExitStack

# # filenames=['temp1.txt','temp2.txt']

# # with ExitStack() as stack:
# #     files=[stack.enter_context(open(fname,'w')) for fname in filenames]
# #     for file in files:
# #         file.write('Hello this is in all Temp files !!')
        
# #     # all files are closed here
  
  
#4
  
# # # now using glob and endstack lets see how to store the all files content in single file:
# # import glob
# # file_paths=glob.glob("*.txt")
# # content={}

# # with ExitStack() as stack :
# #     files=[stack.enter_context(open(path,'r')) for path in file_paths]
# #     for file in files:
# #         content[file.name]=file.read()
    
# # print(content)


#this is the datascietist oriented exercises solution so you can solve the daily solution on GPT
    
        
    
        