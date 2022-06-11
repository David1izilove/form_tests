from faker import Faker


fake = Faker()


def fake_name():
    return fake.name()


def fake_email():
    return fake.email()


def fake_text():
    return fake.text()
