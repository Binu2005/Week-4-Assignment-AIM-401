def countdown(n):
    if n <= 0:
        return "Finished"
    return countdown(n - 1)

print(countdown(3))

def countdown_iterative(n):
    while n > 0:
        n -= 1
    return "Finished"

print(countdown_iterative(3))

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number ** 2, numbers))

print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)

students = [("Asha", 85), ("Ravi", 72), ("Bina", 94)]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print(students_sorted)