# Personal Library Manager :
# import streamlit as st
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


def add_book() :
    title = input("Book ka name : ")
    author = input("Musannif ka name : ")
    library.append({"title" : title , "author" : author})

    print("Kitab add ho gai!")

def view_books() :
    if not library :

        print("Library khali hai.")
        return
 
    for i , book in enumerate(library , 1) :
        print(f"{i}. {book["title"]} by {book["author"]}")

def delete_book() :
    view_books()
    try :
        index = int(input("Konsi kitab delete karni hai (number) : ")) -1
        removed = library.pop(index)
        print(f"`{removed["title"]}` delete ho gai.")

    except :
        print("Apka input ghalat hai!")

def menu() :
    while True :
        print("\n1. Add Book\n2. View Books\n3. Delete Book\n4. Exit")
        choice = input("Option chunein : ")

        if choice == "1" :
            add_book()

        elif choice == "2" :
            view_books()

        elif choice == "3" :
            delete_book()

        elif choice == "4" :
            break

        else :
            print("Option sahi nahi!")

menu()
