import streamlit as st

st.set_page_config(page_title="Sales App", layout="wide")

button_html = st.markdown("""
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
    st.page_link("pages/create_page.py", label="Create New Item", icon="➕")

# 🌳 Button 2 - Tree Navigation (NEW!)
with row1[1]:
    st.page_link("pages/tree_navigation_page.py", label="Browse Inventory", icon="🌳")

# 🧾 Button 3 - View Full Inventory (moved to row1[2])
with row1[2]:
    st.page_link("pages/display_inventory_page.py", label="View Full Inventory", icon="🧾")

# 📊 Button 4 - Stats
with row2[0]:
    st.page_link("pages/coming_soon_page.py", label="Stats", icon="📊")

# ⚙️ Button 5 - Settings
with row2[1]:
    st.page_link("pages/coming_soon_page.py", label="Settings", icon="⚙️")

# 📤 Button 6 - Cross-Post
with row2[2]:
    st.page_link("pages/coming_soon_page.py", label="Cross-Post", icon="📤")

# If you want 6 buttons, add this row:
row3 = st.columns(3)
with row3[0]:
    st.page_link("pages/coming_soon_page.py", label="Bulk Actions", icon="🔁")