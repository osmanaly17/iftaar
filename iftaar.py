import streamlit as st
import random
import time

def select_members():
    fixed_members = ["Usman", "Azoha", "Usama", "Arqam", "Reyan"]
    all_members = [
        "Laiba Javed", "Junaid Fayyaz", "Zohaa Ajmal", "Mohammad Reyan", "Azalfa Aarij",
        "Iman Alam", "Amna Younus", "Ayesha", "Fatima Hammad", "Moaviz Waheed",
        "Ukasha Waqas", "Azoha Shahid", "Mr and Mrs Atta-ul-Latif Khawaja", "Enaas Muzammil",
        "Abdul Haseeb", "Iqra Eman", "Iqra Eman", "Maryam Zia Dar", "Nimra Rafiq", "Farakh",
        "Anna Kamran", "Urwa Ahmad", "Abdullah Ali Chughtai", "Ibrahim Asad", "Alizeh Shahid",
        "Umar Usama"
    ]
    
    remaining_members = list(set(all_members) - set(fixed_members))
    random.shuffle(remaining_members)
    random_members = random.sample(remaining_members, 5)
    
    return fixed_members + random_members

def main():
    st.title("🔮 Random Member Selector")
    
    if st.button("Start Selection 🎲"):
        selected_members = select_members()
        
        st.write("### Selecting Members:")
        placeholder = st.empty()
        
        for i, member in enumerate(selected_members):
            with placeholder:
                st.subheader(f"🎉 {member} 🎉")
            time.sleep(1.5)
        
        time.sleep(1)
        
        st.write("### 🎊 Final Selected Members 🎊")
        final_placeholder = st.empty()
        
        for i in range(3):
            with final_placeholder:
                st.subheader("✨✨✨✨✨")
            time.sleep(0.5)
            with final_placeholder:
                st.subheader("🎇🎇🎇🎇🎇")
            time.sleep(0.5)
        
        for member in selected_members:
            st.success(f"✅ {member}")
    
if __name__ == "__main__":
    main()
