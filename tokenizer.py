from transformers import AutoTokenizer

def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained('tiennvcs/layoutlmv2-large-uncased-finetuned-infovqa')
    return tokenizer

def tokenize_data(job_description, pdf_text, tokenizer):
    inputs = tokenizer(job_description, pdf_text, return_tensors='pt', truncation=True, padding=True)
    return inputs