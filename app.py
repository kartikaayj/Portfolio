from flask import Flask, request, jsonify, render_template
from generation import generate_content
from refinement import refine_content
from bias_mitigation import detect_bias
from evaluation import evaluate_content
from threading import Thread
from transformers import pipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Render the main page with the input form."""
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    """Process the user prompt and return generated content, refined content, biases, and evaluation results."""
    prompt = request.form.get("prompt")
    
    
    if not prompt:
        return render_template("index.html", error="Prompt is required.")

    try:
    
        generated_content = generate_content(prompt)
        
        refined_content = refine_content(generated_content)
    
        biases_detected = detect_bias(refined_content)
        
        
        reference_text = "Water evaporates, forms clouds through condensation, and falls as precipitation."
        evaluation_results = evaluate_content(refined_content, reference_text)
        
        return render_template("index.html", 
                               generated_content=generated_content,
                               refined_content=refined_content,
                               biases_detected=biases_detected,
                               evaluation_results=evaluation_results)
    except Exception as e:
        # Handle any exceptions that occur during processing
        return render_template("index.html", error=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True, use_reloader=False)