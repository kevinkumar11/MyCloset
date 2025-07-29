from db_inventory import InventoryDB

db = InventoryDB()
items = db.fetch_items()

for item in items:
    print(f"Type: {item[2]}, Brand: {item[3]}, Size: {item[7]}")