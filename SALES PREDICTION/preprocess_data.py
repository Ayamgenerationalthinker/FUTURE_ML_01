import pandas as pd

def preprocess_sales_data(input_csv='sales.csv', output_csv='clean_sales.csv'):
    # Load raw data
    df = pd.read_csv(input_csv, encoding='latin1')

    # Convert ORDERDATE to datetime
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
    df = df.dropna(subset=['ORDERDATE'])  # drop rows where date is invalid

    # Extract year and month for grouping
    df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')

    # Aggregate total sales per product per month
    sales_monthly = (
        df.groupby(['PRODUCTCODE', 'YEAR_MONTH'])
          .agg(monthly_sales=('SALES', 'sum'))
          .reset_index()
    )

    # Sort values so lag works correctly
    sales_monthly = sales_monthly.sort_values(['PRODUCTCODE', 'YEAR_MONTH'])

    # Create lag features for sales in previous months
    sales_monthly['sales_in_first_month'] = sales_monthly.groupby('PRODUCTCODE')['monthly_sales'].shift(2)
    sales_monthly['sales_in_second_month'] = sales_monthly.groupby('PRODUCTCODE')['monthly_sales'].shift(1)
    sales_monthly['sales_in_third_month'] = sales_monthly['monthly_sales']

    # Drop rows where lag values are missing (first two months will be NaN)
    sales_monthly = sales_monthly.dropna(subset=['sales_in_first_month', 'sales_in_second_month'])

    # Calculate a simple growth rate (example: % change between first and second month)
    sales_monthly['rate'] = (sales_monthly['sales_in_second_month'] - sales_monthly['sales_in_first_month']) / sales_monthly['sales_in_first_month']

    # Reorder columns as needed
    clean_df = sales_monthly[['rate', 'sales_in_first_month', 'sales_in_second_month', 'sales_in_third_month']]

    # Save to CSV
    clean_df.to_csv(output_csv, index=False)

    print(f"Preprocessed data saved to {output_csv}")

if __name__ == '__main__':
    preprocess_sales_data('sales.csv', 'clean_sales.csv')
