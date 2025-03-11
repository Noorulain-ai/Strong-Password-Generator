import streamlit as st
import re
import random
import string
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Strong Password Generator", page_icon="🔐", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        body { background-color: #0E1117t; }
        .title { color: #FF5733; text-align: center; font-size: 40px !important; font-weight: bold; text-decoration: underline; }
        .subtitle { text-align: center; color: #EFC4C4; font-size: 18px; }
        .password-box { background-color: #1E88E5; padding: 10px; border-radius: 10px; text-align: center; font-size: 20px; color: white; }
        .strength-bar { height: 20px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- Password Strength Checker ---
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# --- Password Generator ---
def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# --- UI Layout ---
st.markdown('<p class="title">🔐 Strong Password Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Generate <b>highly secure passwords</b> with custom length, symbols, and a graphical strength meter! 🔑</p>', unsafe_allow_html=True)

password_length = st.slider("🔢 Password Length:", 6, 30, 12)
use_upper = st.checkbox("🔠 Include Uppercase Letters")
use_digits = st.checkbox("🔢 Include Numbers")
use_special = st.checkbox("💥 Include Special Characters")

if st.button("🔄 Generate Password"):
    password = generate_password(password_length, use_upper, use_digits, use_special)
    strength, feedback = check_password_strength(password)
    
    st.markdown(f'<p class="password-box">🔑 {password}</p>', unsafe_allow_html=True)
    
    # --- Strength Meter ---
    colors = ["#E53935", "#FB8C00", "#43A047", "#1E88E5"]
    strength_labels = ["Weak", "Moderate", "Strong", "Very Strong"]
    
    st.progress(strength / 4)
    st.write(f"**Password Strength:** {strength_labels[strength-1]}")
    
    if feedback:
        st.warning("\n".join(feedback))

# --- Footer ---
st.markdown('<p style="text-align: center; color: #D49DA4;">🚀 Developed by <b>Noor Ul Ain</b> using Python & Streamlit</p>', unsafe_allow_html=True)
