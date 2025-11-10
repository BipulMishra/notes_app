import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Notes App", page_icon="📝", layout="centered")

st.title("📝 Personal Notes Manager")

# Create Note
st.header("Add a New Note")
title = st.text_input("Title")
content = st.text_area("Content")
if st.button("Add Note"):
    if title and content:
        res = requests.post(f"{API_URL}/notes", params={"title": title, "content": content})
        if res.status_code == 200:
            st.success("Note added successfully!")
        else:
            st.error("Failed to add note.")
    else:
        st.warning("Please enter both title and content.")

# View Notes
st.header("Your Notes")
res = requests.get(f"{API_URL}/notes")
if res.status_code == 200:
    notes = res.json()
    for note in notes:
        with st.expander(note['title']):
            st.write(note['content'])
            st.caption(f"Created at: {note['created_at']}")
            if st.button(f"Delete {note['id']}", key=note['id']):
                requests.delete(f"{API_URL}/notes/{note['id']}")
                st.rerun()
else:
    st.error("Could not load notes.")
