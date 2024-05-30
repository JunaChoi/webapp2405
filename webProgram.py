import streamlit as st
import requests

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}',
    }
    data = {
        'prompt': input_text,
        'temperature': 0.7,
        'max_tokens': 150,
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json=data, headers=headers)
    if response.status_code == 200:
        st.info(response.json()['choices'][0]['text'])
    else:
        st.error('오류가 발생했습니다. OpenAI API 키를 확인해 주세요.')

with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
