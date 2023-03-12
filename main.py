from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test_is_correct_mobile_phone_number_ru():
    test_data = (
        ('+79674129902', True),
        ('89674129902', True),
        ('+7(967)4129902', True),
        ('8(967)4129902', True),
        ('+7 967 412-99-02', True),
        ('8 967 412-99-02', True),
        ('+7 (967) 412-99-02', True),
        ('8 (967) 412-99-02', True),

        ('+796741299020', False),
        ('896741299020', False),
        ('+7(967)41299020', False),
        ('8(967)41299020', False),
        ('+7 967 412-99-020', False),
        ('8 967 412-99-020', False),
        ('+7 (967) 412-99-020', False),
        ('8 (967) 412-99-020', False),

        ('+796(7412)9902', False),
        ('89)67412990(2', False),
        ('+7)967(4129902', False),
        ('8()9674129902', False),
        ('+7 9(67 412-99)-02', False),
        ('8 9)67 412-99(-02', False),
        ('+7 (9)67) 412-(99-02', False),
        ('8 (96(7) 412-99-)02', False),

        ('+19674129902', False),
        ('29674129902', False),
        ('+3(967)4129902', False),
        ('4(967)4129902', False),
        ('+5 967 412-99-02', False),
        ('6 967 412-99-02', False),
        ('+9 (967) 412-99-02', False),
        ('0 (967) 412-99-02', False)
    )

    for input_data, correct_output_data in test_data:
        if is_correct_mobile_phone_number_ru(input_data) != correct_output_data:
            return False
    return True


print('YES' if test_is_correct_mobile_phone_number_ru() else 'NO')
