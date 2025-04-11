# library_app.py
import streamlit as st

# Starting library with predefined books
library = [
    {"title": "Islam Aur Jiddat Pasandi", "author": "Mufti Taqi Usmani"},
    {"title": "Usul al-Ifta wa Adabuhu", "author": "Mufti Taqi Usmani"},
    {"title": "Takmilah Fath al-Mulhim bi-Sharh Sahih al-Imam Muslim", "author": "Mufti Taqi Usmani"},
    {"title": "The Noble Quran: Meaning With Explanatory Notes", "author": "Mufti Taqi Usmani"},
    {"title": "An Introduction to Islamic Finance", "author": "Mufti Taqi Usmani"},
    {"title": "Tauzeeh Al-Qur'an", "author": "Mufti Taqi Usmani"},
    {"title": "Islahi Khutbaat", "author": "Mufti Taqi Usmani"},
    {"title": "Khutbat e Usmani", "author": "Mufti Taqi Usmani"},
    {"title": "Islam Aur Hamari Zindagi", "author": "Mufti Taqi Usmani"},
    {"title": "Duniya Mere Aage", "author": "Mufti Taqi Usmani"},
    {"title": "Islahi Majalis", "author": "Mufti Taqi Usmani"},
    {"title": "Bible Say Quran Tak", "author": "Mufti Taqi Usmani"},
    {"title": "Fatawa Usmani", "author": "Mufti Taqi Usmani"},
    {"title": "Hamara Maashi Nizam", "author": "Mufti Taqi Usmani"},
    {"title": "Hamara Taleemi Nizaam", "author": "Mufti Taqi Usmani"},
    {"title": "Hamare Aaili Masail", "author": "Mufti Taqi Usmani"},
    {"title": "Ejaz-e-Esawi Jadeed", "author": "Mufti Taqi Usmani"},
    {"title": "Isaiyat Kya Hai", "author": "Mufti Taqi Usmani"},
    {"title": "Akabir e Deoband Kya Thay", "author": "Mufti Taqi Usmani"},
    {"title": "Falsafa e Hajj o Qurbani", "author": "Mufti Taqi Usmani"},
    {"title": "Ramadan Kis Tarha Guzarain", "author": "Mufti Taqi Usmani"},
    {"title": "Islami Bankari", "author": "Mufti Taqi Usmani"},
    {"title": "Irshadaat e Akabir", "author": "Mufti Taqi Usmani"},
    {"title": "Namoos e Risalat Ki Hifazat Karay", "author": "Mufti Taqi Usmani"}
]

# Streamlit App UI
st.title("📚 Personal Library Manager")

# Add Book Section
st.subheader("➕ Add New Book")
with st.form("add_book_form"):
    new_title = st.text_input("Book ka naam:")
    new_author = st.text_input("Musannif ka naam:")
    add_btn = st.form_submit_button("Add Book")
    if add_btn and new_title and new_author:
        library.append({"title": new_title, "author": new_author})
        st.success(f"✅ `{new_title}` kitab add ho gayi!")

# View Books
st.subheader("📖 View All Books")
if library:
    for i, book in enumerate(library, 1):
        st.write(f"{i}. **{book['title']}** by *{book['author']}*")
else:
    st.warning("Library abhi khali hai.")

# Delete Book
st.subheader("🗑️ Delete a Book")
book_titles = [book['title'] for book in library]
if book_titles:
    selected_book = st.selectbox("Konsi kitab delete karni hai?", book_titles)
    if st.button("Delete Book"):
        library[:] = [book for book in library if book['title'] != selected_book]
        st.success(f"❌ `{selected_book}` delete ho gayi.")
else:
    st.info("Koi kitab delete karne ke liye maujood nahi hai.")
# venv\Scripts\activate
# streamlit run personal_Library_Manager2.py