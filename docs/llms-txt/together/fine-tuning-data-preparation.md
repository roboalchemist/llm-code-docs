# Source: https://docs.together.ai/docs/fine-tuning-data-preparation.md

> Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

# Data Preparation

Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

### Which file format should I use for data?

JSONL is simpler and will work for many cases, while Parquet stores pre-tokenized data, providing flexibility to specify custom attention mask and labels (loss masking). It also saves you time for each job you run by skipping the tokenization step.

By default, it's easier to use JSONL. However, there are a couple of things to keep in mind:

1. For JSONL training data, we use a variation of [sample packing](https://huggingface.co/docs/trl/main/en/reducing_memory_usage#packing) that improves training efficiency by utilizing the maximum context length via packing multiple examples together. This technique changes the effective batch size, making it larger than the specified batch size, and reduces the total number of training steps.\
   If you'd like to disable packing during training, you can provide a tokenized dataset in a Parquet file. [This example script](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py#L34) for tokenizing a dataset demonstrates padding each example with a padding token. Note that the corresponding `attention_mask` and `labels` should be set to 0 and -100, respectively, so that the model ignores the padding tokens during prediction and excludes them from the loss calculation.
2. If you want to specify custom `attention_mask` values or apply some tokenization customizations unique to your setup, you can use the Parquet format as well.

**Note**: Regardless of the dataset format, the data file size must be under 25GB.

## Text Data

## Data formats

Together Fine-tuning API accepts three text dataset formats for the training dataset. Your data file must be in the `.jsonl` format with fields that indicate the dataset format. You can have other fields, but they will be ignored during training. To speed up the data uploading and processing steps and to maximize the number of examples per file, we recommend to remove the unused fields.

Also, if the data has two or more possible formats (e.g., it contains both `text` and `messages`), the Together client will show an error at the file check stage before the upload.

### Conversational Data

For conversational fine-tuning, your data file must contain a `messages` field on each line, with `role` and `content` specified for each message. Each sample should start with either a `system` or `user` message, followed by alternating `user` and `assistant` messages. The Together client will reject any dataset that does not follow this pattern.

Optionally, you can add a `weight` field to any message to control its contribution to the training loss. Messages with `weight=0` will be masked during training (their tokens won't contribute to the loss), while messages with `weight=1` (default) will be included. Only values 0 and 1 are supported for the `weight` field.

```Text JSONL theme={null}
{
  "messages": [
    {"role": "system", "content": "This is a system prompt."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I help you?"},
    {"role": "user", "content": "Can you explain machine learning?", "weight": 0},
    {"role": "assistant", "content": "Machine learning is...", "weight": 1}
  ]
}
```

The resulting conversation dataset will be automatically formatted into the model's [chat template](https://huggingface.co/docs/transformers/main/en/chat_templating) if it is defined for that model, or into the default template otherwise. As a general rule, all instruction-finetuned models have their own chat templates, and base models do not have them.

By default, models will be trained to predict only `assistant` messages. Use `--train-on-inputs true` to include other messages in training. See the [API Reference](/reference/post-fine-tunes) for details.

Note that if any message in a conversation has a `weight` field, the `train-on-inputs` setting will automatically be set to `true`, and all messages without weights in the dataset will be used as targets during training. If you want to train only on assistant messages in this case, you must explicitly set `--train-on-inputs false`.

Example datasets:

* [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat)
* [davanstrien/cosmochat](https://huggingface.co/datasets/davanstrien/cosmochat)

### Instruction Data

For instruction-based fine-tuning, your data file must contain `prompt` and `completion` fields:

```Text JSONL theme={null}
{"prompt": "...", "completion": "..."}
{"prompt": "...", "completion": "..."}
```

By default, models will not be trained to predict the text from the prompt. Use `--train-on-inputs true` to include prompts in training. See the [API Reference](/reference/post-fine-tunes) for details.

Here are some examples with this format that you can download from the Hugging Face Hub:

* [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
* [glaiveai/glaive-code-assistant](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)

### Generic Text Data

If you have no need for instruction or conversational training, you can put the data in the `text` field.

```Text JSONL theme={null}
{"text": "..."}
{"text": "..."}
```

Here are some examples of datasets that you can download from the Hugging Face Hub:

* [unified\_jokes\_explanations.jsonl](https://huggingface.co/datasets/laion/OIG/resolve/main/unified_joke_explanations.jsonl)
* [togethercomputer/RedPajama-Data-1T-Sample](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T-Sample)

### Preference Data

This data format is used for the Preference Fine-Tuning.

Each example in your dataset should contain:

* A context "input" which consists of messages in the [conversational format](/docs/fine-tuning-data-preparation#conversational-data).
* A preferred output (an ideal assistant response).
* A non-preferred output (a suboptimal assistant response).

Each preferred and non-preferred output must contain just a single message from assistant.

The data should be formatted in **JSONL** format, with each line representing an example in the following structure:

```text Text theme={null}
{
  "input": {
    "messages": [
      {
        "role": "assistant",
        "content": "Hi! I'm powered by Together.ai's open-source models. Ask me anything!"
      },
      {
        "role": "user",
        "content": "What’s open-source AI?"
      }
    ]
  },
  "preferred_output": [
    {
      "role": "assistant",
      "content": "Open-source AI means models are free to use, modify, and share. Together.ai makes it easy to fine-tune and deploy them."
    }
  ],
  "non_preferred_output": [
    {
      "role": "assistant",
      "content": "It means the code is public."
    }
  ]
}
```

## Tokenized Data

You can also provide tokenized data for more advanced use cases. You may want to use this data format if you are:

1. Using the same dataset for multiple experiments: this saves the tokenization step and accelerates your fine-tuning job.
2. Using a custom tokenizer that's intentionally different than the base model tokenizer
3. Masking out certain parts of your examples for the loss calculation (which are not covered by instruction or conversational dataset use cases above)

Your data file must meet the following requirements:

* The data file size must be under 25GB.
* The file format must be in the `.parquet` format.
* Allowed fields:
  * `input_ids`(required): List of token ids to be fed to a model.
  * `attention_mask`(required): List of indices specifying which tokens should be attended to by the model.
  * `labels`(optional): List of token ids to be used as target predictions. The default token ID to be ignored in the loss calculation is `-100`. To ignore certain predictions in the loss, replace their corresponding values with `-100`. If this field is not given, `input_ids` will be used.

## Example

You can find an [example script ](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py) that converts text data in Hugging Face Hub to the tokenized format.

In this example, we will use a toy dataset [clam004/antihallucination\_dataset](https://huggingface.co/datasets/clam004/antihallucination_dataset) in Hugging Face Hub with the tokenizer from `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`model. The max sequence length of this model is 32768. To compare the differences between packing and padding, we will run the script twice with and without `--packing`. When packing is not applied, each example will be (left-)padded with the tokenizer's own pad token to keep the length of all examples consistent. Note that packing is used during training by default, and we recommend to use packing during the tokenization step by passing `--packing` in the example script. Also note that we shift labels internally for model training and you do not need to do this.

* With packing,

```Text shell theme={null}
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --packing --out-filename="processed_dataset_packed.parquet"
```

`processed_dataset_packed.parquet` will be saved under the same directory.

* Without packing,

```Text python theme={null}
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --out-filename="processed_dataset.parquet"
```

`processed_dataset_padded.parquet` will be saved under the same directory.

Let's load the generated files to see the results. In python,

```Text python theme={null}
>>> from datasets import load_dataset
>>> dataset_packed = load_dataset("parquet", data_files={'train': 'processed_dataset_packed.parquet'})
>>> dataset_padded = load_dataset("parquet", data_files={'train': 'processed_dataset_padded.parquet'})
```

First, you will see the number of examples from the dataset with packing is only 6 while the one without packing has 238:

```Text python theme={null}
>>> dataset_packed['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 6
})
>>> dataset_padded['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 238
})
```

In the first example of `dataset_padded` you will find the first 31140 tokens are padded and have `-100` as their labels to be ignored during the loss mask. The pad token for this tokenizer is `32000`

```python python theme={null}
{
    "input_ids": [32000, 32000, 32000, ..., 3409, 6898, 28767],
    "attention_masks": [0, 0, 0, ..., 1, 1, 1],
    "labels": [-100, -100, -100, ..., 3409, 6898, 28767],
}
```

On the other hand, in the first example of `dataset_packed`, no padding is used. And the first 1628 token ids match the last 1628 token ids from the first example of `dataset_padded`.

```text Text theme={null}
{
  "input_ids": [1, 523, 434, ..., 6549, 3805, 7457],
  "attention_masks": [1, 1, 1, ..., 1, 1, 1],
  "labels": [1, 523, 434,..., 6549, 3805, 7457]
}
```

## File Check

To confirm that your dataset has the right format, run the following command. This step is optional, but we highly recommend to run this step before uploading the file and using it for fine-tuning.

```text Text theme={null}
together files check PATH_TO_DATA_FILE
```

Here's the output:

```shell Shell theme={null}
together files check joke_explanations.jsonl
{
    "is_check_passed": true,
    "message": "Checks passed",
    "found": true,
    "file_size": 781041,
    "utf8": true,
    "line_type": true,
    "text_field": true,
    "key_value": true,
    "min_samples": true,
    "num_samples": 238,
    "load_json": true,
    "filetype": "jsonl"
}
```

After your data is prepared, upload your file using either [CLI](/reference/finetune) or [Python SDK](https://github.com/togethercomputer/together-python).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt