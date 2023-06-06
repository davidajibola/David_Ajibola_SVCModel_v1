def calculate_even_sum(limit):
    even_sum = 0

    for num in range(2, limit + 1, 2):
        even_sum += num

    return even_sum

# Prompt the user to enter the limit
limit = int(input("Enter the limit: "))

# Call the function to calculate the sum of even numbers
result = calculate_even_sum(limit)

# Display the result
print(f"The sum of even numbers between 1 and {limit} is: {result}")
