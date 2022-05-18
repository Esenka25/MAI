import math #библиотека для работы с тригономертическими, логарифмическими и тп ф-ями
print("Введите функцию, содержащую переменную 'x':")
f = input()
print("Введите границы интеграла(сначала нижнюю, а после верхнюю):")
a, b = map(float, input().split())
af = a
sumdone = 0
y = []
twosum = 0
elsesum = 0
if b - a > 2:
    deli = 3    #поиск наименьшего делителя
    while (b - a) % deli != 0:
        deli += 1
    
    if deli > int((b-a)**0.5 + 1):  #поиск n путем сравнения с корнем из длинны
        n = int((b - a) // deli)
    else:
        n = int(deli)
    h_sm = int(b - a) / (2 * n) # поиск h для дальнейших вычислений в симпсоне
    h1 = h_sm
    h2 = af + h_sm
    x = af
    y.append(eval(f))
    h_tr = (b - a) / (n*2) #поиск для трапеции

    for i in range(n*2): #поиск значение для каждого отрезка и кладём в массив
        x = h2
        y.append(eval(f))
        h2 += h1


    #составная формула Симпсона 
    for i in range(0, len(y)-2, 2): 
        sumdone += (h_sm / 3 *(y[i] + 4 * y[i+1] + y[i+2]))
    
    #составная формула трапеции
    for i in range(2*n + 1):
        if i == 0 or i == 2 * n:
            x = a + i * h_tr
            twosum += eval(f) #сумма значений на концах отрезка
        else:
            x = a + i * h_tr
            elsesum += eval(f) #сумма всех остальных отрезков
else:
    n = 5 #короткий отрезок можно разбить на 5 ещё более коротких
    h_sm = (b - a) / 10
    h1 = h_sm
    h2 = af + h_sm
    x = af
    y.append(eval(f))
    h_tr = (b - a) / 10
    for i in range(n*2): #поиск значение для каждого отрезка и кладём в массив
        x = h2
        y.append(eval(f))
        h2 += h1


    #составная формула Симпсона 
    for i in range(0, len(y)-2, 2): 
        sumdone += (h_sm / 3 *(y[i] + 4 * y[i+1] + y[i+2]))

    #составная формула трапеции
    for i in range(2*n + 1):
        if i == 0 or i == 2 * n:
            x = a + i * h_tr
            twosum += eval(f) #сумма значений на концах отрезка
        else:
            x = a + i * h_tr
            elsesum += eval(f) #сумма всех остальных отрезков
print(sumdone, 'метод симпсона', sep = ' ')
print(h_tr*(twosum/2 + elsesum), 'метод трапеци', sep = ' ')
