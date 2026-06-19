# Use the same file path you specified in acknowledge-model
0g-compute-cli fine-tuning decrypt-model \
  --provider <PROVIDER_ADDRESS> \
  --task-id 0e91ef3d-ac0d-422e-a38c-9d42a28c4412 \
  --encrypted-model /workspace/output/encrypted_model.bin \
  --output /workspace/output/model_output.zip
```

The above command performs the following operations:

- Gets the encrypted key from the contract uploaded by the provider
- Decrypts the key using the user's private key
- Decrypts the model with the decrypted key

:::caution Wait for Settlement
After `acknowledge-model`, the provider needs about **1 minute** to settle fees and upload the decryption key. If you decrypt too early (status is still `UserAcknowledged` instead of `Finished`), you may see an error like `second arg must be public key`. Simply wait and retry.
:::

**Note:** The decrypted result will be saved as a zip file. Ensure that the `<PATH_TO_SAVE_DECRYPTED_MODEL>` ends with .zip (e.g., model_output.zip). After downloading, unzip the file to access the decrypted model.

### Extract LoRA Adapter

After decryption, unzip the model to access the LoRA adapter files:

```bash
unzip model_output.zip -d ./lora_adapter/
```

The extracted folder will contain:

```
lora_adapter/
├── output_model/
│   ├── adapter_config.json       # LoRA configuration
│   ├── adapter_model.safetensors # LoRA weights
│   ├── tokenizer.json            # Tokenizer
│   ├── tokenizer_config.json
│   └── README.md
```

## Using the Fine-tuned Model

After fine-tuning, you receive a **LoRA adapter** (Low-Rank Adaptation), not a full model. To use it, you need to:

1. Download the base model
2. Load the LoRA adapter on top of the base model
3. Run inference

### Step 1: Download Base Model

Download the same base model that was used for fine-tuning from HuggingFace:

```bash