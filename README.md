# 🎓 Merit Map System 

An AI powered college recommendation and admission prediction system helps students find colleges based on their rank, category, branch preference, placement statistics, fees, seat availability and NIRF rankings.

## Problem Statement

Students face challenges in choosing the colleges and branches during counseling. Sometimes they are not aware of college cut-off information. My project aims to create a system that uses machine learning to predict college and branch options for students based on their rank and category with college rank analysis.

## 📌 Project Overview

Choosing a college can be tough for students during admission. Merit Map makes it easier by providing:

* College recommendations

* Admission chance prediction

* Placement analytics

* Fee analysis

* NIRF ranking analysis

* data visualization

The system uses machine learning and data analytics to provide personalized recommendations based on student inputs.

## 🚀 Features

### 🎯 College Recommendation Engine

Recommends colleges based on:

* Student rank

* Category (OC, BC, SC)

* Branch preference

* College cutoff trends

* Seat availability

### 🤖 Admission Predictor

Uses a random forest machine learning model to predict the probability of admission into a selected college.

### 📊 Analytics Dashboard

Provides insights into:

* Placement percentage

* College fees

* NIRF rankings

* Recommendation scores

### 🏆 Top Colleges Ranking

Ranks colleges using a custom recommendation score based on:

* Placement statistics

* package

* NIRF ranking

* Seat availability

## 🛠️ Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas

* NumPy

### Machine Learning

* Scikit-learn

* Random forest classifier

### Visualization

* Plotly

### Deployment

* GitHub

## 📂 Project Structure

```text

Merit-Map-System/
│
├── app.py
├── train_model.ipynb
├── enhanced_college_dataset.csv
├── requirements.txt
├── README.md
│
├── models/
│ ├── admission_model.pkl
│ ├── category_encoder.pkl
│ ├── college_encoder.pkl
│ └── branch_encoder.pkl
│
├── preview/
│ ├── home_page.png
│ ├── Recommendation_page.png
│ ├── Admission_predictor.png
│ └── Analytics.png

```

## 📊 Dataset Attributes

| Feature                | Description                      |
|------------------------|----------------------------------|
| Year                   | Admission year                   |
| category               | Student category                 |
| college                | College name                     |
| branch                 | Department/branch                |
| Cutoff_Rank            | Previous year cutoff rank        |
| Fees                   | tuition fee                      |
| Placement_Percentage   | Placement success rate           |
| Average_Package        | Average salary package           |
| NIRF_Rank              | NIRF ranking                     |
| Total_Seats            | Total available seats            |  
| Available_Seats        | seat availability                |

## 🧠 Machine Learning Model

### Algorithm Used

Random forest classifier

### Input Features

* Student rank
* Category
* College
* Branch
* College cutoff
* Fees

### Output

* Admission probability (%)

* Admission prediction

## 📈 Recommendation Score Formula

```python

Recommendation_Score =

(100. NIRF_Rank) * 0.30 +

Placement_Percentage * 0.30 +

Average_Package * 5 * 0.20 +

Seat_Ratio * 100 * 0.20

```

Where:

```python

Seat_Ratio =

Available_Seats / Total_Seats

```

## ⚙️ Installation

### Clone Repository

```bash

git clone https://github.com/YOUR_USERNAME/Merit-Map-System.git

```

```bash

cd Merit-Map-System

```

### Install Dependencies

```bash

pip install -r requirements.txt

```

## 📸 Application Screenshots

### Home Dashboard

Add screenshot here

```text

preview/home_page.png

```

### College Recommendation

Add screenshot here

```text

preview/Recommendation_page.png

```

### Admission Predictor

Add screenshot

```text

preview/Admission_predictor.png

```

### Analytics Dashboard

Add screenshot here

```text

preview/Analytics.png

```

## 🎯 Future Enhancements

* Multi-year cutoff analysis

* AI career counselor

* Top 10 recommendation

* Gemini AI integration

* Real-time college data updates

* Student login portal

* PDF report generation

* College comparison feature

* Scholarship recommendation system

## 💡 Use Cases

* Engineering college admissions

* Counseling centers

* Institutions

* Student career guidance

* Admission prediction systems

## 📚 Learning Outcomes

This project demonstrates:

* Machine learning

* Data analysis

* Recommendation systems

* Predictive analytics

* Streamlit web development

* Data visualization

* GitHub project management

## 👨‍💻 Author

**Dhanalakshmi B**

Developer | Machine learning enthusiast

GitHub: https://github.com/Dhanalakshmi745

## 📜 License

This project is developed for educational and research purposes.The datum used in this project are not real-time data . It is created for the development and learning purposes.


⭐ If you found this project consider giving it a star, on GitHub.
