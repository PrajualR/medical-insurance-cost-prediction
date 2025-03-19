
# Medical Insurance Prediction

This project uses Linear Regression to predict insurance costs based on various factors such as age, sex, BMI, number of children, smoking habits, and region.
A Streamlit web application has been integrated to allow users to interactively input data and get real-time insurance cost predictions.

## Dataset
The dataset used is insurance.csv from kaggle, which contains the following columns:

age: Age of the insured person.

sex: Gender (male = 1, female = 0).

bmi: Body Mass Index.

children: Number of dependents.

smoker: Whether the person is a smoker (yes = 1, no = 0).

region: Region of the insured person (one-hot encoded).

charges: Actual medical costs (target variable).

## Requirements
- Python 3.x
- Scikit-learn
- Pandas
- Numpy
- matplotlib
- seaborn
- streamlit
- pickle
- joblib

Run the Streamlit app using:
    ```bash
    streamlit run app.py
    ```


