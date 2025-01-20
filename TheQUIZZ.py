import random
import time

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("Answer the questions and try to score at least 10 out of 20 to pass.")
    print("Type your answers carefully and press Enter to submit.")
    print("Good luck!\n")

def get_questions():
    return [
        {"question": "What is the big shape in the sky at night?", "answer": "the moon"},
        {"question": "What color are bananas?", "answer": "yellow"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Which animal barks?", "answer": "dog"},
        {"question": "How many days are there in a week?", "answer": "7"},
        {"question": "What is the opposite of up?", "answer": "down"},
        {"question": "What do you call frozen water?", "answer": "ice"},
        {"question": "What is the color of the sky on a clear day?", "answer": "blue"},
        {"question": "Which fruit is known as the king of fruits?", "answer": "mango"},
        {"question": "How many wheels does a car typically have?", "answer": "4"},
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What is the fastest land animal?", "answer": "cheetah"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
        {"question": "What is H2O commonly known as?", "answer": "water"},
        {"question": "What do bees produce?", "answer": "honey"},
        {"question": "What is the largest mammal?", "answer": "blue whale"},
        {"question": "Which continent is known as the Dark Continent?", "answer": "africa"},
        {"question": "What do you call a baby cat?", "answer": "kitten"},
        {"question": "What is the color of grass?", "answer": "green"},
        {"question": "What shape has three sides?", "answer": "triangle"}
    ]

def run_quiz():
    questions = get_questions()
    random.shuffle(questions)  # Shuffle questions for variety

    score = 0
    total_questions = len(questions)
    start_time = time.time()  # Start the timer
    time_limit = 3 * 60  # 3 minutes in seconds

    for i, question_data in enumerate(questions, start=1):
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        if elapsed_time > time_limit:
            print("Time's up! The quiz is over.")
            break  # Exit the loop if time is up

        print(f"Question {i}: {question_data['question']}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question_data['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['answer']}\n")

    print("Quiz Over!\n")
    print(f"Your score: {score}/{total_questions}")
    if score >= 10:
        print("Congratulations, you passed the quiz!\n")
    else:
        print("Sorry, you failed. Better luck next time!\n")

def main():
    display_welcome()
    run_quiz()

if __name__ == "__main__":
    main()
