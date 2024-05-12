from ValidationHelper import Validation
import unittest

userName_correct = ["sadasd",
                    "123123",
                    "EmilMamedov"]
userName_uncorrect = ["s",
                      "asd",
                      ("s"*66)]

class UserNameTest(unittest.TestCase):
    def test_T_userName(self):
        for userName in userName_correct:
            self.assertTrue(Validation.ValidateUserName(userName))
    def test_F_userName(self):
        for userName in userName_uncorrect:
            self.assertFalse(Validation.ValidateUserName(userName))


if __name__ == '__main__':
    unittest.main()