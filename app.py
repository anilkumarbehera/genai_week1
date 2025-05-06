import streamlit as st
from PIL import Image

st.title('Hello, Streamlit!')
st.header('hello world')
st.text('Hii this is Anil')

st.text_input('Enter your name')
st.text_area('description', "This is genai class")

image_file = "sw.png"
image_bytes = Image.open(image_file)
st.image(image_bytes)

audio_file = "sw_speech.mp3"
audio_bytes = open(audio_file, "rb") 
#  "rb" means read bytes
st.audio(audio_bytes)

video_file = "sw_speech.mp4"
video_bytes = open(video_file, "rb")
st.video(video_bytes)

url = st.text_input("Enter a URL")

if st.button("Submit"):
  st.video(url)

