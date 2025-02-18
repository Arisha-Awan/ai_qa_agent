from pprint import pprint

from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)


OPENAI_API_KEY = "place_your_api_key_here"
client = OpenAI(api_key=OPENAI_API_KEY)


conversations = {}


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    user_id = data.get("user_id", "default")
    user_query = data.get("query")

    print(f"Received query from user {user_id}: {user_query}")

    if not user_query:
        print("Error: Query cannot be empty")
        return jsonify({"error": "Query cannot be empty"}), 400

    # Maintain conversation history
    if user_id not in conversations:
        conversations[user_id] = []

    conversations[user_id].append({"role": "user", "content": user_query})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", store=True, messages=conversations[user_id]
        )

        ai_response = response.choices[0].message.content

        print(f"AI Response: {ai_response}")

        conversations[user_id].append({"role": "assistant", "content": ai_response})
        pprint(conversations)

        return jsonify({"response": ai_response, "history": conversations[user_id]})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
