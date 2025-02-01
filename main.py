from generation import generate_content
from refinement import refine_content
from bias_mitigation import detect_bias
from evaluation import evaluate_content

def main():
    prompt = "Create a Grade 5 science lesson on the water cycle."
    print("Generating content...")
    content = generate_content(prompt)
    print("Generated content:", content)

    print("Refining content...")
    refined_content = refine_content(content)
    print("Refined content after processing:", refined_content)

    if not refined_content:
        print("Refined content is empty. Skipping bias detection.")
        return []

    print("Detecting biases...")
    flagged_issues = detect_bias(refined_content)
    print("Flagged Biases:", flagged_issues)

    print("Evaluating content...")
    reference_text = "Water evaporates, forms clouds through condensation, and falls as precipitation."
    evaluation_results = evaluate_content(refined_content, reference_text)
    print("Evaluation Metrics:", evaluation_results)

   
if __name__ == "__main__":
    main()