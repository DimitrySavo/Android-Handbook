from ValidationHelper import Validation
import unittest


mails_correct = ["testMail1@mail.ru",
                 "user37717@st.guap.ru",
                 "sadas@gmail.com",
                 "asdsd@email.ltp.ad",
                 "asds_.d@mail.com",
                 "asdsa?*d@gmail.com",
                 "g.@gmail.com"]
mails_uncorrect = ["",
                   " ",
                   "2",
                   "sad@"
                   "asd",
                   "@gmail.com",
                   "sadsd @ asd.sd",
                   "@.ru",
                   "asdsd@mail",
                   "asdsd@mail.s",
                   "asdsd@mail.ssad.s",
                   ("d"*300)+"@gmail.com",
                   "asdsd@dsad.asdsasdasdsd",
                   "asdsad@gmail..com"]

class MailTest(unittest.TestCase):
    def test_T_mail(self):
        for mail in mails_correct:
            self.assertTrue(Validation.ValidateEmail(mail))
    def test_F_mail(self):
        for mail in mails_uncorrect:
            self.assertFalse(Validation.ValidateEmail(mail))


if __name__ == '__main__':
    unittest.main()