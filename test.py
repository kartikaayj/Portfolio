import unittest
from generation import generate_content
from refinement import refine_content
from bias_mitigation import detect_bias
from evaluation import evaluate_content

class TestContentGeneration(unittest.TestCase):

    def test_generate_content(self):
        prompt = "Explain the water cycle in simple terms."
        content = generate_content(prompt)
        self.assertIsInstance(content, str)  
        self.assertGreater(len(content), 0)  

    def test_refine_content(self):
        raw_content = "The water cycle is important."
        refined_content = refine_content(raw_content)
        self.assertIsInstance(refined_content, str)

    def test_detect_bias(self):
        content = "All people from X country are bad."
        biases = detect_bias(content)
        self.assertIsInstance(biases, list)

    def test_evaluate_content(self):
        content = "The water cycle consists of evaporation, condensation, and precipitation."
        reference_text = "Water evaporates, forms clouds through condensation, and falls as precipitation."
        evaluation_results = evaluate_content(content, reference_text)
        self.assertIn("readability", evaluation_results) 
        self.assertIn("coherence", evaluation_results) 

if __name__ == "__main__":
    unittest.main()