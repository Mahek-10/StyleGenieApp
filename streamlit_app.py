import streamlit as st
from fabric_recommender_rule import recommend_fabric_rule
from fabric_recommender_ml import recommend_fabric_ml

st.title("🧵 Hybrid Fabric Recommender")

garment = st.selectbox("Select Garment Type", ["Shirt", "Pants", "Dress", "Jacket"])
season = st.selectbox("Select Season", ["Summer", "Winter"])
style = st.selectbox("Select Style", ["Casual", "Formal"])
mode = st.radio("Choose Recommendation Mode", ["Rule-Based", "Machine Learning (ML)"])

if st.button("Recommend Fabric"):
    if mode == "Rule-Based":
        result = recommend_fabric_rule(garment, season, style)
    else:
        result = recommend_fabric_ml(garment, season, style)
    st.success(result)
