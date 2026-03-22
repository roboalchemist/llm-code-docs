# Source: https://docs.wandb.ai/weave/guides/integrations/huggingface.md

# Source: https://docs.wandb.ai/models/integrations/huggingface.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hugging Face

> Visualize and track Hugging Face model performance with W&B, logging hyperparameters, metrics, and GPU utilization.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/huggingface/Huggingface_wandb.ipynb" />

Visualize your [Hugging Face](https://github.com/huggingface/transformers) model's performance quickly with a seamless [W\&B](https://wandb.ai/site) integration.

Compare hyperparameters, output metrics, and system stats like GPU utilization across your models.

## Why should I use W\&B?

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/_OEDykSS2PIumrEw/images/tutorials/huggingface-why.png?fit=max&auto=format&n=_OEDykSS2PIumrEw&q=85&s=06138cad556d6b611c67d197c0406e85" alt="Benefits of using W&B" width="4672" height="816" data-path="images/tutorials/huggingface-why.png" />
</Frame>

* **Unified dashboard**: Central repository for all your model metrics and predictions
* **Lightweight**: No code changes required to integrate with Hugging Face
* **Accessible**: Free for individuals and academic teams
* **Secure**: All projects are private by default
* **Trusted**: Used by machine learning teams at OpenAI, Toyota, Lyft and more

Think of W\&B like GitHub for machine learning models— save machine learning experiments to your private, hosted dashboard. Experiment quickly with the confidence that all the versions of your models are saved for you, no matter where you're running your scripts.

W\&B lightweight integrations works with any Python script, and all you need to do is sign up for a free W\&B account to start tracking and visualizing your models.

In the Hugging Face Transformers repo, we've instrumented the Trainer to automatically log training and evaluation metrics to W\&B at each logging step.

Here's an in depth look at how the integration works: [Hugging Face + W\&B Report](https://app.wandb.ai/jxmorris12/huggingface-demo/reports/Train-a-model-with-Hugging-Face-and-Weights-%26-Biases--VmlldzoxMDE2MTU).

## Install, import, and log in

Install the Hugging Face and W\&B libraries, and the GLUE dataset and training script for this tutorial.

* [Hugging Face Transformers](https://github.com/huggingface/transformers): Natural language models and datasets
* [W\&B](/): Experiment tracking and visualization
* [GLUE dataset](https://gluebenchmark.com/): A language understanding benchmark dataset
* [GLUE script](https://raw.githubusercontent.com/huggingface/transformers/refs/heads/main/examples/pytorch/text-classification/run_glue.py): Model training script for sequence classification

```notebook  theme={null}
!pip install datasets wandb evaluate accelerate -qU
!wget https://raw.githubusercontent.com/huggingface/transformers/refs/heads/main/examples/pytorch/text-classification/run_glue.py
```

```notebook  theme={null}
# the run_glue.py script requires transformers dev
!pip install -q git+https://github.com/huggingface/transformers
```

Before continuing, [sign up for a free account](https://app.wandb.ai/login?signup=true).

## Put in your API key

Once you've signed up, run the next cell and click on the link to get your API key and authenticate this notebook.

```python  theme={null}
import wandb
wandb.login()
```

Optionally, we can set environment variables to customize W\&B logging. See the [Hugging Face integration guide](/models/integrations/huggingface/).

```python  theme={null}
# Optional: log both gradients and parameters
%env WANDB_WATCH=all
```

## Train the model

Next, call the downloaded training script [run\_glue.py](https://huggingface.co/transformers/examples.html#glue) and see training automatically get tracked to the W\&B dashboard. This script fine-tunes BERT on the Microsoft Research Paraphrase Corpus— pairs of sentences with human annotations indicating whether they are semantically equivalent.

```python  theme={null}
%env WANDB_PROJECT=huggingface-demo
%env TASK_NAME=MRPC

!python run_glue.py \
  --model_name_or_path bert-base-uncased \
  --task_name $TASK_NAME \
  --do_train \
  --do_eval \
  --max_seq_length 256 \
  --per_device_train_batch_size 32 \
  --learning_rate 2e-4 \
  --num_train_epochs 3 \
  --output_dir /tmp/$TASK_NAME/ \
  --overwrite_output_dir \
  --logging_steps 50
```

## Visualize results in dashboard

Click the link printed out above, or go to [wandb.ai](https://app.wandb.ai) to see your results stream in live. The link to see your run in the browser will appear after all the dependencies are loaded. Look for the following output: "**wandb**: View run at \[URL to your unique run]"

**Visualize Model Performance**
It's easy to look across dozens of experiments, zoom in on interesting findings, and visualize highly dimensional data.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/_OEDykSS2PIumrEw/images/tutorials/huggingface-visualize.gif?s=7099ba1ff84e51224afe429d985f6360" alt="Model metrics dashboard" width="1986" height="1420" data-path="images/tutorials/huggingface-visualize.gif" />
</Frame>

**Compare Architectures**
Here's an example comparing [BERT vs DistilBERT](https://app.wandb.ai/jack-morris/david-vs-goliath/reports/Does-model-size-matter%3F-Comparing-BERT-and-DistilBERT-using-Sweeps--VmlldzoxMDUxNzU). It's easy to see how different architectures effect the evaluation accuracy throughout training with automatic line plot visualizations.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/_OEDykSS2PIumrEw/images/tutorials/huggingface-comparearchitectures.gif?s=3f05edccc9d0b0bac66b0dd0fea3fa1d" alt="BERT vs DistilBERT comparison" width="1638" height="878" data-path="images/tutorials/huggingface-comparearchitectures.gif" />
</Frame>

## Track key information effortlessly by default

W\&B saves a new run for each experiment. Here's the information that gets saved by default:

* **Hyperparameters**: Settings for your model are saved in Config
* **Model Metrics**: Time series data of metrics streaming in are saved in Log
* **Terminal Logs**: Command line outputs are saved and available in a tab
* **System Metrics**: GPU and CPU utilization, memory, temperature etc.

## Learn more

* [Video walkthroughs on YouTube](http://wandb.me/youtube)
