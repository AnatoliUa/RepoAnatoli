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
def test_product_insert(db_object):
    """Test insertion new record into table. products
    
    Delete inserted record after test
    """
    temp_id = db_object.next_id('products', 'id')
    db_object.insert_product(temp_id, "печиво", "солодке", 30)
    cookie_qnt = db_object.select_product_qnt_by_id(temp_id)
    assert cookie_qnt[0][0] == 30
    db_object.delete_product_by_id(temp_id)                    #cleaning

@pytest.mark.database
def test_product_delete(db_object):
    """Delete record in products by id
    
    Previously record is inserted
    """
    temp_id = db_object.next_id('products', 'id')
    db_object.insert_product(temp_id, "тестові", "дані", 999)
    db_object.delete_product_by_id(temp_id)
    qnt = db_object.select_product_qnt_by_id(temp_id)
    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(db_object):
    orders = db_object.get_detailed_orders()
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"

@pytest.mark.mydb
def test_record_insert(db_object):
    """Check insertion of new record into table."""
    thetable = 'products'
    temp_id = db_object.next_id(thetable, 'id')
    fields_tuple = ("id", "name", "description", "quantity")
    values_tuple = (str(temp_id), '"Something"', '"Somewhat"', str(1))
    db_object.insert_record(thetable, fields_tuple, values_tuple)
    new_qnt = db_object.select_product_qnt_by_id(temp_id)
    assert new_qnt[0][0] == 1
    db_object.delete_record(thetable, temp_id)                    #cleaning

@pytest.mark.mydb
def test_record_delete(db_object):
    """Delete record by id
    
    Previously record is inserted
    """
    thetable = 'products'
    temp_id = db_object.next_id(thetable, 'id')
    fields_tuple = ("id", "name", "description", "quantity")
    values_tuple = (str(temp_id), '"Something"', '"Somewhat"', str(1))
    db_object.insert_record(thetable, fields_tuple, values_tuple)    #insert record that will be deleted
    db_object.delete_record(thetable, temp_id)
    qnt = db_object.select_product_qnt_by_id(temp_id)
    assert len(qnt) == 0   

@pytest.mark.mydb
def test_integrity_products_check(db_object):
    """Check whether is not possible to insert records with same key field value, table products"""
    thetable = 'products'
    temp_id  = db_object.next_id(thetable, 'id')
    fields_tuple = ("id",)
    values_tuple = (str(temp_id),)
    db_object.insert_record(thetable, fields_tuple, values_tuple)    #insert temporal record
    try:
       db_object.insert_record(thetable, fields_tuple, values_tuple) #trying insert a twin record
    except:
        message = "Done correctly"
    else:
        message = "Error"
    db_object.delete_record(thetable, temp_id)                       #cleaning
    assert message == "Done correctly"

@pytest.mark.mydb
def test_integrity_customers_check(db_object):
    """Check whether is not possible to insert records with same key field value, table customers"""
    thetable = 'customers'
    temp_id  = db_object.next_id(thetable, 'id')
    fields_tuple = ("id",)
    values_tuple = (str(temp_id),)
    db_object.insert_record(thetable, fields_tuple, values_tuple)    #insert temporal record
    try:
       db_object.insert_record(thetable, fields_tuple, values_tuple) #trying insert a twin record
    except:
        message = "Done correctly"
    else:
        message = "Error"
    db_object.delete_record('products', temp_id)                       #cleaning
    assert message == "Done correctly"

@pytest.mark.mydb
def test_integrity_orders_check(db_object):
    """Check whether is not possible to insert records with same key field value, table customers"""
    thetable = 'orders'
    temp_id  = db_object.next_id(thetable, 'id')
    fields_tuple = ("id",)
    values_tuple = (str(temp_id),)
    db_object.insert_record(thetable, fields_tuple, values_tuple)    #insert temporal record
    try:
       db_object.insert_record(thetable, fields_tuple, values_tuple) #trying insert a twin record
    except:
        message = "Done correctly"
    else:
        message = "Error"
    db_object.delete_record('products', temp_id)                       #cleaning
    assert message == "Done correctly"

@pytest.mark.mydb
def test_non_existing_customer(db_object):
    """Check whether exists record in orders containing non existing customer"""
    cnt = db_object.check_rel_fields("customers", "id", "orders", "customer_id")
    assert cnt[0][0] == 0

@pytest.mark.mydb
def test_non_existing_product(db_object):
    """Check whether exists record in orders containing non existing product"""
    cnt = db_object.check_rel_fields("products", "id", "orders", "product_id")
    assert cnt[0][0] == 0    