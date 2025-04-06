#add import

from question_a import get_day_of_week

def main():
    
    while True:
        user_input = input("Enter a number from 1 to 7 (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            
            break
        
        if user_input.isdigit():
            number = int(user_input)
            result = get_day_of_week(number)
            print("Result:", result)
        
        else:
            print("Invalid input. Please enter a number or 'q' to quit.")

main()
