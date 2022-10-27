# Square with some spaces in it
n=int(input('Input value n: '))
if n==1:
    for firstline in range(1,2*n+1) :
        print('*', end='')
elif n==2:
    for firstline in range(1,2*n+1) :
        print('*', end='')
    print()
    for firstline in range(1,2*n+1) :
        print('*', end='')
elif n>2:
    for firstline in range(1,2*n+1) :
        print('*', end='')
    print()
    for midline in range(1,n-1) :
        print('*',end='')
        print(' '*(2*n-2),end='')
        print('*')
    for firstline in range(1,2*n+1) :
        print('*', end='')
    print()
else :
    print('The input has to be positive and bigger than zero')
    
# Square without space in it
n=int(input('Input value n: '))
if n<=0 :
    print('The input has to be positive and bigger than zero')    
for length in range (1,n+1) :
    for wide in range(1,2*n+1) :
        print('*', end='')
    print()

