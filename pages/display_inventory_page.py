import streamlit as st
from db_inventory import InventoryDB
from PIL import Image
import pandas as pd
import io

class DisplayInventoryPage:
    def __init__(self, db_name='clothing_inventory.db'):
        self.inventory_db = InventoryDB(db_name=db_name)

    def display(self):
        st.set_page_config(page_title="Inventory Overview", layout="wide")
        st.markdown("""
            <style>
            .stButton button {
                background-color: #f9f9f9;
                border: 2px solid #ccc;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                cursor: pointer;
                transition: 0.3s;
            }
            .stButton button:hover {
                background-color: #e8e8e8;
                border-color: #999; 
            }
            </style>
        """, unsafe_allow_html=True)        
        st.page_link("sales_app.py", label="Home", icon="🏠")
        st.title("📦 Inventory Overview")

        rows = self.inventory_db.fetch_items()

        if not rows:
            st.info("No data found in the database.")
            return
        #id, name, description, brand, type, purchase_price, sold_price, purchase_date, sold_date, size, picture

        on = st.toggle("Image View", value=True, key="image_view_toggle");

        if on:
            self.loadImages2(rows)
        else:
            self.loadDataIntable(rows)


        #self.loadDataIntable(rows)

        #self.loadData(rows)

        #self.loadImages(rows)

        #self.loadImages2(rows)

    def loadData(self, rows):
        # Inline CSS for scrollable div
        st.markdown("""
            <style>
            .scroll-container {
                height: 40px;
                overflow-y: auto;
                border: 1px solid #ccc;
                padding: 10px;
            }
            </style>
            """, unsafe_allow_html=True)
    
        # Display inside scrollable div
        st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
    
        for row in rows:
            description = row[2]
            picture  = row[10]
            image = Image.open(io.BytesIO(picture))
            st.image(image, caption=description, use_container_width=True)
    
        st.markdown('</div>', unsafe_allow_html=True)     

    def loadDataIntable(self, rows):
        df = pd.DataFrame(rows, columns=[
            'ID', 'Name', 'Description', 'Brand', 'Type',
            'Purchase Price', 'Sold Price', 'Purchase Date',
            'Sold Date', 'Size', 'Picture'
        ])
        st.dataframe(
            df,         
            column_config={
                "Picture": st.column_config.ImageColumn("Picture", width="small", help="Product image")
            },
            use_container_width=True)
    
    def loadImages(self, rows):
        st.markdown("""
            <style>
            .image-container {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .image-item {
                width: 150px;
                height: 150px;
                overflow: hidden;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
            .image-item img {
                width: 100%;
                height: auto;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        for row in rows:
            description = row[3]
            picture = row[10]
            if picture:
                image = Image.open(io.BytesIO(picture))
                #st.markdown('<div class="image-item">', unsafe_allow_html=True)
                st.image(image, caption=description, width=150,  use_container_width=False)
                #st.markdown(f'<div class="image-item"><img src="data:image/jpeg;base64,{image.tobytes().hex()}" alt="Image"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def loadImages2(self, rows):
        # --- Convert BLOBs to PIL Images ---
        images = []
        for img_data in rows:
            image = Image.open(io.BytesIO(img_data[10]))
            images.append(image)

        # --- Display images in grid format ---
        cols = st.columns(3)  # 3 images per row

        for index, image in enumerate(images):
            with cols[index % 3]:
                st.image(image, width=150, use_container_width=False)

# Run this page directly
if __name__ == "__main__":
    page = DisplayInventoryPage("clothing_inventory.db")
    page.display()
