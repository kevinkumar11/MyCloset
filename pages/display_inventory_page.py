import streamlit as st
from db_inventory import InventoryDB

class DisplayInventoryPage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.inventory_db = InventoryDB(db_name=db_name)

    def display(self):
        st.page_link("sales_app.py", label="Home", icon="🏠")
        st.title("📦 Inventory Overview")

        rows = self.inventory_db.fetch_items()

        if not rows:
            st.info("No data found in the database.")
            return
        #id, name, description, brand, type, purchase_price, sold_price, purchase_date, sold_date, size, picture

        for row in rows:
            name = row[1]
            description = row[2]
            brand = row[3]
            category_type = row[4]
            purchase_price = row[5]
            sold_price = row[6]
            purchase_date = row[6]
            sold_date = row[8]
            size = row[9]
            picture = row[10]

            with st.container():
                #st.markdown(f"### {name}")
                st.markdown(f"**Description:** {description}")
                st.markdown(f"**Brand:** {brand}")
                st.markdown(f"**Category Type:** {category_type}")
                st.markdown(f"**Size:** {size}")
                st.markdown(f"**Purchase Date:** {purchase_date}")
                st.markdown(f"**Sold Date:** {sold_date if sold_date else '—'}")
                st.markdown(f"**Sold Price:** ${sold_price:.2f}" if sold_price else "**Sold Price:** —")
                if picture:
                    st.image(picture, caption=name, use_column_width=False)
                st.markdown("---")

# Run this page directly
if __name__ == "__main__":
    page = DisplayInventoryPage("clothing_inventory.db")
    page.display()
