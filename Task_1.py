def calculate_average(Score_1, Score_2, Score_3):
    total = Score_1 + Score_2 + Score_3
    average = total / 3
    return average


def get_scores():
    Score_1 = float(input("Enter the first score: "))
    Score_2 = float(input("Enter the second score: "))
    Score_3 = float(input("Enter the third score: "))
    if Score_1 < 0 or Score_1 > 100 or Score_2 < 0 or Score_2 > 100 or Score_3 < 0 or Score_3 > 100:
        print("Invalid score. Please enter scores between 0 and 100.")
        return None, None, None
    return Score_1, Score_2, Score_3

# This is the main part of the program where the scores are retrieved and the average is calculated.
# The main function calls get_scores() to obtain the scores, then calculates the average using calculate_average(), and finally prints the result.
# May try to add a line that makes values over 100 invalid
# For example, could add a check in get_scores() to ensure each score is between 0 and 100
# Liked the validation of scores to ensure they are within the acceptable range and decided to keep it in the program


def main():
    Score_1, Score_2, Score_3 = get_scores()
    if Score_1 is None or Score_2 is None or Score_3 is None:
        print("Failed to retrieve valid scores.")
    else:
        average = calculate_average(Score_1, Score_2, Score_3)
        print("The average score is:", average)
    
    # This is the end of the main function.
    
if __name__ == "__main__":
    main()
