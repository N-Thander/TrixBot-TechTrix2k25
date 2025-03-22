
# **TrixBot - TechTrix 2K25**  

## 🌟 About  
TrixBot is an AI-driven chatbot built for **TechTrix 2025**, designed to assist participants with event information, flagship programs, and even allow easy registrations! Deployed on **Hugging Face Spaces**, TrixBot is your go-to virtual assistant for TechTrix.  

> 🛠 **This project will remain live until the next TechTrix event!**  

---

## 🔗 **Project Links**  

- **🤗 Hugging Face Repository:** [View Repository](https://huggingface.co/spaces/NThander2002/TrixBot-Chat/tree/main)  
- **🚀 Deployed Backend:** [Try It Here](https://nthander2002-trixbot-chat.hf.space/docs)  
- **🌐 TechTrix 2025 Official Website:** [Visit Now](https://techtrix.rcciit.org.in/)  

---

## 📂 **Project Structure**  
```
TrixBot-TechTrix2k25
├── app
│   ├── core
│   │   ├── config.py         # Configuration settings
│   │   └── security.py       # Security utilities
│   ├── __init__.py
│   ├── main.py               # Main API server
│   ├── routes
│   │   ├── chat.py           # Chatbot API routes
│   │   ├── health.py         # Health check endpoint
│   │   └── root.py           # Root endpoints
│   └── services
│       └── rag_service.py    # RAG (Retrieval-Augmented Generation) implementation
├── data                      # Stores event-related data
├── Dockerfile                # Docker container configuration
├── LICENSE                   # Open-source license (Apache 2.0)
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
└── temp
    ├── .cache                # Temporary cache directory
```

---

## 🚀 **Room for Improvements**  

🔹 **Upgrade Vector Database**  
- Replace FAISS with a **more scalable vector database** like **AstraDB** or **Milvus**.  

🔹 **Agentic AI for Registration**  
- Implement **agentic AI capabilities** so users can **register directly** by chatting with TrixBot.  

🔹 **CD/CD Pipelines**  
- Implement **CI/CD pipeline** for smoother updates.  

---

## 🛠 **Installation & Running Locally**  

```bash
# Clone the repository
git clone https://github.com/yourusername/TrixBot-TechTrix2k25.git
cd TrixBot-TechTrix2k25

# Install dependencies
pip install -r requirements.txt

# Run the application
python app/main.py
```

---

## 📜 **License**  
**Apache 2.0** - Feel free to modify, improve, and tweak this project for your own chatbot needs!  

📝 **License File:** [LICENSE](./LICENSE)  

---

🔥 **Built with Passion for TechTrix 2025!** 🚀  

---
