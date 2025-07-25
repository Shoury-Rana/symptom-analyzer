import joblib
import pandas as pd

from django.conf import settings
import os

MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'ai_models', 'health_risk_model.pkl')

# Load files only once
model = joblib.load(os.path.join(settings.BASE_DIR, 'predictor', 'ai_models', 'health_risk_model.pkl'))
scaler = joblib.load(os.path.join(settings.BASE_DIR, 'predictor', 'ai_models', 'scaler.pkl'))
feature_order = joblib.load(os.path.join(settings.BASE_DIR, 'predictor', 'ai_models', 'feature_order.pkl'))
impute_values = joblib.load(os.path.join(settings.BASE_DIR, 'predictor', 'ai_models', 'impute_values.pkl'))

labels = [
    'diabetes_risk', 'heart_attack_risk', 'hypertension_risk',
    'diabetes', 'hypertension', 'heart_disease', 'obesity'
]

def predict_health_risks(input_data):
    input_data['gender'] = 1 if input_data.get('gender', 'male').lower() == 'male' else 0

    # Fill missing values with training means
    for feat in feature_order:
        if feat not in input_data or input_data[feat] is None:
            input_data[feat] = impute_values[feat]

    # Convert to DataFrame and reorder columns
    input_df = pd.DataFrame([input_data])[feature_order]

    # Scale and predict
    input_scaled = scaler.transform(input_df)
    pred = model.predict(input_scaled)[0]

    return dict(zip(labels, pred.tolist()))