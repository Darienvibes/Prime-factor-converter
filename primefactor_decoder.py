import re
from sympy import factorint

def decimal_to_prime_factors(n):
    factors = factorint(n)
    parts = []
    for prime, power in sorted(factors.items()):
        if power == 1:
            parts.append(f"{prime}")
        else:
            parts.append(f"{prime} ^ {power}")
    return " * ".join(parts)

def prime_factors_to_decimal(expr):
    try:
        # Replace ^ with ** for Python exponentiation
        expr = expr.replace('^', '**')
        # Remove all spaces
        expr = expr.replace(' ', '')
        # Evaluate the expression
        return eval(expr)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def main():
    print("=== Prime Factor Tool ===")

    while True:
        print("\nChoose an option:")
        print("1. Decimal to Prime Factor Language")
        print("2. Prime Factor Language to Decimal")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            try:
                num = int(input("Enter a decimal number: "))
                result = decimal_to_prime_factors(num)
                print(f"➡ Prime factor format: {result}")
            except ValueError:
                print("⚠ Please enter a valid integer.")
        elif choice == '2':
            expr = input("Enter prime factor format (e.g., 2 ^ 3 * 5): ")
            result = prime_factors_to_decimal(expr)
            print(f"➡ Decimal value: {result}")
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("⚠ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()


