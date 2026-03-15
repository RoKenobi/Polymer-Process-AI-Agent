import pandas as pd
import numpy as np

def generate_polymer_data(n_rows=1000):
    np.random.seed(42)
    # Fixed: 'H' is deprecated, use 'h'
    dates = pd.date_range(start="2023-01-01", periods=n_rows, freq="h")
    
    # Normal Operating Conditions
    temp = np.random.normal(280, 5, n_rows)       # Extruder Temp (°C)
    pressure = np.random.normal(50, 2, n_rows)    # Pressure (Bar)
    flow_rate = np.random.normal(100, 10, n_rows) # Flow Rate (kg/hr)
    
    # Target Quality (Viscosity)
    viscosity = 200 + (temp * 0.5) - (pressure * 2) + np.random.normal(0, 5, n_rows)
    
    df = pd.DataFrame({
        'Timestamp': dates,
        'Temp_C': temp,
        'Pressure_Bar': pressure,
        'Flow_Rate': flow_rate,
        'Viscosity': viscosity
    })
    
    # Inject Anomalies (5% of data)
    anomaly_indices = np.random.choice(n_rows, size=int(n_rows*0.05), replace=False)
    df.loc[anomaly_indices, 'Temp_C'] += np.random.uniform(20, 40, len(anomaly_indices))
    df.loc[anomaly_indices, 'Viscosity'] -= np.random.uniform(30, 50, len(anomaly_indices))
    
    df['Anomaly_Actual'] = 0
    df.loc[anomaly_indices, 'Anomaly_Actual'] = 1
    
    return df

if __name__ == "__main__":
    df = generate_polymer_data()
    df.to_csv('plant_data.csv', index=False)
    print("Data generated: plant_data.csv")