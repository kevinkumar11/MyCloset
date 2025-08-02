import streamlit as st
from streamlit.components.v1 import html

# Custom function to simulate a big button with icon and JS onclick -> Streamlit event
def icon_button(label, icon="🚀", key="icon_btn"):
    custom_id = f"{key}_clicked"
    js = f"""
        <script>
            function setValue() {{
                const streamlitDoc = window.parent.document;
                streamlitDoc.getElementById("{custom_id}").value = "1";
                streamlitDoc.getElementById("{custom_id}").dispatchEvent(new Event("input", {{ bubbles: true }}));
            }}
        </script>
        <style>
            .icon-button {{
                background-color: #008CBA;
                color: white;
                padding: 20px 40px;
                font-size: 24px;
                border: none;
                border-radius: 12px;
                cursor: pointer;
            }}
            .icon-button:hover {{
                background-color: #0074A2;
            }}
        </style>
        <button class="icon-button" onclick="setValue()">{icon} {label}</button>
        <input type="hidden" id="{custom_id}" name="{custom_id}" />
    """
    clicked = html(js, height=100)
    return st.session_state.get(custom_id) == "1"

# Track state manually
if "icon_btn_clicked" not in st.session_state:
    st.session_state["icon_btn_clicked"] = False

# Use the button
st.subheader("🚀 Custom Big Button with Icon")
html("""
    <style>
        .spacer { margin-top: 20px; }
    </style>
""", height=0)

if icon_button("Launch", "🚀", key="icon_btn"):
    st.write("Button was clicked!")
    st.session_state["icon_btn_clicked"] = True

if st.session_state["icon_btn_clicked"]:
    st.write("Button was clicked!")



