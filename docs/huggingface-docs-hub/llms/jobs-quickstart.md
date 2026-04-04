# Source: https://huggingface.co/docs/hub/jobs-quickstart.md

# Quickstart

In this guide you will run a Job to fine-tune an open source model on Hugging Face infrastructure in only a few minutes.
Make sure you are logged in to Hugging Face and have access to your [Jobs page](https://huggingface.co/settings/jobs), which is available if you have a PRO account, or a Team or Enterprise subscription.

## Getting started

First install the Hugging Face CLI:

### 1. Install the CLI

Recommended approach:

```bash
>>> curl -LsSf https://hf.co/cli/install.sh | bash
```

Or using Homebrew:

```bash
>>> brew install huggingface-cli
```

Or using uv:

```bash
>>> uv tool install hf
```

### 2. Login to your Hugging Face account

Login

```bash
>>> hf auth login
```

### 3. Create your first jobs using the `hf jobs` command

Run a UV command or script

```bash
>>> hf jobs uv run python -c 'print("Hello from the cloud!")'
Job started with ID: 693aef401a39f67af5a41c0e
View at: https://huggingface.co/jobs/lhoestq/693aef401a39f67af5a41c0e
Hello from the cloud!
```

```bash
>>> echo "print('Hello from uv script!')" > script.py
>>> hf jobs uv run script.py
Job started with ID: 695f6cd8d2f3efac77e8cf7f
View at: https://huggingface.co/jobs/lhoestq/695f6cd8d2f3efac77e8cf7f
Hello from uv script!
```

Run a Docker command

```bash
>>> hf jobs run ubuntu echo 'Hello from the cloud!'
Job started with ID: 693aee76c67c9f186cfe233e
View at: https://huggingface.co/jobs/lhoestq/693aee76c67c9f186cfe233e
Hello from the cloud!
```

### 4. Check your first jobs

The job logs appear in your terminal, but you can also see them in your jobs page. Open the job page to see the job information, status and logs:

## The training script

Here is a simple training script to fine-tune a base model to a conversational model using Supervised Fine-Tuning (SFT). It uses the [Qwen/Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) model and the [trl-lib/Capybara](https://huggingface.co/datasets/trl-lib/Capybara) dataset, and the [TRL](https://huggingface.co/docs/trl/en/index) library, and saves the resulting model to your Hugging Face account under the name `"Qwen2.5-0.5B-SFT"`:

```python
from datasets import load_dataset
from trl import SFTTrainer

dataset = load_dataset("trl-lib/Capybara", split="train")
trainer = SFTTrainer(
    model="Qwen/Qwen2.5-0.5B",
    train_dataset=dataset,
)
trainer.train()
trainer.push_to_hub("Qwen2.5-0.5B-SFT")
```

Save this script as `train.py`, and we can now run it with UV on Hugging Face Jobs.

## Run the training job

`hf jobs` takes several arguments: select the hardware with `--flavor`, choose a maximum duration with `--timeout`, and pass environment variable with `--env` and `--secrets`. Here we use the A100 Large GPU flavor with `--flavor a100-large` and pass your Hugging Face token as a secret with `--secrets HF_TOKEN` in order to be able to push the resulting model to your account.

Moreover, UV accepts the `--with` argument to define python dependencies, so we use `--with trl` to have the `trl` library available.

You can now run the final command which looks like this:

```bash
hf jobs uv run \
    --flavor a100-large \
    --timeout 6h \
    --with trl \
    --secrets HF_TOKEN \
    train.py
```

The logs appear in your terminal, and you can safely Ctrl+C to stop streaming the logs, the job will keep running.

```
...
Downloaded nvidia-cudnn-cu12 
Downloaded torch
Installed 66 packages in 233ms
Generating train split: 100%|██████████| 15806/15806 [00:00

Monitor GPU usage and other metrics in the CLI or use the [MacOS menu bar](./jobs-manage#macos-menu-bar). Here with the CLI you get:

```bash
>>> hf jobs stats
JOB ID                   CPU % NUM CPU MEM % MEM USAGE        NET I/O         GPU UTIL % GPU MEM % GPU MEM USAGE   
------------------------ ----- ------- ----- ---------------- --------------- ---------- --------- --------------- 
695e83c5d2f3efac77e8cf18 8%    12.0    7.18% 10.9GB / 152.5GB 0.0bps / 0.0bps 100%       31.92%    25.9GB / 81.2GB
```

Once the job is done, find your model on your account:

Congrats ! You just run your first Job to fine-tune an open source model 🔥

Feel free to try out your model locally and evaluate it using e.g. [transformers](https://huggingface.co/docs/transformers) by clicking on "Use this model", or deploy it to [Inference Endpoints](https://huggingface.co/docs/inference-endpoints) in one click using the "Deploy" button.

