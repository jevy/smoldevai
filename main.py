```python
import os
from load_model import load_model
from process_data import process_data
from prioritize_candidates import prioritize_candidates

def main():
    # Define the job description
    job_description = "Data Scientist with 5+ years of experience in Python, SQL, and Machine Learning"

    # Define the directory of PDF resumes
    resume_directory = "/path/to/resumes"

    # Load the model and tokenizer
    tokenizer, model = load_model()

    # Initialize an empty list to store the scores for each candidate
    candidate_scores = []

    # Iterate over each PDF in the directory
    for filename in os.listdir(resume_directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(resume_directory, filename)

            # Process the data and get the score for the candidate
            score = process_data(file_path, job_description, tokenizer, model)
            candidate_scores.append((filename, score))

    # Prioritize the candidates based on their scores
    top_candidates = prioritize_candidates(candidate_scores)

    # Print the top candidates
    for candidate in top_candidates:
        print(f"Candidate: {candidate[0]}, Score: {candidate[1]}")

if __name__ == "__main__":
    main()
```