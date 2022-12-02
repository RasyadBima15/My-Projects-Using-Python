x = int(input('Masukkan bilangan ke-1: '))
y = int(input('Masukkan bilangan ke-2: '))

x = abs(x)
y = abs(y)

if x>0 or y>0 :
    if x<y :
        terbesar=y
    else :
        terbesar=x
    for i in range (1,terbesar+1) :
        if x%i==0 and y%i==0:
            fpb=i
    hasil_kali = x*y
    kpk = hasil_kali//fpb

elif x==0 and y==0 :
    fpb = 0
    kpk = 0

print(f'FPB dari {x} dan {y}: {fpb}')
print(f'KPK dari {x} dan {y}: {kpk}')