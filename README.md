# AI Notes Summarizer 🧠✨

An AI-powered web application built using **Flask** and **Hugging Face Transformers** that generates concise summaries from long notes or text.  
The application uses the **T5 (Text-to-Text Transfer Transformer)** model for abstractive text summarization.

---

## 🚀 Features

- Paste long notes and generate a concise summary
- Uses **T5-small** transformer model
- Clean and minimal UI with **Bootstrap 5**
- Loading spinner for better user experience
- Character counter and input validation
- Copy summary to clipboard
- Server-side rendering using **Jinja2**

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **AI / ML:** Hugging Face Transformers, PyTorch
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Model:** T5-small

---

## ⚙️ Installation & Setup

### 1 Clone the repository


### 2 Create and activate a virtual environment

python -m venv myEnv
myEnv\Scripts\activate      # Windows
# source myEnv/bin/activate # macOS/Linux

### 3 Install dependencies
pip install -r requirements.txt

### 4 Run the Application
python app.py
