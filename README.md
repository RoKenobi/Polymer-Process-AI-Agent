# 🏭 Ultem Polymer Plant AI Assistant

An intelligent AI-powered monitoring system that detects anomalies in polymer manufacturing processes and provides automated operational insights using Machine Learning and Generative AI.

## 📋 Overview

This project addresses the critical need for automated process monitoring in industrial polymer plants. The system combines unsupervised machine learning (Isolation Forest) with Generative AI (Google Gemini) to:

- Detect process anomalies in real-time
- Generate human-readable diagnostic insights
- Reduce manual monitoring workload
- Prevent costly production deviations

## ✨ Features

- **Automated Anomaly Detection**: Uses Isolation Forest algorithm to identify multivariate process deviations
- **AI-Powered Insights**: Integrates Google Gemini 2.0 Flash to generate plain-English diagnoses and recommendations
- **Interactive Dashboard**: Real-time Streamlit visualization with process trends and metrics
- **Intelligent Alerting**: Context-aware recommendations based on temperature, pressure, and flow rate anomalies
- **Professional Documentation**: Includes complete Control Philosophy documentation for engineering teams

## 🛠️ Tech Stack

- **Programming**: Python 3.12+
- **Machine Learning**: Scikit-Learn (Isolation Forest)
- **Generative AI**: Google Gemini 2.0 Flash
- **Visualization**: Streamlit, Plotly
- **Data Processing**: Pandas, NumPy
- **Security**: python-dotenv for API key management

## 📦 Installation

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd Polymer_AI_Agent
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gemini API key:
    - Create a `.env` file in the project root
    - Add your API key:
        ```
        GEMINI_API_KEY=your_api_key_here
        ```

## 🚀 Usage

1. Generate synthetic plant 
    ```bash
    python data_generator.py
    ```

2. Launch the application:
    ```bash
    streamlit run app.py
    ```

3. Access the dashboard at `http://localhost:8501`

## 📊 How It Works

### Architecture Flow

    Sensor Data → Data Cleaning → Isolation Forest Model → Anomaly Detection
                                                        ↓
                                            Gemini AI Analysis
                                                        ↓
                                        Operational Insights + Dashboard

### Anomaly Detection Logic

- **Hard Limits**: Temperature ±10°C from setpoint triggers critical alerts
- **Soft Limits**: Isolation Forest detects multivariate deviations
- **AI Reasoning**: Gemini analyzes context and provides actionable recommendations

## 📄 Documentation

This project includes professional engineering documentation:

- **Control_Philosophy.pdf**: Complete control logic, alarm definitions, and operational procedures
- **Version Control**: Documented change history and approval workflows
- **Process Standards**: Aligned with industrial automation best practices

## 🎯 Key Achievements

- Detects 5% process anomalies with multivariate analysis
- Generates context-aware insights in <2 seconds
- Reduces manual monitoring workload by automating data analysis
- Provides explainable AI recommendations for engineering teams

## 🔒 Security

- API keys stored securely in `.env` file
- `.env` excluded from version control via `.gitignore`
- No sensitive data committed to repository

## 📝 License

MIT License - feel free to use for educational and commercial purposes.

## 👤 Author

**Ben**

## 🤝 Contributing

Contributions welcome! This project demonstrates:
- Machine Learning for industrial applications
- Generative AI integration
- Process automation
- Technical documentation

---

*Built for industrial process optimization and digitalization*
