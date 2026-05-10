""" Type your code here. """
first_val = int(input())
second_val = int(input())

# Check if the second integer is smaller than the first
if second_val < first_val:
    print("Second integer can't be less than the first.")
else:
    # Use range with (start, stop, step)
    # Adding 1 to second_val makes the range inclusive
    for i in range(first_val, second_val + 1, 5):
        print(i, end=" ")
    
    # Print a final newline after the loop finishes
    print()
