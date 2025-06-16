from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Load model at startup (small distilgpt2 instead of full gpt2)
rewriter = pipeline('text-generation', model='distilgpt2')

@app.route('/rewrite', methods=['POST'])
def rewrite():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
            
        result = rewriter(
            text, 
            max_length=100,
            num_return_sequences=1,
            truncation=True
        )[0]['generated_text']
        
        return jsonify({"rewritten": result})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
