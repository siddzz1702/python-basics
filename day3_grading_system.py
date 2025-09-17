# Day 3: Grading System
# Prompt for a score between 0.0 and 1.0 and assign a grade

# Get user input
score = input("Enter score (0.0 - 1.0): ")

# Convert to float
score = float(score)

# Check range and assign grade
if score < 0.0 or score > 1.0:
    print("Error: Score is out of range. Please enter a value between 0.0 and 1.0.")
elif score >= 0.9:
    print("Grade: A")
elif score >= 0.8:
    print("Grade: B")
elif score >= 0.7:
    print("Grade: C")
elif score >= 0.6:
    print("Grade: D")
else:
    print("Grade: F")
