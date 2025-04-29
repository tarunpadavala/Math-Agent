def check_privacy(user_input: str) -> bool:
    """
    Ensures that no private or sensitive information is shared in the input.
    """
    
    # List of sensitive keywords that should not be exposed
    sensitive_keywords = ["password", "ssn", "credit card", "address"]
    
    if any(keyword in user_input.lower() for keyword in sensitive_keywords):
        return False
    
    return True