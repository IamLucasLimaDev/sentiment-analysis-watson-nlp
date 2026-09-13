"""Flask server for the Sentiment Analysis application using Watson NLP."""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Receives the text from the HTML interface and runs sentiment
    analysis over it using the sentiment_analyzer function. Returns the
    label and confidence score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Please enter some text to analyze."

    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."

    formatted_label = label.split('_')[1]
    return f"The given text has been identified as {formatted_label} with a score of {score}."


@app.route("/")
def render_index_page():
    """Renders the main application page over the Flask channel."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    