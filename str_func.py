def capital_letters(string_of_words):
    """
    Делает все символы заглавными
    :param string_of_words: строка
    :return: строка со всеми заглавными символами
    """
    new_string = string_of_words.upper()
    return new_string


def capital_first_letter(string_of_words):
    """
    Делает каждую первую букву слова заглавной
    :param string_of_words: строка
    :return: строка, где каждая первая буква слова, - заглавная
    """
    new_string = string_of_words.title()
    return new_string
