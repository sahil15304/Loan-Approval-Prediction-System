import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

with open('loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

def convert_to_numeric(data):
    categorical_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    
    dependents_map = {'0': 0, '1': 1, '2': 2, '3': 3}
    
    for column in categorical_columns:
        if data[column] in label_encoders[column].classes_:
            data[column] = label_encoders[column].transform([data[column]])[0]
        else:
            data[column] = 0  
    
    if data['Dependents'] in dependents_map:
        data['Dependents'] = dependents_map[data['Dependents']]
    else:
        data['Dependents'] = 0  
    
    numeric_columns = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
    for column in numeric_columns:
        if data[column] is not None:
            data[column] = float(data[column])  
        else:
            data[column] = 0.0  
    
    return data

def preprocess_input(data):
    data = convert_to_numeric(data)
    
    return np.array([list(data.values())]).reshape(1, -1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        input_data = {
            'Gender': request.form['gender'],
            'Married': request.form['married'],
            'Dependents': request.form['dependents'],
            'Education': request.form['education'],
            'Self_Employed': request.form['self_employed'],
            'ApplicantIncome': request.form['applicant_income'],
            'CoapplicantIncome': request.form['coapplicant_income'],
            'LoanAmount': request.form['loan_amount'],
            'Loan_Amount_Term': request.form['loan_term'],
            'Credit_History': request.form['credit_history'],
            'Property_Area': request.form['property_area']
        }

        preprocessed_data = preprocess_input(input_data)

        prediction = model.predict(preprocessed_data)

        result = 'Approved' if prediction[0] == 1 else 'Rejected'

        return render_template('index.html', prediction_text=f'Loan Status: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
