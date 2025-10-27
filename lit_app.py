import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")

st.title("🎮 Rock Paper Scissors Game")

# Game options
choices = ["Rock", "Paper", "Scissors"]

# User choice input
user_choice = st.radio("Choose your move:", choices, horizontal=True)

# Play button
if st.button("Play"):
    computer_choice = random.choice(choices)

    st.write(f"🤖 **Computer chose:** {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "🎉 You Win!"
    else:
        result = "😢 You Lose!"

    # Display result
    st.markdown(f"## {result}")

# Optional styling
st.markdown("""
    <style>
    .stRadio > div { justify-content: center; }
    button { width: 100%; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)
