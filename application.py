from flask import Flask, request, render_template
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


application = Flask(__name__)

lgr = pickle.load(open("heart-disease.pkl","rb"))

@application.route("/", methods = ['GET'])
def home():
  return render_template("index.html")

@application.route("/predict", methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        init_features = [int(x) for x in request.form.values()]
        final_features = [np.array(init_features)]
        prediction = lgr.predict(final_features)
        if prediction == 1:
              return render_template('index.html',prediction_text = "You are Fine.")
        else:
              return render_template('index.html',prediction_text = "You need treatment.")

if __name__ == '__main__':
  application.run(port=5000,debug=True)