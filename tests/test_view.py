import pytest
import text
from view import *
from customException import InvalidChoiceMenu, InvalidInputUser


def test_print_message_all(test_contact, capsys):

    print_message(str(test_contact))
    expected = '----------------------------------------\nФамилия: Карпин | Имя: Валерий | Телефон: +70008881122  | Kомментарий: Комментарий для контакта\n----------------------------------------\n'

    captured = capsys.readouterr()
    assert expected == captured.out


def test_input_user_data(test_messages):
    pass


def test_print_contacts():
    pass


def test_func_choice_open():
    pass


def test_show_menu():
    pass
