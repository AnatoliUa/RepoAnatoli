import pytest
from modules.ui.page_objects.sign_in_page import SignInPage, SignInRozetka, SignUpBookYe, BuyABook, SignInAmazon

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("onetwo.@three", "wrongpassword")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close() 

@pytest.mark.myui
def test_check_rozetka():
    """Check wrong user sign in Rozetka"""
    sign_in_page = SignInRozetka()
    sign_in_page.go_to()
    assert sign_in_page.try_login("onetwo.@three", "wrongpassword") == True
    sign_in_page.close()

@pytest.mark.myui
def test_check_bookye():
    """Check wrong signup Bookye"""
    sign_in_page = SignUpBookYe()
    sign_in_page.go_to()
    assert sign_in_page.try_signup("Степан Карафолька", "basura@online.ua", "970000001", "12345678") == True
    sign_in_page.close()

@pytest.mark.myui
def test_check_bookye():
    """Check book purchase"""
    bookye_page = BuyABook()
    bookye_page.go_to()
    bookye_page.buy_first_item()
    assert bookye_page.buy_first_item() == True
    bookye_page.close()

@pytest.mark.myui
def test_check_amazon():
    """Check wrong user email Amazon"""
    sign_in_page = SignInAmazon()
    sign_in_page.go_to()
    assert sign_in_page.try_login("onetwo.@three") == True
    sign_in_page.close()