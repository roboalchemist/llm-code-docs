# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, lora_adapter_path)

print("Model loaded successfully!")
```

**For Qwen3-32B (requires 40GB+ VRAM):**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch