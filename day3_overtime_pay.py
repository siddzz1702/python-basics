# Day 3: Overtime Pay Calculator
# Calculate gross pay with overtime (1.5x rate for hours above 40)

# Get input from user
hours = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Convert input to float
hours = float(hours)
rate = float(rate)

# Compute gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * rate * 1.5
    gross_pay = regular_pay + overtime_pay

print("Gross Pay:", gross_pay)
