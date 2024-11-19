# Final Project: Article Summarizer
# Spotify Tracks Sentiment Analysis

## Overview
This project uses Spotify API to retrieve saved ved tracks from a Spotify profile and analyze data.
Sentiment analysis is performed on the retrieved data, and summaries are generated based on both token-based and lemma-based polarity scores.

## Specs
- Retrieve saved Spotify tracks using the Spotify API.
- Convert track metadata into an HTML file for easy viewing.
- Perform sentiment analysis using token-based and lemma-based approaches.
- Generate summaries of the data based on sentiment polarity.

## Process
1. **Data Retrieval**:
   - Get saved Spotify tracks with the Spotify API
   - Python creates an HTML file (spotify_tracks.html) from the API response.

2. **Sentiment Analysis**:
   - The HTML sentences are analyzed with `TextBlob` for polarity scores.
   - Two approaches are used:
     - **Token-Based**: Analyzing sentences directly as they are.
     - **Lemma-Based**: Analyzing sentences after lemmatization using `spaCy`.

3. **Summary Generation**:
   - Summaries are created by selecting sentences with polarity scores above a determined cutoff.
   - Both token-based and lemma-based summaries are generated.

4. **Visualization**:
   - Histograms are created to visualize the distribution of sentiment polarity scores.

## Project Files
- `spotify_tracks.html`: The HTML file displaying track metadata.
- `spotify_tracks.pkl`: The pickle file containing the HTML content.
- Python scripts for:
  - Fetching data from the Spotify API.
  - Performing sentiment analysis and visualization.
  - Generating summaries.

## Technologies Used
- **Python**:
  - Libraries: `spotipy`, `textblob`, `spaCy`, `matplotlib`, `pickle`, `BeautifulSoup`.
- **Spotify API** for data retrieval.

## How to Run
1. Clone the repository:
   ```bash
   git clone <https://github.com/drodmay1/44620_P7.git>
   cd <Users/davidrodriguez/Documents/44620 web mining and applied NPL/44620_p7

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

3. Set up Spotify API credentials:
Create a Spotify Developer account and set up a new app.
Add your client_id, client_secret, and redirect_uri in the code.

4. Run the script to fetch data and perform analysis:
python <auth>.py
View results in the terminal and the generated files (spotify_tracks.html and others).

## Results
Sentiment polarity scores of the original data and summaries.
Visualizations of sentiment polarity distributions.
Clean and concise summaries based on token and lemma polarity scores.

## Acknowledgments
*Spotify API for providing track metadata.
**TextBlob and spaCy for sentiment analysis and natural language processing.
Matplotlib for data visualization.




