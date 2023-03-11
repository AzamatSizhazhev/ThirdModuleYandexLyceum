# Первый вариант функции
# def reverse(s):
#     pass

# Второй вариант функции
# def reverse(s):
#     r = ''
#     for c in s:
#         r = c + r
#     return r

# Третий вариант функции
# def reverse(s):
#     if type(s) != str:
#         raise TypeError()
#     r = ''
#     for c in s:
#         r = c + r
#     return r

# Четвертый вариант функции
# def reverse(s):
#     if type(s) != str:
#         raise TypeError()
#     if len(s) == 1:
#         return s
#     return s[-1] + reverse(s[:-1])

# Пятый вариант функции
# def reverse(s):
#     if type(s) != str:
#         raise TypeError()
#     if len(s) <= 0:
#         return s
#     return s[-1] + reverse(s[:-1])

# Шестой вариант функции
def reverse(s):
    if type(s) != str:
        raise TypeError()
    return s[::-1]

# Седьмой вариант функции
# def reverse(s):
#     return 1 / 0


def test_reverse():
    test_data = (
        (42, None),
        (['a', 'b', 'c'], None),
        ('', ''),
        ('aba', 'aba'),
        ('a', 'a'),
        ('abc', 'cba')
    )

    for input_s, correct_output_s in test_data:
        try:
            output_s = reverse(input_s)
        except TypeError as E:
            if correct_output_s is not None:
                continue
            if type(input_s) == str:
                print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
                return False
        except Exception as E:
            print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
            return False
        else:
            if output_s != correct_output_s:
                print(f'Ошибка! reverse({input_s}) равно {output_s} вместо "{correct_output_s}"')
                return False

    print('Все тесты пройдены успешно!')
    return True


test_reverse()
