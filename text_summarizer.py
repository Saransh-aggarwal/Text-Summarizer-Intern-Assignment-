import streamlit as st
import google.generativeai as genai

API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

def summarize_text(article: str) -> str:
    prompt = f"""
    Summarize the following article into exactly 3 sentences.
    Article:
    {article}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📰 Text Summarizer with Gemini")
st.write("Paste any news article or blog post below, and I'll summarize it into 3 sentences.")

article_text = st.text_area("Paste your article here:", height=200)

if st.button("Summarize"):
    if article_text.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(article_text)
        st.subheader("📌 Summary:")
        st.write(summary)
    else:
        st.warning("⚠️ Please paste some text to summarize.")
