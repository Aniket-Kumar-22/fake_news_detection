# Fake News Detection 📰

A Machine Learning web application that detects whether a news article is **REAL or FAKE** using TF-IDF vectorization, Logistic Regression, and Streamlit.

## 🚀 Features

- Detects whether a news article is real or fake.
- Uses Natural Language Processing (NLP) for text preprocessing.
- Converts text into numerical features using TF-IDF.
- Uses a trained Logistic Regression model for classification.
- Interactive web interface built with Streamlit.

## 🛠️ Tech Stack

- **Language:** Python
- **Machine Learning:** Scikit-learn, Logistic Regression
- **NLP:** NLTK, TF-IDF
- **Web Framework:** Streamlit
- **Data Processing:** Pandas
- **Model Storage:** Pickle
- **Dataset Storage:** Git LFS

## 📂 Project Structure

```text
fake_news_detection/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── news_detection.ipynb
├── dataset/
│   ├── Fake.csv
│   └── True.csv
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aniket-Kumar-22/fake_news_detection.git
cd fake_news_detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

The project uses two datasets:

- `Fake.csv` — fake news articles
- `True.csv` — real news articles

The dataset files are tracked using Git Large File Storage (Git LFS).

## 🧠 How It Works

1. The user enters a news article.
2. The text is cleaned using basic NLP preprocessing.
3. TF-IDF converts the text into numerical features.
4. The trained Logistic Regression model predicts the class.
5. The application displays the result as **REAL** or **FAKE**.

## 🌐 Deployment

This application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

1. Sign in using GitHub.
2. Select the `fake_news_detection`
