import streamlit as st
from db_inventory import InventoryDB

class CreatePage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.inventory_db = InventoryDB(db_name=db_name)

    def display(self):
        st.page_link("sales_app.py", label="Home", icon="🏠")

        st.title("Enter New Item Details")
        description = st.text_input("Description:")
        brand = st.text_input("Brand:")
        cType = st.text_input("Category Type:")
        purchase_price = st.number_input("Purchase Price:", min_value=0.0, format="%.2f")
        sold_price = st.number_input("Sold Price:", min_value=0.0, format="%.2f")
        purchase_dt = st.date_input("Purchase Date:")
        sold_dt = st.date_input("Sold Date:")
        size = st.text_input("Size:")
        picture = st.file_uploader("Upload Picture:", type=["jpg", "jpeg", "png"])

        if st.button("Submit"):
            picture_data = picture.read() if picture else None
            self.inventory_db.add_item(
                description=description,
                brand=brand,
                category_type=cType,
                purchase_price=purchase_price,
                sold_price=sold_price,
                purchase_date=purchase_dt.strftime('%Y-%m-%d'),
                sold_date=sold_dt.strftime('%Y-%m-%d'),
                size=size,
                picture=picture_data
            )
            st.success("Data saved to database!")

# Run this page standalone
if __name__ == "__main__":
    page = CreatePage("clothing_inventory.db")
    page.display()
