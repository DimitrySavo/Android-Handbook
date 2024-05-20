from ValidationHelper import Validation
import unittest

review_correct = ["sadasd",
                    "123123",
                    "some text here"]
review_uncorrect = ["s",
                      "ban",
                      "devil",
                        "dumb",
                        "Dumb",
                        "DUMB"]

class UserNameTest(unittest.TestCase):
    def test_T_reviewText(self):
        for review in review_correct:
            self.assertTrue(Validation.ValidateReviewText(review))
    def test_F_reviewText(self):
        for review in review_uncorrect:
            self.assertFalse(Validation.ValidateReviewText(review))


if __name__ == '__main__':
    unittest.main()