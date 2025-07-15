# Input 5 test scores from user
scores = []

for i in range(1, 6):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

print(f"\nAverage Score: {average:.2f}")

# Check Pass/Fail
if average >= 40:
    print("Result: Pass 🎉")
else:
    print("Result: Fail ❌")
