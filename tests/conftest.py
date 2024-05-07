import pytest

from src.financial_wallet import FinancialWallet
from src.operation import Operation


@pytest.fixture
def financial_wallet():
    my_wallet = FinancialWallet()
    return my_wallet


@pytest.fixture
def operation():
    operation = Operation('2024-05-02', 'Расход', '3000', 'Покупка продуктов')
    return operation
