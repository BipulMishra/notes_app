import streamlit as st
import requests

# -------------------------------
# API URL  
# -------------------------------
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Notes App", page_icon="📝", layout="centered")

st.title("📝 Personal Notes Manager")

# -------------------------------
# ADD NEW NOTE
# -------------------------------
st.header("Add a New Note")
title = st.text_input("Title")
content = st.text_area("Content")

if st.button("Add Note"):
    if not title.strip() or not content.strip():
        st.warning("⚠️ Please fill in both title and content before adding a note.")
    else:
        try:
            res = requests.post(f"{API_URL}/notes", params={"title": title, "content": content})
            if res.status_code == 200:
                st.success("✅ Note added successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to add note.")
        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend. Make sure FastAPI is running.")

st.divider()

# -------------------------------
# VIEW, EDIT, DELETE NOTES
# -------------------------------
st.header("Your Notes")

try:
    res = requests.get(f"{API_URL}/notes")
    if res.status_code == 200:
        notes = res.json()

        if not notes:
            st.info("🗒️ No notes yet. Add your first note above!")
        else:
            for note in notes:
                with st.expander(f"📝 {note['title']}"):
                    st.caption(f"Created at: {note['created_at']}")
                    st.write(note['content'])

                    # Editable fields
                    new_title = st.text_input(f"Edit Title ({note['id']})", value=note['title'], key=f"title_{note['id']}")
                    new_content = st.text_area(f"Edit Content ({note['id']})", value=note['content'], key=f"content_{note['id']}")

                    col1, col2 = st.columns(2)

                    with col1:
                        if st.button(f"💾 Update {note['id']}", key=f"update_{note['id']}"):
                            if not new_title.strip() or not new_content.strip():
                                st.warning("⚠️ Both title and content are required to update.")
                            else:
                                update_res = requests.put(
                                    f"{API_URL}/notes/{note['id']}",
                                    params={"title": new_title, "content": new_content}
                                )
                                if update_res.status_code == 200:
                                    st.success("✅ Note updated successfully!")
                                    st.rerun()
                                else:
                                    st.error("❌ Failed to update note.")

                    with col2:
                        if st.button(f"🗑️ Delete {note['id']}", key=f"delete_{note['id']}"):
                            del_res = requests.delete(f"{API_URL}/notes/{note['id']}")
                            if del_res.status_code == 200:
                                st.success("🗑️ Note deleted successfully!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to delete note.")
    else:
        st.error("❌ Failed to load notes. Backend might be offline.")
except requests.exceptions.ConnectionError:
    st.error("🚫 Cannot connect to backend. Please ensure FastAPI is running.")
