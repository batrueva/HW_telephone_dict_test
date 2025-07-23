import pytest
from model import Contact, PhoneBook


# @pytest.fixture
# def test_contact():
#     return Contact("Карпин", "Валерий",
#                    "+70008881122", "Комментарий для контакта")


# def test_get_random_num(mocker):
#     mocker.patch("random.randint", return_value=5)
#     result = get_random_num(1, 10)
#     assert result == 5


# def test_hello(capsys):
#     hello()
#     result = capsys.readouterr().out
#     assert "Hello" in result

class TestContact:
    def test_create_contact(self, test_contact):
        # test_contact = Contact("Карпин", "Валерий",
        #                        "+70008881122", "Комментарий для контакта")
        assert test_contact.first_name == "Карпин"
        assert test_contact.name == "Валерий"
        assert test_contact.phone == "+70008881122"
        assert test_contact.comment == "Комментарий для контакта"

    def test_contact_from_list(self, test_contact):
        test_list = ["Карпин", "Валерий",
                     "+70008881122", "Комментарий для контакта"]
        # test_contact1 = Contact("Карпин", "Валерий",
        #                         "+70008881122", "Комментарий для контакта")
        test_contact1 = test_contact
        test_contact2 = Contact.from_list(test_list)
        assert test_contact1.first_name == test_contact2.first_name
        assert test_contact1.name == test_contact2.name
        assert test_contact1.phone == test_contact2.phone
        assert test_contact1.comment == test_contact2.comment

    @pytest.mark.parametrize('phone, is_valid', [("+70008881122", True), ("70008881122", False), ("+7000888112", False),])
    def test_contact_is_valid_phone(self, phone, is_valid):
        result = Contact.is_valid_phone(phone)
        assert result is is_valid

    def test_contact_str(self, test_contact):

        result = str(test_contact)
        expected = 'Фамилия: Карпин | Имя: Валерий | Телефон: +70008881122  | Kомментарий: Комментарий для контакта'

        assert result == expected

    def test_contact_repr(self, test_contact):
        # test_contact = Contact("Карпин", "Валерий",
        #                        "+70008881122", "Комментарий для контакта")
        result = repr(test_contact)
        expected = 'Contact(first_name = (Карпин), name =(Валерий), phone = (+70008881122), comment = (Комментарий для контакта))'
        assert result == expected

    def test_contact_eq(self, test_contact):
        test_contact1 = Contact("Карпин", "Валерий1",
                                "+70008881122", "Комментарий для контакта1")
        test_contact2 = Contact("Карпин", "Валерий2",
                                "+70008881122", "Комментарий для контакта2")
        test_contact3 = Contact("Карпин3", "Валерий3",
                                "+70008881122", "Комментарий для контакта3")
        assert (test_contact1.first_name == test_contact2.first_name) and (
            test_contact1.phone == test_contact2.phone) is True

        assert (test_contact1.first_name != test_contact3.first_name) or (
            test_contact1.phone != test_contact3.phone) is False

    def test_contact_eq_false(self, test_pb, test_contact1):
        result = test_pb == test_contact1
        assert result == False

# ------------------------------------------------
# PB


class TestPhoneBook:
    def test_create_pb(self, test_pb, test_contact1, test_contact2, test_contact3):

        pass

    def test_pb_len(self, test_pb, test_contact1, test_contact2, test_contact3):

        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3

    def test_pb_getitem(self, test_pb, test_contact1, test_contact2, test_contact3):

        pass

    def test_pb_iter(self):
        pass

    def test_pb_next_id(self, test_contact1, test_contact2, test_contact3):
        test_pb1 = PhoneBook('test.json')
        test_pb2 = PhoneBook('test.json')
        test_pb2.func_create_contact(list(dict(test_contact1).values()))
        test_pb2.func_create_contact(list(dict(test_contact2).values()))
        test_pb2.func_create_contact(list(dict(test_contact3).values()))

        assert test_pb1.next_id() == 1
        assert test_pb2.next_id() == 4

    def test_PB_func_create_contact(self, test_pb, test_contact):
        test_pb.func_create_contact(list(dict(test_contact).values()))
        assert len(test_pb) == 1

    def test_PB_func_find_contact(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        result = test_pb.func_find_contact("Фамилия1")
        assert result["1"] == test_contact1

    def test_PB_func_change_contact(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3
        expected = "Фамилия_тест"
        result = test_pb.func_change_contact("1", [expected, "", "", ""])
        assert expected == result

    def test_PB_func_del_contact_successfully(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3
        result = test_pb.func_del_contact("1")
        assert len(test_pb) == 2
        assert result == (True, "Фамилия1")

    def test_PB_func_del_contact_error(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3
        result = test_pb.func_del_contact("4")
        assert len(test_pb) == 3
        assert result == (False, "'4'")

    def test_PB_func_reading_from_file(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3
        test_pb.func_write_to_file()
        assert test_pb.flag_change == False
        test_pb.func_reading_from_file()
        assert len(test_pb) == 3

    def test_PB_func_write_to_file(self, test_pb, test_contact1, test_contact2, test_contact3):
        test_pb.func_create_contact(list(dict(test_contact1).values()))
        test_pb.func_create_contact(list(dict(test_contact2).values()))
        test_pb.func_create_contact(list(dict(test_contact3).values()))
        assert len(test_pb) == 3
        test_pb.func_write_to_file()
        assert test_pb.flag_change == False


if __name__ == '__main__':
    pytest.main(['-vv'])
