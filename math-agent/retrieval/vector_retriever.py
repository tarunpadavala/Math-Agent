import json
import math
from collections import Counter

# Load knowledge base
def load_knowledge_base():
    try:
        with open("knowledge_base.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Knowledge base file not found.")
        return []

# Convert text to word frequency vector (Bag of Words)
def text_to_vector(text):
    words = text.lower().split()
    return Counter(words)

# Calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([val ** 2 for val in vec1.values()])
    sum2 = sum([val ** 2 for val in vec2.values()])
    
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if denominator == 0:
        return 0.0
    return float(numerator) / denominator

# Create vectors for knowledge base
def index_knowledge_base():
    knowledge_base = load_knowledge_base()
    questions = [entry["question"] for entry in knowledge_base]
    solutions = [entry["solution"] for entry in knowledge_base]
    vectors = [text_to_vector(question) for question in questions]
    return questions, solutions, vectors

# Search for the most similar question
def search(query):
    questions, solutions, vectors = index_knowledge_base()

    if not questions:
        return "Sorry, I couldn't find an answer in the knowledge base."
    
    query_vector = text_to_vector(query)
    similarities = [cosine_similarity(query_vector, vec) for vec in vectors]

    # Find the best match
    best_score = max(similarities)
    best_match_index = similarities.index(best_score)

    # Threshold to decide if a match is good enough
    THRESHOLD = 0.5
    if best_score >= THRESHOLD:
        return solutions[best_match_index]
    else:
        return "Sorry, I couldn't find an answer in the knowledge base."
