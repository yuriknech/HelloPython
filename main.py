# Information Systems Tools - Hello Python

import time
from tkinter import *
from tkinter import messagebox

def retrywindow():
    window.withdraw()
    time.sleep(10)
    window.deiconify()


if __name__ == '__main__':

    #task 1...
    print(2 + 2)        #Сложение чисел
    print(37 / 10)      #Деление которое выводит число с плавающей точкой
    print(37 // 10)     #Деление которое выводит только целое число
    print(37 % 10)      #Деление которое выводит остаток
    #...task 1

    #task 2...
    print('Hello world')
    #...task 2

    #task 3...
    a = 3
    print(type(a))
    a = 3.5
    print(type(a))
    a = 'qwerty'
    print(type(a))
    a = True
    print(type(a))
    a = '123'
    print(type(a))
    #...task 3

    # task 4...
    print(int(5.7))
    print(int(-5.7))
    print(3**39 - int(float(3**39)))
    # ...task 4

    # task 5...
    name = input('Введите свое имя ')
    print('Привет,' + name + '!', end='\n\n')
    # ...task 5

    # task 6...
    x = int(input('X='))
    y = int(input('Y='))
    print('Итого минут: ' + str(x+y))
    # ...task 6

    # task 7...
    a = False
    b = True
    c = False
    print(not a or b and c)     #Получилась Истина
    print((not a or b) and c)   #Получилась Ложь
    # ...task 7

    # task 8...
    Year = int(input('Введите год: '))
    if Year < 1900 or Year > 3000:
        print('Год не входит в выборку')
    elif Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        print('С Днем Рождения!')
    else:
        print('Год обычный')
    # ...task 8

    # task 9...
    a = 1;
    while a <= 20:
        if a % 2 == 0:
            print(a, end = ' ')
        a = a + 1
    # ...task 9

    # task 10...
    a = int(input('Введите число: '))
    sum = 0
    while a != 0:
        sum = sum + a
        a = int(input('Введите число: '))
    print('Итого: ' + str(sum))
    # ...task 10

    # task 11...
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    m = max(x, y)
    while True:
        if m % x == 0 and m % y == 0:
            print(m)
            break
        else:
            m += 1
    print('Нужно кусков : ' + str(m))
    print('Пицца порезана')
    # ...task 11

    # task 12...
    a = 1
    for a in range(20):
        if a % 2 == 0:
            print(a, end=' ')
    # ...task 12

    # task 13...
    a, b, c, d = [int(input('Введите число: ')) for i in range(4)] #генератор списков, каждое значение вводится в своей строке
    print('', end='\t')                                            #табуляция
    for j in range(c, d + 1):                                      #вывод диапозона чисел по горизонтали с расстоянием табуляции
        print(j, end='\t')
    print()                                                        #Перевод строки
    for i in range(a, b + 1):                                      #вывод диапозона чисел по вертикали с расстоянием табуляции
        print(i, end='\t')
        for j in range(c, d + 1):                                  #Прохождение по вложенному массиву и вывод результата умножения строки на колонку
            print(i * j, end='\t')
        print()                                                    #Перевод строки
    # ...task 13
    
    # task 14...
    n = int(input('Введите размер матрицы: '))
    a = [[0 for j in range(n)] for i in range(n)]
    x = 0
    for j in range(n):
        x += 1
        a[0][j] = x
    i = 0
    j = n - 1
    n -= 1
    while len(a)**2 != x:
        for k in range(n):
            i += 1
            x += 1
            a[i][j] = x
        for k in range(n):
            j -= 1
            x += 1
            a[i][j] = x
        for k in range(n-1):
            i -= 1
            x += 1
            a[i][j] = x
        for k in range(n-1):
            j += 1
            x += 1
            a[i][j] = x
        n -= 2
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end='\t')
        print()
    #...task 14

    # task 15...
    messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно')
    time.sleep(10)
    messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно')
    #...task 15

    # task 16...
    window = Tk()
    window.title('Useful Python')
    window.geometry('400x100')
    lbl = Label(window, text="Вы долго смотрели в монитор, теперь посмотрите в окно")
    lbl.pack()
    btn = Button(window, text="Retry", width=10,
                 command=retrywindow)
    btn.pack(side=LEFT)
    btn = Button(window, text="Quit", width=10,
                 command=window.destroy)
    btn.pack(side=RIGHT)
    window.mainloop()
    # ...task 16
