# Source: https://docs.axolotl.ai/docs/getting-started.html

Title: Quickstart – Axolotl

URL Source: https://docs.axolotl.ai/docs/getting-started.html

Markdown Content:
This guide will walk you through your first model fine-tuning project with Axolotl.

Quick Example
-------------

Let’s start by fine-tuning a small language model using LoRA. This example uses a 1B parameter model to ensure it runs on most GPUs. Assuming `axolotl` is installed (if not, see our [Installation Guide](https://docs.axolotl.ai/docs/installation.html))

1. Download example configs:

`axolotl fetch examples`

1. Run the training:

`axolotl train examples/llama-3/lora-1b.yml`

That’s it! Let’s understand what just happened.

Understanding the Process
-------------------------

### The Configuration File

The YAML configuration file controls everything about your training. Here’s what (part of) our example config looks like:

```
base_model: NousResearch/Llama-3.2-1B

load_in_8bit: true
adapter: lora

datasets:
  - path: teknium/GPT4-LLM-Cleaned
    type: alpaca
dataset_prepared_path: last_run_prepared
val_set_size: 0.1
output_dir: ./outputs/lora-out
```

Tip

`load_in_8bit: true` and `adapter: lora` enables LoRA adapter finetuning.

* To perform Full finetuning, remove these two lines.
* To perform QLoRA finetuning, replace with `load_in_4bit: true` and `adapter: qlora`.

See our [config options](https://docs.axolotl.ai/docs/config-reference.html) for more details.

### Training

When you run `axolotl train`, Axolotl:

1. Downloads the base model
2. (If specified) applies QLoRA/LoRA adapter layers
3. Loads and processes the dataset
4. Runs the training loop
5. Saves the trained model and / or LoRA weights

Your First Custom Training
--------------------------

Let’s modify the example for your own data:

1. Create a new config file `my_training.yml`:

```
base_model: NousResearch/Nous-Hermes-llama-1b-v1

load_in_8bit: true
adapter: lora

# Training settings
micro_batch_size: 2
num_epochs: 3
learning_rate: 0.0003

# Your dataset
datasets:
  - path: my_data.jsonl        # Your local data file
    type: alpaca               # Or other format
```

This specific config is for LoRA fine-tuning a model with instruction tuning data using the `alpaca` dataset format, which has the following format:

```
{
    "instruction": "Write a description of alpacas.",
    "input": "",
    "output": "Alpacas are domesticated South American camelids..."
}
```

Please see our [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats) for more dataset formats and how to format them.

1. Prepare your JSONL data in the specified format (in this case, the expected `alpaca` format):

```
{"instruction": "Classify this text", "input": "I love this!", "output": "positive"}
{"instruction": "Classify this text", "input": "Not good at all", "output": "negative"}
```

1. Run the training:

`axolotl train my_training.yml`

Common Tasks
------------

Tip

The same yaml file is used for training, inference, and merging.

### Testing Your Model

After training, test your model:

`axolotl inference my_training.yml --lora-model-dir="./outputs/lora-out"`

More details can be found in [Inference](https://docs.axolotl.ai/docs/inference.html).

### Using a UI

Launch a Gradio interface:

`axolotl inference my_training.yml --lora-model-dir="./outputs/lora-out" --gradio`

### Preprocessing Data

For large datasets, preprocess first:

`axolotl preprocess my_training.yml`

Please make sure to set `dataset_prepared_path:` in your config to set the path to save the prepared dataset.

More details can be found in [Dataset Preprocessing](https://docs.axolotl.ai/docs/dataset_preprocessing.html).

### Merging LoRA weights

To merge the LoRA weights back into the base model, run:

`axolotl merge-lora my_training.yml --lora-model-dir="./outputs/lora-out"`

The merged model will be saved in the `{output_dir}/merged` directory.

More details can be found in [Merging LoRA weights](https://docs.axolotl.ai/docs/inference.html#sec-merging).

Next Steps
----------

Now that you have the basics, you might want to:

* Try different model architectures
* Experiment with hyperparameters
* Use more advanced training methods
* Scale up to larger models

Check our other guides for details on these topics:

* [Configuration Guide](https://docs.axolotl.ai/docs/config-reference.html) - Full configuration options
* [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html) - Loading datasets from various sources
* [Dataset Formats](https://docs.axolotl.ai/docs/dataset-formats) - Working with different data formats
* [Multi-GPU Training](https://docs.axolotl.ai/docs/multi-gpu.html)
* [Multi-Node Training](https://docs.axolotl.ai/docs/multi-node.html)
