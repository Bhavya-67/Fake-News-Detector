import streamlit as st

page_bg = """
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1504711434969-e33886168f5c");
background-size: cover;
background-position: center;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("📰 Fake News Detector")

news = st.text_area("Enter News Text")

if st.button("Check News"):
    st.success("Prediction will appear here")
