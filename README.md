# GENERATIVE-TEXT-MODEL

*COMPANY *: CODTECH IT SOLUTIONS

*NAME *: RIDHI SINGLA

*INTERN ID *: CT04DR441

*DOMAIN *: ARTIFICIAL INTELLIGENCE 

*DURATION *: 4 WEEEKS

*MENTOR *: NEELA SANTOSH

### 📋 Project Description

This project is a **Generative Text Web App** built using **Flask** and **Ollama**.
It allows users to enter any topic or question, and the app generates **2–3 detailed paragraphs** of coherent, creative text using a **locally running AI model** (like **LLaMA 3**).

💡 The best part?
It works **entirely offline** — no cloud APIs, no internet connection, and no data sent outside your device.
Everything runs on your **local machine** via **Ollama**.

---

### 🧰 Tech Stack

* **Python 3.x**
* **Flask (Backend Web Framework)**
* **HTML/CSS (Frontend)**
* **Ollama (Local AI Model Runner)**
* **LLaMA 3 / Mistral / Gemma (Offline LLM Models)**

---

### ⚙️ Features

✅ Generate meaningful, grammatically correct text for any topic
✅ Output includes **2–3 detailed paragraphs (150–250 words)**
✅ Fully **offline** once the model is downloaded
✅ Clean, modern user interface
✅ User input remains visible after generation
✅ Simple and lightweight Flask app (no external dependencies)

---

### 🚀 How It Works

1. The user enters a **topic/question** in the text box.
2. Flask sends the prompt to the **local Ollama server** running at `http://localhost:11434`.
3. Ollama processes the request using your **locally installed LLM** (e.g., `llama3`).
4. The generated text is displayed instantly on the webpage.

No internet. No API keys. 100% local processing. 🔒

---

### 🧩 Project Structure

```
├── app.py                # Flask backend logic
├── templates/
│   └── index.html        # Frontend (HTML + CSS)
└── README.md             # Project documentation
```

---

### ⚡ Installation & Setup

#### 1️⃣ Install Ollama

Download and install Ollama from:
👉 [https://ollama.ai/download](https://ollama.ai/download)

Once installed, open a terminal and pull your model (e.g., LLaMA 3):

```bash
ollama pull llama3
```

#### 2️⃣ Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

Install Flask and Requests:

```bash
pip install flask requests
```

#### 3️⃣ Start Ollama (runs locally)

```bash
ollama serve
```

This starts the local API server at `http://localhost:11434`.

#### 4️⃣ Run the Flask App

In another terminal, run:

```bash
python app.py
```
Then open your browser and visit:

```
http://127.0.0.1:5000
```

### 🌐 Offline Functionality

This project works **100% offline** after setup:

* The AI model (LLaMA 3) runs locally through **Ollama**.
* Flask runs locally on your machine.
* All requests stay on `localhost` (no external calls or APIs).
* You can even **disable Wi-Fi** and the app will still function normally.

### 🧑‍💻 Example (OUTPUT)

