# System Architecture

## Overview
The AI-driven educational content system is built using **NLP techniques** and follows a modular architecture for **scalability and flexibility**.

## Workflow
1️⃣ **User  Input:** User provides a specific educational prompt.  
2️⃣ **AI Generation:** Hugging Face's GPT-Neo generates educational content.  
3️⃣ **Content Refinement:** Grammar and coherence are improved using LanguageTool.  
4️⃣ **Bias Detection:** The text is analyzed for fairness.  
5️⃣ **Evaluation:** Readability and coherence are measured using Textstat and SentenceTransformers.  
6️⃣ **Output:** The final educational content is provided via a **web interface**.  

## Technical Stack
- **Python** for core logic.
- **Hugging Face GPT-Neo** for text generation.
- **Flask** for web application deployment.
- **Textstat** for readability analysis.
- **Transformers & SentenceTransformers** for coherence evaluation.

## User Guidance
**Prototype Notice**: This application is a prototype. Users should enter specific and structured prompts to get the best results. Adding context can help guide the model in generating relevant content.

## System Diagram

A[User  Input] --> B[AI Content Generation]
B --> C[Content Refinement]
C --> D[Bias Detection]
D --> E[Evaluation]
E --> F[Final Output]