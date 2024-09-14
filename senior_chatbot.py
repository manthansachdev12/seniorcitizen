from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=user_message,
        max_tokens=150
    )
    
    chatbot_response = response.choices[0].text.strip()
    
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
