```markdown
# Sales Forecast ML Web Application

This project develops a web application using Flask and a pre-trained machine learning model to predict sales for the third month based on the sales figures of the two preceding months and an estimated growth rate. The application provides an intuitive user interface for input, generates a dynamic visualization of the sales forecast trend, and handles potential input errors gracefully.


## Project Requirements

**Skills Gained:**
- Regression Modeling
- Web Application Development (Flask)
- Data Visualization (Matplotlib)
- Model Deployment

**Tools & Libraries:**
- Python
- Flask for web application framework
- NumPy for numerical operations
- Matplotlib for creating plots
- Scikit-learn (or other ML library used for training) for the predictive model
- Pickle for model serialization and deserialization

**Dataset:**
- The model used by this application was pre-trained on historical sales data (the specifics of this dataset are not part of this deployment project). The application takes growth rate and the sales of the first two months as input features to predict the third month's sales.

**Final Deliverables:**
- A functional Flask web application that takes user input and displays the predicted third-month sales.
- A dynamic visualization of the sales trend (first month, second month, predicted third month).
- Basic error handling for invalid user inputs.

## Project Structure


FUTURE\_ML\_01/
├── static/
│   └── css/
│       └── style.css         \# Stylesheet for the web application
│   └── plots/                \# Directory to store dynamically generated forecast plot images
│   └── img/
│       └── fallback.png    \# Fallback image for error display (though not explicitly used in the provided code)
├── templates/
│   └── index.html          \# Main HTML template for the user interface
├── app.py                    \# Flask application with routing and prediction logic
├── model.pkl                 \# Serialized pre-trained ML model file
├── requirements.txt          \# List of Python dependencies for the project
├── .gitignore
└── README.md                 \# Project overview and instructions



## 2. Install Dependencies

Create a virtual environment (recommended) and install the required packages listed in `requirements.txt`:


pip install -r requirements.txt


If a `requirements.txt` file is not available, you can manually install the necessary libraries:


pip install Flask numpy matplotlib scikit-learn


## 3\. Run the Flask Application

Execute the `app.py` file to start the web server:

python app.py

Open your web browser and navigate to `http://localhost:5000` to access the sales forecasting application.

## Output & Evaluation

After submitting the sales data and growth rate through the web interface:

  - The application displays the predicted sales figure for the third month.
  - A line plot is generated and shown, visualizing the sales trend from the first month through the predicted third month. This provides a visual representation of the forecast.
  - Basic error handling ensures that if non-numeric values are entered, an appropriate error message is displayed to the user.

**Note:** The evaluation of the pre-trained model's performance (e.g., MSE, RMSE) would have been conducted during the model training phase (the script for which is not part of this deployment). This application focuses on using the already trained model for predictions and visualization.

## Acknowledgments

  - The structure and initial code for this project were provided by the user.
  - The underlying machine learning model was pre-trained on historical sales data (details of which are not specified).
  - The web application framework used is Flask.
  - Data manipulation and numerical operations are performed using NumPy.
  - Visualization is achieved using Matplotlib.
  - The pre-trained model was likely developed using Scikit-learn.

## 👤 Author

Prince Fiebor

