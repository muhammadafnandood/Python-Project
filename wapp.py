import streamlit as st

# Dummy users
users = {"admin": "password", "afnan": "1234"}

qa_data = {
    "what is python": "Python is a high-level, interpreted programming language.",
    "how to create a list": "Use square brackets: my_list = [1, 2, 3]",
}

mcqs = [
    {"q": "What is the keyword to define a function?", "a": "def"},
    {"q": "Which data type is immutable?", "a": "tuple"},
    {"q": "What does len() do?", "a": "Returns length"},
    {"q": "Which symbol is used for comments?", "a": "#"},
]

# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = ""
    st.session_state.history = []

# Login
if not st.session_state.logged_in:
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")
else:
    st.sidebar.title(f"Welcome, {st.session_state.user}")
    menu = st.sidebar.radio("Navigate", ["Search Q&A", "MCQs", "Wordlist Generator", "Logout"] + (["Admin Panel"] if st.session_state.user == "admin" else []))

    if menu == "Search Q&A":
        st.header("Ask Python Questions")
        query = st.text_input("Enter your question")
        if st.button("Ask"):
            ans = qa_data.get(query.lower().strip(), "Sorry, I don't know that yet.")
            st.write(f"*Answer:* {ans}")
            st.session_state.history.append(query)
        if st.session_state.history:
            st.subheader("Search History")
            for item in st.session_state.history:
                st.write("-", item)

    elif menu == "MCQs":
        st.header("Python MCQs")
        for item in mcqs:
            st.write(f"*Q:* {item['q']}")
            st.write(f"*A:* {item['a']}")
            st.markdown("---")

    elif menu == "Wordlist Generator":
        st.header("Custom Wordlist Generator")
        words_input = st.text_input("Enter comma-separated words")
        if st.button("Generate Wordlist"):
            wordlist = []
            words = [w.strip() for w in words_input.split(",")]
            for w in words:
                wordlist += [w + "123", w + "2024", w.upper(), w.lower(), w[::-1], w + "!", "123" + w]
            st.subheader("Generated Wordlist:")
            for word in wordlist:
                st.write(word)

    elif menu == "Admin Panel":
        st.header("Admin Panel - Add New Q&A")
        q = st.text_input("New Question")
        a = st.text_input("Answer")
        if st.button("Add Q&A"):
            if q and a:
                qa_data[q.lower().strip()] = a
                st.success("Q&A added successfully")

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.history = []
        st.success("Logged out successfully")
        st.rerun()
