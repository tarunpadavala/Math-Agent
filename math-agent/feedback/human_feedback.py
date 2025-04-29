def collect_feedback(answer):
    print("\n--- Feedback Section ---")
    feedback = input("Is the answer good? (yes/no): ")
    comments = input("Any additional comments?: ")
    return {"feedback": feedback, "comments": comments}