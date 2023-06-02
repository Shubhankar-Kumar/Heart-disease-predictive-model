from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
data = pd.read_csv('dataset_heart.csv',usecols=lambda col: col != 'heart disease')

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/make_prediction', methods= ["POST"])
def make_pred():
    predictor = []
    for i in data.columns:
        x = float(request.form.get(i))
        predictor.append(x)

    predictor = np.array(predictor).reshape(1,-1)
    predicted_class = model.predict(predictor)
    if predicted_class[0]==1:
        x = "Your cardiovascular health may be at risk. Seek medical attention for further evaluation."
        color = "red"

    else:
        x = "Great news! No signs of heart disease detected. Stay committed to a healthy lifestyle."
        color = "green"

    return render_template('index.html',pred=x,pred_color=color)



if __name__ == "__main__":
    app.run(debug=True)