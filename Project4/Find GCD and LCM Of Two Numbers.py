while True :
    try :
        x = int(input('Masukkan bilangan ke-1: '))
        y = int(input('Masukkan bilangan ke-2: '))
        if x==0 and y==0 :
            print('Undefined')
            break
        elif x>=0 and y>=0 :
            if x<y :
                terbesar=y
            else :
                terbesar=x
            for i in range (1,terbesar+1) :
                if x%i==0 and y%i==0:
                    fpb=i
            hasil_kali = x*y
            kpk = hasil_kali//fpb
            print(f'FPB dari {x} dan {y}: {fpb}')
            print(f'KPK dari {x} dan {y}: {kpk}')
            break    
        elif x<0 or y<0 :
            print('Inputan harus berupa bilangan bulat positif dan bukan bilangan rasional/desimal')
    except :
        print('Inputan harus berupa bilangan bulat positif dan bukan bilangan rasional/desimal')
