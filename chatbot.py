from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_question = data.get("question", "")

    # Define a better context (replace with real FAQs)
    context = """
    If you need to reset your password, go to the login page and click 'Forgot Password'. 
    Follow the instructions sent to your registered email to reset it.
    """

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    result = qa_pipeline({"question": user_question, "context": context})
    response = {"question": user_question, "answer": result["answer"]}
    
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

