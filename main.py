# 1. Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)

# 2. Extract even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# 3. Get all strings starting with the letter 'A' from a list of strings
names = ["Alice", "Bob", "Amy", "Steve", "Amanda", "Tom"]
starts_with_A = [name for name in names if name.startswith('A')]
print("Strings starting with 'A':", starts_with_A)

# 4. Generate a list of tuples with each number and its square from 1 to 5
number_square_pairs = [(x, x**2) for x in range(1, 6)]
print("Number and their squares as tuples:", number_square_pairs)
