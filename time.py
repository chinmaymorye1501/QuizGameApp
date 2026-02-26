import random
import time



questions = [
    {
        "question": "Capital of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Chennai", "D) Kolkata"],
        "answer": "B"
    },
    {
        "question": "5 + 3 = ?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) HTML", "C) Java", "D) All of the above"],
        "answer": "D"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"
    },
    {
        "question": "Which company developed Python?",
        "options": ["A) Google", "B) Microsoft", "C) Python Software Foundation", "D) Apple"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Processing Unit", "C) Central Program Unit", "D) Control Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False in Python?",
        "options": ["A) int", "B) string", "C) bool", "D) float"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A) ^", "B) **", "C) %", "D) //"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    }
]

random.shuffle(questions)

print("timer feature to quiz game")
start = time.time()
answer = input("Your answer: ")



score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")
end = time.time()
print("Time taken:", round(end - start, 2), "seconds")
