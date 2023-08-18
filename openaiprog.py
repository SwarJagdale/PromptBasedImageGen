import openai
import requests
from PIL import Image
from io import BytesIO
import streamlit as st

st.title('Prompt Based Image Generation')
# Replace with your API key
openai.api_key = 'your_api_key'

prompt= st.text_input("How can I help you")
keep_prompting= st.button("Go")
if keep_prompting:
    response = openai.Image.create(prompt=prompt,size="512x512",response_format="url")
    image_url = response["data"][0]["url"]
    response = requests.get(image_url)
    img_bytes = BytesIO(response.content)
    img = Image.open(img_bytes)
    st.image(img)
    keep_prompting=False
