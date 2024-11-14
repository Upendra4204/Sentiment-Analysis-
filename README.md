# Sentiment Analysis on E-commerce

## Description
Sentiment Analysis on E-commerce is a project that aims to analyze customer reviews from an e-commerce platform to determine whether the sentiment is positive, negative, or neutral. This project uses various machine learning techniques, including **TF-IDF (Term Frequency-Inverse Document Frequency)** and **XGBoost**, to predict the sentiment of customer reviews based on their text.

Key Features:
- **Text Preprocessing**: The project includes steps for cleaning and preprocessing raw text data.
- **Feature Engineering**: Utilizes TF-IDF vectorizer to transform textual data into numerical features.
- **Sentiment Prediction**: XGBoost model is trained to classify reviews into positive, negative, or neutral sentiments.
- **Model Saving**: The trained models (XGBoost, TF-IDF vectorizer) are saved as `.joblib` files for easy reuse and deployment.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Installation

To get started with the project, clone the repository and install the necessary dependencies.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Upendra4204/Sentiment-Analysis-.git
2.**Navigate into the project directory**: 
   cd sentiment-analysis-on-e-commerce
3.**Create a virtual environment (optional but recommended):
   python -m venv venv
4.**Activate the virtual environment**:
   venv\Scripts\activate
5.**Install Dependencies**:
  particularly there is no folder to install depencies go through manually  
  ####    Usage
  Once the project is set up, you can run the sentiment analysis on your e-commerce reviews by using the following commands:
 6.**Run the main app**:
   python app.py 
   This will start a Flask web application (if app.py is a web application) or run the analysis directly in the command line. 
  7.**Run the analysis**:
    You can use the provided main_file_1.py to train the model, test it on your own dataset, or predict sentiment based on new e-commerce reviews.
    python main_file_1.py
View Results: After running the model, you'll see the sentiment classification for each review (Positive, Negative, Neutral). 

Thanks Namasthe ..! Incase of doubts can contact ugummilla@gmail.com
