from ValidationHelper import Validation
import unittest


telephone_correct = ["+79533487453", 
                     "89533487453", 
                     "8 953 348 74 53", 
                     "+7 953 348 74 53", 
                     "+7-953-348-74-53", 
                     "8-953-348-74-53",
                     "+7 9533487453",
                     "8 953348 74 53",
                     "+7(953)348-74-53"]
telephone_uncorrect = ["adf",
                       "+7s953348745",
                       "dasdsadsad",
                       "+795334874633",
                       "8sad213123",
                       "79533487453",
                       "8-953-34-74-53",
                       "8-953-34-74-53"]

class TelephoneTest(unittest.TestCase):
    def test_T_telephone(self):
        for telephone in telephone_correct:
            self.assertTrue(Validation.ValidateTelephone(telephone))
    def test_F_telephone(self):
        for telephone in telephone_uncorrect:
            self.assertFalse(Validation.ValidateTelephone(telephone))


if __name__ == '__main__':
    unittest.main()