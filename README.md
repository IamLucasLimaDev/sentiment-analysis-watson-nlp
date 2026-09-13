# Sentiment Analysis with Watson NLP

A Flask web application that analyzes the sentiment of user-provided text using IBM Watson's NLP (BERT-based) sentiment analysis service. Users enter a sentence through a simple web interface and receive back a sentiment label (positive, negative, or neutral) along with a confidence score.

## Demo

Enter any text into the input field, click **Run Sentiment Analysis**, and the app returns the identified sentiment with its confidence score.

Example:
```
Input:  "I love this new technology"
Output: The given text has been identified as POSITIVE with a score of 0.997183.
```

## Features

- **Sentiment classification** — Positive, Negative, or Neutral, powered by a BERT-based model via Watson NLP.
- **Confidence scoring** — Each prediction includes a numeric confidence score.
- **Error handling** — Gracefully handles invalid input, empty fields, and unexpected API responses instead of crashing.
- **Unit tested** — Core sentiment analysis logic is covered by `unittest` test cases.
- **PEP8 compliant** — Code quality verified with `pylint`, scoring 10.00/10.

## Tech Stack

- **Python 3.11**
- **Flask** — web server and routing
- **Requests** — HTTP calls to the Watson NLP API
- **IBM Watson NLP (Embeddable AI)** — BERT-based sentiment analysis model
- **HTML / JavaScript** — front-end interface
- **unittest** — automated testing
- **pylint** — static code analysis

## Project Structure

```
.
├── SentimentAnalysis/
│   ├── __init__.py
│   └── sentiment_analysis.py    # Core function that calls the Watson NLP API
├── static/
│   └── mywebscript.js           # Front-end logic (AJAX call to /sentimentAnalyzer)
├── templates/
│   └── index.html               # Web interface
├── server.py                    # Flask app and route definitions
├── test_sentiment_analysis.py   # Unit tests for sentiment_analyzer()
└── README.md
```

## How It Works

1. The user submits text through the web form (`index.html`).
2. `server.py` receives the request at the `/sentimentAnalyzer` endpoint and passes the text to `sentiment_analyzer()`.
3. `sentiment_analyzer()` (in `SentimentAnalysis/sentiment_analysis.py`) sends a POST request to the Watson NLP sentiment prediction API.
4. The response is parsed, and the sentiment label and score are extracted.
5. If the input is invalid, empty, or the API fails to process it, the app returns a clear error message instead of crashing.
6. The result is displayed back to the user on the web page.

## Running Locally

> **Note:** This project was built and tested inside an IBM Skills Network Cloud IDE, which provides access to the Watson NLP Embeddable AI service. The Watson NLP endpoint used here may not be reachable outside that environment.

1. Clone the repository:
   ```bash
   git clone https://github.com/IamLucasLimaDev/sentiment-analysis-watson-nlp.git
   cd sentiment-analysis-watson-nlp
   ```

2. Install dependencies:
   ```bash
   pip install flask requests
   ```

3. Run the server:
   ```bash
   python3.11 server.py
   ```

4. Open your browser at `http://localhost:5000`.

## Running Tests

```bash
python3.11 test_sentiment_analysis.py
```

## Code Quality

Static analysis was performed using `pylint`:

```bash
pylint server.py
pylint SentimentAnalysis/sentiment_analysis.py
```

Both files score **10.00/10**, following PEP8 style guidelines (docstrings, f-strings, line length, and naming conventions).

## What I Learned

This project was built as a hands-on exercise in:
- Consuming a third-party NLP API and handling its responses safely
- Structuring a Flask application with proper routing
- Writing and running unit tests with `unittest`
- Debugging real-world issues (indentation errors, inconsistent tabs/spaces, variable naming mismatches)
- Applying static code analysis and PEP8 conventions
- Version control workflow: committing changes and pushing to a personal GitHub repository

## License

This project is licensed under the Apache 2.0 License — see the [LICENSE](LICENSE) file for details.