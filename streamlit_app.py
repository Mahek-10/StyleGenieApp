import streamlit as st
import os
import json
import openai
from PIL import Image
from utils.ai_model import generate_outfit
from utils.color_palette import generate_palette
from utils.fabric_recommender import recommend_fabric

# Set API key from secrets
openai.api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else os.getenv("OPENAI_API_KEY")

# Setup
UPLOAD_FOLDER = 'uploads'
USER_DATA = 'user_data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(USER_DATA, exist_ok=True)
USER_FILE = 'users.txt'
users = {}

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            for line in f:
                uname, pwd = line.strip().split(',')
                users[uname] = pwd

def save_user(username, password):
    with open(USER_FILE, 'a') as f:
        f.write(f"{username},{password}\n")

load_users()

def login_ui():
    st.title("👗 StyleGenie Login")
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
    with login_tab:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state["username"] = username
                st.success("Logged in successfully!")
            else:
                st.error("Invalid credentials")
    with signup_tab:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            if new_user in users:
                st.error("Username already exists")
            else:
                save_user(new_user, new_pass)
                st.success("User registered! Please login.")

def main_ui():
    st.title(f"🎨 Welcome, {st.session_state['username']}!")

    st.header("1. Outfit Generator")
    prompt = st.text_input("Describe your occasion/style:")
    if st.button("Generate Outfit"):
        if prompt:
            outfit = generate_outfit(prompt)
            st.success(outfit)

    st.header("2. Color Palette")
    base_color = st.color_picker("Choose a base color")
    if st.button("Generate Palette"):
        palette = generate_palette(base_color)
        st.write(palette)

    st.header("3. Fabric Recommendation")
    fabric_type = st.selectbox("Select clothing item", ["Shirt", "Pants", "Jacket", "Dress"])
    season = st.selectbox("Season", ["Summer", "Winter"])
    style = st.selectbox("Style", ["Casual", "Formal"])
    if st.button("Recommend Fabric"):
        fabric = recommend_fabric(fabric_type, season, style)
        st.info(fabric)

    st.header("4. Create My Dress 🎨👗")
    gender = st.selectbox("Gender", ["Female", "Male", "Unisex"])
    dress_type = st.selectbox("Dress Type", ["Gown", "Kurta", "Suit", "Jacket", "Casual Wear", "Ethnic Wear"])
    occasion = st.text_input("Occasion (e.g., Wedding, Party, Office)")
    if st.button("Create Dress"):
        palette = generate_palette(base_color)
        fabric = recommend_fabric(fabric_type, season, style)
        outfit = generate_outfit(occasion)
        st.subheader("🧵 Dress Design Summary")
        st.markdown(f"**Occasion:** {occasion}")
        st.markdown(f"**Style:** {style}")
        st.markdown(f"**Season:** {season}")
        st.markdown(f"**Base Color:** {base_color}")
        st.markdown(f"**Suggested Palette:** {palette}")
        st.markdown(f"**Recommended Fabric:** {fabric}")
        st.markdown(f"**Outfit Suggestion:** {outfit}")
        try:
            image_prompt = f"A {gender.lower()} {dress_type.lower()} for a {occasion.lower()} in {season.lower()} season. Style: {style.lower()}, color: {base_color}."
            response = openai.Image.create(prompt=image_prompt, n=1, size="512x512")
            image_url = response['data'][0]['url']
            st.image(image_url, caption="AI-Generated Dress", use_column_width=True)
        except Exception as e:
            st.warning(f"Image generation failed: {e}")

    st.header("5. AI Stylist Tips 💄")
    st.markdown("Accessories: Silver heels, clutch bag\nMakeup: Neutral tones\nHairstyle: Soft curls or bun")


    st.header("7. Feedback 📣")
    feedback = st.radio("Do you like this design?", ["👍 Yes", "👎 No"])
    if st.button("Submit Feedback"):
        st.success("Thanks for your feedback!")

    st.header("8. Smart Color Suggestions 🎨")
    st.write(f"Recommended matches for {base_color}: {generate_palette(base_color)}")

  
    st.header("10. Style Quiz 🎯")
    q1 = st.selectbox("Weekend outfit:", ["Jeans & Tee", "Boho Dress", "Power Suit", "Athleisure"])
    q2 = st.selectbox("Color palette:", ["Earth Tones", "Brights", "Monochrome", "Pastels"])
    if st.button("Find My Style"):
        if "Boho" in q1 or "Earth" in q2:
            st.success("You're a Bohemian Fashionista 🌼")
        elif "Power" in q1:
            st.success("You're a Minimalist Maven 🖤")
        elif "Athleisure" in q1:
            st.success("You're Sporty & Chic 🧢")
        else:
            st.success("You're a Casual Cool Cat 😎")

  

def app():
    if "username" not in st.session_state:
        login_ui()
    else:
        main_ui()

if __name__ == "__main__":
    app()
