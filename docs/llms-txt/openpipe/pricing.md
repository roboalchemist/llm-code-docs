# Source: https://docs.openpipe.ai/pricing/pricing.md

# Pricing Overview

## Training

We charge for training based on the size of the model and the number of tokens in the dataset.

| Model Category     | Cost per 1M tokens |
| ------------------ | ------------------ |
| **8B and smaller** | \$0.48             |
| **14B models**     | \$1.50             |
| **32B models**     | \$1.90             |
| **70B+ models**    | \$2.90             |

## Hosted Inference

Choose between two billing models for running models on our infrastructure:

### 1. Per-Token Pricing

Available for our most popular, high-volume models. You only pay for the tokens you process, with no minimum commitment and automatic infrastructure scaling.

| Model                      | Input (per 1M tokens) | Output (per 1M tokens) |
| -------------------------- | --------------------- | ---------------------- |
| **Llama 3.1 8B Instruct**  | \$0.30                | \$0.45                 |
| **Qwen 2.5 14B Instruct**  | \$1.00                | \$1.50                 |
| **Llama 3.1 70B Instruct** | \$1.80                | \$2.00                 |

### 2. Hourly Compute Units

Designed for experimental and lower-volume models. A Compute Unit (CU) can handle up to 24 simultaneous requests per second. Billing is precise down to the second, with automatic scaling when traffic exceeds capacity. Compute units remain active for 60 seconds after traffic spikes.

| Model                  | Rate per CU Hour |
| ---------------------- | ---------------- |
| **Llama 3.1 8B**       | \$1.50           |
| **Mistral Nemo 12B**   | \$1.50           |
| **Qwen 2.5 32B Coder** | \$6.00           |
| **Qwen 2.5 72B**       | \$12.00          |
| **Llama 3.1 70B**      | \$12.00          |

## Third-Party Models (OpenAI, Gemini, etc.)

Third-party models fine-tuned through OpenPipe like OpenAI's GPT series or Google's Gemini, we provide direct API integration without any additional markup. You will be billed directly by the respective provider (OpenAI, Google, etc.) at their standard rates. We simply pass through the API calls and responses.

## Enterprise Plans

For organizations requiring custom solutions, we offer enterprise plans that include:

* Volume discounts
* On-premises deployment options
* Dedicated support
* Custom SLAs
* Advanced security features
* Increased data storage

Contact our team at [hello@openpipe.ai](mailto:hello@openpipe.ai) to discuss enterprise pricing and requirements.
