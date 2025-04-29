
def validate_output(solution: str) -> bool:
    """
    Validates the solution output before returning to the user.
    Ensures the solution is meaningful and does not contain invalid content.
    """
    
    # Check for anything inappropriate in the solution (e.g., potentially harmful commands)
    forbidden_keywords = ["hack", "exploit", "error", "inappropriate"]
    if any(keyword in solution.lower() for keyword in forbidden_keywords):
        return False
    
    # Ensure the solution is not empty
    if len(solution.strip()) == 0:
        return False
    
    return True