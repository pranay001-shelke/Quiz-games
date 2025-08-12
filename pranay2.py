# 
# By Pranay Shelke

def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! The correct answer is {q['answer']}")
    print(f"\n You got {score} out of {len(questions)} correct.")

def main():
    print("=====  Welcome to the Online Quiz Game  =====")
    
    questions = [
        {
            "question": "1. What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
            "answer": "B"
        },
        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "C"
        },
        {
            "question": "3. Who developed Python programming language?",
            "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
            "answer": "B"
        },
        {
            "question": "4. Which is the largest ocean on Earth?",
            "options": ["A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
            "answer": "C"
        }
    ]

    run_quiz(questions)
    print("\n Thanks for playing!")

if __name__ == "__main__":
    main()
