from yandex_testing_lesson import strip_punctuation_ru


def test_strip_punctuation_ru():
    test_data = (
        ('Ваш коллега написал функцию, которая удаляет знаки препинания из передаваемой в нее строки',
         'Ваш коллега написал функцию которая удаляет знаки препинания из передаваемой в нее строки'),
        ('Подсказка - кое-какие слова в русском языке состоят не только из букв, и такое слово есть в этой фразе.',
         'Подсказка кое-какие слова в русском языке состоят не только из букв и такое слово есть в этой фразе'),
        ('''!()—[]{};:'"\,<>./?@#$%^&*_~''', '')
    )

    for input_data, correct_output_data in test_data:
        if strip_punctuation_ru(input_data) != correct_output_data:
            return False
    return True


print('YES' if test_strip_punctuation_ru() else 'NO')
