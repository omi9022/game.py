import random
import time

def math_quiz_game():
    print("Welcome to the Time Pressure Math Quiz!")
    
    num_questions = 5
    score = 0
    time_limit = 10  
    
    def generate_question(difficulty):
        if difficulty == "easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == "medium":
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
        else:  
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
        
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            correct_answer = num1 + num2
            question = f"What is {num1} + {num2}?"
        elif operation == '-':
            correct_answer = num1 - num2
            question = f"What is {num1} - {num2}?"
        elif operation == '*':
            correct_answer = num1 * num2
            question = f"What is {num1} * {num2}?"
        else:  
            num2 = random.randint(1, 10)  
            while num1 % num2 != 0:
                num2 = random.randint(1, 10)
            correct_answer = num1 / num2
            question = f"What is {num1} / {num2}?"
        
        return question, correct_answer
    
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty. Please select 'easy', 'medium', or 'hard'.")
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    
    print(f"\nYou have {time_limit} seconds to answer each question!")
    
    for i in range(num_questions):
        print(f"\nQuestion {i + 1}:")
        question, correct_answer = generate_question(difficulty)
        print(question)
        
        start_time = time.time()
        try:
            player_answer = float(input("Your answer: "))
            time_taken = time.time() - start_time
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if time_taken > time_limit:
            print(f"Time's up! You took {time_taken:.2f} seconds. The correct answer was {correct_answer}.")
            continue
        
        time_bonus = max(0, time_limit - int(time_taken))
        if player_answer == correct_answer:
            print(f"Correct! You took {time_taken:.2f} seconds. You earned {time_bonus} bonus points.")
            score += 1 + time_bonus  
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    print(f"\nYou scored {score} points out of a possible {num_questions * (time_limit + 1)}!")

if __name__ == "__main__":
    math_quiz_game()
    
    
