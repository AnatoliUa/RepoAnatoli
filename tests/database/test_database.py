import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection(db_object):
    db_object.test_connection()

@pytest.mark.database
def test_check_all_users(db_object):
    users = db_object.get_all_users()
    print(users)

@pytest.mark.database
def test_get_check_user_Sergii(db_object):
    user = db_object.get_user_address_by_name('Sergii')
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"

@pytest.mark.database
def test_product_qnt_update(db_object):
    db_object.update_product_qnt_by_id(1, 25)
    water_qnt = db_object.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(db_object, db_del_rec_after_test):
    db_object.insert_product(4, "печиво", "солодке", 30)
    cookie_qnt = db_object.select_product_qnt_by_id(4)
    print(cookie_qnt)
    assert cookie_qnt[0][0]

@pytest.mark.database
def test_product_delete(db_object):
    db_object.insert_product(99, "тестові", "дані", 999)
    db_object.delete_product_by_id(99)
    qnt = db_object.select_product_qnt_by_id(99)
    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(db_object):
    orders = db_object.get_detailed_orders()
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"