import random

# функция определяющая длину последовательности
def posl_func(long_posl:int):
    pasword = ''
    for i in range(long_posl):
        pasword = chr(random.randint(34, 123)) + pasword
    return pasword

def posl_func_telefon(long_posl_telefon: int):
    pasword1 = ''
    for i in range(long_posl_telefon):
        pasword1 = chr(random.randint(48, 57)) + pasword1
    return pasword1


# код программы меню
while True:
    print('Если хотите пароль с неограниченными символами введите 1')
    print('Если хотите пароль с цифрами введите 2')

    f = int(input())

    if f == 1:
        p1 = int(input('укажите длинну'))
        print('Ваш пароль', ':', posl_func(p1))
    elif f == 2:
        p1 = int(input('укажите длинну'))
        print('Ваш пароль', ':', posl_func_telefon(p1))
    elif f != 1 or f != 2:
        print('Error')



