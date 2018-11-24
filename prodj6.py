def len_error(x):
    """ Считает длину пароля """
    if len(pas) < 8:
        len_er = False
    else:
        len_er = True
    return len_er

def space_check(x):
    """ Считает количество пробелов """
    if pas.find(' ') == -1:
        space_error = True
    else:
        space_error = False
    return space_error

def spec_sim(x):
    """ Считает количество специальных символов """
    special_sim = 0
    for j in range(len(pas)):
        for i in '=-/*():;&$@+%#?!,.^':
            if i == pas[j]:
                special_sim += 1
    if special_sim > 0:
        special_sim = True
    else:
        special_sim = False
    return special_sim

def cap(x):
    """ Считает количество заглавных букв """
    capital_letter = 0
    for i in x:
        if i.isalpha():
            if i == i.upper():
                capital_letter += 1

    if capital_letter > 0:
        capital_letter = True
    else:
        capital_letter = False
    return capital_letter

def numberp(x):
    """ Считает количество чисел """
    numb = 0
    for y in pas:
        if y.isdigit():
            numb += 1

    if numb > 0:
        numb = True
    else:
        numb = False
    return numb

def main():
    """ Главная функция """
    right_parametr = len_error(pas) + space_check(pas) + spec_sim(pas) + numberp(pas)
    if cap(pas) > 0:
        right_parametr += 1
    print('password scores:', right_parametr,'/ 5')

if __name__ == '__main__':
    pas = input()
    len_er = None
    main()