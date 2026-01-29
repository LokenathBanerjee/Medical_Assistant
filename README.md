# 🩺 AI Medical Assistant (Streamlit + Gemini)

An intelligent **AI-powered Medical Assistant** built using **Streamlit** and **Google Gemini API**.  
The system interacts like a doctor by asking step-by-step questions, detects medical emergencies, restricts non-medical queries, and provides safe diagnostic suggestions with medicine recommendations.

---

## 🚀 Features

- ✅ **Doctor-like step-by-step questioning**
- 🚨 **Automatic emergency detection** (calls 112 advice)
- 🔒 **Medical-only query guard**
- 💊 **Medicine suggestions** (Cheap / Moderate / Expensive in INR)
- 🧠 **AI-powered diagnosis using Google Gemini**
- ♻️ **Session-based patient memory**
- 🖥️ **Simple & clean Streamlit UI**

---

## 🧩 Project Structure

medical_assistant/
│
├── app.py # Streamlit UI entry point
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .env # Environment variables (API key)
├── .gitignore
│
├── llm/
│ └── gemini_langchain.py # Gemini API integration
│
└── logic/
├── chat_controller.py # Main conversation flow
├── diagnosis_flow.py # Adaptive questioning logic
├── emergency.py # Emergency detection & message
├── medical_guard.py # Medical-only question filter
└── answer_guard.py # Follow-up answer validation            

---

## 🧠 How It Works

1. User starts chat
2. Assistant asks **5 structured medical questions**
3. Answers are stored in session memory
4. Emergency keywords are checked **on every message**
5. After all questions:
   - Probable diagnosis
   - Medicine options (INR)
   - Home care advice
   - Medical disclaimer

---

## ⚠️ Emergency Detection

The assistant immediately stops and shows an emergency alert if it detects:
- Chest pain
- Severe bleeding
- Breathing difficulty
- Seizures
- Unconsciousness
- Accidents or poisoning

📞 **Emergency number used:** 112 (India)

---

## 🔐 Medical Guard

If the user asks **non-medical questions**, the assistant responds with:

> ⚠️ I am designed to answer medical-related questions only.

This ensures **domain safety**.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/medical_assistant.git
cd medical_assistant
2️⃣ Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Setup environment variables
Create a .env file:
streamlit run app.py
⚕️ Medical Disclaimer

This application is NOT a replacement for a licensed medical professional.
The information provided is for educational purposes only.
Always consult a qualified doctor for diagnosis and treatment.

🧪 Tech Stack

Python

Streamlit

Google Gemini API

Session-based state management

Rule-based medical safety layers

🌟 Future Enhancements

Patient history persistence (database)

Multi-language support

Voice-based interaction

PDF prescription generation

Doctor login panel

👨‍💻 Authors

1. Lokenath Banerjee
B.Tech CSE (AI & ML)
Haldia Institute of Technology

2. Ayush Raj
B.Tech CSE (AI & ML)
Haldia Institute of Technology

3. Prakriti Dheeraj
B.Tech CSE (AI & ML)
Haldia Institute of Technology

4. Manidipa Mandal
B.Tech CSE (DS)
Haldia Institute of Technology

5. Raisa Sharfeen
B.Tech CSE (AI & ML)
Haldia Institute of Technology