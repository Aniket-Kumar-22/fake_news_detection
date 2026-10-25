import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = stopwords.words("english")

# Load saved model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)



# UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detection App")
st.write("Enter a news article and check whether it is **REAL** or **FAKE**")

# Clear function
def clear_text():
    st.session_state.news_text = ""

# Initialize session state
if "news_text" not in st.session_state:
    st.session_state.news_text = ""

user_input = st.text_area(
    "Paste News Text Here",
    key="news_text"
)

col1, col2 = st.columns(2)

with col1:
    check_button = st.button(
        "🔍 Check News",
        use_container_width=True
    )

with col2:
    st.button(
        "🗑️ Clear",
        on_click=clear_text,
        use_container_width=True
    )

if check_button:
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)

        if prediction[0] == 1:
            st.success("✅ This looks like REAL news")
        else:
            st.error("❌ This looks like FAKE news")

st.markdown("---")
st.markdown("Built with ❤️ using Machine Learning")
