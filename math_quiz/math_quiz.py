import random

def show_question(question_number,num1, num2, operator):
#show question to user
    print(f'{question_number}. {num1} {operator} {num2}')

def get_answer(num1, num2, operator):
#return the answer for that question
    if operator == '+':
        answer = num1 + num2
            
    elif operator == '-':
        answer = num1 - num2
                    
    elif operator == '*':
        answer = num1 * num2
            
    elif operator == '/':
        answer = num1 / num2

    return answer

def get_valid_input():
#get valid answer from user
    while True:
        try:
            return float(input('Enter your answer: '))
        except ValueError:
            print ('🔴 Invalid input! Try again')
    
def main():

    symbol = ("+","-","*","/") 

    mark = 0
    question = 1

    while question <= 10:

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
            
        operator = random.choice(symbol)

        show_question(question, num1, num2, operator)
        user_answer = get_valid_input()
        answer = round(get_answer(num1, num2, operator), 2)

        if user_answer == answer:
            print("Correct!")
            mark += 1
        else:
            print(f" Wrong! The answer was {answer}")
        question += 1

    print(f'🚩Final score: {mark}/10')

if __name__ == '__main__':
    main()