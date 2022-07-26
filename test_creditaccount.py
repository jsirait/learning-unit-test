from creditaccount import CreditAccount
from bankaccountimpl import BankAccountImpl
import pytest
from insufficientfunds import InsufficientFunds

class TestCreditAccount(object):
    def test_get_balance(self):
        openingBalance = 100
        parent = BankAccountImpl(openingBalance)
        subject = CreditAccount(parent)
        result = subject.get_balance()
        assert result == openingBalance

    def test_debit_negative(self):
        openingBalance = 100
        parent = BankAccountImpl(openingBalance)
        subject = CreditAccount(parent)
        with pytest.raises(InsufficientFunds):
            assert subject.debit(150)

    def test_debit_positive(self):
        openingBalance = 100
        parent = BankAccountImpl(openingBalance)
        subject = CreditAccount(parent)
        result = subject.debit(50)
        assert result == openingBalance-50

    def test_credit_positive(self):
        openingBalance = 100
        parent = BankAccountImpl(openingBalance)
        subject = CreditAccount(parent)
        result = subject.credit(50.5)
        assert result == openingBalance+50.5

    def test_credit_negative(self):
        openingBalance = 100
        parent = BankAccountImpl(openingBalance)
        subject = CreditAccount(parent)
        result = subject.credit(-100)
        assert result == openingBalance-100