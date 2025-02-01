Overview
This project is an AI-driven educational content generation system that:

Generates educational content based on prompts.
Refines and enhances content for readability.
Detects and mitigates biases in the generated text.
Evaluates content for quality and fairness.
Provides a web interface for user interaction.
Features
> AI-based content generation using Hugging Face's GPT-Neo model.
> Grammar refinement using LanguageTool for high clarity and correctness.
> Bias detection & mitigation for fair and inclusive content.
> Evaluation metrics to measure readability, coherence, and fairness.
> Flask web application for easy interaction and deployment.

Setup Instructions
1️. Install Dependencies
Run the following command to install all required dependencies:
pip install -r requirements.txt

2️. Set Up Hugging Face API Key
Obtain an API key from Hugging Face and set it as an environment variable:
export HF_API_KEY="YOUR_API_KEY"

3️. Run the Flask Application
Start the Flask web application by running:
python app.py
By default, the application runs at: http://127.0.0.1:5000/

4️. Test the Application
Open your web browser and navigate to the application URL. You can enter prompts in the provided text area to generate educational content.

Code Structure
app.py: The main Flask application that handles user requests and responses.
generation.py: Contains the function for generating content using the GPT-Neo model.
refinement.py: Contains the function for refining generated content for grammar and clarity.
bias_mitigation.py: Contains functions for detecting and mitigating biases in the content.
evaluation.py: Contains functions for evaluating the generated content's readability and coherence.
templates/index.html: The HTML template for the web interface.