# Source: https://docs.wandb.ai/models/track/config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Use a dictionary-like object to save your experiment configuration

# Configure experiments

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/wandb-log/Configs_in_W%26B.ipynb" />

Use the `config` property of a run to save your training configuration:

* hyperparameter
* input settings such as the dataset name or model type
* any other independent variables for your experiments.

The `wandb.Run.config` property makes it easy to analyze your experiments and reproduce your work in the future. You can group by configuration values in the W\&B App, compare the configurations of different W\&B runs, and evaluate how each training configuration affects the output. The `config` property is a dictionary-like object that can be composed from multiple dictionary-like objects.

<Note>
  To save output metrics or dependent variables like loss and accuracy, use `wandb.Run.log()` instead of `wandb.Run.config`.
</Note>

## Set up an experiment configuration

Configurations are typically defined in the beginning of a training script. Machine learning workflows may vary, however, so you are not required to define a configuration at the beginning of your training script.

Use dashes (`-`) or underscores (`_`) instead of periods (`.`) in your config variable names.

Use the dictionary access syntax `["key"]["value"]` instead of the attribute access syntax `config.key.value` if your script accesses `wandb.Run.config` keys below the root.

The following sections outline different common scenarios of how to define your experiments configuration.

### Set the configuration at initialization

Pass a dictionary at the beginning of your script when you call the `wandb.init()` API to generate a background process to sync and log data as a W\&B Run.

The following code snippet demonstrates how to define a Python dictionary with configuration values and how to pass that dictionary as an argument when you initialize a W\&B Run.

```python  theme={null}
import wandb

# Define a config dictionary object
config = {
    "hidden_layer_sizes": [32, 64],
    "kernel_sizes": [3],
    "activation": "ReLU",
    "pool_sizes": [2],
    "dropout": 0.5,
    "num_classes": 10,
}

# Pass the config dictionary when you initialize W&B
with wandb.init(project="config_example", config=config) as run:
    ...
```

If you pass a nested dictionary as the `config`, W\&B flattens the names using dots.

Access the values from the dictionary similarly to how you access other dictionaries in Python:

```python  theme={null}
# Access values with the key as the index value
hidden_layer_sizes = run.config["hidden_layer_sizes"]
kernel_sizes = run.config["kernel_sizes"]
activation = run.config["activation"]

# Python dictionary get() method
hidden_layer_sizes = run.config.get("hidden_layer_sizes")
kernel_sizes = run.config.get("kernel_sizes")
activation = run.config.get("activation")
```

<Note>
  Throughout the Developer Guide and examples we copy the configuration values into separate variables. This step is optional. It is done for readability.
</Note>

### Set the configuration with argparse

You can set your configuration with an argparse object. [argparse](https://docs.python.org/3/library/argparse.html), short for argument parser, is a standard library module in Python 3.2 and above that makes it easy to write scripts that take advantage of all the flexibility and power of command line arguments.

This is useful for tracking results from scripts that are launched from the command line.

The proceeding Python script demonstrates how to define a parser object to define and set your experiment config. The functions `train_one_epoch` and `evaluate_one_epoch` are provided to simulate a training loop for the purpose of this demonstration:

```python  theme={null}
# config_experiment.py
import argparse
import random

import numpy as np
import wandb


# Training and evaluation demo code
def train_one_epoch(epoch, lr, bs):
    acc = 0.25 + ((epoch / 30) + (random.random() / 10))
    loss = 0.2 + (1 - ((epoch - 1) / 10 + random.random() / 5))
    return acc, loss


def evaluate_one_epoch(epoch):
    acc = 0.1 + ((epoch / 20) + (random.random() / 10))
    loss = 0.25 + (1 - ((epoch - 1) / 10 + random.random() / 6))
    return acc, loss


def main(args):
    # Start a W&B Run
    with wandb.init(project="config_example", config=args) as run:
        # Access values from config dictionary and store them
        # into variables for readability
        lr = run.config["learning_rate"]
        bs = run.config["batch_size"]
        epochs = run.config["epochs"]

        # Simulate training and logging values to W&B
        for epoch in np.arange(1, epochs):
            train_acc, train_loss = train_one_epoch(epoch, lr, bs)
            val_acc, val_loss = evaluate_one_epoch(epoch)

            run.log(
                {
                    "epoch": epoch,
                    "train_acc": train_acc,
                    "train_loss": train_loss,
                    "val_acc": val_acc,
                    "val_loss": val_loss,
                }
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-b", "--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument(
        "-e", "--epochs", type=int, default=50, help="Number of training epochs"
    )
    parser.add_argument(
        "-lr", "--learning_rate", type=int, default=0.001, help="Learning rate"
    )

    args = parser.parse_args()
    main(args)
```

### Set the configuration throughout your script

You can add more parameters to your config object throughout your script. The following code snippet demonstrates how to add new key-value pairs to your config object:

```python  theme={null}
import wandb

# Define a config dictionary object
config = {
    "hidden_layer_sizes": [32, 64],
    "kernel_sizes": [3],
    "activation": "ReLU",
    "pool_sizes": [2],
    "dropout": 0.5,
    "num_classes": 10,
}

# Pass the config dictionary when you initialize W&B
with wandb.init(project="config_example", config=config) as run:
    # Update config after you initialize W&B
    run.config["dropout"] = 0.2
    run.config.epochs = 4
    run.config["batch_size"] = 32
```

You can update multiple values at a time:

```python  theme={null}
run.config.update({"lr": 0.1, "channels": 16})
```

### Set the configuration after your Run has finished

Use the [W\&B Public API](/models/ref/python/public-api/) to update a completed run's config.

You must provide the API with your entity, project name and the run's ID. You can find these details in the Run object or in the [W\&B App](/models/track/workspaces/):

```python  theme={null}
with wandb.init() as run:
    ...

# Find the following values from the Run object if it was initiated from the
# current script or notebook, or you can copy them from the W&B App UI.
username = run.entity
project = run.project
run_id = run.id

# Note that api.run() returns a different type of object than wandb.init().
api = wandb.Api()
api_run = api.run(f"{username}/{project}/{run_id}")
api_run.config["bar"] = 32
api_run.update()
```

## `absl.FLAGS`

You can also pass in [`absl` flags](https://abseil.io/docs/python/guides/flags).

```python  theme={null}
flags.DEFINE_string("model", None, "model to run")  # name, default, help

run.config.update(flags.FLAGS)  # adds absl flags to config
```

## File-Based Configs

If you place a file named `config-defaults.yaml` in the same directory as your run script, the run automatically picks up the key-value pairs defined in the file and passes them to `wandb.Run.config`.

The following code snippet shows a sample `config-defaults.yaml` YAML file:

```yaml  theme={null}
batch_size:
  desc: Size of each mini-batch
  value: 32
```

You can override the default values automatically loaded from `config-defaults.yaml` by setting updated values in the `config` argument of `wandb.init`. For example:

```python  theme={null}
import wandb

# Override config-defaults.yaml by passing custom values
with wandb.init(config={"epochs": 200, "batch_size": 64}) as run:
    ...
```

To load a configuration file other than `config-defaults.yaml`, use the `--configs command-line` argument and specify the path to the file:

```bash  theme={null}
python train.py --configs other-config.yaml
```

### Example use case for file-based configs

Suppose you have a YAML file with some metadata for the run, and then a dictionary of hyperparameters in your Python script. You can save both in the nested `config` object:

```python  theme={null}
hyperparameter_defaults = dict(
    dropout=0.5,
    batch_size=100,
    learning_rate=0.001,
)

config_dictionary = dict(
    yaml=my_yaml_file,
    params=hyperparameter_defaults,
)

with wandb.init(config=config_dictionary) as run:
    ...
```

## TensorFlow v1 flags

You can pass TensorFlow flags into the `wandb.Run.config` object directly.

```python  theme={null}
with wandb.init() as run:
    run.config.epochs = 4

    flags = tf.app.flags
    flags.DEFINE_string("data_dir", "/tmp/data")
    flags.DEFINE_integer("batch_size", 128, "Batch size.")
    run.config.update(flags.FLAGS)  # add tensorflow flags as config
```
