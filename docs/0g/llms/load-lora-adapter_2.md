# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, lora_adapter_path)

print("Model loaded successfully!")
```

:::tip Memory Optimization for Large Models
If you encounter out-of-memory errors with Qwen3-32B, you can use quantization:

```python