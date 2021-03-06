import unittest
from user import User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviour"""

    def setUp(self):
        '''This will run before each test to check whether the classes are  instantiated correctly.'''
        self.new_user = User("NewUser", "12345")

    def test_init(self):
        '''Test to ensure that the object is initialized properly'''
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        '''Method that tests wether a user credentials are saved '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()