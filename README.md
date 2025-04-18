# Letterboxd Movie Review Sentiment Analysis

This project involves scraping user reviews from Letterboxd for 50 popular movies and analyzing their sentiment using natural language processing (NLP). The reviews are collected using Selenium and organized into a CSV file. The data is then used to build an interactive Streamlit dashboard that visualizes public sentiment and review trends for each movie.

## Project Features

- Scrape reviews from Letterboxd using Selenium.
- Store scraped data in a structured CSV format.
- Perform sentiment analysis using tools like VADER or Hugging Face Transformers.
- Build a Streamlit dashboard that displays:
  - Movie metadata (title, poster, genre, runtime, etc.)
  - Sentiment distribution charts
  - Word clouds for positive and negative reviews
  - Sample user reviews
  - Time-based sentiment trends (optional)

## Tools and Libraries Used

- Python
- Selenium
- Pandas, NumPy
- NLTK, VADER, or Transformers (for sentiment analysis)
- WordCloud, Matplotlib, Plotly
- Streamlit
- TMDb API (for fetching movie metadata)

## Project Structure

- `scraper.py`: Script for scraping reviews from Letterboxd.
- `movies.csv`: Contains movie titles to be scraped.
- `all_reviews.csv`: Output file storing collected reviews.
- `app.py`: Streamlit dashboard displaying the analysis (optional, if implemented).
- `README.md`: Project documentation.

## How the Scraping Works

- The project uses Selenium with a headless Chrome browser to simulate user interaction.
- A delay is added between scrolls and movie loads to reduce the chance of getting blocked.
- Each team member is responsible for scraping a portion of the movies. This project scrapes 18 out of the total 50 movies.
- Reviews are stored under the column corresponding to each movie name in the output CSV.

## How to Use

1. Install dependencies listed in `requirements.txt`.
2. Add your movies to `movies.csv` (one column per movie).
3. Run the scraping script:
   ```bash
   python scraper.py
   ```
4. Once data is collected, use it for sentiment analysis or visualization using the Streamlit app.

## Notes

- Scraping is performed in batches with randomized delays to stay within acceptable usage limits.
- The project avoids excessive scraping to minimize the risk of IP blocking.

