import re


def phone_numbers(text):
    return re.findall(r"\(\d{3}\)\s\d{3}-\d{4}", text)


def emails(text):
    return re.findall(r"[A-Za-z0-9.]+@\w+.\w+", text)


if __name__ == '__main__':
    text = "hello mister@gmail.com"
    print(text)
    print(emails(text))

    text2 = """Veggies  amaranth@gmail.com  cucumber.earthnut@pea.net"""
    print(emails(text2))

    text3 = """Dear  (454) 999-1212. at (919) 123-4569 at your convenience."""
    print(phone_numbers(text3))
