
import pandas as pd

def load_csv(file):
    """
    Load and validate a CSV file.
    :param file: Uploaded file object
    :return: DataFrame if successful, error message if failed
    """
    try:
        df = pd.read_csv(file.name)
        return df
    except Exception as e:
        return f"Error loading CSV: {str(e)}"