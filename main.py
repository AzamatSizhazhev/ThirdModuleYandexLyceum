from yandex_testing_lesson import is_prime


def test_is_palindrome():
    test_data = (
        (2027, True),
        (2028, False),
        (2, True),
        (6, False),
        (27, False),
        (3, True),
        (4, False)
    )

    for input_data, correct_output_data in test_data:
        output_data = is_prime(input_data)
        if output_data != correct_output_data:
            return 'NO'

    return 'YES'


print(test_is_palindrome())
