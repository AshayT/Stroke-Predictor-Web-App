import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'gender': 'Male', 'age':20, 'hypertension':0, 'heart_disease': 0, 'ever_married': 'No','work_type' : 'Private', 'Residence_type' : 'Urban', 'avg_glucose_level' : 120, 'bmi' : 22})

print(r.json())

#idhhar sab input daalS