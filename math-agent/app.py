import json
from googleapiclient.discovery import build  # For Google Custom Search API
from guardrails.input_guardrails import validate_input
from guardrails.output_guardrails import validate_output
from guardrails.privacy_guardrails import check_privacy
from retrieval.vector_retriever import search  # Import the search function from vector_retrieve.py
import requests

# Google Custom Search API setup
API_KEY = "AIzaSyBiv2hEbHGZNOyvRgAj3viKSOQ82PK_0Yk"
CX =  "74760e37ec93b4656"


# Function to perform web search
def web_search(query):
    app_id = "UQ22G6-2XQ853UEPJ"
    url = f"https://api.wolframalpha.com/v2/query?input={query}&appid={app_id}&output=json"
    response = requests.get(url)
    data = response.json()
    print(data)
    result = data["queryresult"]["pods"]
    for pod in result:
        if pod["title"] == "Result":
            answer = pod["subpods"][0]["plaintext"]
            print("Answer:", answer)

"""query = "solve 2x + 3 = 7" """

""" service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CX).execute()
    if "items" in res:
        return res["items"][0]["snippet"]  # Return the snippet from the top result
    return "Sorry, I couldn't find a relevant answer online." """

# Main function
if __name__ == "__main__":
    # Step 1: Receive the question from the user
    question = input("Enter your math problem: ")

    # Step 2: Check privacy
    if not check_privacy(question):
        print("Warning: Your input contains sensitive information, and it will not be processed.")
    else:
        # Step 3: Validate input
        if not validate_input(question):
            print("Invalid input. Please enter a valid mathematical question.")
        else:
            # Step 4: Perform the search using vector retrieval (from vector_retrieve.py)
            solution = search(question)
            
            # Step 5: If no solution found in knowledge base, perform web search
            if solution == "Sorry, I couldn't find an answer in the knowledge base.":
                print("No solution found in the knowledge base. Performing a web search...")
                solution = web_search(question)
            
            # Step 6: Validate the output before displaying it
            """if validate_output(solution):
                print(f"Solution: {solution}")
            else:
                print("The solution could not be generated or is invalid.")"""
            
            # Step 7: Collect feedback from the user
            feedback = input("Was this solution helpful? (yes/no): ")
            if feedback.lower() == "yes":
                print("Thank you for your feedback!")
            else:
                print("Thank you! We'll work to improve the system.")
