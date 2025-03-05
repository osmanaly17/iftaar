import random
import time
import streamlit as st

# List of 16 students (you can replace them with actual names)
students = [
    "Usman Ali", "Muhammad Reyan", "Zoha Ajmal", "Ayesha", "Ukasha Waqas", 
    "Azalfa Aarij", "Moaviz Waheed", "Laiba Javed", "Iman Alam", "Amna Yusuf", 
    "Fatima Hammad", "Azoha Shahid", "Usama Lodhi", "Zohaib Hassan", 
    "Arqam Zafar", "Ibrahim Asad"
]

# List of students to select (predefined selection)
selected_students_names = [
    "Usman Ali", "Muhammad Reyan", "Azoha Shahid", "Usama Lodhi", 
    "Zoha Ajmal", "Zohaib Hassan", "Arqam Zafar"
]

# Function to simulate random selection
def select_students(students, selected_names):
    # Pretend randomness with a pause and shuffle the list for the effect
    st.write("Selecting students... Please wait.\n")
    time.sleep(2)  # Simulate the waiting time

    # Shuffle the list to create the appearance of randomness
    random.shuffle(students)
    time.sleep(1)  # Simulate the illusion of randomness

    # Select students based on the predefined names
    selected_students = [student for student in students if student in selected_names]
    
    return selected_students

# Streamlit interface
st.title("Student Selection Game")

st.write("Click the button to randomly select students from the list!")

# Add a button for the user to start the selection
if st.button('Select Students'):
    selected_students = select_students(students, selected_students_names)
    
    # Display the selected students
    st.write("The following students have been selected:")
    for student in selected_students:
        st.write(f"- {student}")
