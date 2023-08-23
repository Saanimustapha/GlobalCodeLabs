#Write a function called calculate that takes one string and two int arguments. The string should be "add", "subtract", "multiply" or "divide", or any of those words in uppercase. The calculate function should then do the right operation with the two numbers and return the result.

def calculate(operation,num_1,num_2):
    
    if operation == 'add':
        result = num_1 + num_2
        return result
    elif operation == 'subtract':
        result = num_1 - num_2
        return result
    elif operation == 'multiply':
        result = num_1 * num_2
        return result
    elif operation == 'divide':
        result = num_1/num_2
        return result
    
print(calculate(lower.('ADD'),5,7))   

    
