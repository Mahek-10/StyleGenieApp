# 👗 StyleGenie: AI-Powered Personalized Dress Designer

StyleGenie is a Streamlit web app that helps users generate stylish outfit designs using AI. Users can:
- Get outfit suggestions
- Generate color palettes
- Receive fabric recommendations
- View simulated or AI-generated dress designs
- Save, load, and give feedback on designs
- Upload their virtual wardrobe
- Take a fashion personality quiz!

## 🧠 Features
- AI Outfit Generator
- Color Palette Creator
- Fabric Recommendation Engine
- AI Dress Design using DALL·E
- Personal Wardrobe Upload & Style Quiz
- Save & Load Designs
- Feedback & Smart Color Matching

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/stylegenie.git
cd stylegenie
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
Create a `.streamlit/secrets.toml` file:
```toml
openai_api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 4. Run the app
```bash
streamlit run streamlit_app.py
```

---

## 📦 Folder Structure
- `utils/` – Logic for AI, color, and fabric recommendation
- `uploads/` – For image uploads
- `user_data/` – Saved user preferences
- `users.txt` – Login system backend

## 🛡️ Disclaimer
For educational use only. OpenAI API key required for image generation.
