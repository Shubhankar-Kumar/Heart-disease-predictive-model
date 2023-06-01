from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)