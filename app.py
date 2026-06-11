import streamlit as st
import spacy
import joblib
import numpy as np

nlp = spacy.load("en_core_web_lg")

model = joblib.load("fake_news_nb_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Fake News Detector")

st.write("Enter a news article and click Predict.")


news_text = st.text_area("News Article")

if st.button("Predict"):

    if news_text.strip() == "":
        st.warning("Please enter a news article.")
    else:

       
        vector = nlp(news_text).vector

        
        vector = np.array(vector).reshape(1, -1)

      
        vector_scaled = scaler.transform(vector)

        prediction = model.predict(vector_scaled)[0]

       
        if prediction == 1:
            st.success("Real News")
        else:
            st.error("Fake News")