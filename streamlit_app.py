import streamlit as st
from fabric_recommender_ml import recommend_fabric_ml

st.title("🧵 ML-Based Fabric Recommender")

garment = st.selectbox("Select Garment Type", ["Shirt", "Pants", "Dress", "Jacket"])
season = st.selectbox("Select Season", ["Summer", "Winter"])
style = st.selectbox("Select Style", ["Casual", "Formal"])

if st.button("Recommend Fabric"):
    result = recommend_fabric_ml(garment, season, style)
    st.success(result)
