#task1------------------------------------------------------------
"""
���� ������ �������������� �����: x1, y1, x2, y2. �������� ������� distance(x1, y1, x2, y2), ����������� ���������� ����� ������ (x1,y1) � (x2,y2). 
�������� ������ �������������� ����� � �������� ��������� ������ ���� �������. 
"""

import math

x1=float(input())

y1=float(input())

x2=float(input())

y2=float(input())

def long(x1,y1,x2,y2):
    
	l=math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
	return l

print(long(x1,y1,x2,y2)) 

#-----------------------------------------------------------------
#task2------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n. 
��������� an. ������� �������� � ���� ������� power(a, n). 
"""


a=float(input())

n=int(input())

def power(a,n):
    
	add=1
    
	for i in range(abs(n)):
        
	add*=a
    
	if n>=0:
        
	return add
    
	else:
        
	return 1/add
power= power(a,n)    

print(power)   

#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����� ��������������� ����� n. ��������� an �� ��������� �����, ���������� � ������� ����� ** � ������� math.pow(), 
� ��������� ������������ ����������� an=a?an-1. 
"""




a=float(input())

n=int(input())

def power(a,n):
    
	if n==0:
        
		return 1
   
	else:
        
		c=1
        
		c*=a*power(a, n - 1)
       
		return c

print(power(a,n))
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
�������� ������� fib(n), ������� �� ������� ������ ���������������� n ���������� n-e ����� ���������. � ���� ������ ������ ������������ ����� � ����������� ��������. 
"""


n = int(input())

def fib(n):
    
	if n == 0:
        
		return 0
    
	elif n == 1 or n == 2:
        
		return 1
    
	else:
  
     		return fib(n - 2) + fib(n - 1)

fibonachi = fib(n)

print(fibonachi)

#-----------------------------------------------------------------

    