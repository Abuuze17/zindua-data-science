import random

questions = [
    {
        "question": "What is the capital of Kenya?",
        "choices": {
            "A": "Nairobi",
            "B": "Mombasa",
            "C": "Kisumu",
            "D": "Nakuru"
        },
        "answer": "A"
    },

    {
        "question": "Which keyword is used to create a loop in Python?",
        "choices": {
            "A": "repeat",
            "B": "loop",
            "C": "for",
            "D": "iterate"
        },
        "answer": "C"
    },

    {
        "question": "What is 5 + 7?",
        "choices": {
            "A": "10",
            "B": "12",
            "C": "13",
            "D": "14"
        },
        "answer": "B"
    },

    {
        "question": "Which data type stores True or False?",
        "choices": {
            "A": "String",
            "B": "Integer",
            "C": "Boolean",
            "D": "Float"
        },
        "answer": "C"
    }
]

random.shuffle(questions)

score = 0

print("=== PYTHON QUIZ ===")

for q in questions:
    print("\n" + q["question"])

    for key, value in q["choices"].items():
        print(f"{key}. {value}")

    while True:
        try:
            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer not in ["A", "B", "C", "D"]:
                raise ValueError

            break

        except ValueError:
            print("Invalid input! Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}")

print("\n=== QUIZ COMPLETE ===")
print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good!")
else:
    print("Try Again!")