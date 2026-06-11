Fake News Detector Using NLP and Machine Learning
Project Overview

The Fake News Detector is a Natural Language Processing (NLP) and Machine Learning project designed to classify news articles as either Fake or Real based on their textual content.

The system analyzes the text of news articles, converts them into numerical representations using NLP techniques, and applies machine learning algorithms to predict their authenticity.

Objective

The main objective of this project is to build a machine learning model that can:

Process and understand news text using NLP techniques
Convert text data into numerical vector representations
Train machine learning models on labeled datasets
Accurately classify news as Fake or Real
Dataset

The dataset contains labeled news articles:

Text: News content
Label: Fake or Real
Label Encoding:
Fake → 0
Real → 1
Technologies Used
Python
Pandas
NumPy
spaCy (for word embeddings)
Scikit-learn
Machine Learning Algorithms

The following models are used:

Multinomial Naive Bayes
K-Nearest Neighbors (KNN)
Workflow
Data Loading
Data Preprocessing
Text Vectorization using spaCy
Feature and Label Separation
Train-Test Split
Feature Scaling using MinMaxScaler
Model Training
Model Evaluation
Prediction on New Data
Text Representation

The textual data is converted into numerical form using spaCy word embeddings.

Each news article is transformed into a fixed-length vector representation, which is used as input for machine learning models.

Model Training

The dataset is split into training and testing sets. The models are trained on the training data and evaluated on unseen test data using performance metrics.

Evaluation Metrics

The performance of models is measured using:

Accuracy
Precision
Recall
F1-Score
Results

The trained model is capable of distinguishing between fake and real news based on learned patterns from text data.

Installation and Setup
pip install pandas numpy spacy scikit-learn
python -m spacy download en_core_web_lg
How to Run
Load the dataset
Run preprocessing steps
Generate word vectors using spaCy
Train the model
Evaluate performance
Test with new input data
Project Structure
Fake-News-Detector/
│
├── dataset/
├── notebooks/
├── fake_news_model.ipynb
├── README.md
└── requirements.txt
Future Improvements
Use deep learning models (LSTM, BERT)
Improve preprocessing pipeline
Deploy as a web application
Improve accuracy using advanced embeddings
