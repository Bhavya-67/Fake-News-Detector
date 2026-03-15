import base64

def set_bg():
    with open("background.jpeg","rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-position: center;
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_bg()
