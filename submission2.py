# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:31:12 2020

@author: vishnumaganti
"""

def fib(n):
    if n<=1:
           return n
    else:
         for i in range (2, n+1):
            return  fib(n-1)+fib(n-2)        
       
m=int(input())
print(fib(m))    
        
    


