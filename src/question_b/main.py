#add import

from question_b import get_bonus_pay_amount

def main():
    
    try:
        sales = int(input("Enter sales amount: "))
        bonus = get_bonus_pay_amount(sales)
        print(f"Bonus: {bonus}")
    
    except ValueError:
        print("Please enter a valid number.")

main()