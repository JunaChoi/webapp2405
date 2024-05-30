import streamlit as st
import random

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

def generate_response(input_text):
    # 랜덤한 이모티콘 선택
    emoticons = ['😊', '😄', '😃', '🤖', '👍', '🌟', '🎉', '🚀', '💡']
    response = random.choice(emoticons)
    st.info(response)

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
