def print_number_triangle(n=5):
    # Outer loop controls the current row (1 through n)
    for i in range(1, n + 1):
        # Inner loop prints column values from 1 up to current row 'i'

        # Move to the next line after completing the row
        print()

# Function call
print_number_triangle(5)