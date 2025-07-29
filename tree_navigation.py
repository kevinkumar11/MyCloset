import streamlit as st
from db_inventory import InventoryDB
import base64

def render_tree_navigation():
    """Render the clothing inventory tree navigation in Streamlit"""
    
    # Initialize database
    db = InventoryDB()
    tree_data = db.get_tree_data()
    
    # Predefined type categories
    type_categories = [
        'short-sleeve', 'long-sleeve', 'pants', 'shorts', 'sweaters', 
        'jackets/hoodies', 'coats', 'shoes', 'hats', 'accessories'
    ]
    
    st.markdown("### 📦 Clothing Inventory Navigation")
    
    # Create three columns for the main categories
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 👕 TYPE")
        render_type_section(tree_data, type_categories)
    
    with col2:
        st.markdown("#### 🏷️ BRAND")
        render_brand_section(tree_data)
    
    with col3:
        st.markdown("#### 📏 SIZE")
        render_size_section(tree_data)

def render_type_section(tree_data, type_categories):
    """Render the TYPE section"""
    for type_name in type_categories:
        items = tree_data['types'].get(type_name, [])
        count = len(items)
        
        # Create expandable section
        with st.expander(f"📂 {type_name.replace('-', ' ').title()} ({count})", expanded=False):
            if items:
                for item in items:
                    render_item_line(item)
            else:
                st.write("No items in this category")

def render_brand_section(tree_data):
    """Render the BRAND section"""
    # Sort brands alphabetically
    sorted_brands = sorted(tree_data['brands'].items())
    
    for brand_name, items in sorted_brands:
        count = len(items)
        
        # Create expandable section
        with st.expander(f"🏷️ {brand_name.title()} ({count})", expanded=False):
            for item in items:
                render_item_line(item)

def render_size_section(tree_data):
    """Render the SIZE section"""
    # Sort sizes: S, M, L, XL first, then numeric
    def sort_sizes(size_item):
        size_name = size_item[0]
        size_order = {'S': 1, 'M': 2, 'L': 3, 'XL': 4}
        return size_order.get(size_name, int(size_name) if size_name.isdigit() else 999)
    
    sorted_sizes = sorted(tree_data['sizes'].items(), key=sort_sizes)
    
    for size_name, items in sorted_sizes:
        count = len(items)
        
        # Create expandable section
        with st.expander(f"📏 {size_name} ({count})", expanded=False):
            for item in items:
                render_item_line(item)

def render_item_line(item):
    """Render individual item line with image"""
    # Create two columns: one for text, one for image
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Item name and details
        st.write(f"**{item['name']}**")
        st.caption(f"Type: {item['type']} | Brand: {item['brand']} | Size: {item['size']} | ${item['price']}")
    
    with col2:
        # Item image or placeholder
        if item['picture']:
            try:
                # Display actual image if available
                image_data = base64.b64decode(item['picture'])
                st.image(image_data, width=50)
            except:
                # Fallback to placeholder
                st.write("📦")
        else:
            # Placeholder icon
            st.write("📦")
    
    # Add click functionality
    if st.button(f"View Details", key=f"item_{item['id']}", help=f"Click to view {item['name']} details"):
        show_item_details(item)
    
    st.divider()

def show_item_details(item):
    """Show detailed item information"""
    st.sidebar.markdown("### 🔍 Item Details")
    st.sidebar.write(f"**Name:** {item['name']}")
    st.sidebar.write(f"**Description:** {item.get('description', 'No description')}")
    st.sidebar.write(f"**Type:** {item['type']}")
    st.sidebar.write(f"**Brand:** {item['brand']}")
    st.sidebar.write(f"**Size:** {item['size']}")
    st.sidebar.write(f"**Price:** ${item['price']}")
    st.sidebar.write(f"**Purchase Date:** {item['purchase_date']}")
    
    if item['picture']:
        try:
            image_data = base64.b64decode(item['picture'])
            st.sidebar.image(image_data, caption=item['name'])
        except:
            st.sidebar.write("📦 Image not available")

# Main function to call from your Streamlit app
def main():
    st.set_page_config(page_title="Clothing Inventory", page_icon="👕", layout="wide")
    render_tree_navigation()

if __name__ == "__main__":
    main()