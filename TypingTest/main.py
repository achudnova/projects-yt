import random
import time

# Customizable list of sentences for the test
sentences = [
    "This is a typing test.",
    "Type the sentence above this one.",
    "The quick brown fox jumps over the lazy dog.",
    "I love to type because it is so much fun!",
    "Type as fast as you can without making mistakes.",
    "The rain in Spain falls mainly on the plain."
]

# Initialize best scores list
best_scores = []

def run_test(sentences):
    
    # Shuffle the sentences so they appear in a random order
    random.shuffle(sentences)

    # Start the timer
    start_time = time.time()

    # Initialize score and word count
    score = 0
    word_count = 0

    # Iterate through each sentence
    for sentence in sentences:

        # Display the sentence to be typed
        print(sentence)

        # Get the user's input
        typed_sentence = input()

        # Split the sentence into words
        words = sentence.split()

        # Update word count
        word_count += len(words)

        # Check if the input is correct
        if typed_sentence == sentence:

            # Increment score
            score += 1

            # Print a success message in green color
            print("\033[92mCorrect!\033[0m")

        else:
            # Print an error message in red color
            print("\033[91mIncorrect.\033[0m")

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Calculate words per minute (WPM)
    wpm = word_count / (elapsed_time / 60)

    # Print results
    print(f"You scored {score} out of {len(sentences)} in {elapsed_time:.2f} seconds!")
    print(f"Your WPM is {wpm:.2f}")

    # Add score to best scores list
    best_scores.append(score)

# Run the typing test
run_test(sentences)

# Display best scores
print("\nBest scores:")
for score in best_scores:
    print(score)