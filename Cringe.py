num = 1
print('1.Вывести квадрат числа\n'
      '2.По двум заданным числам проверять является ли первое квадратом второго\n'
      '3.Даны два числа. Показать большее и меньшее число\n'
      '4.По заданному номеру дня недели вывести его название\n'
      '5.Найти максимальное из трех чисел\n'
      '6.Написать программу вычисления значения функции y = f(a)\n'
      '7.Выяснить является ли число чётным\n'
      '8.Показать последнюю цифру трёхзначного числа\n'
      '9.Показать вторую цифру трёхзначного числа\n'
      '10.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа\n'
      '11.Удалить вторую цифру трёхзначного числа\n'
      '12.Выяснить, кратно ли число заданному, если нет, вывести остаток.\n'
      '13.Найти третью цифру числа или сообщить, что её нет\n'
      '0.Завершить программу')
while num != 0:
    print('Введите номер программы')
    num = int(input())
    if num == 1:
        print('1.Вывести квадрат числа\n')
        print('Введите число')
        a = int(input())
        b = a * a
        print('Квадрат введенного число=', b)
    if num == 2:
        print('2.По двум заданным числам проверять является ли первое квадратом второго\n')
        print('Введите первое число')
        a = int(input())
        print('Введите второе число')
        b = int(input())
        if b == a * a:
            print('Второе число является квадратом второго')
        else:
            print('Не является.')
    if num == 3:
        print('3.Даны два числа. Показать большее и меньшее число\n')
        print('Введите первое число')
        a = int(input())
        print('Введите второе число')
        b = int(input())
        if a > b:
            print('Большее число=', a)
            print('Меньшее число=', b)
        if a < b:
            print('Большее число=', b)
            print('Меньшее число=', a)
        if a == b:
            print('Числа равны')
    if num == 4:
        print('4.По заданному номеру дня недели вывести его название\n')
        a = int(input())
        if a == 1:
            print('Понедельник')
        if a == 2:
            print('Вторник')
        if a == 3:
            print('Среда')
        if a == 4:
            print('Четверг')
        if a == 5:
            print('Пятница')
        if a == 6:
            print('Суббота')
        if a == 7:
            print('Воскресенье')
    if num == 5:
        print('5.Найти максимальное из трех чисел\n')
        a = int(input())
        b = int(input())
        c = int(input())
        max = a
        if b >= max:
            max = b
        if c >= max:
            max = c
        print('Большее число=', max)
    if num == 6:
        print('6.Написать программу вычисления значения функции y = f(a)\n')
        print('Введите число')
        a = int(input())
        y = 3 * a * a * a + (a ** 0.5)
        print('Значение функции=', y)
    if num == 7:
        print('7.Выяснить является ли число чётным\n')
        print('Введите число')
        a = int(input())
        if a % 2 == 0:
            print('Число чётное')
        else:
            print('Число нечётное')
    if num == 8:
        print('8.Показать последнюю цифру трёхзначного числа\n')
        print('Введите трёхзначное число')
        a = int(input())
        b = a % 100
        print('Последняя цифра трёхзначного числа=', b)
    if num == 9:
        print('9.Показать вторую цифру трёхзначного числа\n')
        print('Введите трёхзначное число')
        a = int(input())
        b = (a % 10) // 10
        print('Вторая цифра трёхзначного числа=', b)
    if num == 10:
        print('10.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа\n')
        print('Введите число в промежутке [10..99]')
        a = int(input())
        if (a >= 10) and (a <= 99):
            b = a % 10
            c = a // 10
            if b > c:
                print('Большая цифра=', b)
                print('Меньшая цифра=', c)
            if b < c:
                print('Большая цифра=', c)
                print('Меньшая цифра=', b)
            if b == c:
                print('Цифры равны')
        else:
            print('В промежутке [10..99]')
    if num == 11:
        print('11.Удалить вторую цифру трёхзначного числа\n')
        print('Введите трёхзначное число')
        a = int(input())
        b = str(a % 10)
        c = str(a // 100)
        txt = int(c + b)
        print('Полученное число=', txt)
    if num == 12:
        print('12.Выяснить, кратно ли число заданному, если нет, вывести остаток.\n')
        print('Введите число')
        a = int(input())
        print('Введите кратность числа')
        b = int(input())
        if a % b == 0:
            print('Число кратно')
        else:
            c = a % b
            print('Остаток=', c)
    if num == 13:
        print('13.Найти третью цифру числа или сообщить, что её нет\n')
        print('Введите число')
        a = int(input())
        while a > 1000:
            a //= 10
        print(a % 10)
