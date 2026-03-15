import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os
from dotenv import load_dotenv

# Load API Key securely
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Try to import new Google GenAI package
try:
    from google import genai
    if API_KEY:
        client = genai.Client(api_key=API_KEY)
        USE_GEMINI = True
    else:
        USE_GEMINI = False
except ImportError:
    USE_GEMINI = False
    client = None

class ProcessAgent:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.is_trained = False

    def train(self, df):
        features = df[['Temp_C', 'Pressure_Bar', 'Flow_Rate']]
        self.model.fit(features)
        self.is_trained = True
        joblib.dump(self.model, 'agent_model.pkl')

    def detect_anomalies(self, df):
        features = df[['Temp_C', 'Pressure_Bar', 'Flow_Rate']]
        predictions = self.model.predict(features) 
        # FIXED: Convert numpy array to series before using .map()
        df['Anomaly_Predicted'] = pd.Series(predictions).map({1: 0, -1: 1})
        return df

    def generate_insight(self, row):
        # Prepare context for the AI
        context = (
            f"Temperature: {row['Temp_C']:.2f}C, "
            f"Pressure: {row['Pressure_Bar']:.2f}Bar, "
            f"Flow: {row['Flow_Rate']:.2f}kg/hr. "
            f"Anomaly Detected: {bool(row['Anomaly_Predicted'])}"
        )
        
        if USE_GEMINI and client and row['Anomaly_Predicted'] == 1:
            try:
                prompt = (
                    f"You are a Plant Engineer. Analyze this sensor data: {context}. "
                    f"Provide a one-sentence diagnosis and recommended action. "
                    f"Keep it professional and concise."
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                return f"🤖 AI Insight: {response.text}"
            except Exception as e:
                return f"⚠️ AI Error: {str(e)} - Check Cooling System."
        
        # Fallback logic if no API key or normal operation
        if row['Anomaly_Predicted'] == 1:
            if row['Temp_C'] > 290:
                return "⚠️ High Temperature: Check cooling water flow."
            elif row['Pressure_Bar'] > 55:
                return "⚠️ High Pressure: Potential blockage in filter."
            else:
                return "⚠️ Process Deviation: Review sensor calibration."
        else:
            return "✅ Process Normal."

    def load_model(self):
        try:
            self.model = joblib.load('agent_model.pkl')
            self.is_trained = True
        except:
            pass