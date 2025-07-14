import streamlit as st
import sqlite3
import os

from db_inventory import InventoryDB


st.title("Sales Application");
st.write("Welcome to the Sales Application! This app helps you manage and analyze your sales data effectively.");

name = st.text_input("Name:");
desc = st.text_input("Description:");
brand = st.text_input("Brand:");
cType = st.text_input("Category Type:");
price = st.number_input("Price:", min_value=0.0, format="%.2f");
purchase_dt = st.date_input("Purchase Date:");
size = st.text_input("Size:");
picture = st.file_uploader("Upload Picture:", type=["jpg", "jpeg", "png"]);


# Get the path of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Join with your database path
db_path = os.path.join(base_dir, "db", "clothing_inventory.db")




# Connect to SQLite database (creates file if not exists)
#conn = sqlite3.connect(db_path)
#print(f"Connecting to DB at: {db_path}")
#c = conn.cursor()


if st.button("Submit"):
    picture_data = picture.read() if picture else None
    invenotory_db = InventoryDB(db_name='clothing_inventory.db')
    invenotory_db.add_item(name, desc, brand, cType, price, purchase_dt.strftime('%Y-%m-%d'), size, picture_data)
    st.success("Data saved to database!")
    #conn.close()

# Displaying the data from the database
st.subheader("Sales Data");
invenotory_db = InventoryDB(db_name='clothing_inventory.db')
rows = invenotory_db.fetch_items();
#c.execute("SELECT * FROM inventory");
#rows = c.fetchall()
if rows:
    for row in rows:
        st.write(f"Name: {row[1]}, Description: {row[2]}, Brand: {row[3]}, Category Type: {row[4]}, Price: ${row[5]:.2f}, Purchase Date: {row[6]}, Size: {row[7]}")
        if row[8]:
            st.image(row[8], caption=row[1], use_column_width=True)
else:
    st.write("No data found in the database.");


