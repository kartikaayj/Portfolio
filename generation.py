import os
from transformers import pipeline
from huggingface_hub import login
import torch

API_KEY = os.getenv("HF_API_KEY")
if not API_KEY:
    raise ValueError("Hugging Face API key not found. Set it as an environment variable.")

# Authenticate with Hugging Face
print("Authenticating...")
login(API_KEY)


model_name = "EleutherAI/gpt-neo-1.3B"
generator = pipeline("text-generation", model=model_name, device=0) 
print("Model loaded successfully.")

def generate_content(prompt, max_length=400, temperature=0.2, top_p=0.8):
    """Generate text based on the input prompt."""
    print("Generating content...")
    
    # Generate text
    generated_text = generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
        truncation=True
    )[0]["generated_text"].strip()
    
    # Check if the generated text ends with a complete sentence
    if generated_text.endswith(('.', '!', '?')):
        return generated_text
    
    # If the text does not end properly, attempt to clean it up
    last_words = generated_text.split()[-5:]  # Get the last 5 words
    if len(last_words) < 5 or last_words[-1] not in ['.', '!', '?']:
        print("Generated text seems incomplete. Attempting to clean up...")
       
        generated_text += '.'  # Append a period to indicate the end of the sentence

    return generated_text

if __name__ == "__main__":
    prompt = "Explain the water cycle in simple terms, suitable for a 5th-grade student."
    result = generate_content(prompt)
    print("Generated Text:")
    print(result)

