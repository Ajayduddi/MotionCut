# Welcome message
print("Welcome to the Quiz Game!")
print("NOTE: If your spelling is incorrect, it will be considered a wrong answer.")

# Initialize score and question number
score = 0
question_no = 0

# Ask if the user wants to play
playing = input("Do you want to play? (yes/no): ").lower()

if playing == "yes":
    # Question 1
    question_no += 1
    answer = input(f"\n{question_no}. What does CPU stand for? ").lower()
    if answer == "central processing unit":
        score += 1
        print("Correct! You got 1 point.")
    else:
        print("Incorrect!")
        print(f"Current answer is: Central Processing Unit")

    # Question 2
    question_no += 1
    answer = input(f"\n{question_no}. What does GPU stand for? ").lower()
    if answer == "graphics processing unit":
        score += 1
        print("Correct! You got 1 point.")
    else:
        print("Incorrect!")
        print(f"Current answer is: Graphics Processing Unit")

    # Question 3
    question_no += 1
    answer = input(f"\n{question_no}. What does RAM stand for? ").lower()
    if answer == "random access memory":
        score += 1
        print("Correct! You got 1 point.")
    else:
        print("Incorrect!")
        print(f"Current answer is: Random Access Memory")

    # Question 4
    question_no += 1
    answer = input(f"\n{question_no}. What does PSU stand for? ").lower()
    if answer == "power supply unit":
        score += 1
        print("Correct! You got 1 point.")
    else:
        print("Incorrect!")
        print(f"Current answer is: Power Supply Unit")

    # Question 5 (you can add more questions if needed)

else:
    print("Thank you! You are out of the game.")

# Display final score
print(f"\nNumber of questions: {question_no}")
print(f"Your score: {score}")
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print("0% questions are correct")
else:
    print(f"{percentage:.2f}% questions are correct.")
