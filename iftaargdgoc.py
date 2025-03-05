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

# Function to simulate random selection and reveal names one by one
def select_students(students, selected_names):
    # Shuffle the students list to simulate randomness
    random.shuffle(students)

    # Filter out the students that should be selected
    selected_students = [student for student in students if student in selected_names]
    
    return selected_students

# Streamlit interface
st.title("Student Selection Game")

st.write("Click the button to start selecting students one by one!")

# Button to trigger the selection process
if st.button('Start Selection'):
    selected_students = select_students(students, selected_students_names)
    
    # Sequentially display the selected students one by one with a delay
    st.write("The following students have been selected:")

    # Display each name one by one with a delay
    for student in selected_students:
        time.sleep(1)  # Simulate a delay before showing the next name
        st.write(f"- {student}")
