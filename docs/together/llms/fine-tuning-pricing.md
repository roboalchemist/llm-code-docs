# Source: https://docs.together.ai/docs/fine-tuning-pricing.md

# Pricing

> Fine-tuning pricing at Together AI is based on the total number of tokens processed during your job.

## Overview

This includes both training and validation processes, and varies based on the model size, fine-tuning type (Supervised Fine-tuning or DPO), and implementation method (LoRA or Full Fine-tuning).

## How Pricing Works

The total cost of a fine-tuning job is calculated using:

* **Model size** (e.g., Up to 16B, 16.1-69B, etc.)
* **Fine-tuning type** (Supervised Fine-tuning or Direct Preference Optimization (DPO))
* **Implementation method** (LoRA or Full Fine-tuning)
* **Total tokens processed** = (n\_epochs × n\_tokens\_per\_training\_dataset) + (n\_evals × n\_tokens\_per\_validation\_dataset)

Each combination of fine-tuning type and implementation method has its own pricing. For current rates, refer to our [fine-tuning pricing page](https://together.ai/pricing).

## Token Calculation

The tokenization step is part of the fine-tuning process on our API. The exact token count and final price of your job will be available after tokenization completes. You can find this information in:

* Your [jobs dashboard](https://api.together.xyz/jobs)
* Or by running `together fine-tuning retrieve $JOB_ID` in the CLI

## Frequently Asked Questions

### Is there a minimum price for fine-tuning?

No, there is no minimum price for fine-tuning jobs. You only pay for the tokens processed.

### What happens if I cancel my job?

The final price is determined based on the tokens used up to the point of cancellation.

#### Example:

If you're fine-tuning Llama-3-8B with a batch size of 8 and cancel after 1000 training steps:

* Training tokens: 8192 \[context length] × 8 \[batch size] × 1000 \[steps] = 65,536,000 tokens
* If your validation set has 1M tokens and ran 10 evaluation steps: + 10M tokens
* Total tokens: 75,536,000
* Cost: Based on the model size, fine-tuning type (SFT or DPO), and implementation method (LoRA or Full FT) chosen (check the [pricing page](https://www.together.ai/pricing))

### How can I estimate my fine-tuning job cost?

1. Calculate your approximate training tokens: context\_length × batch\_size × steps × epochs
2. Add validation tokens: validation\_dataset\_size × evaluation\_frequency
3. Multiply by the per-token rate for your chosen model size, fine-tuning type, and implementation method


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt