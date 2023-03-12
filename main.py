from yandex_testing_lesson import is_prime


def test_is_palindrome():
    test_data = (('asdasd', None),
                 (-1, None),
                 (2, True),
                 (11, True),
                 (4, False),
                 (128736129873682163817632, False),
                 (0, None),
                 (1, None))

    for input_data, correct_output_data in test_data:
        try:
            if is_prime(input_data) != correct_output_data:
                return 'NO'
        except TypeError:
            if type(input_data) == int:
                return 'NO'
        except ValueError:
            if input_data > 1:
                'NO'
        else:
            return 'YES'


print(test_is_palindrome())
