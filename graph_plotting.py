import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(csv_data, x_column, y_column):
   
    try:
        df = pd.read_csv(csv_data.name)
        # Plot the graph
        df.plot(kind='bar', x=x_column, y=y_column)
        plt.title(f"{x_column} vs {y_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        # Save the plot
        plot_path = "plot.png"
        plt.savefig(plot_path)
        plt.close()  # Close the plot to free memory
        return plot_path
    except Exception as e:
        return f"Error generating graph: {str(e)}"
