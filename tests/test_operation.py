def test_operation_init(operation):
    assert operation.date == '2024-05-02'
    assert operation.category == 'Расход'
    assert operation.amount == 3000
    assert operation.description == 'Покупка продуктов'


def test_operation_str(operation):
    assert str(operation) == 'Дата: 2024-05-02\nКатегория: Расход\n Сумма: 3000\nОписание: Покупка продуктов\n'
