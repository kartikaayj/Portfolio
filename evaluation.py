import textstat
from sentence_transformers import SentenceTransformer, util
import json

def calculate_readability(content):
    """Calculates readability score using Flesch Reading Ease Score."""
    grade_level = textstat.flesch_kincaid_grade(content)
    print("Grade Level:", grade_level)

    return grade_level

def calculate_coherence(text, reference_text):
    """Measures coherence by comparing generated text to reference content using cosine similarity."""
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings_1 = model.encode(text, convert_to_tensor=True)
    embeddings_2 = model.encode(reference_text, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embeddings_1, embeddings_2).item()
    return similarity_score

def evaluate_content(content, reference_text):
    """Runs all evaluations on generated content."""
    results = {
        "readability": calculate_readability(content),
        "coherence": calculate_coherence(content, reference_text)
    }
    
    return results

if __name__ == "__main__":
    generated_content = "The water cycle consists of evaporation, condensation, and precipitation."
    reference_content = "Water evaporates, forms clouds through condensation, and falls as precipitation."

    evaluation_results = evaluate_content(generated_content, reference_content)
    print(json.dumps(evaluation_results, indent=4))
