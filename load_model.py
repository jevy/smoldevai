```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def load_model():
    tokenizer = AutoTokenizer.from_pretrained('tiennvcs/layoutlmv2-large-uncased-finetuned-infovqa')
    model = AutoModelForQuestionAnswering.from_pretrained('tiennvcs/layoutlmv2-large-uncased-finetuned-infovqa')
    return tokenizer, model
```