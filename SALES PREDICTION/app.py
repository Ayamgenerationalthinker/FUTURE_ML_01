import matplotlib
matplotlib.use('Agg')
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
import matplotlib.pyplot as plt
import uuid
import time

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Ensure the 'static/plots' directory exists
plots_dir = os.path.join('static', 'plots')
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

def cleanup_old_plots(max_age_seconds=3600):
    """
    Delete plot images older than max_age_seconds from the plots directory.
    Default is 1 hour (3600 seconds).
    """
    now = time.time()
    for filename in os.listdir(plots_dir):
        file_path = os.path.join(plots_dir, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > max_age_seconds:
                try:
                    os.remove(file_path)
                    print(f"Deleted old plot image: {filename}")
                except Exception as e:
                    print(f"Error deleting file {filename}: {e}")

@app.route('/')
def home():
    return render_template('index.html', prediction_text="", plot_url=None)

@app.route('/predict', methods=['POST'])
def predict():
    cleanup_old_plots()
    try:
        # Retrieve and clean input values
        rate = float(request.form['rate'].replace('%', '').strip())
        month1 = float(request.form['month1'].replace('$', '').strip())
        month2 = float(request.form['month2'].replace('$', '').strip())

        # Prepare features and predict the sales for the 3rd month
        final_features = np.array([[rate, month1, month2]])
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        # Create a forecast line plot
        months = ['1st Month', '2nd Month', 'Predicted 3rd Month']
        values = [month1, month2, output]

        plt.figure(figsize=(6, 4))
        plt.plot(months, values, marker='o', linestyle='-', color='#3a86ff')
        plt.title('Sales Forecast Trend')
        plt.xlabel('Month')
        plt.ylabel('Sales ($)')
        plt.grid(True)

        # Save the plot with a unique name
        plot_id = f"{uuid.uuid4().hex}.png"
        plot_path = os.path.join(plots_dir, plot_id)
        plt.savefig(plot_path)
        plt.close()

        # Provide relative URL path for the image in template
        plot_url = f'/static/plots/{plot_id}'

        return render_template(
            'index.html',
            prediction_text=f'Predicted third month sales: ${output:,} (Growth Rate: {rate}%)',
            plot_url=plot_url
        )

    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('index.html', prediction_text="Error: Please enter valid numeric values.", plot_url=None)

@app.route('/results', methods=['POST'])
def results():
    try:
        data = request.get_json(force=True)
        features = np.array([list(data.values())])
        prediction = model.predict(features)
        output = prediction[0]
        return jsonify(output)
    except Exception as e:
        print(f"Error in /results endpoint: {e}")
        return jsonify({'error': 'Invalid input'}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
