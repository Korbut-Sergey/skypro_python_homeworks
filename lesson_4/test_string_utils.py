import pytest
from string_utils import StringUtils

utils = StringUtils()

### capitalize ###
# 1 Вариант написания

def test_capitalize():
    # Positive #
    assert utils.capitalize("сергей") == "Сергей"
    assert utils.capitalize("начало положено") == "Начало положено"
    assert utils.capitalize("371290") == "371290"
    # Negative #
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("04апреля2024") == "04апреля2024"

# 2 Вариант написания

@pytest.mark.parametrize("input_string, expected_output", [
    # Positive #
    ("сергей", "Сергей"),
    ("начало положено", "Начало положено"),
    ("371290", "371290"),
    # Negative #
    ("", ""),
    (" ", " "),
    ("04апреля2024", "04апреля2024"),
])
def test_capitalize(input_string, expected_output):
    assert utils.capitalize(input_string) == expected_output

### trim ###

def test_trim():
    # Positive #
    assert utils.trim("   сергей") == "сергей"
    assert utils.trim("   Начало положено   ") == "Начало положено   "
    assert utils.trim("  МЕСЯЦ  ") == "МЕСЯЦ  "
    # Negative #
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(371290) == "371290"

### to_list ###

@pytest.mark.parametrize("string, delimeter, result", [
    # Positive #
    ("Европа,Азия,Америка", ",", ["Европа", "Азия", "Америка"]),
    ("3,7,1,2,9,0", ",", ["3", "7", "1", "2", "9", "0"]),
    ("&-%-*-!", "-", ["&", "%", "*", "!"]),
    # Negative #
    ("3,7,1,2,9,0", None, ["3", "7", "1", "2", "9", "0"]),
    ("", None, []),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

### contains ###

@pytest.mark.parametrize("string, symbol, result", [
    # Positive #
    ("слово", "л", True),
    ("  пробел", "о", True),
    ("конец  ", "ц", True),
    ("Санкт-Петербург", "-", True),
    ("371290", "2", True),
    ("Главная", "г", False),
    ("буква", "ч", False),
    ("знак", "@", False),
    ("", "а", False),
    ("371290", "Б", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

### delete_symbol ###

@pytest.mark.parametrize("string, symbol, result", [
    # Positive #
    ("сергей", "с", "ергей"),
    ("Описание", "а", "Описние"),
    ("Название", "Н", "азвание"),
    ("371290", "7", "31290"),
    ("Начало Положено", " ", "НачалоПоложено"),
    ("Сергей", "а", "Сергей"),
    ("", "", ""),
    ("", "а", ""),
    ("Первый", "", "Первый"),
    ("Пробел", " ", "Пробел"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

### starts_with ###

@pytest.mark.parametrize("string, symbol, result", [
    # Positive #
    ("кнопка", "к", True),
    ("Город", "Г", True),
    ("Language", "L", True),
    ("Санта-Мария", "С", True),
    ("371290", "3", True),
    ("", "", True),
    ("Город", "г", False),
    ("кнопка", "К", False),
    ("", "%", False),
    ("City", "Ж", False),
    ("кошка", "с", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

### end_with ###

@pytest.mark.parametrize("string, symbol, result", [
    # Positive #
    ("кнопка", "а", True),
    ("ГороД", "Д", True),
    ("Language", "e", True),
    ("Санта-Мария", "я", True),
    ("371290", "0", True),
    ("", "", True),
    ("Пробел ", " ", True),
    ("Царь1", "1", True),
    ("Город", "Д", False),
    ("КнопкА", "а", False),
    ("", "?", False),
    ("City", "ф", False),
    ("кошка", "к", False),
])
def test_end_with (string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

### is_empty ###

@pytest.mark.parametrize("string, result", [
    # Positive #
    ("", True),
    (" ", True),
    ("  ", True),
    ("слово", False),
    (" впереди пробел", False),
    ("371290", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

### list_to_string ###

@pytest.mark.parametrize("lst, joiner, result", [
    # Positive #
    (["F", "B", "I"], ",", "F,B,I"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Santa", "Maria"], "-", "Santa-Maria"),
    (["Север", "Юг"], "Центр", "СеверЦентрЮг"),
    (["К", "Г", "Б"], "", "КГБ"),
    # Negative #
    ([], None, ""),
    ([], ",", ""),
    ([], "слово", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

### Конец документа ###