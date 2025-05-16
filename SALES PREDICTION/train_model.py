import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

def train_and_save_model(data_path='clean_sales.csv', model_path='model.pkl'):

    # Check if data file exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file '{data_path}' not found.")

    # Load dataset
    df = pd.read_csv(data_path, encoding='latin1')

    print("Columns in CSV:", df.columns.tolist())

    # Check required columns exist
    required_columns = ['rate', 'sales_in_first_month', 'sales_in_second_month', 'sales_in_third_month']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Data file must contain columns: {required_columns}")

    # Prepare features and target
    X = df[['rate', 'sales_in_first_month', 'sales_in_second_month']]
    y = df['sales_in_third_month']

    # Train linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Save trained model to file
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Model trained and saved successfully to '{model_path}'.")

if __name__ == "__main__":
    train_and_save_model()
