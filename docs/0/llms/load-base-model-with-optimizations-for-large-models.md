# Load base model with optimizations for large models
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,      # Use fp16 to reduce memory
    device_map="auto",               # Automatically distribute across GPUs
    low_cpu_mem_usage=True,          # Reduce CPU memory usage during loading
    trust_remote_code=True           # Required for some Qwen models
)