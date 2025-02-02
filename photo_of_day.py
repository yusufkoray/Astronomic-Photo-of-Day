import streamlit as st
import requests

api_key="NdprQHWFOD8f01CslqWZVHmz1bqlVop9iGVU16ch"
url="https://api.nasa.gov/planetary/apod?"\
    f"api_key=DEMO_KEY"
response1=requests.get(url)
data=response1.json()

date=data["date"]
title=data["title"]
explanation=data["explanation"]

image_filepath="image.jpg"

url_image=data["url"]

response2=requests.get(url_image)

with open(image_filepath,"wb") as file:
    file.write(response2.content)

st.title(date)
st.title(title)
st.image(image_filepath)
st.text(explanation)

print(url_image)
print(data)