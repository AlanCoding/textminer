import re

word_regx = "([A-Za-z0-9]+\-)?[A-Za-z]+"


def words(text):
    p = re.compile(r"\b(?:\w*\-)?[A-Za-z]+\b")
    a_list = re.findall(p, text)
    if len(a_list) == 0:
        return None
    else:
        return a_list


def phone_number(text):
    d = {}
    a_list = re.findall(r"(\d{4}$|\d{3})", text)
    if len(a_list[-1]) < 4:
        return None
    if len(a_list) == 2:
        d["number"] = a_list[0]+"-"+a_list[1]
        return d
    elif len(a_list) == 3:
        d["area_code"] = a_list[0]
        d["number"] = a_list[1]+"-"+a_list[2]
        return d
    else:
        return None


def money(text):
    a_list = re.findall(r"(\$|\.|\d+|\d{2}$)", text)
    print(a_list)
    if "$" not in a_list:
        return None
    d = {}
    d["currency"] = a_list.pop(0)
    if "." in a_list:
        dot = a_list.index(".")
        a_list.remove(".")
        if len(a_list[dot]) != 2:
            return None
        cents = int(a_list[dot])
        a_list.pop(dot)
    else:
        cents = 0
    the_sum = cents/100.0
    power = 1
    if len(a_list) == 0:
        return None
    while len(a_list) > 0:
        n = len(a_list)-1
        p = len(a_list[n])
        if not a_list[n].isdigit():
            return None
        if n > 0 and len(a_list[n]) < 3:
            return None
        the_sum = the_sum + int(a_list[n])*power
        power *= 10**p
        a_list.pop(n)
    d["amount"] = the_sum
    return d


def zipcode(text):
    regex = re.compile(r"^(?P<zip>\d{5})(\-(?P<plus4>\d{4}))?$")

    match = regex.search(text)
    if match is None:
        return None
    a_dict = match.groupdict()
    return a_dict


def date(text):
    if bool(re.search(r"\-", text)):
        regex = re.compile(r"(?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2})")
    elif bool(re.search(r"/", text)):
        regex = re.compile(r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})")
    else:
        return None
    match = regex.search(text)
    if match is None:
        return None
    a_dict = match.groupdict()
    for tag in a_dict:
        a_dict[tag] = int(a_dict[tag])
    return a_dict


if __name__ == '__main__':
    text = "mary had a little 18-wheeler lamb"
    print(words(text))
    print(" ")
    print(phone_number("919-555-1212"))
    print(phone_number("555-1212"))

    print(" ")
    print(" money")
    print(money("$1000"))
    print(" ")
    print(" zip")
    print(zipcode("28692"))
    print(" ")
    print(" date")
    print(date("1976-09-40"))
