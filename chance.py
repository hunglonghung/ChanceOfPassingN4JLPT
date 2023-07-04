from scipy.stats import binom

# Number of remaining questions and their corresponding probabilities
n_3choice, p_3choice = 11, 1/3  # for remaining 3-choice questions
n_4choice, p_4choice = 13, 1/4  # for remaining 4-choice questions

minimum_score = 6  # Now you're looking for the probability of scoring 6 or more points
maximum_score = n_3choice + n_4choice  # Maximum possible score is the total number of remaining questions
prob_total = 0

# Iterating over all possible total scores from the minimum to the maximum
for total_score in range(minimum_score, maximum_score + 1):
    # Iterating over all possible combinations of scores from two types of questions
    for score_3choice in range(total_score + 1):  # possible scores from 3-choice questions
        score_4choice = total_score - score_3choice  # remaining scores should be from 4-choice questions
        if score_4choice > n_4choice:  # skip if the score from 4-choice questions exceeds their total number
            continue
        # calculate the probability of each combination
        prob_3choice = binom.pmf(score_3choice, n_3choice, p_3choice)
        prob_4choice = binom.pmf(score_4choice, n_4choice, p_4choice)
        # sum the product of the probabilities
        prob_total += prob_3choice * prob_4choice

# Output the total probability
print(prob_total)
