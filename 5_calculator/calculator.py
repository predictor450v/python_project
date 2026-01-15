import math
import re

# Custom eval function to include math functions
def custom_eval(expression):
    try:
        # Replace power operator (^) with Python's (**) for exponentiation
        expression = expression.replace("^", "**")
        
        # Use regex to replace common functions with their Python math equivalents
        expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)
        expression = re.sub(r'log\((.*?)\)', r'math.log10(\1)', expression)
        expression = re.sub(r'sqrt\((.*?)\)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'fact\((.*?)\)', r'math.factorial(int(\1))', expression)
        
        # Evaluate the final expression safely
        result = eval(expression, {"math": math, "__builtins__": None})
        return result
    except Exception as e:
        return f"Error: {e}"

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("You can use operators like +, -, *, /, ^, and functions like sin(), cos(), tan(), log(), sqrt(), fact()")
    print("Example: sin(30) + log(100) ^ 2 / sqrt(16)")
    
    while True:
        # Take the mathematical expression input from the user
        expression = input("\nEnter your expression (or 'exit' to quit): ")

        if expression.lower() == "exit":
            break
        
        # Calculate and display the result
        result = custom_eval(expression)
        print(f"Result: {result}")

# Run the scientific calculator
scientific_calculator()
