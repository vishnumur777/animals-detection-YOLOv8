import streamlit as st
import os
import time

st.title("Marine Animals detection")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  st.header("Preview")
  st.image(uploaded_file)
  if st.button("Predict"):
    with st.spinner('Wait for predicted results...'):
      os.system(f"cp images/{uploaded_file.name} {uploaded_file.name}")
      os.system(f"yolo task=detect mode=predict model=yolov8m-marine.pt conf=0.5 source={uploaded_file.name}")
    st.success(uploaded_file.name)
    st.image(f"/home/hdd/pythonPract/miniproject/runs/detect/predict/{uploaded_file.name}")
    os.system(f"rm -rf {uploaded_file.name}")
else:
  os.system(f"rm -rf /home/hdd/pythonPract/miniproject/runs")
  

hide = """<style>
	#MainMenu {visbility: hidden;}	
	footer {visibility: hidden;}
	header {visibility: hidden;}
	</style?"""

st.markdown(hide,unsafe_allow_html=True)

bk = """<style>.css-102e70e{
  background-color: #000000;
  </style?"""

st.markdown(bk,unsafe_allow_html=True)
