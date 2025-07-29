# pages/tree_navigation_page.py
import streamlit as st
import sys
import os

# Add the parent directory to the path so we can import from the main folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tree_navigation import render_tree_navigation

st.set_page_config(page_title="Inventory Navigation", page_icon="🌳", layout="wide")

st.title("🌳 Clothing Inventory Navigation")
st.markdown("Browse your inventory by Type, Brand, or Size")

render_tree_navigation()