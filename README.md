# Fake News Detection Using NLP and Machine Learning

## Overview

Fake News Detection is a Natural Language Processing (NLP) and Machine Learning project designed to classify news articles as **Fake** or **Real** based on their textual content. The system utilizes spaCy word embeddings and supervised machine learning algorithms to analyze linguistic patterns and determine the authenticity of news articles.

This project demonstrates a complete NLP pipeline, including data preprocessing, text vectorization, feature scaling, model training, evaluation, and prediction.

## Features

* Automated classification of news articles into Fake or Real categories
* NLP-based text representation using spaCy word embeddings
* Implementation of machine learning classification algorithms
* Feature scaling using MinMaxScaler
* Performance evaluation using standard classification metrics
* Interactive prediction interface using Streamlit
* End-to-end machine learning workflow

## Technologies Used

* Python
* Pandas
* NumPy
* spaCy
* Scikit-learn
* Streamlit
* Joblib

## Machine Learning Models

### Multinomial Naive Bayes

A probabilistic machine learning algorithm widely used for text classification tasks. It is computationally efficient and performs well on high-dimensional textual data.

### K-Nearest Neighbors (KNN)

A distance-based classification algorithm that predicts the class of a news article by analyzing the labels of its nearest neighboring samples.

## Project Workflow

### 1. Data Collection

Load and explore the fake and real news dataset.

### 2. Data Preprocessing

Clean the text data, remove unnecessary characters, and encode target labels.

### 3. Text Vectorization

Convert news articles into numerical feature vectors using spaCy's pre-trained word embeddings.

### 4. Feature Scaling

Normalize feature values using MinMaxScaler to improve model performance and consistency.

### 5. Train-Test Split

Split the dataset into training and testing sets for model evaluation.

### 6. Model Training

Train machine learning models using the processed feature vectors.

### 7. Model Evaluation

Evaluate model performance using classification metrics such as accuracy, precision, recall, and F1-score.

### 8. Prediction

Classify unseen news articles as Fake or Real using the trained model.

## Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score

These metrics provide a comprehensive assessment of the classifier's effectiveness and reliability.

 screenshot1
<img width="819" height="416" alt="Screenshot from 2026-06-11 14-56-39" src="https://github.com/user-attachments/assets/6c55d4ca-dc85-471b-8ce6-e78c34502737" />
 screenshot2
<img width="819" height="416" alt="Screenshot from 2026-06-11 14-57-16" src="https://github.com/user-attachments/assets/c9ae5f2e-98de-46d3-b3d1-d3273bb969aa" />
```

```markdown
![Fake News Detector Home Page](assets/home_page.png)
```

### Prediction Result

```text
assets/prediction_result.png
```

```markdown
![Prediction Result](assets/prediction_result.png)
```

> Replace the image paths with your actual screenshots after uploading them to the repository.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy language model:

```bash
python -m spacy download en_core_web_lg
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Project Structure

```text
Fake-News-Detector/
│
├── Fake_Real_Data.csv
├── app.py
├── fake_news_detector.ipynb
├── fake_news_nb_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── assets/
│   ├── home_page.png
│   └── prediction_result.png
│
├── models/
└── notebooks/
```

## Learning Outcomes

This project provides practical experience in:

* Natural Language Processing (NLP)
* Word Embeddings and Text Vectorization
* Feature Engineering
* Machine Learning Classification
* Model Evaluation and Validation
* Streamlit Application Development
* Text Analytics

## Future Enhancements

* Integration of deep learning architectures such as LSTM, GRU, and Transformers
* Real-time news verification system
* Deployment using cloud platforms
* Advanced text preprocessing and feature extraction techniques
* Hyperparameter optimization for improved accuracy
* Explainable AI (XAI) for prediction transparency
* Support for multilingual news classification

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be combined to build an effective fake news detection system. By transforming textual information into meaningful numerical representations and applying classification algorithms, the system can accurately classify news articles as Fake or Real. The project serves as a practical example of applying NLP techniques to address the growing challenge of misinformation in the digital era.

















