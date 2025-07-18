import streamlit as st
from create_page import CreatePage
from display_inventory_page import DisplayInventoryPage

st.set_page_config(page_title="Sales App", layout="wide")

st.markdown("""
    <style>
    .button-tile {
        background-color: #f9f9f9;
        border: 2px solid #ccc;
        padding: 30px 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s;
        height: 130px;
    }
    .button-tile:hover {
        background-color: #e8e8e8;
        border-color: #999;
    }
    .button-icon {
        font-size: 40px;
        display: block;
        margin-bottom: 10px;
    }
    .tile-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Sales Application")
st.subheader("What can I help you with today?")

row1 = st.columns(3)
row2 = st.columns(3)

# ➕ Button 1 - Create New Item
with row1[0]:
    if st.button("Create New Item", key="create"):
        CreatePage("clothing_inventory_new.db").display()
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">➕</span>Create New Item</div></div>',
        unsafe_allow_html=True,
    )

# 🧾 Button 2 - View Inventory
with row1[1]:
    if st.button("View Full Inventory", key="view"):
        DisplayInventoryPage("clothing_inventory_new.db").display()
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">🧾</span>View Inventory</div></div>',
        unsafe_allow_html=True,
    )

# 📊 Button 3 - Stats
with row1[2]:
    if st.button("Stats", key="stats"):
        st.write("Stats page coming soon.")
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">📊</span>Stats</div></div>',
        unsafe_allow_html=True,
    )

# ⚙️ Button 4 - Settings
with row2[0]:
    if st.button("Settings", key="settings"):
        st.write("Settings page coming soon.")
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">⚙️</span>Settings</div></div>',
        unsafe_allow_html=True,
    )

# 📤 Button 5 - Cross-Post
with row2[1]:
    if st.button("Cross-Post", key="cross"):
        st.write("Cross-posting functionality coming soon.")
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">📤</span>Cross-Post</div></div>',
        unsafe_allow_html=True,
    )

# 🔁 Button 6 - Bulk Actions
with row2[2]:
    if st.button("Bulk Actions", key="bulk"):
        st.write("Bulk actions functionality coming soon.")
    st.markdown(
        '<div class="tile-wrapper"><div class="button-tile"><span class="button-icon">🔁</span>Bulk Actions</div></div>',
        unsafe_allow_html=True,
    )
