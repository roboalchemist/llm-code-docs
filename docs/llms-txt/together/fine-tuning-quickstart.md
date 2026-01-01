# Source: https://docs.together.ai/docs/fine-tuning-quickstart.md

> Learn the basics and best practices of fine-tuning large language models.

# Fine-tuning Guide

## Introduction

Large Language Models (LLMs) offer powerful general capabilities, but often require **fine-tuning** to excel at specific tasks or understand domain-specific language. Fine-tuning adapts a trained model to a smaller, targeted dataset, enhancing its performance for your unique needs.

This guide provides a step-by-step walkthrough for fine-tuning models using the Together AI platform. We will cover everything from preparing your data to evaluating your fine-tuned model.

We will cover:

1. **Dataset Preparation:** Loading a standard dataset, transforming it into the required format for supervised fine-tuning on Together AI, and uploading your formatted dataset to Together AI Files.
2. **Fine-tuning Job Launch:** Configuring and initiating a fine-tuning job using the Together AI API.
3. **Job Monitoring:** Checking the status and progress of your fine-tuning job.
4. **Inference:** Using your newly fine-tuned model via the Together AI API for predictions.
5. **Evaluation:** Comparing the performance of the fine-tuned model against the base model on a test set.

By following this guide, you'll gain practical experience in creating specialized LLMs tailored to your specific requirements using Together AI.

<Info>
  ### Fine-tuning Guide Notebook

  Here is a runnable notebook version of this fine-tuning guide: [Fine-tuning Guide Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb)
</Info>

## Table of Contents

1. [What is Fine-tuning?](#what-is-fine-tuning)
2. [Getting Started](#getting-started)
3. [Dataset Preparation](#dataset-preparation)
4. [Starting a Fine-tuning Job](#starting-a-fine-tuning-job)
5. [Monitoring Your Fine-tuning Job](#monitoring-your-fine-tuning-job)
6. [Using Your Fine-tuned Model](#using-your-fine-tuned-model)
7. [Evaluating Your Fine-tuned Model](#evaluating-your-fine-tuned-model)
8. [Advanced Topics](#advanced-topics)

## What is Fine-tuning?

Fine-tuning is the process of improving an existing LLM for a specific task or domain. You can enhance an LLM by providing labeled examples for a particular task which it can learn from. These examples can come from public datasets or private data specific to your organization.

Together AI facilitates every step of the fine-tuning process, from data preparation to model deployment. Together supports two types of fine-tuning:

1. **LoRA (Low-Rank Adaptation) fine-tuning**: Fine-tunes only a small subset of weights compared to full fine-tuning. This is faster, requires less computational resources, and is **recommended for most use cases**. Our fine-tuning API defaults to LoRA.

2. **Full fine-tuning**: Updates all weights in the model, which requires more computational resources but may provide better results for certain tasks.

## Getting Started

**Prerequisites**

1. **Register for an account**: Sign up at [Together AI](https://api.together.xyz/settings/api-keys) to get an API key.

2. **Set up your API key**:

   ```shell  theme={null}
   export TOGETHER_API_KEY=your_api_key_here
   ```

3. **Install the required libraries**:

   ```shell  theme={null}
   # Python
   pip install -U together datasets transformers tqdm
   ```

**Choosing Your Model**

The first step in fine-tuning is choosing which LLM to use as the starting point for your custom model:

* **Base models** are trained on a wide variety of texts, making their predictions broad
* **Instruct models** are trained on instruction-response pairs, making them better for specific tasks

For beginners, we recommend an instruction-tuned model:

* *meta-llama/Meta-Llama-3.1-8B-Instruct-Reference* is great for simpler tasks
* *meta-llama/Meta-Llama-3.1-70B-Instruct-Reference* is better for more complex datasets and domains

You can find all available models on the Together API [here](/docs/fine-tuning-models).

## Dataset Preparation

Fine-tuning requires data formatted in a specific way. We'll use a conversational dataset as an example - here the goal is to improve the model on multi-turn conversations.

**Data Formats**

Together AI supports several data formats:

1. **Conversational data**: A JSON object per line, where each object contains a list of conversation turns under the `"messages"` key. Each message must have a `"role"` (`system`, `user`, or `assistant`) and `"content"`. See details [here](/docs/fine-tuning-data-preparation#conversational-data).

   ```json  theme={null}
   {
     "messages": [
       { "role": "system", "content": "You are a helpful assistant." },
       { "role": "user", "content": "Hello!" },
       { "role": "assistant", "content": "Hi! How can I help you?" }
     ]
   }
   ```

2. **Instruction data**: For instruction-based tasks with prompt-completion pairs. See details [here](/docs/fine-tuning-data-preparation#instruction-data).

3. **Preference data**: For preference-based fine-tuning. See details [here](/docs/fine-tuning-data-preparation#preference-data).

4. **Generic text data**: For simple text completion tasks. See details [here](/docs/fine-tuning-data-preparation#generic-text-data).

**File Formats**

Together AI supports two file formats:

1. **JSONL**: Simpler and works for most cases.
2. **Parquet**: Stores pre-tokenized data, provides flexibility to specify custom attention mask and labels (loss masking).

By default, it's easier to use `JSONL`. However, `Parquet` can be useful if you need custom tokenization or specific loss masking.

**Example: Preparing the CoQA Dataset**

Here's an example of transforming the CoQA dataset into the required chat format:

```python Python theme={null}
from datasets import load_dataset

## Load the dataset
coqa_dataset = load_dataset("stanfordnlp/coqa")

## The system prompt, if present, must always be at the beginning
system_prompt = (
    "Read the story and extract answers for the questions.\nStory: {}"
)


def map_fields(row):
    # Create system prompt
    messages = [
        {"role": "system", "content": system_prompt.format(row["story"])}
    ]

    # Add user and assistant messages
    for q, a in zip(row["questions"], row["answers"]["input_text"]):
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    return {"messages": messages}


## Transform the data using the mapping function
train_messages = coqa_dataset["train"].map(
    map_fields,
    remove_columns=coqa_dataset["train"].column_names,
)

## Save data to JSON file
train_messages.to_json("coqa_prepared_train.jsonl")
```

**Loss Masking**

In some cases, you may want to fine-tune a model to focus on predicting only a specific part of the prompt:

1. When using Conversational or Instruction Data Formats, you can specify `train_on_inputs` (bool or 'auto') - whether to mask the user messages in conversational data or prompts in instruction data.
2. For Conversational format, you can mask specific messages by assigning weights.
3. With pre-tokenized datasets (Parquet), you can provide custom `labels` to mask specific tokens by setting their label to `-100`.

**Checking and Uploading Your Data**

Once your data is prepared, verify it's correctly formatted and upload it to Together AI:

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import os
  import json

  TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
  WANDB_API_KEY = os.getenv(
      "WANDB_API_KEY"
  )  # Optional, for logging fine-tuning to wandb

  ## Check the file format

  from together.utils import check_file

  client = Together(api_key=TOGETHER_API_KEY)

  sft_report = check_file("coqa_prepared_train.jsonl")
  print(json.dumps(sft_report, indent=2))

  assert sft_report["is_check_passed"] == True

  ## Upload the data to Together

  train_file_resp = client.files.upload(
      "coqa_prepared_train.jsonl", purpose="fine-tune", check=True
  )
  print(train_file_resp.id)  # Save this ID for starting your fine-tuning job
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together files check "coqa_prepared_train.jsonl"
  together files upload "coqa_prepared_train.jsonl"
  ```

  ```python Python v2 theme={null}
  from together import Together
  import os
  import json

  TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
  WANDB_API_KEY = os.getenv(
      "WANDB_API_KEY"
  )  # Optional, for logging fine-tuning to wandb


  client = Together(api_key=TOGETHER_API_KEY)

  train_file_resp = client.files.upload(
      "coqa_prepared_train.jsonl",
      purpose="fine-tune",
      check=True,
  )
  print(train_file_resp.id)  # Save this ID for starting your fine-tuning job
  ```
</CodeGroup>

The output from checking the file should look similar to:

```json JSON theme={null}
{
  "is_check_passed": true,
  "message": "Checks passed",
  "found": true,
  "file_size": 23777505,
  "utf8": true,
  "line_type": true,
  "text_field": true,
  "key_value": true,
  "has_min_samples": true,
  "num_samples": 7199,
  "load_json": true,
  "filetype": "jsonl"
}
```

## Starting a Fine-tuning Job

With our data uploaded, we can now launch the fine-tuning job using `client.fine_tuning.create()`.

**Key Parameters**

* `model`: The base model you want to fine-tune (e.g., `'meta-llama/Meta-Llama-3.1-8B-Instruct-Reference'`)
* `training_file`: The ID of your uploaded training JSONL file
* `validation_file`: Optional ID of validation file (highly recommended for monitoring)
* `suffix`: A custom string added to create your unique model name (e.g., `'test1_8b'`)
* `n_epochs`: Number of times the model sees the entire dataset
* `n_checkpoints`: Number of checkpoints to save during training (for resuming or selecting the best model)
* `learning_rate`: Controls how much model weights are updated
* `batch_size`: Number of examples processed per iteration (default: "max")
* `lora`: Set to `True` for LoRA fine-tuning
* `train_on_inputs`: Whether to mask user messages or prompts (can be bool or 'auto')
* `warmup_ratio`: Ratio of steps for warmup

<Icon icon="link" iconType="solid" /> For an exhaustive list of all the available
fine-tuning parameters refer to the [Together AI Fine-tuning API Reference](/reference/post-fine-tunes)
docs.

**LoRA Fine-tuning (Recommended)**

<CodeGroup>
  ```python Python theme={null}
  ## Using Python - This fine-tuning job should take ~10-15 minutes to complete
  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      wandb_api_key=WANDB_API_KEY,  # Optional, for visualization
      lora=True,  # Default True
      warmup_ratio=0,
      learning_rate=1e-5,
      suffix="test1_8b",
  )

  print(ft_resp.id)  # Save this job ID for monitoring
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --lora \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --learning-rate 1e-5 \
    --suffix "test1_8b" \
    --wandb-api-key $WANDB_API_KEY  # Optional
  ```
</CodeGroup>

**Full Fine-tuning**

For full fine-tuning, simply omit the `lora` parameter:

<CodeGroup>
  ```python Python theme={null}
  ## Using Python
  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      warmup_ratio=0,
      lora=False,  # Must be specified as False, defaults to True
      learning_rate=1e-5,
      suffix="test1_8b_full_finetune",
  )
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --no-lora \
    --learning-rate 1e-5 \
    --suffix "test1_8b_full_finetune"
  ```
</CodeGroup>

The response will include your job ID, which you'll use to monitor progress:

```text Text theme={null}
ft-d1522ffb-8f3e #fine-tuning job id
```

## Monitoring a Fine-tuning Job

Fine-tuning can take time depending on the model size, dataset size, and hyperparameters. Your job will progress through several states: Pending, Queued, Running, Uploading, and Completed.

You can monitor and manage the job's progress using the following methods:

* **List all jobs**: `client.fine_tuning.list()`
* **Status of a job**: `client.fine_tuning.retrieve(id=ft_resp.id)`
* **List all events for a job**: `client.fine_tuning.list_events(id=ft_resp.id)` - Retrieves logs and events generated during the job
* **Cancel job**: `client.fine_tuning.cancel(id=ft_resp.id)`
* **Download fine-tuned model**: `client.fine_tuning.download(id=ft_resp.id)` (v1) or `client.fine_tuning.with_streaming_response.content(ft_id=ft_resp.id)` (v2)

Once the job is complete (`status == 'completed'`), the response from `retrieve` will contain the name of your newly created fine-tuned model. It follows the pattern: `<your-account>/<base-model-name>:<suffix>:<job-id>`.

**Check Status via API**

<CodeGroup>
  ```python Python theme={null}
  ## Check status of the job
  resp = client.fine_tuning.retrieve(ft_resp.id)
  print(resp.status)

  ## This loop will print the logs of the job thus far
  for event in client.fine_tuning.list_events(id=ft_resp.id).data:
      print(event.message)
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning retrieve "your-job-id"
  ```
</CodeGroup>

Example output:

```text Text theme={null}
Fine tune request created
Job started at Thu Apr  3 03:19:46 UTC 2025
Model data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:19:48 UTC 2025
Data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at 2025-04-03T03:19:55.595750
WandB run initialized.
Training started for model togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT
Epoch completed, at step 24
Epoch completed, at step 48
Epoch completed, at step 72
Training completed for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:27:55 UTC 2025
Uploading output model
Compressing output model
Model compression complete
Model upload complete
Job finished at Thu Apr  3 03:31:33 UTC 2025
```

**Dashboard Monitoring**

You can also monitor your job on the [Together AI jobs dashboard](https://api.together.xyz/jobs).

If you provided a Weights & Biases API key, you can view detailed training metrics on the W\&B platform, including loss curves and more.

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=2973b0ebdc3f38a4b7466c02fd0ddc40" alt="" data-og-width="3290" width="3290" data-og-height="1366" height="1366" data-path="images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c511ef3fd1475fd005d3387fa3ef5194 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8ae7668e3592726f6bb90272d45d16b4 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9246196bf8f56237a60bc35020873347 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=11bf77aec25449cdd17fc5f9b5252fb7 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b7833a099df09e37c228384c3e203685 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5ad6e32772425ac3006d368830a3d999 2500w" />

## Deleting a fine-tuning job

You can also delete your fine-tuning job. This action can not be undone. This will destroy all files produced by your job including intermediate and final checkpoints.

<CodeGroup>
  ```python Python theme={null}
  ## Run delete
  resp = client.fine_tuning.delete(ft_resp.id)
  print(resp)
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning delete "your-job-id"
  ```
</CodeGroup>

## Using a Fine-tuned Model

Once your fine-tuning job completes, your model will be available for use:

**Option 1: Serverless LoRA Inference**

If you used LoRA fine-tuning and the model supports serverless LoRA inference, you can immediately use your model without deployment. We can call it just like any other model on the Together AI platform, by providing the unique fine-tuned model `output_name` from our fine-tuning job.

<Icon icon="link" iconType="solid" /> See the list of all models that support [LoRA
Inference](/docs/lora-training-and-inference).

```python Python theme={null}
## The first time you run this it'll take longer to load the adapter weights for the first time
finetuned_model = ft_resp.output_name  # From your fine-tuning job response

user_prompt = "What is the capital of France?"

response = client.chat.completions.create(
    model=finetuned_model,
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    max_tokens=124,
)

print(response.choices[0].message.content)
```

You can also prompt the model in the Together AI playground by going to your [models dashboard](https://api.together.xyz/models) and clicking `"OPEN IN PLAYGROUND"`. Read more about Serverless LoRA Inference [here](https://docs.together.ai/docs/lora-training-and-inference)

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a9a719d70fd612b05fc6eec5a0ea3247" alt="" data-og-width="2814" width="2814" data-og-height="932" height="932" data-path="images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5bc7260604b428600c48a2c0776a04a9 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=350efd822699951645e5716175603968 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0d5a33d838354de3f8f5c1e74473e1d8 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=79f3c8611c70fb67dd344be32cccf8a5 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e641991ae1ffe95ad3794dbe3f615c3a 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=02181a091af1ab544aa7dc88b3c477f8 2500w" />

**Option 2: Deploy a Dedicated Endpoint**

Another way to run your fine-tuned model is to deploy it on a custom dedicated endpoint:

1. Visit [your models dashboard](https://api.together.xyz/models)
2. Click `"+ CREATE DEDICATED ENDPOINT"` for your fine-tuned model
3. <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d3551d242d1ebd1fdf9df14c5a5dc132" alt="" data-og-width="2814" width="2814" data-og-height="1342" height="1342" data-path="images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=adc835ab47098775f088fbfbec5c9b2a 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4c6c23dbd1e571c4209dccbc836ac7c6 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=14072171333d10ebdc86bf2fb41e0c1e 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=313c71850d15ff94864432be006640d2 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5ac0985b84e22754b8a8981e5bbf6edb 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=212e815b464e1f8c2c7134de2a3b2681 2500w" />

   Select hardware configuration and scaling options, including min and max replicas which affects the maximum QPS the deployment can support and then click `"DEPLOY"`

You can also deploy programmatically:

```python Python theme={null}
response = client.endpoints.create(
    display_name="Fine-tuned Meta Llama 3.1 8B Instruct 04-09-25",
    model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-test1_8b-e5a0fb5d",
    hardware="4x_nvidia_h100_80gb_sxm",
    autoscaling={"min_replicas": 1, "max_replicas": 1},
)

print(response)
```

⚠️ If you run this code it will deploy a dedicated endpoint for you. For detailed documentation around how to deploy, delete and modify endpoints see the [Endpoints API Reference](/reference/createendpoint).

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=82c195dda7e8b0e0133ad07e0ee4eaf0" alt="" data-og-width="2832" width="2832" data-og-height="932" height="932" data-path="images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=95aba9294ddb100f539c1e61efd90f93 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=343a48385e9e66b64e9f599c5eb85a1f 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=530b41d9f625410cb8afc9ea72186e63 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a103ce58d60d78de5db666b02fd3c070 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=fa519ae89f25ea4fa5756d140885faca 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=048f087fefb75c4f94bd0bcc2dbd0568 2500w" />

Once deployed, you can query the endpoint:

```python Python theme={null}
response = client.chat.completions.create(
    model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-test1_8b-e5a0fb5d-ded38e09",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    max_tokens=128,
)

print(response.choices[0].message.content)
```

## Evaluating a Fine-tuned Model

To assess the impact of fine-tuning, we can compare the responses of our fine-tuned model with the original base model on the same prompts in our test set. This provides a way to measure improvements after fine-tuning.

**Using a Validation Set During Training**

You can provide a validation set when starting your fine-tuning job:

```python Python theme={null}
response = client.fine_tuning.create(
    training_file="your-training-file-id",
    validation_file="your-validation-file-id",
    n_evals=10,  # Number of times to evaluate on validation set
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
)
```

**Post-Training Evaluation Example**

Here's a comprehensive example of evaluating models after fine-tuning, using the CoQA dataset:

1. First, load a portion of the validation dataset:

```python Python theme={null}
coqa_dataset_validation = load_dataset(
    "stanfordnlp/coqa",
    split="validation[:50]",
)
```

2. Define a function to generate answers from both models:

```python Python theme={null}
from tqdm.auto import tqdm
from multiprocessing.pool import ThreadPool

base_model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"  # Original model
finetuned_model = ft_resp.output_name  # Fine-tuned model


def get_model_answers(model_name):
    """
    Generate model answers for a given model name using a dataset of questions and answers.
    Args:
        model_name (str): The name of the model to use for generating answers.
    Returns:
        list: A list of lists, where each inner list contains the answers generated by the model.
    """
    model_answers = []
    system_prompt = (
        "Read the story and extract answers for the questions.\nStory: {}"
    )

    def get_answers(data):
        answers = []
        messages = [
            {
                "role": "system",
                "content": system_prompt.format(data["story"]),
            }
        ]
        for q, true_answer in zip(
            data["questions"],
            data["answers"]["input_text"],
        ):
            try:
                messages.append({"role": "user", "content": q})
                response = client.chat.completions.create(
                    messages=messages,
                    model=model_name,
                    max_tokens=64,
                )
                answer = response.choices[0].message.content
                answers.append(answer)
            except Exception:
                answers.append("Invalid Response")
        return answers

    # We'll use 8 threads to generate answers faster in parallel
    with ThreadPool(8) as pool:
        for answers in tqdm(
            pool.imap(get_answers, coqa_dataset_validation),
            total=len(coqa_dataset_validation),
        ):
            model_answers.append(answers)

    return model_answers
```

3. Generate answers from both models:

```python Python theme={null}
base_answers = get_model_answers(base_model)
finetuned_answers = get_model_answers(finetuned_model)
```

4. Define a function to calculate evaluation metrics:

```python Python theme={null}
import transformers.data.metrics.squad_metrics as squad_metrics


def get_metrics(pred_answers):
    """
    Calculate the Exact Match (EM) and F1 metrics for predicted answers.
    Args:
        pred_answers (list): A list of predicted answers.
    Returns:
        tuple: A tuple containing EM score and F1 score.
    """
    em_metrics = []
    f1_metrics = []

    for pred, data in tqdm(
        zip(pred_answers, coqa_dataset_validation),
        total=len(pred_answers),
    ):
        for pred_answer, true_answer in zip(
            pred, data["answers"]["input_text"]
        ):
            em_metrics.append(
                squad_metrics.compute_exact(true_answer, pred_answer)
            )
            f1_metrics.append(
                squad_metrics.compute_f1(true_answer, pred_answer)
            )

    return sum(em_metrics) / len(em_metrics), sum(f1_metrics) / len(f1_metrics)
```

5. Calculate and compare metrics:

```python Python theme={null}
## Calculate metrics for both models
em_base, f1_base = get_metrics(base_answers)
em_ft, f1_ft = get_metrics(finetuned_answers)

print(f"Base Model - EM: {em_base:.2f}, F1: {f1_base:.2f}")
print(f"Fine-tuned Model - EM: {em_ft:.2f}, F1: {f1_ft:.2f}")
```

You should get figures similar to the table below:

| Llama 3.1 8B | EM   | F1   |
| ------------ | ---- | ---- |
| Original     | 0.01 | 0.18 |
| Fine-tuned   | 0.32 | 0.41 |

We can see that the fine-tuned model performs significantly better on the test set, with a large improvement in both Exact Match and F1 scores.

## Advanced Topics

**Continuing a Fine-tuning Job**

You can continue training from a previous fine-tuning job:

<CodeGroup>
  ```python Python theme={null}
  response = client.fine_tuning.create(
      training_file="your-new-training-file-id",
      from_checkpoint="previous-finetune-job-id",
      wandb_api_key="your-wandb-api-key",
  )
  ```

  ```shell Shell theme={null}
  together fine-tuning create \
    --training-file "your-new-training-file-id" \
    --from-checkpoint "previous-finetune-job-id" \
    --wandb-api-key $WANDB_API_KEY
  ```
</CodeGroup>

You can specify a checkpoint by using:

* The output model name from the previous job
* Fine-tuning job ID
* A specific checkpoint step with the format `ft-...:{STEP_NUM}`

To check all available checkpoints for a job, use:

```shell Shell theme={null}
together fine-tuning list-checkpoints {FT_JOB_ID}
```

### Continued Fine-tuning jobs and LoRA Serverless Inference

Continued Fine-tuning supports various training method combinations: you can train an adapter module on top of a fully trained model or continue training an existing adapter from a previous job. Therefore, LoRA Serverless can be enabled or disabled after training is completed.
If you continue a LoRA fine-tuning job with the same LoRA hyperparameters (rank, alpha, selected modules), the trained model will be available for LoRA Serverless. However, if you change any of these parameters or continue with Full training, LoRA Serverless will be disabled. Additionally, if you continue a Full fine-tuning job, LoRA Serverless will remain disabled.
\*Note: The feature is disabled when parameters change because the Fine-tuning API merges the parent fine-tuning adapter to the base model when it detects different adapter hyperparameters, ensuring optimal training quality.

**Training and Validation Split**

To split your dataset into training and validation sets:

```shell Shell theme={null}
split_ratio=0.9  # Specify the split ratio for your training set

total_lines=$(wc -l < "your-datafile.jsonl")
split_lines=$((total_lines * split_ratio))

head -n $split_lines "your-datafile.jsonl" > "your-datafile-train.jsonl"
tail -n +$((split_lines + 1)) "your-datafile.jsonl" > "your-datafile-validation.jsonl"
```

**Using a Validation Set During Training**

A validation set is a held-out dataset to evaluate your model performance during training on unseen data. Using a validation set provides multiple benefits such as monitoring for overfitting and helping with hyperparameter tuning.

To use a validation set, provide `validation_file` and set `n_evals` to a number above 0:

```python Python theme={null}
response = client.fine_tuning.create(
    training_file="your-training-file-id",
    validation_file="your-validation-file-id",
    n_evals=10,  # Number of evaluations over the entire job
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
)
```

At set intervals during training, the model will be evaluated on your validation set, and the evaluation loss will be recorded in your job event log. If you provide a W\&B API key, you'll also be able to see these losses in the W\&B dashboard.

**Recap**

Fine-tuning LLMs with Together AI allows you to create specialized models tailored to your specific requirements. By following this guide, you've learned how to:

1. Prepare and format your data for fine-tuning
2. Launch a fine-tuning job with appropriate parameters
3. Monitor the progress of your fine-tuning job
4. Use your fine-tuned model via API or dedicated endpoints
5. Evaluate your model's performance improvements
6. Work with advanced features like continued training and validation sets


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt