import streamlit as st
from transformers import pipeline

# @st.cache_data: use tasks relevant to load data
# @st.cache_resource: use for ML model, connect to database
# https://docs.streamlit.io/develop/concepts/architecture/caching

@st.cache_resource
def load_model():
    classifier = pipeline("sentiment-analysis")
    return classifier

classifier = load_model()

st.title("Check up your status")

stt = st.text_area("Enter your status")
# st.write(f"You entered: {stt}")

stt = stt.split('.')
print(stt)
if stt[-1] == '':
    stt = stt[:-1]

if st.button("Submit"):
    rs = classifier(stt)
    st.write('Prediction :sunglasses:')
    for element in rs:
        # st.write(f"label: {element['label']}, with score: {round(element['score'], 4)}")
        st.write(element)
        # st.write(element)
else:
    st.write('Please, press "Submit" to submit your status')
