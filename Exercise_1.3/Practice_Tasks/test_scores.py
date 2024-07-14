# Create the list of test scores
test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]
print("Original test scores:", test_scores)

# Sort the test scores in descending order
test_scores.sort(reverse=True)
print("Sorted test scores in descending order:", test_scores)

# Print the top three scores
print("Top three scores:")
for i in range(3):
    print(test_scores[i])
