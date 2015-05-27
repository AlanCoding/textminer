import re

def phone_numbers(text):
    return re.findall(r"\(\d{3}\)\s\d{3}-\d{4}", text)



def emails(text):
    return re.findall(r"[A-Za-z0-9.]+@\w+.\w+", text)


if __name__ == '__main__':
    text = "hello mister@gmail.com"

    print(text)

    print(emails(text))

    text2 = """Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi
    welsh onion daikon amaranth@gmail.com tatsoi tomatillo azuki bean garlic.

    Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
    tatsoi pea@sprouts.org fava bean collard greens dandelion okra wakame
    tomato. Dandelion cucumber.earthnut@pea.net peanut soko zucchini."""

    print(emails(text2))

    text3 = """Dear Mr. Davis,

I got to know of your company through our mutual friend Fiona Williams and the
training you offer to graduate students in Advertising.

I am a graduate student of Mass Communications with specialization in
Advertising.  I am currently pursuing the last year of my course.
I would very much like to see firsthand the work environment in an advertising
agency.

If you would like a reference, my advisor can be reached at (454) 999-1212.

You can contact me at (919) 123-4569 at your convenience."""

    print(phone_numbers(text3))
