# fp-contentrecommender
### Narrative-Based Content Recommendation System

#### Video Demo: https://us06web.zoom.us/rec/share/tDo8rcCsdJkUo1bcItZAHxl3Pd6hHb94U3UNbyqTBKLRzRakeXZ-FWsgIvkombHO.scdP6mq4LyvfLm4A 
Passcode: NBU5gwf&

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

- project.py: Main application. Handles user interaction, displays
  the catalog, and prints ranked recommendations with match explanations.
- helpers.py: Recommendation engine. Loads data, builds feature
  vectors, computes cosine similarity, and returns ranked results.
- data.json: Database of 18 books and movies, each tagged with
  genres, themes, tone, mood, pace, and complexity.
- test_project.py: Test suite with 17 tests covering data loading,
  similarity math, search, recommendations, and feature vectors.
- requirements.txt: Python package dependencies.

## Data Sources

Movie entries sourced from the AFI 100 Greatest American Films list (https://www.afi.com/afis-100-years-100-movies/) with some additional contemporary films selected to improve thematic diversity. Book entries sourced from TIME Magazine's 100 Best Novels list (https://time.com/collection/100-best-novels/) with additional titles from the Modern Library 100 Best Novels list (https://www.modernlibrary.com/top-100/novels/). All theme, tone, pace, and complexity tags were manually assigned by the author based on each work's narrative characteristics.

