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

# Function to simulate the blinking effect and selection
def select_students_with_blink(students, selected_names):
    # Shuffle the students list to simulate randomness
    random.shuffle(students)

    # Filter out the students that should be selected
    selected_students = [student for student in students if student in selected_names]
    
    return selected_students

# Streamlit interface
st.title("Student Selection Game")

st.write("Click the button to start selecting students one by one with a blinking effect!")

# Button to trigger the selection process
if st.button('Start Selection'):
    selected_students = select_students_with_blink(students, selected_students_names)

    final_selected_students = []  # List to store final selected students

    # Display the blinking effect and select each one sequentially
    for i in range(len(selected_students)):
        # "Blink" effect: Show all names and clear them rapidly
        for _ in range(5):  # Blink 5 times (appear and disappear rapidly)
            st.write(" ")
            time.sleep(0.5)
            st.write(students)  # Show all students briefly
            time.sleep(0.5)
            st.write(" ")  # Clear the names

        # Select one student and show it bigger
        st.markdown(f"### **Selected Student: {selected_students[i]}**")
        final_selected_students.append(selected_students[i])
        time.sleep(1)  # Short pause before next selection

    # Finally, show the full list of selected students
    st.write("Final List of Selected Students:")
    for student in final_selected_students:
        st.write(f"- {student}")
