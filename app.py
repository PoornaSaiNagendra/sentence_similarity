import os
import logging
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Configuration
app.config.from_object(os.environ.get('FLASK_CONFIG', 'config.ProductionConfig'))

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/v1/calculate_similarity', methods=['POST'])
def calculate_similarity_api():
    try:
        data = request.get_json()
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')

        if not text1 or not text2:
            raise ValueError("Text1 and Text2 are required")

        # Encode the texts into embeddings
        embeddings1 = model.encode(text1, convert_to_tensor=True)
        embeddings2 = model.encode(text2, convert_to_tensor=True)

        # Calculate cosine similarity between the embeddings
        similarity_score = util.pytorch_cos_sim(embeddings1, embeddings2)[0][0].item()

        return jsonify({"similarity_score": similarity_score})

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
