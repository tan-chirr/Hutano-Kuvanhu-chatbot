# Mini quiz game for kids to learn food groups

def food_quiz():
    questions = {
        "Is avocado a fruit or vegetable?": "fruit",
        "Which food gives us energy: sadza or water?": "sadza"
    }
    score = 0
    for q, a in questions.items():
        ans = input(q + " ").lower()
        if ans == a:
            score += 1
            print("Correct!")
        else:
            print(f"Oops! The correct answer is {a}.")
    print(f"You got {score}/{len(questions)} correct.")

if __name__ == "__main__":
    food_quiz()
