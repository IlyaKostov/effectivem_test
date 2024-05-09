from unittest.mock import patch


def test_get_validated_amount_valid_input(validator):
    with patch('builtins.input', side_effect=['100', '25.75', '500']):
        assert validator.get_validated_amount() == 100
        assert validator.get_validated_amount() == 25.75
        assert validator.get_validated_amount() == 500


def test_get_validated_category_valid_input(validator):
    with patch('builtins.input', side_effect=['доход', 'расход']):
        assert validator.get_validated_category() == 'доход'
        assert validator.get_validated_category() == 'расход'


def test_get_validated_date_valid_input(validator):
    with patch('builtins.input', side_effect=['2024-05-03', '2023-12-31']):
        assert validator.get_validated_date() == '2024-05-03'
        assert validator.get_validated_date() == '2023-12-31'


def test_get_validated_search_key_valid_input(validator):
    with patch('builtins.input', side_effect=['дата']):
        categories = {'дата': 'date', 'категория': 'category', 'сумма': 'amount'}
        assert validator.get_validated_search_key(categories) == 'date'


def test_get_validated_id_input_valid_input(validator):
    with patch('builtins.input', side_effect=['1', '100', '42']):
        assert validator.get_validated_id_input() == 1
        assert validator.get_validated_id_input() == 100
        assert validator.get_validated_id_input() == 42


def test_get_validated_field_input_valid_input(validator):
    with patch('builtins.input', side_effect=['дата', 'категория', 'сумма', 'описание']):
        assert validator.get_validated_field_input() == 'date'
        assert validator.get_validated_field_input() == 'category'
        assert validator.get_validated_field_input() == 'amount'
        assert validator.get_validated_field_input() == 'description'
