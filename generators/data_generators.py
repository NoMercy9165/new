import random
from faker import Faker


def generate_russian_passport():
    series = random.randint(10000, 99999)
    number = random.randint(10000, 99999)
    passport = f"{series}{number}"
    return passport


def generate_passenger_data():
    fake = Faker('ru_RU')
    gender = fake.random_element(['m', 'f'])

    if gender == 'm':
        firstname = fake.first_name_male()
        middlename = firstname + 'ович'
    else:
        firstname = fake.first_name_female()
        middlename = firstname + 'овна'

    birth_date = fake.date_of_birth(minimum_age=20, maximum_age=70)

    return {
        'passport': generate_russian_passport(),
        'lastname': fake.last_name(),
        'firstname': firstname,
        'middlename': middlename,
        'birth_date': {
            'day': str(birth_date.day).zfill(2),
            'month': fake.month_name(),
            'year': str(birth_date.year)
        },
        'gender': gender
    }


def generate_random_credentials():
    fake = Faker()
    username = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return {
        "username": username,
        "password": password
    }
