import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline ("summarization",model="sshleifer/distilbar-cnn-12-6")
  summarizer = load_summarizer()
  st.title("AI text summarizer")
  st.erite("enter a loge text below,and get a concise summeary!")
  long_text = st.text_area("enter text to summarize:",height=200)

max_length = st.slider("max Summary Length",min_value=50,
                       max_values=300,value=30)
min_length = st.slider("Min Summary Length", min_value=20, max_value=100, value=30)

if st.button("Summarize"):
    if long_text:
        summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=False)
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text!")
  
