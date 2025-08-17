# Heart Disease Prediction Web App 🚑❤️

This project is a **Flask web application** that predicts whether a person is at risk of heart disease using a pre-trained Machine Learning model (`heart-disease.pkl`).  
It provides a simple web interface (`index.html`) where users can input medical parameters and get instant predictions.

---

## 🚀 Features
- Built with **Flask**
- Uses a **pickled ML model (Logistic Regression / sklearn)**
- Deployed on **AWS Elastic Beanstalk**
- Frontend: HTML templates (Jinja2)
- Prediction served via **Gunicorn (WSGI server)**

---

## 📂 Project Structure
```
.
├── application.py          # Flask entry point
├── heart-disease.pkl       # Trained ML model
├── Procfile                # Tells EB to use Gunicorn
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Web form for inputs + results
└── README.md               # Project documentation
```

---

## ⚙️ Installation (Local Setup)

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts\activate       # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app locally:
   ```bash
   python application.py
   ```
   Visit: `http://127.0.0.1:5000/`

---

## ☁️ Deployment (AWS Elastic Beanstalk)

1. Ensure you have these files in project root:
   - `application.py`
   - `requirements.txt`
   - `Procfile`
   - `heart-disease.pkl`
   - `templates/`

2. Initialize EB environment:
   ```bash
   eb init -p python-3.9 heart-disease-app
   ```

3. Create an environment and deploy:
   ```bash
   eb create heart-disease-env
   eb deploy
   ```

4. Open in browser:
   ```bash
   eb open
   ```

---

## 📦 Requirements
Key Python dependencies (see `requirements.txt` for full list):
- Flask
- gunicorn
- numpy
- scikit-learn

---

## 🖼️ Screenshot
<img width="775" height="943" alt="image" src="https://github.com/user-attachments/assets/4a744222-a952-4c85-80e4-99b4ed13ba30" />

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is licensed under the MIT License.
