import streamlit as st
from db_inventory import InventoryDB

st.title("Clothing Inventory Stats")

db = InventoryDB()

group_by = st.selectbox("Group stats by:", options=['brand', 'type'])

stats_df = db.get_stats(group_by=group_by)

if stats_df.empty:
    st.write("No sold items data available yet.")
else:
    st.dataframe(stats_df)

    st.subheader(f"Average Time in System by {group_by.capitalize()}")
    st.bar_chart(data=stats_df.set_index(group_by)['time_in_system'], use_container_width=True)

    st.subheader(f"Average Profit by {group_by.capitalize()}")
    st.bar_chart(data=stats_df.set_index(group_by)['profit'], use_container_width=True)
