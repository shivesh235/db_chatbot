# AI-Powered Chatbot for Suppliers

## Overview
This project is an AI-powered chatbot system designed to facilitate supplier and product queries. It includes a FastAPI backend, a LangGraph-based chatbot agent, SQLAlchemy ORM for database interactions, and a Hugging Face transformer-based language model. The frontend is built using React, Material-UI, Redux, and Axios for seamless user interaction.

## Features
- **FastAPI Backend** for handling chatbot requests.
- **LangGraph-based Chat Agent** for query classification and information retrieval.
- **PostgreSQL Database** using SQLAlchemy ORM to store supplier and product information.
- **Hugging Face Transformer Model** for generating responses.
- **React Frontend** with Material-UI and Redux for managing chat interactions.
- **REST API** for communication between frontend and backend.

---

## Project Structure
```
supplier_chatbot/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── database.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── chat_agent.py
│   └── utils/
│       ├── __init__.py
│       └── llm_utils.py
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components/
│   │   │   ├── ChatInterface.js
│   │   │   ├── MessageHistory.js
│   │   │   └── QueryInput.js
│   │   ├── store/
│   │   │   ├── store.js
│   │   │   └── chatSlice.js
│   │   └── services/
│   │       └── api.js
└── requirements.txt
```

---

## Setup & Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/supplier_chatbot.git
cd supplier_chatbot
```

### **2. Setup Backend**
#### **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### **Install Dependencies**
```bash
pip install -r requirements.txt
```
#### **Configure Database**
Modify `backend/config.py` with your database credentials.
Create the database tables:
```bash
python -c "from backend.database.database import Base, engine; Base.metadata.create_all(bind=engine)"
```
#### **Run FastAPI Server**
```bash
uvicorn backend.main:app --reload
```
The server will start at `http://127.0.0.1:8000/`.

---

### **3. Setup Frontend**
```bash
cd frontend
npm install
npm start
```
The frontend will be available at `http://localhost:3000/`.

---

## API Endpoints
### **Chat API**
- **POST** `/api/chat`
  - **Request Body:** `{ "text": "Find me a supplier for electronics" }`
  - **Response:** `{ "response": "Here is the supplier information..." }`

### **Swagger API Documentation**
Access the interactive docs at:
```
http://127.0.0.1:8000/docs
```

---

## Testing the Chatbot

### **1. Test with cURL**
```bash
curl -X POST "http://127.0.0.1:8000/api/chat" -H "Content-Type: application/json" -d '{"text": "List all suppliers"}'
```

### **2. Test with Python Requests**
```python
import requests

url = "http://127.0.0.1:8000/api/chat"
data = {"text": "What products do you have?"}

response = requests.post(url, json=data)
print(response.json())
```

---

## Technology Stack
### **Backend:**
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- LangGraph
- Hugging Face Transformers
- Pydantic

### **Frontend:**
- React
- Material-UI
- Redux Toolkit
- Axios

---

## Debugging & Logs
Run FastAPI with debug mode:
```bash
uvicorn backend.main:app --reload --log-level debug
```
Check Redux state in **Chrome DevTools** (`F12` → Redux tab).

---

## Future Enhancements
- Add authentication (JWT-based login)
- Implement real-time chat with WebSockets
- Deploy to cloud (AWS/GCP/Azure)

---

## Contributors
- **Shivesh Singh** - Developer

---

## License
This project is licensed under the MIT License.

