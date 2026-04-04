# Save the merged model
merged_model.save_pretrained("./merged_model")
tokenizer = AutoTokenizer.from_pretrained("./lora_adapter/output_model")
tokenizer.save_pretrained("./merged_model")

print("Merged model saved to ./merged_model")
```

### Requirements

Install the required Python packages:

#### For GPU Environments (Recommended)

If you have an NVIDIA GPU, install PyTorch with CUDA support. **Important:** Match the CUDA version to your environment.

```bash