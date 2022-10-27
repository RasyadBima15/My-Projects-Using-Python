# Find the value of x1 and x2 in Quadratic Equation
import math
try :
    a=int(input('Input Value a: '))
    b=int(input('Input Value b: '))
    c=int(input('Input Value c: '))
except :
    print('Please Make Sure That You Put Integer in Input')
else :
    try:
        x1=(-b+(math.sqrt(b**2-4*a*c)))/2*a
        x2=(-b-(math.sqrt(b**2-4*a*c)))/2*a
        print(f'x1= {x1}')
        print(f'x2= {x2}')
    except :
        print('Undefined x')
