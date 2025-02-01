from transformers import pipeline

# Use a model trained to detect toxicity and bias
bias_checker = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")

def detect_bias(content):
    results = bias_checker([content])
    print("Content to check for bias:", content)
    print("Full Model Output:", results)
    flagged = []
    for res in results:
        if res['label'] in ["toxic", "severe_toxic", "identity_hate", "insult", "hate"]: 
            flagged.append(res)
    return flagged

def mitigate_bias(content, flagged_issues):
    
    if flagged_issues:
        return "Content contains biased language and has been flagged."
    return content


if __name__ == "__main__":
    content = "All people from X country are bad."
    flagged_issues = detect_bias(content)
    print(flagged_issues)
    mitigated_content = mitigate_bias(content, flagged_issues)
    print("Mitigated Content:", mitigated_content)