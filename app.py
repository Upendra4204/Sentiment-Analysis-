from flask import Flask, render_template, request, jsonify
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
from io import BytesIO

app = Flask(__name__)

model = joblib.load('Xgboost.joblib')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')
analyzer = SentimentIntensityAnalyzer()
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if text input is provided
    if 'text' in request.form:
        text = request.form['text']
    
    # Check if audio file is provided
    elif 'audio' in request.files:
        audio_file = request.files['audio']
        
        # Convert audio file to text
        with sr.AudioFile(BytesIO(audio_file.read())) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
    else:
        return jsonify({"error": "No text or audio provided"}), 400

    # Sentiment Analysis using VADER
    predicted_probability = analyzer.polarity_scores(text)['compound']
    xgb_prediction = "Positive" if predicted_probability > 0 else "Negative" if predicted_probability < 0 else "Neutral"

    result = {
        'vader_sentiment': xgb_prediction,
        'probability_score': predicted_probability,
        'transcribed_text': text
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
