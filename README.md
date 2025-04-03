# AI-Powered FAQ Chatbot

This is an AI-powered FAQ chatbot using a pre-trained NLP model to answer user queries.

## Features
- Uses a **question-answering model** (`distilbert-base-cased-distilled-squad`).
- Built with **Flask** for a lightweight API.
- Accepts user questions and context for better responses.

## Installation

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd faq_chatbot

2. Set up a virtual environment

python -m venv faq_chatbot_env
source faq_chatbot_env/bin/activate  # On macOS/Linux
faq_chatbot_env\Scripts\activate     # On Windows

3. Install dependencies

pip install -r requirements.txt

Usage
1. Run the chatbot API

python chatbot.py

The server will start on http://127.0.0.1:5000/.
2. Test the API with curl

curl -X POST "http://127.0.0.1:5000/chat" -H "Content-Type: application/json" -d "{\"question\": \"How do I reset my password?\", \"context\": \"To reset your password, go to the login page, click 'Forgot Password', and follow the email instructions.\"}"

3. Example Response

{
  "question": "How do I reset my password?",
  "answer": "Follow the instructions sent to your registered email"
}

File Structure

faq_chatbot/
│── chatbot.py          # Main API script
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│── example_requests.json # Example API request format

Notes

    Ensure torch is installed, as transformers requires it.

    Modify chatbot.py to improve responses as needed.
