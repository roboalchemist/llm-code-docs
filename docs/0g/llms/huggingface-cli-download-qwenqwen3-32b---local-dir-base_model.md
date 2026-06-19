# huggingface-cli download Qwen/Qwen3-32B --local-dir ./base_model
```

### Step 2: Load LoRA with Base Model

Use the following Python code to combine the LoRA adapter with the base model.

**For Qwen2.5-0.5B-Instruct:**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch