import pytest
import mock
import builtins
from Task1.main import find_autor_document, find_shelf_document, add_new_shell, del_shell


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


fixture_find_autor_document = [('11-2', 'Геннадий Покемонов'), ('10006', 'Аристарх Павлов'), ('100500', None)]
fixture_find_shelf_document = [('10006', ('2', '10006')), ('100500', None), ('11-2', ('1', '11-2'))]
fixture_add_new_shell = [('1', 'Такая полка уже есть!'), ('5', 'Добавлена полка')]


@pytest.mark.parametrize('data,answer', fixture_find_autor_document)
def test_find_autor_document(data, answer):
    assert find_autor_document(data, documents) == answer


@pytest.mark.parametrize('data,answer', fixture_find_shelf_document)
def test_find_shelf_document(data, answer):
    assert find_shelf_document(data, directories) == answer


@pytest.mark.parametrize('data,answer', fixture_add_new_shell)
def test_add_new_shell(data, answer):
    with mock.patch.object(builtins, 'input', lambda _: data):
        assert add_new_shell(data, directories) == answer


def test_del_shell():
    with mock.patch.object(builtins, 'input', lambda _: '3'):
        assert del_shell(directories) == 'Полка удалена'