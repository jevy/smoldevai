```python
from transformers import AutoModelForQuestionAnswering

def load_model():
    model = AutoModelForQuestionAnswering.from_pretrained('tiennvcs/layoutlmv2-large-uncased-finetuned-infovqa')
    return model
```