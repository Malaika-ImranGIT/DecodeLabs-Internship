def evaluate_answer(user_input, correct_choice):
    clean_input = user_input.strip().upper()
    if clean_input == correct_choice:
        return 1, "Correct answer!"
    return 0, f"Wrong answer. The correct choice was {correct_choice}."

def run_quiz_engine():
    questions = [
        "What is the capital of France?",
        "Which planet is known as the Red Planet?",
        "What is the largest mammal on Earth?"
    ]
    
    options = [
        ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. White Shark"]
    ]
    
    answers = ["C", "B", "B"]
    
    score = 0
    total_questions = len(questions)
    
    print("=======================================")
    print("    DECODELABS QUIZ SYSTEM v4.0        ")
    print("=======================================")
    
    for i in range(total_questions):
        print(f"\nQuestion {i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
            
        user_choice = input("Your answer (A, B, C, or D): ")
        points, message = evaluate_answer(user_choice, answers[i])
        score += points
        print(message)
        
    print("\n=======================================")
    print(f"QUIZ COMPLETE. FINAL SCORE: {score}/{total_questions}")
    print("=======================================")

if __name__ == "__main__":
    run_quiz_engine()