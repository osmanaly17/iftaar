import streamlit as st
import random
import time

def select_members():
    fixed_members = ["Usman", "Azoha", "Usama", "Arqam", "Reyan", "Enaas Muzammil"]
    all_members = [
        "Laiba Javed", "Junaid Fayyaz", "Zohaa Ajmal", "Mohammad Reyan", "Azalfa Aarij",
        "Iman Alam", "Amna Younus", "Ayesha", "Fatima Hammad", "Moaviz Waheed",
        "Ukasha Waqas", "Azoha Shahid", "Mr and Mrs Atta-ul-Latif Khawaja", "Enaas Muzammil",
        "Abdul Haseeb", "Iqra Eman", "Maryam Zia Dar", "Nimra Rafiq", "Farakh",
        "Anna Kamran", "Urwa Ahmad", "Abdullah Ali Chughtai", "Ibrahim Asad", "Alizeh Shahid"
    ]
    
    remaining_members = list(set(all_members) - set(fixed_members))
    random.shuffle(remaining_members)
    random_members = random.sample(remaining_members, 4)  # Now selecting 4 instead of 5 since Enaas is fixed
    
    return fixed_members + random_members, all_members  # Return full list for blinking effect

def blinking_selection_animation(all_members, selected_pool, display_placeholder):
    for _ in range(20):  # Slower blinking effect
        selected_name = random.choice(all_members)  # Blink from full list
        display_placeholder.markdown(f"<h2 style='text-align: center;'>🔄 {selected_name} 🔄</h2>", unsafe_allow_html=True)
        time.sleep(0.3)
    
    selected = random.choice(selected_pool)
    selected_pool.remove(selected)
    return selected

def main():
    st.title("🔮 Random Member Selector")
    
    if st.button("Start Selection 🎲"):
        selected_members = []
        all_candidates, all_members = select_members()
        remaining_pool = all_candidates.copy()
        
        display_placeholder = st.empty()
        
        for _ in range(10):
            selected = blinking_selection_animation(all_members, remaining_pool, display_placeholder)
            display_placeholder.markdown(f"<h1 style='text-align: center;'>🎉 {selected} 🎉</h1>", unsafe_allow_html=True)
            selected_members.append(selected)
            time.sleep(1.5)
        
        time.sleep(1)
        
        st.write("### 🎊 Final Selected Members 🎊")
        final_placeholder = st.empty()
        
        for _ in range(3):
            final_placeholder.markdown("<h2 style='text-align: center;'>✨✨✨✨✨</h2>", unsafe_allow_html=True)
            time.sleep(0.7)
            final_placeholder.markdown("<h2 style='text-align: center;'>🎇🎇🎇🎇🎇</h2>", unsafe_allow_html=True)
            time.sleep(0.7)
        
        final_placeholder.empty()
        
        for member in selected_members:
            st.markdown(f"<h3 style='text-align: center; color: green;'>✅ {member}</h3>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
