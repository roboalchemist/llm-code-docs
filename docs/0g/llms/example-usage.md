# Example usage
response = generate_response("Hello, how are you?")
print(response)
```

### Optional: Merge and Save Full Model

If you want to create a standalone model without needing to load the adapter separately:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch