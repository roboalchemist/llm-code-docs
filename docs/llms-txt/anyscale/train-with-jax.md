# Source: https://docs.anyscale.com/tutorials/train-with-jax.md

# Train a model with Jax on GPUs

[View Markdown](/tutorials/train-with-jax.md)

# Train a model with Jax on GPUs

This example uses Jax to train a small model on 16 T4 GPUs.

## Install the Anyscale CLI[​](#install-the-anyscale-cli "Direct link to Install the Anyscale CLI")

```
pip install -U anyscale
anyscale login
```

## Submit the job[​](#submit-the-job "Direct link to Submit the job")

Clone this repository

Clone the example from GitHub.

```
git clone https://github.com/anyscale/examples.git
cd examples/jax_training
```

Submit the job with

```
anyscale job submit -f job.yaml
```

## Understanding the example[​](#understanding-the-example "Direct link to Understanding the example")

* This example installs a nightly version of Ray in the [Dockerfile](https://github.com/anyscale/examples/blob/main/jax_training/Dockerfile) because Ray Train GPU support for Jax is very recent.
