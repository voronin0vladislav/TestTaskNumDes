def fbn(N: int) -> int:
    c=2
    row=[0,1,1]
    if N < 2:
        return N
    else:
        while c <= N:
                row[2]=row[0] + row[1]
                row[0]=row[1]
                row[1]=row[2]
                c+=1
        print('Ваше число равно: ')
        print(row[1])
        return row[1]


N=int(input('Какое число N Фибоначчи нужно найти? '))
fbn(N)

