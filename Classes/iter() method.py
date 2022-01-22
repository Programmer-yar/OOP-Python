# basic use of iter() 
listA = ['a','e','i','o','u'] 
  
iter_listA = iter(listA) 
  
try: 
    print( next(iter_listA))  
    print( next(iter_listA))  
    print( next(iter_listA))  
    print( next(iter_listA))  
    print( next(iter_listA)) 
    print( next(iter_listA)) #StopIteration error 
except: 
    pass
