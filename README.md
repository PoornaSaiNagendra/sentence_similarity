# Report: Semantic Textual Similarity Model

## Overview:

The objective of this report is to outline the core approach taken in Part A of building a Semantic Textual Similarity (STS) model. The STS model is designed to assess the degree of semantic equivalence between two text sentences, providing a similarity score ranging from 0 (highly dissimilar) to 1 (highly similar). The approach leverages pre-trained models, specifically utilizing the BERT (Bidirectional Encoder Representations from Transformers) architecture.

## Core Approach (Part A):

### 1. Selection of Pre-trained Model:

The core approach involves the selection of a pre-trained model for semantic textual similarity. In this implementation, the BERT-based model from the `sentence-transformers` library is chosen. The selected model is 'paraphrase-MiniLM-L6-v2,' a lightweight version of BERT fine-tuned for paraphrase identification.

### 2. Text Encoding:

The selected model is employed to encode input text sentences into dense vector representations. The encoding process captures the semantic information of the sentences, allowing for meaningful comparisons.

### 3. Similarity Calculation:

The cosine similarity metric is utilized to quantify the degree of similarity between the encoded vectors of two input sentences. Cosine similarity ranges from -1 to 1, with 1 indicating identical vectors and 0 indicating orthogonal vectors. The final similarity score is obtained by normalizing the cosine similarity to a scale between 0 and 1.

### 4. Implementation in Python:

The core approach is implemented using Python programming language. The `sentence-transformers` library facilitates easy integration with pre-trained BERT models. The `util.pytorch_cos_sim` function is employed to calculate the cosine similarity between the encoded vectors.

## Key Components:

1. **Model Selection:**
   - The choice of the 'paraphrase-MiniLM-L6-v2' model is based on its lightweight nature and suitability for semantic textual similarity tasks.

2. **Encoding Strategy:**
   - The BERT model is employed to convert input text into dense vector representations, capturing semantic information.

3. **Similarity Metric:**
   - Cosine similarity is used to measure the similarity between encoded vectors, providing a normalized similarity score.

4. **Python Implementation:**
   - The implementation is carried out in Python, ensuring accessibility and ease of integration.

## Conclusion:

The core approach in Part A focuses on leveraging pre-trained BERT models for semantic textual similarity assessment. By encoding input text sentences and calculating cosine similarity, the model provides a quantitative measure of semantic equivalence. This approach balances computational efficiency with accuracy, making it suitable for a range of applications requiring textual similarity evaluation.
