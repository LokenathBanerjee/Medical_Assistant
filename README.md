# 🩺 AI Medical Assistant

An intelligent **clinical-style AI assistant** that performs step-by-step symptom analysis, asks follow-up questions like a doctor, checks emergency conditions, and finally provides **diagnosis guidance + exact medicine recommendations with cheap vs expensive alternatives**.

Built with **LLM + Medical Logic + RAG + Voice Assistant + Memory**.

---

## 📖 About This Project

The **AI Medical Assistant** simulates a clinical consultation process using Artificial Intelligence.  
It interacts with users step-by-step, gathers symptom information, evaluates safety conditions, and provides structured medical guidance along with medicine suggestions.

This project demonstrates:

- Conversational AI in healthcare  
- Rule-based medical reasoning  
- LLM-powered diagnosis-style analysis  
- Retrieval Augmented Generation (RAG)  
- Voice-based symptom input  
- Structured symptom extraction  
- Medicine recommendation with price comparison  

⚠️ The system focuses on **guidance**, not medical diagnosis replacement.

---

## 🚀 Features

✅ Conversational medical symptom checker  
✅ Step-by-step questioning (sequence-to-sequence interaction)  
✅ Emergency symptom detection (safety first)  
✅ Only answers medical-related queries  
✅ Extracts structured data:
- Symptoms  
- Duration  
- Temperature  
- Severity  

✅ Memory of entire session  
✅ RAG (Retrieval Augmented Generation) for medical knowledge  
✅ Diagnosis-style explanation  
✅ 💊 Medicine recommendation system:
- Exact medicine names  
- Cheap vs Expensive comparison  
- Dosage guidance  
- Warnings  

✅ 🎙️ Voice Assistant (Speech-to-Text)  
✅ Modern medical-themed UI (custom CSS)

---

## 🧠 System Architecture

User Input (Text / Voice)  
⬇  
**app.py** (UI + session memory)  
⬇  
**agent/router.py** (Conversation controller)  
⬇  
Medical Logic + LLM + RAG  
⬇  
Diagnosis + Medicine Recommendation  

---

## 📁 Project Structure

```
medical_ai_agent/
│
├── app.py                  → Streamlit UI + CSS + Chat Interface
├── .env                    → API keys
│
├── agent/
│   ├── router.py           → Main conversation logic
│   ├── gemini_agent.py     → LLM API calls (Groq/Gemini)
│   ├── memory.py           → Chat memory handling
│   ├── prompt.py           → Prompt templates
│
├── medical_logic/
│   ├── symptom_rules.py    → Extracts symptoms/duration/temp/severity
│   ├── emergency.py        → Emergency detection
│   ├── medicines.py        → Medicine recommendation engine
│
├── rag/
│   ├── retriever.py        → Fetches medical knowledge
│   ├── vectorstore.py      → Embedding storage
│   ├── loader.py           → Loads documents
│
├── voice/
│   ├── speech_to_text.py   → Voice input
│   ├── text_to_speech.py   → Voice output
│
└── utils/
    └── validators.py       → Medical query validation
```

---

## ⚙️ Tech Stack

| Category | Tools Used |
|---------|-------------|
| LLM | Groq (LLaMA 3) / Gemini |
| Framework | Streamlit |
| Voice | SpeechRecognition, pyttsx3 |
| Memory | Session-based chat memory |
| RAG | FAISS / LangChain retriever |
| Backend | Python |
| UI | Custom CSS in Streamlit |

---

## 🎙️ Voice Support

The assistant can:
- Listen to symptoms via microphone  
- Convert speech to text  
- Continue the medical questioning flow  
- Provide final diagnosis + medicines  

---

## 💊 Medicine System

The assistant suggests medicines based on symptoms and guidance logic:

- Fever & pain relief  
- Cold and flu support  
- Dehydration & ORS  
- Acidity & stomach issues  
- Diarrhea care  
- Sore throat relief  

Each recommendation includes:
✔ Exact medicine names  
✔ Dosage guidance  
✔ Cheap vs expensive options  
✔ Safety warnings  

---

## 🚨 Safety Notice

This AI system is for **educational and informational purposes only**.  
It is **not a substitute for a licensed doctor**.  
In case of severe symptoms, always seek professional medical care.

---

## 🧾 Git Warning Note (Not an Error)

If you see messages like:

```
LF will be replaced by CRLF the next time Git touches it
```

This is **not an error**.  
It simply means Git is adjusting line endings between Linux and Windows formats.  
It does not affect your project functionality.

---

## 👨‍💻 Authors

| Name | Degree | Institute |
|------|--------|------------|
| **Lokenath Banerjee** | B.Tech CSE (AI & ML) | Haldia Institute of Technology |
| **Ayush Raj** | B.Tech CSE (AI & ML) | Haldia Institute of Technology |
| **Prakriti Dheeraj** | B.Tech CSE (AI & ML) | Haldia Institute of Technology |
| **Manidipa Mandal** | B.Tech CSE (DS) | Haldia Institute of Technology |
| **Raisa Sharfeen** | B.Tech CSE (AI & ML) | Haldia Institute of Technology |

---

## 🌟 Future Improvements

- Disease probability scoring  
- Prescription PDF generation  
- Multilingual voice support  
- Auto-filled consultation panel  
- Patient history storage
