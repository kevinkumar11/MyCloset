import sqlite3
import os
import pandas as pd

class InventoryDB:
    def __init__(self, db_name='clothing_inventory.db'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "db", db_name)
        self.conn = sqlite3.connect(db_path)
        print(f"Connecting to DB at: {db_path}")
        self.create_table()
        self.add_purchase_price_column()  # safely add purchase_price column if missing

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS "inventory" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "description" TEXT,
            "type" TEXT NOT NULL,
            "brand" TEXT NOT NULL,
            "purchase_date" TEXT NOT NULL,
            "sold_date" TEXT,
            "sold_price" REAL,
            "purchase_price" REAL,
            "size" TEXT,
            "name" TEXT,
            "picture" BLOB
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_purchase_price_column(self):
        # Add purchase_price column if not exists
        cursor = self.conn.execute("PRAGMA table_info(inventory)")
        columns = [col[1] for col in cursor.fetchall()]
        if "purchase_price" not in columns:
            try:
                self.conn.execute("ALTER TABLE inventory ADD COLUMN purchase_price REAL")
                self.conn.commit()
                print("Added purchase_price column to inventory table.")
            except sqlite3.OperationalError:
                # If column already exists or error happens, just pass
                pass

    def add_item(self, description, brand, category_type, purchase_price, sold_price, purchase_date, sold_date, size, picture):
        query = '''
        INSERT INTO inventory (description, brand, type, purchase_price, sold_price, purchase_date, sold_date, size, picture)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (description, brand, category_type, purchase_price, sold_price, purchase_date, sold_date, size, picture))
        self.conn.commit()

    def fetch_items(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, description, brand, type, purchase_price, sold_price, purchase_date, sold_date, size, picture
                FROM inventory
                ORDER BY sold_date DESC NULLS LAST, purchase_date DESC
            """)
            return cursor.fetchall()

    def update_item(self, item_id, **kwargs):
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(item_id)
        query = f'UPDATE inventory SET {", ".join(fields)} WHERE id = ?'
        self.conn.execute(query, values)
        self.conn.commit()

    def delete_item(self, item_id):
        query = 'DELETE FROM inventory WHERE id = ?'
        self.conn.execute(query, (item_id,))
        self.conn.commit()

    def mark_item_as_sold(self, item_id, sold_price, sold_date):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE inventory
            SET sold_price = ?, sold_date = ?
            WHERE id = ?
        ''', (sold_price, sold_date, item_id))
        self.conn.commit()

    def get_tree_data(self):
        query = '''
        SELECT id, description, type, brand, purchase_date, sold_price, sold_date, size, name, picture
        FROM inventory
        ORDER BY type, brand, name
        '''
        cursor = self.conn.execute(query)
        items = cursor.fetchall()

        columns = ['id', 'description', 'type', 'brand', 'purchase_date', 'sold_price', 'sold_date', 'size', 'name', 'picture']
        items_list = [dict(zip(columns, item)) for item in items]

        tree_data = {
            'types': {},
            'brands': {},
            'sizes': {}
        }

        for item in items_list:
            tree_data['types'].setdefault(item['type'], []).append(item)
            tree_data['brands'].setdefault(item['brand'], []).append(item)
            tree_data['sizes'].setdefault(item['size'], []).append(item)

        return tree_data

    def get_stats(self, group_by='brand'):
        query = f'''
            SELECT brand, type, purchase_date, sold_date, purchase_price, sold_price
            FROM inventory
            WHERE sold_date IS NOT NULL AND sold_price IS NOT NULL AND purchase_price IS NOT NULL
        '''
        df = pd.read_sql_query(query, self.conn)

        if df.empty:
            return pd.DataFrame()  # no data to show

        df['purchase_date'] = pd.to_datetime(df['purchase_date'])
        df['sold_date'] = pd.to_datetime(df['sold_date'])

        df['time_in_system'] = (df['sold_date'] - df['purchase_date']).dt.days
        df['profit'] = df['sold_price'] - df['purchase_price']

        stats = df.groupby(group_by).agg({
            'time_in_system': 'mean',
            'profit': 'mean'
        }).reset_index()

        stats['time_in_system'] = stats['time_in_system'].round(1)
        stats['profit'] = stats['profit'].round(2)

        return stats

    def __del__(self):
        self.conn.close()

    # Helper to get connection context for fetch_items (fix missing connect method)
    def connect(self):
        return self.conn
