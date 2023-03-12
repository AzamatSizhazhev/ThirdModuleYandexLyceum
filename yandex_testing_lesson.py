def strip_punctuation_ru(s):
    punctuations = '''!()—[]{};:'"\,<>./?@#$%^&*_~'''

    new_s = ""
    for char in s:
        if char in punctuations:
            new_s += ' '
        else:
            new_s += char

    new_s = new_s.replace(" - ", " ")
    return " ".join(new_s.split())
