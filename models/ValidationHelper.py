import re
from datetime import datetime

class Validation():

    patternEmail = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9._\?*]{0,254}@[a-zA-Z0-9-]{1,63}+(\.[a-z0-9-]{2,7})+$"
    patternTelephone = r"^(?:\+7|8)[(\- ]?\d{3}[)\- ]?\d{3}[- ]?\d{2}[- ]?\d{2}$"

    bannedWords = ["ban", "devil", "dumb"]

    delimiters = ['.', ' ']

    def ValidateEmail(email):
        return bool(re.match(Validation.patternEmail, email))
    
    def ValidateTelephone(telephoneNumber):
        return bool(re.match(Validation.patternTelephone, telephoneNumber))
    
    def ValidateUserName(userName):
        return len(userName) > 3 and len(userName) < 64
    @staticmethod
    def ValidateDate(date_str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return date <= datetime.now().date()
        except ValueError:
            return False


    def ValidateReviewText(inputText):
        isValidated = True

        inputArray = []

        inputStringForDelimiter = ""

        for delimiter in Validation.delimiters:
            inputStringForDelimiter = " ".join(inputText.split(delimiter))

        inputArray = inputStringForDelimiter.lower().split()

        if(len(inputText) < 5 or len(inputText) > 200):
            isValidated = False

        for word in Validation.bannedWords:
            if word in inputArray:
                isValidated = False

        return isValidated
    

    