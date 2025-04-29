import re

def validate_input(query: str) -> bool:
    """
    Validates the user input for the question.
    Ensures the input is a mathematical question.
    """

    # Check if the input contains mathematical symbols (e.g., numbers, operators)
    if re.search(r'[0-9+\-*/^=()]{2,}', query):
        return True
    
    # Check for offensive or inappropriate words (this can be expanded)
    offensive_keywords = ["offensive_word1", "offensive_word2"]
    if any(word in query.lower() for word in offensive_keywords):
        return False
    
    return False