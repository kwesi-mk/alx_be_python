rows = int(input("Enter the size of the pattern: "))

current_row = 1

while current_row <= rows:
    for i in range(rows):
        print("*", end="")
    print()
    current_row += 1