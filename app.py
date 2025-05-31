import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")
st.divider()

st.write('Check your sentences here')

user_input  = st.text_input("Enter your sentence")


if user_input:
    blob =  TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        st.write("Positive")
    elif sentiment < 0 :
        st.write("Negative")
    else:
        st.write("Neutral")

    st.write(f"Sentiment Score : {sentiment}")