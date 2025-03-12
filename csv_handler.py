
import pandas as pd

def load_csv(file):
   
    try:
        df = pd.read_csv(file.name)
        return df
    except Exception as e:
        return f"Error loading CSV: {str(e)}"
