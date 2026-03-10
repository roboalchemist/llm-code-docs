# List available models
0g-compute-cli fine-tuning list-models
```

<details>
<summary>📋 Available Models Summary</summary>

The CLI displays two categories of models: predefined models available across all providers and provider-specific models with unique capabilities.

#### Predefined Models
These are standard models available across all providers:

| Model Name | Type | Price per Million Tokens | Description |
|------------|------|--------------------------|-------------|
| `Qwen2.5-0.5B-Instruct` | Causal LM | 0.5 0G | Qwen 2.5 instruction-tuned model (0.5B parameters). More details: [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) |
| `Qwen3-32B` | Causal LM | 4 0G | Qwen 3 large language model (32B parameters). More details: [HuggingFace](https://huggingface.co/Qwen/Qwen3-32B) |

</details>

The output consists of two main sections:

- **Predefined Models:** Models provided by the system as predefined options. They are built-in, curated, and maintained to ensure quality and reliability.

- **Provider's Model:** Models offered by external service providers. Providers may customize or fine-tune models to address specific needs.

:::caution Model Name Format
Use model names **without** the `Qwen/` prefix when specifying the `--model` parameter. For example:
- ✅ `--model "Qwen2.5-0.5B-Instruct"`
- ❌ `--model "Qwen/Qwen2.5-0.5B-Instruct"`
:::

### Prepare Configuration File

Use the standard configuration template below and **only modify the parameter values** as needed. Do not add additional parameters.

#### Standard Configuration Template

```json
{
  "neftune_noise_alpha": 5,
  "num_train_epochs": 1,
  "per_device_train_batch_size": 2,
  "learning_rate": 0.0002,
  "max_steps": 3
}
```

:::caution Important Configuration Rules
1. **Use the template above** - Copy the entire template
2. **Only modify parameter values** - Do not add or remove parameters
3. **Use decimal notation** - Write `0.0002` instead of `2e-4` for `learning_rate`

**Common mistakes to avoid:**
- ❌ Adding extra parameters (e.g., `"fp16": true`, `"bf16": false`)
- ❌ Removing existing parameters
- ❌ Using scientific notation like `2e-4`
:::

#### Adjustable Parameters

You can modify these parameter values based on your training needs:

| Parameter | Description | Notes |
|-----------|-------------|-------|
| `neftune_noise_alpha` | Noise injection for fine-tuning | 0-10 (0 = disabled), typical: 5 |
| `num_train_epochs` | Number of complete passes through the dataset | Positive integer, typical: 1-3 for fine-tuning |
| `per_device_train_batch_size` | Training batch size | 1-4, reduce to 1 if out of memory |
| `learning_rate` | Learning rate (use decimal notation) | 0.00001-0.001, typical: 0.0002 |
| `max_steps` | Maximum training steps | -1 (use epochs) or positive integer |

:::tip GPU Memory Management
- If you encounter out-of-memory errors, **reduce batch size to 1**
- The provider automatically handles mixed precision training with `bf16`
:::

*Note:* For custom models provided by third-party Providers, you can download the usage template including instructions on how to construct the dataset and training configuration using the following command:

```bash
0g-compute-cli fine-tuning model-usage --provider <PROVIDER_ADDRESS>  --model <MODEL_NAME>   --output <PATH_TO_SAVE_MODEL_USAGE>
```

### Prepare Your Data

Your dataset must be in **JSONL format** with a **`.jsonl` file extension**. Each line is a JSON object representing one training example.

#### Supported Dataset Formats

**Format 1: Instruction-Input-Output**
```json
{"instruction": "Translate to French", "input": "Hello world", "output": "Bonjour le monde"}
{"instruction": "Translate to French", "input": "Good morning", "output": "Bonjour"}
{"instruction": "Summarize the text", "input": "Long article...", "output": "Brief summary"}
```

**Format 2: Chat Messages**
```json
{"messages": [{"role": "user", "content": "What is 2+2?"}, {"role": "assistant", "content": "2+2 equals 4."}]}
{"messages": [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there! How can I help you?"}]}
```

**Format 3: Simple Text (for text completion)**
```json
{"text": "The quick brown fox jumps over the lazy dog."}
{"text": "Machine learning is a subset of artificial intelligence."}
```

#### Dataset Guidelines

- **File format**: Must be a `.jsonl` file (JSONL format)
- **Minimum examples**: At least 10 examples recommended for meaningful fine-tuning
- **Quality**: Ensure examples are accurate and representative of your use case
- **Consistency**: Use the same format throughout the dataset
- **Encoding**: UTF-8 encoding required

### Create Task

Create a fine-tuning task. The fee will be **automatically calculated** by the broker based on the actual token count of your dataset.

**Option A: Using local dataset file (Recommended)**

The CLI will automatically upload the dataset to 0G Storage and create the task in one step:

```bash
0g-compute-cli fine-tuning create-task \
  --provider <PROVIDER_ADDRESS> \
  --model <MODEL_NAME> \
  --dataset-path <PATH_TO_DATASET> \
  --config-path <PATH_TO_CONFIG_FILE>
```

**Option B: Using dataset root hash**

If you prefer to upload the dataset separately first, or need to reuse the same dataset:

1. Upload your dataset to 0G Storage:

```bash
0g-compute-cli fine-tuning upload --data-path <PATH_TO_DATASET>
```

Output:
```bash
Root hash: 0xabc123...
```

2. Create the task using the root hash:

```bash
0g-compute-cli fine-tuning create-task \
  --provider <PROVIDER_ADDRESS> \
  --model <MODEL_NAME> \
  --dataset <DATASET_ROOT_HASH> \
  --config-path <PATH_TO_CONFIG_FILE>
```

**Parameters:**

| Parameter | Description |
|-----------|-------------|
| `--provider` | Address of the service provider |
| `--model` | Name of the pretrained model (without `Qwen/` prefix) |
| `--dataset-path` | Path to local dataset file — automatically uploads to 0G Storage (Option A) |
| `--dataset` | Root hash of the dataset on 0G Storage — mutually exclusive with `--dataset-path` (Option B) |
| `--config-path` | Path to the training configuration file |
| `--gas-price` | Gas price (optional) |

The output will be like:

```bash
Verify provider...
Provider verified
Creating task (fee will be calculated automatically)...
Fee will be automatically calculated by the broker based on actual token count
Created Task ID: 6b607314-88b0-4fef-91e7-43227a54de57
```

*Note:* When creating a task for the same provider, you must wait for the previous task to be completed (status `Finished`) before creating a new task. If the provider is currently running other tasks, you will be prompted to choose between adding your task to the waiting queue or canceling the request.

### Fee Calculation

The fine-tuning service fee is **automatically calculated** based on your dataset size and training configuration. The fee consists of two components:

#### Formula

```
Total Fee = Training Fee + Storage Reserve Fee
```

Where:
- **Training Fee** = `(tokenSize / 1,000,000) × pricePerMillionTokens × trainEpochs`
- **Storage Reserve Fee** = Fixed amount based on model size

#### Components Explained

| Component | Description |
|-----------|-------------|
| `tokenSize` | Total number of tokens in your dataset (automatically counted) |
| `pricePerMillionTokens` | Price per million tokens (model-specific, see [Predefined Models](#predefined-models)) |
| `trainEpochs` | Number of training epochs (from your config) |
| `Storage Reserve Fee` | Fixed fee to reserve storage for the fine-tuned model:• Qwen3-32B (~900 MB LoRA): 0.09 0G• Qwen2.5-0.5B-Instruct (~100 MB LoRA): 0.01 0G |

#### Example

For a dataset with 10,000 tokens, trained for 3 epochs on Qwen2.5-0.5B-Instruct:
- Price per million tokens = 0.5 0G (see [Predefined Models](#predefined-models))
- Training Fee = (10,000 / 1,000,000) × 0.5 × 3 = 0.015 0G
- Storage Reserve Fee = 0.01 0G (for Qwen2.5-0.5B-Instruct)
- **Total Fee = 0.025 0G**

:::tip
The actual fee is calculated during the setup phase after your dataset is analyzed. You can view the final fee using the [`get-task`](#monitor-progress) command before training begins.
:::

### Monitor Progress
You can monitor the progress of your task by running the following command:

```bash
0g-compute-cli fine-tuning get-task --provider <PROVIDER_ADDRESS> --task <TASK_ID>
```

The output will be like:

```bash
┌───────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────┐
│ Field                             │ Value                                                                               │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ ID                                │ beb6f0d8-4660-4c62-988d-00246ce913d2                                                │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Created At                        │ 2025-03-11T01:20:07.644Z                                                            │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Pre-trained Model Hash            │ 0xcb42b5ca9e998c82dd239ef2d20d22a4ae16b3dc0ce0a855c93b52c7c2bab6dc                  │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Dataset Hash                      │ 0xaae9b4e031e06f84b20f10ec629f36c57719ea512992a6b7e2baea93f447a5fa                  │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Training Params                   │ {......}                                                                            │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Fee (neuron)                      │ 82                                                                                  │
├───────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────┤
│ Progress                          │ Delivered                                                                           │
└───────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────┘
```

**Field Descriptions:**
- **ID**: Unique identifier for your fine-tuning task
- **Pre-trained Model Hash**: Hash identifier for the base model being fine-tuned
- **Dataset Hash**: Hash identifier for your training dataset (0G Storage root hash)
- **Training Params**: Configuration parameters used during fine-tuning
- **Fee (neuron)**: Total cost for the fine-tuning task (automatically calculated based on token count)
- **Progress**: Task status. Possible values are:
  - `Init`: Task submitted
  - `SettingUp`: Provider is preparing the environment (downloading dataset, etc.)
  - `SetUp`: Provider is ready to start training
  - `Training`: Provider is training the model
  - `Trained`: Provider has finished training
  - `Delivering`: Provider is encrypting and uploading the model to 0G Storage
  - `Delivered`: Fine-tuning result is ready for download
  - `UserAcknowledged`: User has downloaded and confirmed the result
  - `Finished`: Provider has settled fees and shared decryption key — task is completed
  - `Failed`: Task failed

### View Task Logs

You can view the logs of your task by running the following command:

```bash
0g-compute-cli fine-tuning get-log --provider <PROVIDER_ADDRESS> --task <TASK_ID>
```

The output will be like:

```bash
creating task....
Step: 0, Logs: {'loss': ..., 'accuracy': ...}
...
Training model for task beb6f0d8-4660-4c62-988d-00246ce913d2 completed successfully
```

### Download and Acknowledge Model

Use the [Check Task](#monitor-progress) command to view task status. When the status changes to `Delivered`, the provider has completed fine-tuning and the encrypted model is ready. Download and acknowledge the model:

```bash
0g-compute-cli fine-tuning acknowledge-model \
  --provider <PROVIDER_ADDRESS> \
  --task-id <TASK_ID> \
  --data-path <PATH_TO_SAVE_MODEL_FILE>
```

The CLI will automatically download the encrypted model from 0G Storage. If 0G Storage download fails, it will fall back to downloading directly from the provider's TEE.

:::danger 48-Hour Deadline
**You must download and acknowledge the model within 48 hours after the task status changes to `Delivered`.**

If you fail to acknowledge within 48 hours:
- The provider will **force settlement** automatically
- You will **lose access to the fine-tuned model**
- **30% of the total task fee** will be deducted as compensation for the provider's compute resources

**Action required:** Monitor your task status and download promptly when it reaches `Delivered`.
:::

:::caution File Path Required
`--data-path` **must be a file path**, not a directory.

**Example:**
```bash
0g-compute-cli fine-tuning acknowledge-model \
  --provider <PROVIDER_ADDRESS> \
  --task-id 0e91ef3d-ac0d-422e-a38c-9d42a28c4412 \
  --data-path /workspace/output/encrypted_model.bin
```
:::

:::tip Data Integrity Verification
The `acknowledge-model` command performs automatic data integrity verification to ensure the downloaded model matches the root hash that the provider submitted to the blockchain contract. This guarantees you receive the authentic model without corruption or tampering.
:::

**Note:** The model file downloaded with the above command is encrypted, and additional steps are required for decryption.

### Decrypt Model

After acknowledging the model, the provider automatically settles the fees and uploads the decryption key to the contract (encrypted with your public key). Use the `get-task` command to check the task status. **When the status changes to `Finished`**, you can decrypt the model:

```bash
0g-compute-cli fine-tuning decrypt-model \
  --provider <PROVIDER_ADDRESS> \
  --task-id <TASK_ID> \
  --encrypted-model <PATH_TO_ENCRYPTED_MODEL_FILE> \
  --output <PATH_TO_SAVE_DECRYPTED_MODEL>
```

**Example:**
```bash