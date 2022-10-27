# Triangle
n=int(input('Input value n: '))
if n<=0 :
    print('The input has to be positive and bigger than zero')
elif n>0 :
    for b in range(n-1,0,-1) :
        print(' '*b,end='')
        print('*'*(n*2-(2*b+1)),end='')
        print(' '*b,end='')
        print()
    for a in range(1,n*2) :
        print('*', end='')
    print()

# Inverted Triangle
n=int(input('Input value n: '))
if n<=0 :
    print('The input has to be positive and bigger than zero')
elif n>0 :
    for a in range(1,n*2) :
        print('*', end='')
    print()
    for b in range(1,n) :
        print(' '*b,end='')
        print('*'*(n*2-(2*b+1)),end='')
        print(' '*b,end='')
        print()