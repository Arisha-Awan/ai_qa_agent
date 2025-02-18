# AI-Powered Q&A Agent

This repository contains the code for an AI-powered Q&A agent built with:

- **Backend**: Flask
- **Frontend**: React
- **AI Integration**: OpenAI GPT API

## Features

- Accepts user queries and generates responses using an AI model.
- Maintains conversation history per user using LocalStorage.
- Provides a dynamic UI with chat bubbles for queries and responses.
- Implements error handling for better user experience.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Arisha-Awan/ai_qa_agent.git
cd ai-qa-agent
```

### 2. Backend Setup (Flask)

#### Install Dependencies

```sh
cd backend
##Create a Virtual Environment
python -m venv venv
##Activate Virtual Environment
venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the Flask Server

```sh
python app.py
```

The Flask backend will start at `http://127.0.0.1:5000`

---

### 3. Frontend Setup (React)

#### Install Dependencies

```sh
cd ../frontend
npm install
```

#### Run the React App

```sh
cd ai_agent_frontend
npm start
```

The frontend will be available at `http://localhost:3000`

---

## Dependencies

### **Backend (Flask)**

- `flask`
- `flask-cors`
- `openai`

### **Frontend (React)**

- `react`
- `axios`

---

## Usage

1. Open `http://localhost:3000` in your browser.
2. Type a question in the input box and click Send.
3. The AI will generate a response, and the conversation will be stored in memory dictionary object of python.
4. After refreshing the page, the chat history not remains because I am not storing it on Local storage or db.
