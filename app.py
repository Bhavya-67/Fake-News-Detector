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
    if news.strip() == "":
        st.warning("Please enter some news text")
    else:
        fake_keywords = ["rumor", "cure all", "viral post", "internet shutdown"]

        if any(word in news.lower() for word in fake_keywords):
            st.error("Fake News ❌")
        else:
            st.success("Real News ✅")
