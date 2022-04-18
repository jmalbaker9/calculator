def add(n1,n2):
    '''
    takes two numbers as input
    and returns the sum
    '''
    return n1+n2

def subtract(n1,n2):
    '''
    takes two numbers as input
    and returns the difference
    '''    
    return n1-n2

def multiply(n1,n2):
    '''
    multiplies n1 by n2
    '''
    return n1*n2


n1=int(input("Enter 1st number"))
#taking first number as input
n2=int(input("Enter 2nd number"))
# taking second number as input

oper=input("Choose operation - 1. add 2. sub 3. mul")

if oper=="add":
    print("sum=",add(n1,n2))
elif oper=="sub":
    print("differnce=",subtract(n1,n2))
elif oper=="mul":
    print("product=",multiply(n1,n2))
