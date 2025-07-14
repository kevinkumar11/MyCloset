import streamlit as st

from create_page import CreatePage
from display_inventory_page import DisplayInventoryPage


st.title("Sales Application");
st.write("Welcome to the Sales Application! This app helps you manage and analyze your sales data effectively.");

if st.button("Create New Item"):
    create_pg = CreatePage("clothing_inventory.db")
    create_pg.display()
elif st.button("Display Inventory"):
    display_pg = DisplayInventoryPage("clothing_inventory.db")
    display_pg.display()
else:
    st.write("Please select an option to proceed: Create New Item or Display Inventory.")

