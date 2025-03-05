import streamlit as st
import random
import time

def select_members():
    fixed_members = ["Usman", "Azoha", "Usama", "Arqam", "Reyan"]
    all_members = [
        "Laiba Javed", "Junaid Fayyaz", "Zohaa Ajmal", "Mohammad Reyan", "Azalfa Aarij",
        "Iman Alam", "Amna Younus", "Ayesha", "Fatima Hammad", "Moaviz Waheed",
        "Ukasha Waqas", "Azoha Shahid", "Mr and Mrs Atta-ul-Latif Khawaja", "Enaas Muzammil",
        "Abdul Haseeb", "Iqra Eman", "Maryam Zia Dar", "Nimra Rafiq", "Farakh",
        "Anna Kamran", "Urwa Ahmad", "Abdullah Ali Chughtai", "Ibrahim Asad", "Alizeh Shahid"
    ]
    
    remaining_members = list(set(all_members) - set(fixed_members))
    random.shuffle(remaining_members)
    random_members = random.sample(remaining_members, 5)
    
    return fixed_members + random_members

def blinking_selection_animation(members):
    placeholder = st.empty()
    for _ in range(15):  # Blink effect
        shuffled_names = random.sample(members, min(len(members), 10))  # Show 10 random names at a time
        names_display = " | ".join(shuffled_names)
        with placeholder:
            st.markdown(f"### 🔄 {names_display} 🔄")
        time.sleep(0.2)
    
    selected = random.choice(members)
    members.remove(selected)
    return selected

def main():
    st.title("🔮 Random Member Selector")
    
    if st.button("Start Selection 🎲"):
        selected_members = []
        all_candidates = select_members()
        remaining_pool = all_candidates.copy()
        
        st.write("### Selecting Members:")
        placeholder = st.empty()
        
        for _ in range(10):
            selected = blinking_selection_animation(remaining_pool)
            with placeholder:
                st.subheader(f"🎉 {selected} 🎉")
            selected_members.append(selected)
            time.sleep(1)
        
        time.sleep(1)
        
        st.write("### 🎊 Final Selected Members 🎊")
        final_placeholder = st.empty()
        
        for _ in range(3):
            with final_placeholder:
                st.subheader("✨✨✨✨✨")
            time.sleep(0.5)
            with final_placeholder:
                st.subheader("🎇🎇🎇🎇🎇")
            time.sleep(0.5)
        
        final_placeholder.empty()
        
        for member in selected_members:
            st.success(f"✅ {member}")
    
if __name__ == "__main__":
    main()
