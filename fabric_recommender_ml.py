import os
import joblib

MODEL_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(MODEL_DIR, "fabric_model.pkl"))
le_garment = joblib.load(os.path.join(MODEL_DIR, "le_garment.pkl"))
le_season = joblib.load(os.path.join(MODEL_DIR, "le_season.pkl"))
le_style = joblib.load(os.path.join(MODEL_DIR, "le_style.pkl"))
le_fabric = joblib.load(os.path.join(MODEL_DIR, "le_fabric.pkl"))

def recommend_fabric_ml(garment, season, style):
    g = le_garment.transform([garment])[0]
    s = le_season.transform([season])[0]
    st = le_style.transform([style])[0]
    pred_encoded = model.predict([[g, s, st]])[0]
    return f"Recommended fabric: {le_fabric.inverse_transform([pred_encoded])[0]}"
