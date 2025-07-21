import streamlit as st


from db_inventory import InventoryDB

class CreatePage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.invenotory_db = InventoryDB(db_name=db_name)

    def display(self):
        st.page_link("sales_app.py", label="Home", icon="🏠")

        st.title("Enter New Item Details")
        name = st.text_input("Name:")
        desc = st.text_input("Description:")
        brand = st.text_input("Brand:")
        cType = st.text_input("Category Type:")
        price = st.number_input("Price:", min_value=0.0, format="%.2f")
        purchase_dt = st.date_input("Purchase Date:")
        sold_dt = st.date_input("Sold Date:")
        size = st.text_input("Size:")
        picture = st.file_uploader("Upload Picture:", type=["jpg", "jpeg", "png"])

        if st.button("Submit"):
            picture_data = picture.read() if picture else None
            self.invenotory_db.add_item(name, desc, brand, cType, price, purchase_dt.strftime('%Y-%m-%d'), sold_dt.strftime('%Y-%m-%d'), size, picture_data)
            st.success("Data saved to database!")

# Create an instance of the createPage class and call the display method
if __name__ == "__main__":
    page = CreatePage("clothing_inventory_new.db")
    page.display() 
# This code is part of a Streamlit application that allows users to create and manage sales data.   
# The createPage class encapsulates the functionality for displaying the sales form and handling database interactions.
#conn.close()
