import unittest
import Task2.YandexDiscCrDir


token_ya = ''


class Testfunction(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp ===> STARTTEST')

    def test_unitest_make_dir(self):
        example_t = Task2.YandexDiscCrDir.YaDisc(token_ya)
        result = example_t.create_directory('test_dir')
        self.assertEqual(result.status_code, 201)

    def tearDown(self) -> None:
        print('tearDown ===> STOPTEST')