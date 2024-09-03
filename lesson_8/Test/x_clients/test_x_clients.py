import pytest
import requests
from lesson_8.Pages.Employee import Employer, Company


employer = Employer()
company = Company()

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

def test_get_company_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'string',
        'lastName': 'string',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        "birthdate": '2024-09-03T19:10:07.571Z',
        "isActive": 'true'
    }
    new_employer_id = (employer.add_new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()

    info = employer.get_info(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200

def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
        'id': 0,
        'firstName': 'string',
        'lastName': 'string',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        "birthdate": '2024-09-03T19:10:07.571Z',
        "isActive": 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['massage'] == 'Unauthorized'

def test_addemployer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['massage'] == 'Internal server error'

def test_get_employer():
    com_id = company.last_active_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)

def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as a:
        assert str(a) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as a:
        assert str(a) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_info_new_employers_missing_employer_id():
    try:
        employer.get_info()
    except TypeError as a:
        assert str(a) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
         'id': 0,
        'firstName': 'string',
        'lastName': 'string',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        "birthdate": '2024-09-03T19:10:07.571Z',
        "isActive": 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'string2',
        'email': 'test2@mail.ru',
        'url': 'url2',
        'phone': '12345',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    assert id == employer_changed.json()['id']
    assert (employer_changed.json()["email"]) == body_change_employer.get("email")

def test_employers_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as a:
        assert str(a) == "Employer.get_list() missing 3 required positional argument: 'token', 'employee_id', and 'body'"