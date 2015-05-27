import re

word_regx = "([A-Za-z0-9]+\-)?[A-Za-z]+"


def binary(text):
    return bool(re.search(r"^[10]+$", text))


def binary_even(text):
    if binary(text):
        return bool(re.search(r"0$", text))
    else:
        return False


def hex(text):
    return bool(re.search(r"^[0-9A-Fa-f]+$", text))


def word(text):
    p = re.compile("^"+word_regx+"$")
    return bool(re.search(p, text))


def words(text, count=None):
    if count is None:
        p = re.compile("^("+word_regx+"\s?)+$")
    else:
        p = re.compile("^"+word_regx+"(\s"+word_regx+"){"+str(count-1)+"}$")
    return bool(re.search(p, text))


def phone_number(text):
    return bool(re.search(r"(\d{3}\)?)?[\s\.]?\d{3}[\s\-\.]?\d{4}", text))


def zipcode(text):
    return bool(re.search(r"^[0-9]{5}(\-[0-9]{4})?$", text))


def money(text):
    return bool(re.search(r"^\$(\d{1,3})(\,?\d{3})*(\.\d{2})?$", text))


def date(text):
    return bool(re.search(r"\d+[/\-]\d+[/\-]\d+", text))


if __name__ == '__main__':
    print(binary("0"))
    print(binary("911"))
    print(" ")
    print(binary_even("10"))
    print(hex("CAFE"))
    print(" word")
    print(word("hello"))
    print(" phone")
    print(phone_number("828 297-2120"))
    print(" word")
    print(word("12"))
    print(words("hello world"))
    print(" ")
    print(" money")
    print(money("$12,34"))
