import re
import datetime

class Validation():

    patternEmail = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9._\?*]{0,254}@[a-zA-Z0-9-]{1,63}+(\.[a-z0-9-]{2,7})+$"

    def ValidateEmail(email):
        return bool(re.match(Validation.patternEmail, email))
    
    def ValidateUserName(userName):
        return len(userName) > 3 and len(userName) < 64
    
    def ValidateDate(date_str):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return date <= datetime.now().date()
        except ValueError:
            return False

    