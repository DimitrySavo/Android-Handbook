import re

class Validation:

    patternEmail = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9._\?*]{0,254}@[a-zA-Z0-9-]{1,63}+(\.[a-z0-9-]{2,7})+$"

    def ValidateEmail(self,email):
        return bool(re.match(self.patternEmail, email))