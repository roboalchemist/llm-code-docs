# Source: https://docs.anyscale.com/llm/fine-tuning/data-preparation.md

# Dataset preparation for LLM post-training

[View Markdown](/llm/fine-tuning/data-preparation.md)

# Dataset preparation for LLM post-training

tip

This guide uses LlamaFactory as an example framework. Anyscale supports multiple frameworks for LLM post-training. See [Choose a framework for LLM post-training](/llm/fine-tuning/comparison.md).

This guide prepares custom datasets for post-training with LLaMA-Factory. You acquire raw data and format it correctly for various training methods, including pre-training, supervised fine-tuning, Preference Tuning (DPO, KTO), and multimodal fine-tuning.

## Sources of training data[​](#data-sources "Direct link to Sources of training data")

Training data comes from three main categories: public datasets, internal data, and synthetically generated data. Choose the best source based on your project goals, budget, and data privacy requirements.

### Public datasets[​](#public-datasets "Direct link to Public datasets")

Use public datasets for academic projects, learning fine-tuning, or when you need a general-purpose dataset without proprietary information.

Public datasets are large, well-documented, and free. They work well for replicating research and benchmarking model performance. The Hugging Face Hub is the primary repository for these datasets.

Browse the Hugging Face Hub for popular datasets such as `databricks-dolly-15k` for instruction following. These datasets are well-structured and require minimal reformatting. Map the existing column names (for example, `instruction`, `response`) to the names LLaMA-Factory expects in the `dataset_info.json` file, covered later in this guide.

### Internal data[​](#internal-data "Direct link to Internal data")

Use internal data to create a high-value, proprietary model that understands your specific business, products, or customers.

Internal data is the only way to teach a model about your unique domain. This approach offers two major advantages:

1. **Privacy**: Your sensitive company data remains in-house and doesn't go to third-party API providers.
2. **Cost-effectiveness**: Fine-tuning and serving a smaller, specialized model is significantly cheaper than paying for API calls to a large, general-purpose model.

Internal data requires a transformation script, usually in Python, to reshape it into the required training format.

For example, to convert a CSV export of support tickets into a conversational dataset, your script groups messages by ticket and maps your internal author roles to the required format, such as converting `customer` to `human` and `agent` to `gpt` before writing the final structured JSON file.

### Synthetic data generation[​](#synthetic-data "Direct link to Synthetic data generation")

Use synthetic data generation when high-quality, real-world data is scarce, or you need to augment an existing dataset to cover more topics and improve its diversity.

Synthetic data creates a large, high-quality dataset tailored to your needs. You control the format, style, and content with precision.

This process is automated using a script that reads from an external data source, such as a product database, and uses a powerful "teacher" LLM to generate the desired outputs for each entry.

Before using a proprietary model for data generation, check its terms of service. Many providers, including OpenAI, prohibit using their model's output to develop or train competing models. A common and safe alternative is to use a powerful open source LLM for this task. You can do this efficiently at scale using Ray's batch inference frameworks.

The general process remains the same regardless of the model you choose. For example, to generate marketing descriptions in the Alpaca format:

1. **Start with your raw, external data source**, such as a CSV file containing your product catalog with columns for `product_name` and `features`.

2. **Write a script** to read each row from your source file. For each product, the script programmatically constructs a unique prompt to send to the teacher LLM. The core of your script's logic might look like the following:

   ```
   # For each product_name and features from your CSV
   prompt = f"Write a short, exciting marketing description for a product named '{product_name}' with the following features: {features}."

   # Input this prompt to the teacher LLM and get a response
   ```

3. **Assemble the final training records.** Your script takes the response from the teacher LLM and combines it with the original data to create the final JSON object for your training file. The resulting record looks like the following:

   ```
   {
     "instruction": "Write a short, exciting marketing description for a product named 'Solar-Powered Smartwatch' with the following features: GPS, heart rate monitor, waterproof.",
     "output": "Explore without limits! Our new Solar-Powered Smartwatch keeps you charged and connected on any adventure with built-in GPS and heart rate monitoring."
   }
   ```

## Choose your data format[​](#data-format "Direct link to Choose your data format")

LLaMA-Factory supports datasets in several file types, including `json`, `jsonl`, `csv`, `parquet`, and `arrow`. Internally, these files should be structured in one of two primary formats: **Alpaca** or **ShareGPT**.

Choose the format based on your fine-tuning goal and the structure of your available data. For a simple question-and-answer model, use Alpaca. For a conversational chatbot, especially one that can use tools (function calling), use ShareGPT.

The field names shown in the examples below (`instruction`, `output`, `conversations`, and more) can be different in your own data files. As long as your fields serve the same purpose, you can map them to the names LLaMA-Factory expects, covered in the next section.

### Alpaca format[​](#alpaca-format "Direct link to Alpaca format")

The Alpaca format is ideal for instruction-following tasks. It's structured as a flat list of JSON objects, where each object represents a single instruction-response pair.

**Use case**: Best for training models on tasks such as summarization, translation, and simple Q\&A based on a single prompt.

**Format**:

```
[
  {
    "instruction": "Provide a brief summary of the plot of 'Dune'.",
    "input": "",
    "output": "Dune is a sci-fi epic about Paul Atreides, a young nobleman whose family accepts stewardship of the desert planet Arrakis, the only source of a valuable spice. After his family is betrayed, Paul must lead the native Fremen to reclaim the planet.",
    "system": "You are a helpful assistant that provides concise summaries.",
    "history": [
      ["What is the main theme of 'Dune'?", "The main themes include politics, religion, and humanity's relationship with nature."],
      ["Who is the author?", "Frank Herbert."]
    ]
  }
]
```

**Important notes**:

* **Record structure**: Each JSON object requires an `instruction` and `output`. The `input`, `system`, and `history` fields are optional.
* During training, the system constructs the final user prompt by combining `instruction` and `input` (separated by a newline).
* The model learns to generate the content in the `output` field.
* The model also learns responses in the optional `history` column during supervised fine-tuning, providing conversational context.

### ShareGPT format[​](#sharegpt-format "Direct link to ShareGPT format")

The ShareGPT format is designed for multi-turn conversations and is the standard for training modern chatbots and agents. Its nested structure explicitly defines the back-and-forth flow of a dialog. The popular OpenAI format is a special case of ShareGPT, typically using `role` and `content` for the field names instead of `from` and `value`.

**Use case**: Essential for building conversational agents, modeling complex dialogs, and fine-tuning models for tool use (function calling).

**Format**:

```
[
  {
    "tools": "[{\"name\": \"search_recipes\", \"description\": \"Search for recipes based on ingredients\", \"parameters\": {\"type\": \"object\", \"properties\": {\"ingredients\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}}}}]",
    "conversations": [
      {
        "from": "human",
        "value": "I have chicken, bell peppers, and rice. What can I make?"
      },
      {
        "from": "function_call",
        "value": "{\"name\": \"search_recipes\", \"arguments\": {\"ingredients\": [\"chicken\", \"bell peppers\", \"rice\"]}}"
      },
      {
        "from": "observation",
        "value": "{\"recipe\": \"Chicken and Bell Pepper Stir Fry\"}"
      },
      {
        "from": "gpt",
        "value": "Based on the ingredients, you could make a Chicken and Bell Pepper Stir Fry."
      }
    ]
  }
]
```

**Important notes**:

* **Record structure**: Each JSON object requires a `conversations` field, which contains an ordered list of turns. Each turn must have a role (for example, `from`) and content (for example, `value`). The `tools` field is optional but required for function calling.
* You must follow a strict turn order: `human` and `observation` (tool output) must appear in odd-numbered positions, while `gpt` and `function_call` must appear in even-numbered positions. The model learns to generate the content in the `gpt` and `function_call` turns.
* **`from` tags aren't "learned"**: These tags are metadata for the training process that convert into special tokens, telling the model which role to adopt for a given turn. The model only learns to generate the content in the `value` field.

## Register your dataset[​](#register-dataset "Direct link to Register your dataset")

Once you have a formatted data file, tell LLaMA-Factory where to find it and how to interpret it by adding an entry to the `dataset_info.json` file. This file serves as a manifest that registers your custom datasets with LLaMA-Factory.

To register your dataset, add a new key-value pair to the `dataset_info.json` file. The key is your chosen dataset name (for example, `"my_custom_sft"`), and the value is a JSON object describing the dataset.

Below is a basic example for a local Alpaca-style dataset where your source file uses custom column names such as `task_instruction`, `context_data`, and `expected_answer`:

```
{
  "my-custom-sft": {
    "file_name": "/mnt/shared_storage/data/sft/my_sft_data.json",
    "columns": {
      "prompt": "task_instruction",
      "query": "context_data",
      "response": "expected_answer"
    }
  }
}
```

This file tells LLaMA-Factory the following:

1. Define a dataset named "my-custom-sft" that you can reference in the training configuration.
2. Find the data in the local file `/mnt/shared_storage/data/sft/my_sft_data.json`.
3. For the Alpaca format, map the `task_instruction` column to the internal `prompt` field, `context_data` to `query`, and `expected_answer` to `response`.

In your main training YAML file, you must update two parameters:

1. **`dataset`**: Set to the custom name you defined in `dataset_info.json`.
2. **`dataset_dir`**: Set to the path of the directory containing your `dataset_info.json` file.

```
# In your main training config (e.g., sft_lora.yaml)

### Dataset
# 1. This is the custom name defined inside dataset_info.json
dataset: my-custom-sft

# 2. This directory contains the dataset_info.json file
dataset_dir: /mnt/cluster_storage/my_project
```

caution

For distributed training jobs, like Anyscale jobs, it's critical that **you place both the `dataset_dir` and the actual data files it references in a storage location that all workers can access** like a shared mount or object storage. This ensures all remote worker nodes can find and load the data.

### Use cloud-hosted datasets (S3/GCS)[​](#cloud-datasets "Direct link to Use cloud-hosted datasets (S3/GCS)")

warning

At this time, LLaMA-Factory doesn't support Azure for cloud-hosted datasets.

If your dataset lives in cloud object storage, install the appropriate library: `pip install s3fs` for Amazon S3, `pip install gcsfs` for Google Cloud Storage. Then, in **dataset\_info.json**, use **cloud\_file\_name** (instead of **file\_name**) and set it to your object URI. Ensure all workers can access the bucket. See [Configure IAM permissions](/storage/configure.md#iam) for how to access private storage buckets.

* Amazon S3
* Google Cloud Storage

```
{
  "my-custom-sft-s3": {
    "cloud_file_name": "s3://my-bucket/alpaca_en_demo.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
  }
}
```

```
{
  "my-custom-sft-gcs": {
    "cloud_file_name": "gs://my-bucket/alpaca_en_demo.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
  }
}
```

Below is a comprehensive list of all possible fields you can use to configure a dataset entry:

```
"dataset_name": {
    "hf_hub_url": "the name of the dataset repository on the Hugging Face hub. (if specified, ignore script_url, file_name and cloud_file_name)",
    "ms_hub_url": "the name of the dataset repository on the Model Scope hub. (if specified, ignore script_url, file_name and cloud_file_name)",
    "script_url": "the name of the directory containing a dataset loading script. (if specified, ignore file_name and cloud_file_name)",
    "cloud_file_name": "the name of the dataset file in s3/gcs cloud storage. (if specified, ignore file_name)",
    "file_name": "the name of the dataset folder or dataset file in this directory. (required if above are not specified)",
    "formatting": "the format of the dataset. (optional, default: alpaca, can be chosen from {alpaca, sharegpt})",
    "ranking": "whether the dataset is a preference dataset or not. (default: False)",
    "subset": "the name of the subset. (optional, default: None)",
    "split": "the name of dataset split to be used. (optional, default: train)",
    "folder": "the name of the folder of the dataset repository on the Hugging Face hub. (optional, default: None)",
    "num_samples": "the number of samples in the dataset to be used. (optional, default: None)",
    "columns (optional)": {
      "prompt": "the column name in the dataset containing the prompts. (default: instruction)",
      "query": "the column name in the dataset containing the queries. (default: input)",
      "response": "the column name in the dataset containing the responses. (default: output)",
      "history": "the column name in the dataset containing the histories. (default: None)",
      "messages": "the column name in the dataset containing the messages. (default: conversations)",
      "system": "the column name in the dataset containing the system prompts. (default: None)",
      "tools": "the column name in the dataset containing the tool description. (default: None)",
      "images": "the column name in the dataset containing the image inputs. (default: None)",
      "videos": "the column name in the dataset containing the videos inputs. (default: None)",
      "audios": "the column name in the dataset containing the audios inputs. (default: None)",
      "chosen": "the column name in the dataset containing the chosen answers. (default: None)",
      "rejected": "the column name in the dataset containing the rejected answers. (default: None)",
      "kto_tag": "the column name in the dataset containing the kto tags. (default: None)"
    },
    "tags (optional, used for the sharegpt format)": {
      "role_tag": "the key in the message represents the identity. (default: from)",
      "content_tag": "the key in the message represents the content. (default: value)",
      "user_tag": "the value of the role_tag represents the user. (default: human)",
      "assistant_tag": "the value of the role_tag represents the assistant. (default: gpt)",
      "observation_tag": "the value of the role_tag represents the tool results. (default: observation)",
      "function_tag": "the value of the role_tag represents the function call. (default: function_call)",
      "system_tag": "the value of the role_tag represents the system prompt. (default: system, can override system column)"
    }
  }    
```

## Method-specific data formats[​](#method-formats "Direct link to Method-specific data formats")

This section provides data formatting requirements and examples for each post-training method supported by LLaMA-Factory.

### Continued pre-training[​](#continued-pretraining "Direct link to Continued pre-training")

Continued pre-training extends the foundational learning process of an LLM on large amounts of unlabeled text. This post-training technique adapts a model to a new domain (for example, medical, legal, or scientific text) or continues its general training. For this method, your dataset only needs a single text column.

**Alpaca example**:

**Example data (`c4.jsonl`)**:

```
{"text": "Foil plaid lycra and spandex shortall with metallic slinky insets. Attached metallic elastic belt with O-ring..."}
```

**`dataset_info.json` Entry**:

```
"continued_pretrain_alpaca": {
    "file_name": "alpaca/c4.jsonl",
    "columns": {
        "prompt": "text"
    }
}
```

note

Continued pre-training doesn't support the ShareGPT format.

For continued pre-training, full-parameter fine-tuning generally yields the best quality but requires significantly more compute, longer training, and large checkpoints. LoRA adapters are much faster and cheaper with small adapter checkpoints, but recent work shows that standard low-rank LoRA configurations can underperform full fine-tuning on challenging domains such as code and math. See [Biderman et al., "LoRA Learns Less and Forgets Less"](https://arxiv.org/pdf/2405.09673). You usually see the clearest gains from continued pre-training when you train on a focused, reasonably clean corpus for your target domain rather than a very broad or noisy mix, regardless of whether you use LoRA or full fine-tuning.

### Supervised fine-tuning[​](#sft "Direct link to Supervised fine-tuning")

Supervised fine-tuning is the most common method for teaching a model to follow specific instructions or adopt a particular style. Provide high-quality examples of prompts and the ideal responses. The core requirements are fields for the user's instruction and the model's desired output.

**Alpaca example**:

**Example data (`alpaca_en_demo.json`)**:

```
{
  "instruction": "Describe a process of making crepes.",
  "input": "",
  "output": "Making crepes is an easy and delicious process! Here are step-by-step instructions..."
}
```

**`dataset_info.json` Entry**:

```
"sft_alpaca": {
    "file_name": "alpaca/alpaca_en_demo.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
}
```

**ShareGPT Example**:

**Example Data (`glaive_toolcall_en_demo.json`)**:

```
{
  "conversations": [
    { "from": "human", "value": "I have chicken, bell peppers, and rice." },
    { "from": "function_call", "value": "{\"name\": \"search_recipes\", ...}" },
    { "from": "observation", "value": "{\"recipes\": [{\"name\": \"Chicken and Bell Pepper Stir Fry\", ...}]}" },
    { "from": "gpt", "value": "I found two recipes for you..." }
  ],
  "tools": "[{\"name\": \"search_recipes\", ...}]"
}
```

**`dataset_info.json` Entry**:

```
"sft_sharegpt": {
    "file_name": "sharegpt/glaive_toolcall_en_demo.json",
    "formatting": "sharegpt",
    "columns": {
        "messages": "conversations",
        "tools": "tools"
    }
}
```

### Preference-based methods: DPO, ORPO, SimPO[​](#preference-methods "Direct link to Preference-based methods: DPO, ORPO, SimPO")

Use a preference-based method when you can judge which of two responses is better. This format requires a `chosen` and `rejected` field in your data, and the `ranking: true` flag must be set in your `dataset_info.json` entry. Methods such as DPO, ORPO, and SimPO all use this structure.

**Alpaca example**:

**Example data (`ultrafeedback.jsonl`)**:

```
{
  "prompt": "Definition: Given a sentence in French, provide an equivalent paraphrased version...",
  "rejected": "On 6th March 1725, Elizabeth Crowley...",
  "chosen": "1. Paraphrase the given sentence in French..."
}
```

**`dataset_info.json` Entry**:

```
"preference_alpaca": {
    "file_name": "alpaca/ultrafeedback.jsonl",
    "ranking": true,
    "columns": {
      "prompt": "prompt",
      "chosen": "chosen",
      "rejected": "rejected"
    }
}
```

**ShareGPT example**:

**Example data (`dpo_en_demo.json`)**:

```
{
  "conversations": [
    { "from": "human", "value": "Hi! I'd like to create a new language game..." }
  ],
  "chosen": { "from": "gpt", "value": "That sounds like a fun and engaging idea! Here are some tips..." },
  "rejected": { "from": "gpt", "value": "Hello! I'd be happy to help you create a language game..." }
}
```

**`dataset_info.json` Entry**:

```
"preference_sharegpt": {
    "file_name": "sharegpt/dpo_en_demo.json",
    "ranking": true,
    "formatting": "sharegpt",
    "columns": {
      "messages": "conversations",
      "chosen": "chosen",
      "rejected": "rejected"
    }
}
```

### Kahneman-Tversky optimization (KTO)[​](#kto "Direct link to Kahneman-Tversky optimization (KTO)")

KTO is a simpler preference method. Instead of a chosen and rejected pair, this format requires a single model response and a boolean `kto_tag` field indicating whether a human user would find that response desirable.

**Alpaca example**:

**Example data (`instructions_kto.jsonl`)**:

```
// A chosen and good example
{
  "prompt": "User: What is the mean inclination for randomly oriented orbits?",
  "completion": "For randomly oriented orbits, the inclinations follow a sine distribution. This results in a mean inclination of approximately 57.3 degrees, or 1 radian.",
  "label": true
}
// A rejected and bad example
{
  "prompt": "User: Can you list three benefits of drinking water?",
  "completion": "Drinking water gives you superpowers like flight, invisibility, and the ability to talk to squirrels.",
  "label": false
}
```

**`dataset_info.json` Entry**:

```
"kto_alpaca": {
    "file_name": "alpaca/instructions_kto.jsonl",
    "columns": {
      "prompt": "prompt",
      "response": "completion",
      "kto_tag": "label"
    }
}
```

**ShareGPT example**:

**Example data (`kto_en_demo.json`)**:

```
[
  // Chosen response
  {
    "messages": [
      { "content": "The Federal Trade Commission is going after spyware that gets secretly installed on people's phones. What's a good way to summarize this for a non-technical audience?", "role": "user" },
      { "content": "Think of it like this: The government's top consumer watchdog is fighting back against sneaky software that spies on you through your phone. They're working to protect your privacy.", "role": "assistant" }
    ],
    "label": true
  },
  // Rejected response
  {
    "messages": [
      { "content": "How does a car engine work in simple terms?", "role": "user" },
      { "content": "I am unable to simplify complex mechanical topics. Please consult an automotive engineer.", "role": "assistant" }
    ],
    "label": false
  }
]
```

**`dataset_info.json` Entry**:

```
"kto_sharegpt": {
    "file_name": "sharegpt/kto_en_demo.json",
    "formatting": "sharegpt",
    "columns": { "messages": "messages", "kto_tag": "label" },
    "tags": { "role_tag": "role", "content_tag": "content" }
}
```

### Multimodal fine-tuning[​](#multimodal "Direct link to Multimodal fine-tuning")

Use this format to train a model that can understand non-text inputs. This requires an `images`, `videos`, or `audios` field containing a list of file paths, and corresponding `<image>`, `<video>`, or `<audio>` placeholder tokens in the text. The number of tokens must exactly match the number of file paths.

**Alpaca example**:

**Example data file (`my_vlm_data.json`)**:

```
[
  {
    "instruction": "What is in this image? <image>",
    "output": "The image shows a golden retriever playing fetch in a park.",
    "images": ["images/dog_in_park.jpg"]
  }
]
```

**`dataset_info.json` Entry**:

```
"multimodal_alpaca": {
  "file_name": "my_vlm_data.json",
  "columns": {
    "prompt": "instruction",
    "response": "output",
    "images": "images"
  }
}
```

**ShareGPT example**:

**Example data (`mllm_demo.json`)**:

```
{
  "messages": [
    { "content": "<image>Who are they?", "role": "user" },
    { "content": "They're Kane and Gretzka from Bayern Munich.", "role": "assistant" }
  ],
  "images": [ "sharegpt/mllm_demo_data/1.jpg" ]
}
```

**`dataset_info.json` Entry**:

```
"multimodal_sharegpt": {
    "file_name": "sharegpt/mllm_demo.json",
    "formatting": "sharegpt",
    "columns": { "messages": "messages", "images": "images" },
    "tags": { "role_tag": "role", "content_tag": "content" }
}
```

## Quality checklist[​](#quality-checklist "Direct link to Quality checklist")

Before launching a fine-tuning job, run your data through these essential checks:

* **Structural integrity**: Ensure every row is valid (for example, proper JSON) and contains all required columns for its format.
* **Remove duplicates**: Remove exact or near-duplicate samples to avoid biasing the model and wasting compute.
* **Length constraints**: Check that your samples generally fit within the model's context window (`cutoff_len`), as the system truncates longer inputs.
* **Content filtering**: Scan for and remove toxic content or personally identifiable information (PII).
* **Media path validation (for multimodal)**: Confirm that every path in `images`, `videos`, or `audios` exists and is accessible.
