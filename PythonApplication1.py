from datetime import *
from random import *
print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a  = abs(int(input("Введите целое число => ")))
        if a == 0:
            print("Это не целое число")
    except ValueError:
        print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
print()
a = int(input("Введите число: "))
b = a
paaris = 0
paaritu = 0

while b > 0:
    if b % 2 == 0:
        paaris += 1
    else:
        paaritu += 1
    b //= 10

print("Чётных цифр:", paaris)
print("Нечётных цифр:", paaritu)
print()

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0
        number = a % 10
        a = a // 10
        b = b * 10
         b =+ number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Проверяем гипотезу Сиракуз")
    print()
    if c % 2 = 0:
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
            if c % 2 = 0:
                    c == c / 2
            else:
                    c == (3*c + 1) / 2
            print(c, end=""):
    print()
    print("Гипотеза верна")



























for j in range(1,11):
    for i in range(1,11):
        print(f"j*i:4",end=" ")
    print()
















#12 pank
algsumma=float(input("Mis summa paneme panka?"))
alg=lõppsumma=algsumma
intress=randint(1,10)
print(f"Paned panka summa,mis võrdub {algsumma}.Intress on{intress}")
aastad=int(input("Mitmeks aastaks?"))
print("Aasta algsumma intress aasta_lõpuks")
for i in range(1,aastad+1):
    intsumma=(algsumma*intress)/100
    lõppsumma=algsumma+intsumma
    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
    algsumma=lõppsumma
print(f"Summa kokku: {lõppsumma} Eur")
print(f"kasum: {lõppsumma-alg} Eur")