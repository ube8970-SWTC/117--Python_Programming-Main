def is_passing(score):
    return score >= 75

while True:
    print("Enter your score: ")
    score_text = input()
    score = float(score_text)
    if score > 100:
        print("Invalid score")
    else:
        print(is_passing(score))
        break
