import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")
st.title("🎮 Rock Paper Scissors")

# --- Game options ---
choices = ["ROCK", "PAPER", "SCISSORS"]

# --- Session State for persistent score ---
if "user_points" not in st.session_state:
    st.session_state.user_points = 0
if "comp_points" not in st.session_state:
    st.session_state.comp_points = 0
if "result" not in st.session_state:
    st.session_state.result = ""
if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""
if "comp_choice" not in st.session_state:
    st.session_state.comp_choice = ""

# --- Sidebar: Instructions ---
with st.sidebar:
    st.header("📋 Game Instructions")
    st.markdown("""
    **Rules to Remember:**
    - 🪨 Rock beats ✂️ Scissors  
    - ✂️ Scissors beat 📄 Paper  
    - 📄 Paper beats 🪨 Rock  
    """)
    st.info("🎮 Make your move wisely and see if you can beat the computer!")

# --- Display current score ---
st.markdown(f"### 🧮 Scoreboard")
st.write(f"**You:** {st.session_state.user_points} | **Computer:** {st.session_state.comp_points}")

# --- Game UI ---
st.markdown("### ✊ ✋ ✌️ Make Your Move:")
cols = st.columns(3)

with cols[0]:
    if st.button("🪨 ROCK"):
        st.session_state.user_choice = "ROCK"
with cols[1]:
    if st.button("📄 PAPER"):
        st.session_state.user_choice = "PAPER"
with cols[2]:
    if st.button("✂️ SCISSORS"):
        st.session_state.user_choice = "SCISSORS"

# --- Play round when user makes a choice ---
if st.session_state.user_choice:
    st.session_state.comp_choice = random.choice(choices)
    user = st.session_state.user_choice
    comp = st.session_state.comp_choice

    # Determine winner
    if user == comp:
        st.session_state.result = "It's a Tie! 😐"
    elif (user == "ROCK" and comp == "SCISSORS") or \
         (user == "PAPER" and comp == "ROCK") or \
         (user == "SCISSORS" and comp == "PAPER"):
        st.session_state.user_points += 1
        st.session_state.result = "🎉 You Won!"
    else:
        st.session_state.comp_points += 1
        st.session_state.result = "😢 You Lost!"

    # --- Display results ---
    st.markdown("---")
    st.subheader("🕹️ Round Result")
    st.write(f"**You chose:** {user}")
    st.write(f"**Computer chose:** {comp}")
    st.success(st.session_state.result)

# --- End Game button ---
if st.button("🏁 End Game"):
    st.markdown("## 🎯 Final Results")
    st.write(f"**Your Score:** {st.session_state.user_points}")
    st.write(f"**Computer Score:** {st.session_state.comp_points}")

    if st.session_state.user_points > st.session_state.comp_points:
        st.balloons()
        st.success("🏆 You Win the Game!")
    elif st.session_state.comp_points > st.session_state.user_points:
        st.error("🤖 Computer Wins!")
    else:
        st.info("⚖️ It's a Draw!")

    # Reset scores
    st.session_state.user_points = 0
    st.session_state.comp_points = 0
    st.session_state.result = ""
    st.session_state.user_choice = ""
    st.session_state.comp_choice = ""

# --- Styling ---
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        font-size: 18px;
        padding: 10px 0;
        border-radius: 10px;
    }
    .stAlert {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
