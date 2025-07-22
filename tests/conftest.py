import pytest
from model import Contact, PhoneBook


@pytest.fixture
def test_contact():
    return Contact("Карпин", "Валерий",
                   "+70008881122", "Комментарий для контакта")


@pytest.fixture
def test_contact1():
    return Contact("Фамилия1", "Имя1",
                   "+70008881121", "Комментарий для контакта1")


@pytest.fixture
def test_contact2():
    return Contact("Фамилия2", "Имя2",
                   "+70008881122", "Комментарий для контакта2")


@pytest.fixture
def test_contact3():
    return Contact("Фамилия3", "Имя3",
                   "+70008881123", "Комментарий для контакта3")


@pytest.fixture
def test_pb():
    return PhoneBook('test.json')
# @pytest.fixture
# def sample_Contact(list_contact):  # scope='module'/'function'/'session'/'class'
#     return Contact.from_list(list_contact)


@pytest.fixture
def test_messages():
    return [
        'Введите фамилию:',
        'Введите имя:',
        'Введите телефон:',
        'Введите комментарий:',

    ]
