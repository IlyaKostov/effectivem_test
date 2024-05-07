def test_add_operation(financial_wallet, operation):
    financial_wallet.add_operation(operation)
    assert financial_wallet.get_balance() == 'Баланс: 500, Доходы: 600, Расходы: 100'


# def test_remove_record(financial_wallet):
#     financial_wallet.remove_record()
#     assert financial_wallet.get_balance() == 'Баланс: 200, Доходы: 600, Расходы: 400'


def test_edit_operation(financial_wallet, operation):
    financial_wallet.edit_operation()
    assert financial_wallet.get_balance() == 'Баланс: 200, Доходы: 600, Расходы: 400'


def test_search_operation(financial_wallet):
    search_key = 'Дата'
    search_value = '2024-05-02'
    operation = financial_wallet.search_operation(search_key, search_value)
    assert operation == ''


def test_get_balance(financial_wallet):
    assert financial_wallet.get_balance() == 0
