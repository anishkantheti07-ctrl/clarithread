import streamlit as st
from logic.group_manager import load_groups, add_group

st.set_page_config(
    page_title="ClariThread",
    page_icon="💬",
    layout="wide"
)

st.title("💬 ClariThread")

st.subheader("Create Group")

group_name = st.text_input("Group Name")

if st.button("Create Group"):
    if group_name:
        add_group(group_name)
        st.success(f"{group_name} created successfully!")
    else:
        st.warning("Please enter a group name.")

st.divider()

st.subheader("Available Groups")

groups = load_groups()

if groups:
    for group in groups:
        st.write(f"📁 {group}")
else:
    st.info("No groups created yet.")