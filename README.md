# content-recommender
### Narrative-Based Content Recommendation System

#### Video Demo: ruby to add url herel.

#### Description:

A command-line tool that recommends books and movies based on deeper narrative similarities like themes, tone, mood, pace, and complexity rather than just genre. Users select 1-3 items they enjoy, and the system builds a preference profile to find content that feels similar.

The recommendation engine converts each item's attributes into a binary feature vector and uses cosine similarity to score every remaining item against the user's aggregated profile. Results are ranked by match percentage with explanations of why each item was recommended.

#### How to Run

1. Open a terminal in the project directory.
2. Install dependencies:
3. Run the program
4. Follow the prompts we've created below to go through and test out the recommendation engine:

#### Running Tests

pytest test_project.py -v

#### Files

- project.py — Main application. Handles user interaction, displays
  the catalog, and prints ranked recommendations with match explanations.
- helpers.py — Recommendation engine. Loads data, builds feature
  vectors, computes cosine similarity, and returns ranked results.
- data.json — Database of 18 books and movies, each tagged with
  genres, themes, tone, mood, pace, and complexity.
- test_project.py — Test suite with 17 tests covering data loading,
  similarity math, search, recommendations, and feature vectors.
- requirements.txt — Python package dependencies.

