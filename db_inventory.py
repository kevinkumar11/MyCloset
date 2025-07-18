import sqlite3
import os

class InventoryDB:
    def __init__(self, db_name='clothing_inventory.db'):
        # Get the path of the current script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Join with your database path
        db_path = os.path.join(base_dir, "db", db_name)        

        self.conn = sqlite3.connect(db_path)
        print(f"Connecting to DB at: {db_path}")
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "inventory" (
            "id" INTEGER,
            "description"	TEXT,
            "type"	TEXT NOT NULL,
            "brand"	TEXT NOT NULL,
            "purchase_date"	TEXT NOT NULL,
            "sold_date"	TEXT NOT NULL,
            "price"	REAL NOT NULL,
            "size"	TEXT,
            "name"	TEXT,
            "picture"	BLOB,
            PRIMARY KEY("id" AUTOINCREMENT)
        )        
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_item(self, name, description, brand, category_type, price, purchase_date, sold_date, size, picture):
        #query = 'INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)'
        query = 'INSERT INTO inventory (name, description, brand, type, price, purchase_date, sold_date size, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'

        self.conn.execute(query, (name, description, brand, category_type, price, purchase_date, sold_date, size, picture))
        self.conn.commit()

    def fetch_items(self):
        query = 'SELECT * FROM inventory'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_item(self, item_id, name=None, quantity=None, price=None):
        fields = []
        values = []
        if name is not None:
            fields.append('name = ?')
            values.append(name)
        if quantity is not None:
            fields.append('quantity = ?')
            values.append(quantity)
        if price is not None:
            fields.append('price = ?')
            values.append(price)
        values.append(item_id)
        query = f'UPDATE inventory SET {", ".join(fields)} WHERE id = ?'
        self.conn.execute(query, values)
        self.conn.commit()

    def delete_item(self, item_id):
        query = 'DELETE FROM inventory WHERE id = ?'
        self.conn.execute(query, (item_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()