import gradio as gr
from csv_handler import load_csv
from llm_integration import ask_llm
from graph_plotting import plot_graph

def process_csv(file):
    """
    Process the uploaded CSV file.
    :param file: Uploaded file object
    :return: DataFrame or error message
    """
    return load_csv(file)

def process_question(question, csv_data):
    """
    Process the user's question using the LLM.
    :param question: User's question
    :param csv_data: DataFrame containing CSV data
    :return: LLM-generated answer
    """
    return ask_llm(question, csv_data)

def process_graph(csv_data, x_column, y_column):
    """
    Generate a graph based on the CSV data.
    :param csv_data: Uploaded file object
    :param x_column: Column for the x-axis
    :param y_column: Column for the y-axis
    :return: Path to the saved plot image
    """
    return plot_graph(csv_data, x_column, y_column)

# Custom CSS for advanced styling
custom_css = """
/* General styling */
.gradio-container {
    font-family: 'Arial', sans-serif;
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    max-width: 1200px;
    margin: auto;
}

/* Header styling */
.gradio-header {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 30px;
    padding: 10px;
    background: linear-gradient(90deg, #4CAF50, #45a049);
    color: white;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* File upload section */
.gradio-file-upload {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

/* Textbox styling */
.gradio-textbox {
    margin: 10px 0;
    padding: 12px;
    border-radius: 5px;
    border: 1px solid #ddd;
    font-size: 14px;
    width: 100%;
    box-sizing: border-box;
}

.gradio-textbox:focus {
    border-color: #4CAF50;
    outline: none;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

/* Button styling */
.gradio-button {
    margin: 10px 0;
    padding: 12px 24px;
    border-radius: 5px;
    border: none;
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.gradio-button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.gradio-button:active {
    transform: scale(0.95);
}

/* Dataframe styling */
.gradio-dataframe {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    overflow-x: auto;
}

/* Image (graph) styling */
.gradio-image {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
    text-align: center;
}

/* Graph-specific styling */
.gradio-image img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
}
"""

# Gradio Interface with advanced styling
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# CSV Question Answering and Visualization App", elem_classes="gradio-header")

    # File Upload
    with gr.Row():
        with gr.Column():
            file_input = gr.File(label="Upload CSV File", elem_classes="gradio-file-upload")
            csv_output = gr.Dataframe(label="CSV Data", elem_classes="gradio-dataframe")
            file_input.change(process_csv, file_input, csv_output)

    # Question Answering
    with gr.Row():
        with gr.Column():
            question_input = gr.Textbox(label="Ask a Question", elem_classes="gradio-textbox")
            answer_output = gr.Textbox(label="Answer", elem_classes="gradio-textbox")
            submit_button = gr.Button("Submit", elem_classes="gradio-button")
            submit_button.click(process_question, [question_input, csv_output], answer_output)

    # Graph Plotting
    with gr.Row():
        with gr.Column():
            x_column = gr.Textbox(label="X-Axis Column", elem_classes="gradio-textbox")
            y_column = gr.Textbox(label="Y-Axis Column", elem_classes="gradio-textbox")
            plot_button = gr.Button("Generate Graph", elem_classes="gradio-button")
            plot_output = gr.Image(label="Graph", elem_classes="gradio-image")
            plot_button.click(process_graph, [file_input, x_column, y_column], plot_output)

# Launch the app
demo.launch()