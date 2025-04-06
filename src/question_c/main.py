#add import

from question_c import get_person_category

def main():
    
    while True:
        user_input = input("Enter a person's age (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            
            break
        
        if not user_input.isdigit():
            print("Please enter a valid number.")
            
            continue

        age = int(user_input)
        category = get_person_category(age)
        print(f"The person is a(n): {category}")

main()
