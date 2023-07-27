import sqlite3

class Database():
     
    def __init__(self):
        self.connection = sqlite3.connect(r'become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQlite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT INTO products (id, name, description, quantity) VALUES({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"    
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def next_id(self, table, id_field):
        """Generate next temporal id key either numerical or text"""
        query = f"SELECT Max(id) FROM {table}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        query2 = f"SELECT typeof({id_field}) FROM  {table}"
        self.cursor.execute(query2)
        record2 = self.cursor.fetchall()
        if record2[0][0] == 'integer':        #if key is numerical
            nextid = record[0][0] + 1
        elif record2[0][0] == 'text':         #if key is text
            nextid = "@#$%"
        return nextid
    
    def insert_record(self, table, fields_tuple, values_tuple):
        """Insert new record into table."""
        fields = ", ".join(fields_tuple)
        print(fields)
        values = ", ".join(values_tuple)
        print(values)
        query = f"INSERT INTO {table} ({fields}) VALUES({values})"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def delete_record(self, table, temp_id):
        """Delete record by id value"""
        query = f"DELETE FROM {table} WHERE id = {temp_id}"
        self.cursor.execute(query)
        self.connection.commit()
        
    def check_rel_fields(self, table1, field1, table2, field2):
        """Select records from table2 where field2 value don't match any value of field1 in table1"""
        query = f"SELECT Count(*) FROM (SELECT {field2} FROM {table2} WHERE {field2} NOT IN (SELECT DISTINCT {field1} FROM {table1}))"
        self.cursor.execute(query)
        cnt = self.cursor.fetchall()
        return cnt