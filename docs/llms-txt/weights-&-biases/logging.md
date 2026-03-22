# Source: https://docs.wandb.ai/models/ref/sdk-coding-cheat-sheet/logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Logging

> Log metrics, hyperparameters, tables, and custom data to W&B.

Log metrics, hyperparameters, tables, and custom data to W\&B.

## Log a custom summary metric

```python  theme={null}
"""
Log a custom summary metric to W&B.
"""
import wandb
import random 

with wandb.init(project="<project>") as run:
    # Log a custom summary metric with a random integer value between 1 and 10
    run.summary["<metric_name>"] = random.randint(1, 10)
```

## Download and log an existing artifact from a registry collection

```python  theme={null}
"""
Download and log an existing artifact from a W&B registry collection.
Replace the placeholders with actual registry, collection names, entity,
project, and version.
"""
import wandb

# Construct the full artifact name with version
registry_name = "<registry_name>"  # Specify the registry name
collection_name = "<collection_name>" # Specify the collection name
version = 0 # Specify the version of the artifact to use
artifact_name_registry = f"wandb-registry-{registry_name}/{collection_name}:v{version}"

# Initialize a W&B run in the different team and project
with wandb.init(entity="<entity>", project="<project>") as run:
    # Use the model artifact from the registry
    registry_model = run.use_artifact(artifact_or_name=artifact_name_registry)

    # Download the model to a local directory
    local_model_path = registry_model.download()
```

## Initialize a run and log hyperparameters

```python  theme={null}
"""Initializes a W&B run and logs hyperparameters."""
import wandb

config = {
    "learning_rate": 0.01,
    "batch_size": 32,
    "optimizer": "adam",
}

with wandb.init(project="<project>", config=config) as run:
    # Training and logging code goes here
    pass
```

## Initialize a run and log a metric

```python  theme={null}
"""Initializes a W&B run and logs a metric."""
import wandb

with wandb.init(project="<project>") as run:
    # Training and logging code goes here

    # Example of logging a metric
    run.log({"accuracy": 0.95})
```

## Log a table

```python  theme={null}
"""
Log a table to W&B.
"""
import wandb

# Create a table object with two columns and two rows of data
my_table = wandb.Table(
    columns=["a", "b"],
    data=[["a1", "b1"], ["a2", "b2"]],
    log_mode="<log_mode>"
    )

# Start a new run
with wandb.init(project="<project>") as run:
    # Log the table to W&B
    run.log({"<table_name>": my_table})
```
