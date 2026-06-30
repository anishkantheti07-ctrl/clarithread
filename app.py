import streamlit as st
from logic.group_manager import load_groups, add_group
from logic.message_manager import add_message, get_group_messages

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

st.divider()

if groups:

    selected_group = st.selectbox(
        "Open Group",
        groups
    )

    st.subheader(f"💬 {selected_group}")

    sender = st.text_input("Your Name")

    message = st.text_input("Message")

    if st.button("Send Message"):

        if sender and message:

            add_message(
                selected_group,
                sender,
                message
            )

            st.success("Message Sent!")
            st.rerun()

    st.divider()

    st.subheader("Chat History")

    messages = get_group_messages(selected_group)

    for msg in messages:

        with st.chat_message("user"):
            st.write(f"**{msg['sender']}**")
            st.write(msg["text"])
            st.caption(msg["timestamp"])