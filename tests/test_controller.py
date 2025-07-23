import pytest
from model import Contact, PhoneBook
from controller import *
from view import *
from text import *
from contextlib import nullcontext as does_not_raise
from customException import InvalidContactData, InvalidInputUser, FileOpenError


@pytest.mark.usefixtures("delete_file")
class TestController:
    @pytest.mark.parametrize(
        "pb, res, expectation",
        [
            (PhoneBook('test.json'), True, does_not_raise()),
            (PhoneBook('test_notfound.json'), False,
             pytest.raises(FileOpenError))
        ]
    )
    def test_open_file(self, pb, res, expectation):
        with expectation:
            result, error = pb.func_reading_from_file()
            assert result == res

    @pytest.mark.parametrize(
        "pb, res, expectation",
        [
            (PhoneBook('test.json'), True, does_not_raise()),
            (PhoneBook('test_notfound1.json'), True, does_not_raise()),
            # (PhoneBook('test_notfound.json'), True,
            #  pytest.raises(FileOpenError))
        ]
    )
    def test_save_file(self, pb, res, expectation):
        with expectation:
            result, error = pb.func_write_to_file()
            assert result == res

    def test_output_contacts(self, ):
        pass

    def test_create_contact(self, ):
        pass

    def test_find_contact(self, ):
        pass

    def test_change_contact(self, ):
        pass

    def test_del_contact(self, ):
        pass

    def test_close_program(self, ):
        pass
