# Heart-disease-predictive-model

This is an end-to-end heart disease predictive model that utilizes Python libraries such as Pandas, NumPy, Scikit-learn, Matplotlib, and Seaborn. The model is deployed using Flask and integrated with HTML and CSS for web-based deployment. The predictive model is hosted on the Render web hosting platform.

## Overview

This project aims to predict the presence or absence of heart disease based on a set of input features. The model uses a dataset containing various cardiovascular health parameters such as age, sex, blood pressure, cholesterol levels, and other clinical measurements. By training a machine learning algorithm on this dataset, we have developed a predictive model capable of providing insights into an individual's heart health status. Data is gathered from kaggle platform.

## Libraries used

- Pandas: Used for data manipulation and preprocessing.
- NumPy: Used for numerical computations and operations.
- Seaborn: Used for data visualization and creating informative plots.
- Matplotlib: Used for creating various types of plots and charts.
- Scikit-learn: Used for building the price predictive model using machine learning algorithms.

## Model Deployment

The model is deployed using the Flask framework, which allows for easy integration of the machine learning model with HTML and CSS for a user-friendly interface. Flask handles the HTTP requests and responses, while the HTML templates define the structure and appearance of the web pages.

The predictive model is trained on a dataset using machine learning algorithms available in the scikit-learn library. The trained model is then saved and loaded during the Flask application's runtime to make predictions based on user input.

## Hosting on Render

The project is deployed on the Render web hosting platform. Render simplifies the process of deploying and managing web applications, providing a scalable and reliable hosting solution. The Flask application, along with the necessary dependencies, is deployed on Render to make the heart disease predictive model accessible over the internet.

## Project Structure

The project repository contains the following files and directories:

app.py: The Flask application file that handles HTTP requests and model deployment.
templates/: This directory contains the HTML templates used for rendering the user interface.
static/css/: This directory contains CSS files for styling the HTML templates.
dataset_heart.csv: This file contains the dataset used for training and evaluation.
model.pkl: pickle file containing the trained model
README.md: This file, providing an overview of the project and instructions for usage.


