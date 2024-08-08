# Printing a welcome message for the quiz game
print("**********************")
print("Welcome to my quiz game!!!!")

# Defining the question bank with questions and their correct answers
question_bank = [
    {
        "text": "The ability of one class to acquire methods and attributes of another class is called_ _ _ .",
        "answer": "A",
    },
    {
        "text": "Which of the following is a type of inheritance?",
        "answer": "D",
    },
    {
        "text": "What type of inheritance has multiple subclasses to a single superclass?",
        "answer": "C",
    },
    {
        "text": "What is the depth of multilevel inheritance in Python?",
        "answer": "C",
    },
    {
        "text": "What does MRO stand for?",
        "answer": "B",
    },
]

# Defining the options for each question
options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Object"],
    ["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
    ["A. Multiple inheritance", "B. Multilevel inheritance", "C. Hierarchical inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Method recursive", "B. Method resolution", "C. Main resolution order", "D. Method resolution object"]
]

# Function to check if the user's answer is correct
def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

# Initialize the score
score = 0

# Loop through each question in the question bank
for question_num in range(len(question_bank)):
    print("*************")
    print(f"Q{question_num + 1}: {question_bank[question_num]['text']}")
    for option in options[question_num]:
        print(option)
    
    # Get the user's guess
    guess = input("Enter your answer (A/B/C/D): ").upper()
    
    # Check if the guess is correct
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer.")
    
    # Display the user's answer and the correct answer
    print(f"Your answer: {guess}")
    print(f"Correct answer: {question_bank[question_num]['answer']}")
    print()

# Print the final score
print(f"Your final score is {score} out of {len(question_bank)}")
