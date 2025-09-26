# 📰 Text Summarizer (Intern Assignment)

A tiny AI-powered app that takes any news article or blog post and summarizes it into exactly 3 sentences.

Output:

![Text Summarizer Screenshot](https://github.com/Saransh-aggarwal/Text-Summarizer-Intern-Assignment-/blob/main/text-summarizer.png)

---

## 🚀 Features

- **AI-Powered Summaries:** Summarizes any article/blog post into exactly 3 sentences.
- **Modern API:** Built using Python and the Google Gemini API.
- **Simple UI:** Features a clean Streamlit interface where users can paste text and get a summary in their browser.
- **Extendable:** The code is structured to be easily extendable (e.g., to fetch article text directly from a URL).

---

## ⚙️ Setup Instructions

### 1. Install Python
Make sure you have Python 3.8+ installed. You can check your version by running:
```bash
python --version
```

### 2. Clone this Repository
Open your terminal and run the following commands:
```bash
git clone https://github.com/YOUR-USERNAME/text-summarizer.git
cd text-summarizer
```

### 3. Create a Virtual Environment (Optional but Recommended)
A virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
My `requirements.txt` contains:
```
streamlit
google-generativeai
```
Install them by running:
```bash
pip install -r requirements.txt
```

### 5. Get a Gemini API Key
1. Go to **[Google AI Studio](https://aistudio.google.com/)**.
2. Click on "**Get API key**" and generate a new key.
3. Copy the key and open the `app.py` file in this project.
4. Replace the placeholder with your actual key:
   ```python
   # In app.py
   API_KEY = "YOUR_API_KEY"
   ```

---

## 🖥️ Running the App

⚠️ **Important:** Do not run with `python app.py`. Streamlit apps must be launched with the `streamlit` command.

In your terminal, run the following command from the project directory:
```bash
streamlit run text_summarizer.py
```
This will automatically open the application in your default web browser at:
👉 **http://localhost:8501**

Simply paste an article into the text box, click the "Summarize" button, and get your 3-sentence summary!

---

## 🛠️ What I Tried & Learned

#### ✅ Step 1: Basic Summarizer (Command Line)
I started by writing a simple Python script (`summarizer.py`) that took text as input and printed a summary to the console. This helped me verify that the `google-generativeai` library was working correctly with the `gemini-flash` model.


#### ✅ Step 2: Building the Streamlit UI
Once the backend was working, I created the user interface in `app.py`. I added a text area for user input, a button to trigger the summarization, and a clean subheader to display the final summary.

#### ⚠️ Issue: Streamlit "Bare Mode" Error
Initially, I tried to run the Streamlit app using the standard Python command:
```bash
python app.py
```
This resulted in a `missing ScriptRunContext!` error. After some research, I learned that Streamlit applications have their own lifecycle and must be run using the dedicated `streamlit run` command. This was a key learning moment.

---

## 👨‍💻 Author

Built by **Saransh Aggarwal** as part of an Intern Assignment.
