def calculate_average(scores):
    print("\n=== Grade Report ===")
    print(f"Test Scores: {scores}")
    average = sum(scores)/len(scores)
    print(f"Average Score: {average}")
    return average

def get_letter_grade(average):
    if average >= 90:
        print("Letter Grade: A")
    elif average >= 80:
        print("Letter Grade: B")
    elif average >= 70:
        print("Letter Grade: C")
    elif average >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")

while True:
    num_scores = int(input("How many test scores do you want to enter? (Enter 0 to quit)"))
    if num_scores == 0:
        print("Goodbye!")
        break

    scores = []
    for i in range(num_scores):
        while True:
            score = float(input(f"Enter score {i+1}: "))
            if score < 0:
                print("Please enter a valid score. Score cannot be negative.")
            else:
                break
        scores.append(score)

    print("Test scores: ", scores)

    average = calculate_average(scores)
    get_letter_grade(average)