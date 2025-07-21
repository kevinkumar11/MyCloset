import streamlit as st


from db_inventory import InventoryDB

class ComingSoonPage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.invenotory_db = InventoryDB(db_name=db_name)

    def display(self):
        st.page_link("sales_app.py", label="Home", icon="🏠")
        st.title("Comming Soon Page")

# Create an instance of the createPage class and call the display method
if __name__ == "__main__":
    page = ComingSoonPage()
    page.display() 