from yandex_testing_lesson import is_palindrome


def test_is_palindrome():
    test_data = (
        ('', True),
        ('a', True),
        ('aa', True),
        ('Aa', False),
        ('fg', False),
        ('ada', True),
        ('Ada', False),
        ('AdA', True),
        ('uia', False),
        ('asdfdsa', True),
        ('ipwubtg', False),
        ('AsDfDsA', True)
    )

    for input_data, correct_output_data in test_data:
        output_data = is_palindrome(input_data)
        if output_data != correct_output_data:
            return 'NO'

    return 'YES'


print(test_is_palindrome())
