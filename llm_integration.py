import ollama

def ask_llm(question, csv_data):
   
    try:
        
        csv_str = csv_data.to_string()
        
        response = ollama.generate(model="llama3:8b", prompt=f"{question}\n{csv_str}")
        return response['response']
    except Exception as e:
        return f"Error generating answer: {str(e)}"
