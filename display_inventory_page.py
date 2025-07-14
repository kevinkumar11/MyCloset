import streamlit as st
import sqlite3
import os

from db_inventory import InventoryDB

class DisplayInventoryPage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.inventory_db = InventoryDB(db_name=db_name)

    def display(self):

        # Displaying the data from the database
        st.subheader("Sales Data")
        rows = self.inventory_db.fetch_items()
        if rows:
            for row in rows:
                st.write(f"Name: {row[1]}, Description: {row[2]}, Brand: {row[3]}, Category Type: {row[4]}, Price: ${row[5]:.2f}, Purchase Date: {row[6]}, Size: {row[7]}")
                if row[8]:
                    st.image(row[8], caption=row[1], use_column_width=True)
        else:
            st.write("No data found in the database.")

# Create an instance of the displayInventoryPage class and call the display method
if __name__ == "__main__":
    page = displayInventoryPage()
    page.display()
# This code is part of a Streamlit application that allows users to view sales data.
# The displayInventoryPage class encapsulates the functionality for displaying the sales data from the database.    
#conn.close()
