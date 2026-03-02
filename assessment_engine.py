def scoring_calculator(answers):
    score = 0
    # Example scoring logic
    for answer in answers:
        if answer:
            score += 1  # Increment score for each positive answer
    return score


def result_generator(score):
    if score >= 8:
        return "High potential for STEM careers."
    elif score >= 5:
        return "Moderate potential for STEM careers."
    else:
        return "Low potential for STEM careers."


# Example usage
if __name__ == '__main__':
    sample_answers = [True, False, True, True, False, True, True, False]
    score = scoring_calculator(sample_answers)
    result = result_generator(score)
    print(f'Score: {score}')
    print(f'Result: {result}')