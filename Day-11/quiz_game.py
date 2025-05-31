"""quiz"""

def ask_question(question_data):
    print("\n" + question_data['question'])
    for option in question_data['options']:
        print(option)
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == question_data['answer']:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer is '{question_data['answer']}'.")
        return 0

def run_quiz():
    questions = [
        {
            'question': "1. What is the capital of France?",
            'options': ['a) Berlin', 'b) Madrid', 'c) Paris', 'd) Rome'],
            'answer': 'c'
        },
        {
            'question': "2. Who wrote 'Romeo and Juliet'?",
            'options': ['a) William Shakespeare', 'b) Charles Dickens', 'c) Mark Twain', 'd) Jane Austen'],
            'answer': 'a'
        },
        {
            'question': "3. What is the chemical symbol for water?",
            'options': ['a) H2O', 'b) CO2', 'c) O2', 'd) NaCl'],
            'answer': 'a'
        },
        {
            'question': "4. Which planet is known as the Red Planet?",
            'options': ['a) Earth', 'b) Mars', 'c) Jupiter', 'd) Venus'],
            'answer': 'b'
        },
        {
            'question': "5. What is the largest ocean on Earth?",
            'options': ['a) Atlantic Ocean', 'b) Indian Ocean', 'c) Arctic Ocean', 'd) Pacific Ocean'],
            'answer': 'd'
        }
    ]

    score = 0
    for q in questions:
        score += ask_question(q)

    print(f"\n You scored {score} out of {len(questions)}.")

def main():
    print("Welcome to the Quiz Game!")
    while True:
        run_quiz()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
