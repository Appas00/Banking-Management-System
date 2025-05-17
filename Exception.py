class AccountAlreadyExisted(Exception):
    pass

class PasswordIncorrectException(Exception):
    pass

class AccountNotFound (Exception):
    pass

class NotLoggedIn (Exception):
    pass

class InsuffientBalanceException (Exception):
    pass