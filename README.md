# Fake News Detection Using NLP and Machine Learning

## Overview

Fake News Detection is a Natural Language Processing (NLP) and Machine Learning project that classifies news articles as either **Fake** or **Real** based on their textual content. The project leverages word embeddings and supervised machine learning algorithms to identify patterns within news articles and determine their authenticity.

---

## Features

* Automated classification of news articles into Fake or Real categories
* NLP-based text representation using spaCy word embeddings
* Implementation of multiple machine learning algorithms
* Feature scaling using MinMaxScaler
* Model evaluation using standard classification metrics
* End-to-end machine learning workflow

---

## Technologies Used

* Python
* Pandas
* NumPy
* spaCy
* Scikit-learn

---

## Machine Learning Models

### Multinomial Naive Bayes

A probabilistic classification algorithm commonly used in text classification tasks due to its efficiency and strong performance on textual data.

### K-Nearest Neighbors (KNN)

A distance-based classification algorithm that predicts the class of a news article based on the labels of its nearest neighbors.

---

## Project Workflow

### 1. Data Collection

Load and explore the fake and real news dataset.

### 2. Data Preprocessing

Prepare the dataset by cleaning text and encoding labels.

### 3. Text Vectorization

Convert news articles into numerical feature vectors using spaCy word embeddings.

### 4. Feature Scaling

Normalize feature values using MinMaxScaler to improve model performance.

### 5. Train-Test Split

Split the dataset into training and testing sets.

### 6. Model Training

Train machine learning models on the processed data.

### 7. Model Evaluation

Evaluate model performance using classification metrics.

### 8. Prediction

Predict whether unseen news articles are Fake or Real.

---

## Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score

These metrics provide a comprehensive assessment of the classifier's performance.

---

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

---

## Project Structure

```text
Fake-News-Detector/
│
├── Fake_Real_Data.csv
├── fake_news_detector.ipynb
├── requirements.txt
├── README.md
│
├── models/
├── notebooks/
└── assets/
```

<img width="819" height="416" alt="Screenshot from 2026-06-11 14-56-39" src="https://github.com/user-attachments/assets/6c55d4ca-dc85-471b-8ce6-e78c34502737" />
<img width="819" height="416" alt="Screenshot from 2026-06-11 14-57-16" src="https://github.com/user-attachments/assets/c9ae5f2e-98de-46d3-b3d1-d3273bb969aa" />

---

## Learning Outcomes

This project provides practical experience in:

* Natural Language Processing
* Word Embeddings
* Feature Engineering
* Machine Learning Classification
* Model Evaluation
* Text Analytics

---

## Future Enhancements

* Integration of deep learning architectures such as LSTM and Transformers
* Deployment using Flask or Streamlit
* Real-time news classification interface
* Advanced text preprocessing techniques
* Hyperparameter optimization for improved accuracy

---

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be combined to build an effective fake news detection system. By transforming textual information into meaningful numerical representations and applying classification algorithms, the system can accurately determine the authenticity of news articles and assist in combating misinformation.
