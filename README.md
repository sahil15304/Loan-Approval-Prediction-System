# 🏦 Loan Approval Prediction System

A **Machine Learning-based Loan Approval Prediction System** built using **Logistic Regression**.  
This project predicts whether a loan application should be **approved or denied** based on applicant details.  

We trained the model in **Jupyter Lab**, saved it as `.pkl` files, and built a **Python backend** with a **simple HTML interface** for easy predictions.

---

## 🚀 Features
- 🔢 **ML Model:** Logistic Regression for binary classification.
- 📊 **Data Preprocessing:** Encoding categorical values and scaling numerical features.
- 📓 **Training in Jupyter Lab:** Dataset cleaned, analyzed, and used to train the model.
- 🐍 **Backend Integration:** Python script (`app.py`) connects the model to the frontend.
- 🌐 **HTML Interface:** User-friendly form for entering loan details.
- ⚡ **Instant Predictions:** Loan Approved ✅ or Not Approved ❌.

---

## 🛠️ Tech Stack
| Layer            | Technology                  |
|------------------|---------------------------|
| **Model**        | Logistic Regression (Scikit-learn) |
| **Development**  | Python, Jupyter Lab        |
| **Backend**      | Flask / Python Script      |
| **Frontend**     | HTML (inside `templates/`) |
| **Dataset**      | CSV (Loan data)            |

---

## 📂 Project Structure
```
Loan-Approval-Prediction/
│
├── templates/               # HTML templates for frontend
├── app.py                   # Python backend file
├── label_encoders.pkl       # Encoders for categorical variables
├── loan_model.pkl           # Trained Logistic Regression model
├── New loan data.csv        # Dataset used for training/testing
└── README.md                # Project documentation
```

---

## ⚙️ How It Works
1. User inputs loan-related details (income, credit history, etc.) on the HTML form.
2. `app.py` loads the pre-trained model (`loan_model.pkl`) and label encoders.
3. The model predicts loan eligibility in real time.
4. Results (Approved/Denied) are displayed instantly on the web page.

---

## 📈 Model Training Steps
- Cleaned missing data and encoded categorical values.
- Trained Logistic Regression model using Scikit-learn.
- Evaluated performance with accuracy and confusion matrix.
- Saved trained model as `loan_model.pkl`.

---

⭐ If you found this project helpful, **give it a star** on GitHub!
