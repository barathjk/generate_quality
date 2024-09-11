import pandas as pd
import logging
import os

# Set up logging to both file and console
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler to log to a file
file_handler = logging.FileHandler('app.log', mode='w')
file_handler.setLevel(logging.INFO)

# Create console handler to log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def read_excel(file_path):
    try:
        logging.info(f"Attempting to read Excel file: {file_path}")
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
        logging.info("File read successfully!")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Example usage
file_path = 'test_report.xlsx'  # Replace with your Excel file path
current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, file_path)
df = read_excel(file_path)
pd.set_option('display.max_rows', None)

if df is not None:
    filtered_df = df[(df['AGE'] >= 18) & (df['AGE'] <= 22)]# Display the first few rows of the DataFrame
    logging.info(filtered_df)
    filtered_df.to_excel("Generated_excel.xlsx", na_rep=True)
    zuul_path = r"generated.xlsx"
    filtered_df.to_excel(zuul_path)
    print(os.getcwd())
    for each_file in os.listdir(os.getcwd()):
        print(each_file)
    print(os.path.dirname(os.path.realpath(__file__)))
    for each_file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        print(each_file)
