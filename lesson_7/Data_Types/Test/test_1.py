from lesson_7.Data_Types.Pages.Mainpage import Mainpage
from lesson_7.Data_Types.Pages.Datafields import DataField


def test_assertion(chrome_browser):
    main_page = Mainpage(chrome_browser)
    main_page.find_fields()
    main_page.filling_in_the_fields()
    main_page.click_submit_button()

    data_field = DataField(chrome_browser)
    data_field.find_fields()
    data_field.get_class_first_name()
    data_field.get_class_last_name()
    data_field.get_class_address()
    data_field.get_class_phone()
    data_field.get_class_zipcode()
    data_field.get_class_city()
    data_field.get_class_country()
    data_field.get_class_job_position()
    data_field.get_class_company()
    
    assert "success" in data_field.get_class_first_name()
    assert "success" in data_field.get_class_last_name()
    assert "success" in data_field.get_class_address()
    assert "success" in data_field.get_class_phone()
    assert "danger" in data_field.get_class_zipcode()
    assert "success" in data_field.get_class_city()
    assert "success" in data_field.get_class_country()
    assert "success" in data_field.get_class_job_position()
    assert "success" in data_field.get_class_company()
