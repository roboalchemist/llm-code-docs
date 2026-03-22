# Source: https://docs.wandb.ai/models/ref/python/public-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Public API overview

> Use the W&B Public API to programmatically access and manage W&B data

The W\&B Public API provides programmatic access to query, export, and update data stored in W\&B. Use this API for post-hoc analysis, data export, and programmatic management of runs, artifacts, and sweeps. While the main SDK handles real-time logging during training, the Public API enables you to retrieve historical data, update metadata, manage artifacts, and perform analysis on completed experiments. The main `Api` class serves as the entry point to most functionality.

> Training and fine-tuning models is done elsewhere in [the W\&B Python SDK](/models/ref/python). Use the Public API for querying and managing data *after* it has been logged to W\&B.

## Available components

| Component                                             | Description                                                                                        |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [`Api`](/models/ref/python/public-api/api/)           | Main entry point for the Public API. Query runs, projects, and artifacts across your organization. |
| [`Runs`](/models/ref/python/public-api/runs/)         | Access and manage individual training runs, including history, logs, and metrics.                  |
| [`Artifacts`](/models/artifacts/)                     | Query and download model artifacts, datasets, and other versioned files.                           |
| [`Sweeps`](/models/sweeps/)                           | Access hyperparameter sweep data and analyze optimization results.                                 |
| [`Projects`](/models/ref/python/public-api/projects/) | Manage projects and access project-level metadata and settings.                                    |
| [`Reports`](/models/reports/create-a-report/)         | Programmatically access and manage W\&B Reports.                                                   |
| [`Team`](/models/ref/python/public-api/team)          | Query team information and manage team-level resources.                                            |
| [`User`](/models/ref/python/public-api/user)          | Access user profiles and user-specific data.                                                       |
| [`Files`](/models/ref/python/public-api/files/)       | Download and manage files associated with runs.                                                    |
| `History`                                             | Access detailed time-series metrics logged during training (see Run.history).                      |
| [`Automations`](./automations/)                       | Manage automated workflows and actions.                                                            |
| [`Integrations`](/models/integrations)                | Configure and manage third-party integrations.                                                     |

## Common use cases

### Data export and analysis

* Export run history as DataFrames for analysis in Jupyter notebooks
* Download metrics for custom visualization or reporting
* Aggregate results across multiple experiments

### Post-Hoc Updates

* Update run metadata after completion
* Add tags or notes to completed experiments
* Modify run configurations or summaries

### Artifact Management

* Query artifacts by version or alias
* Download model checkpoints programmatically
* Track artifact lineage and dependencies

### Sweep Analysis

* Access sweep results and best performing runs
* Export hyperparameter search results
* Analyze parameter importance

## Authentication

The Public API uses the same authentication mechanism as the Python SDK. You can authenticate in several ways:

Use the `WANDB_API_KEY` environment variable to set your API key:

```bash  theme={null}
export WANDB_API_KEY=your_api_key
```

Pass the API key directly when initializing the `Api` class:

```python  theme={null}
api = Api(api_key="your_api_key")
```

Or use `wandb.login()` to authenticate the current session:

```python  theme={null}
import wandb

wandb.login()
api = Api()
```

## Example usage

### Download an Artifact by name and alias

The following example shows how to retrieve an artifact logged to W\&B by its name and alias, and then download its contents.

```python  theme={null}
import wandb

api = wandb.Api()
artifact = api.artifact("entity/project/artifact:alias")
artifact.download()
```

### Download an Artifact from a registry

The following example shows how to retrieve a linked artifact from a W\&B Registry

```python  theme={null}
import wandb

REGISTRY = "<registry_name>"
COLLECTION = "<collection_name>"
VERSION = "<version>"

api = wandb.Api()
artifact_name = f"wandb-registry-{REGISTRY}/{COLLECTION}:{VERSION}"

# Fetch the artifact
fetched_artifact = api.artifact(name = artifact_name)

# Download artifact. Returns path to downloaded contents
downloaded_path = fetched_artifact.download()
```

### Query W\&B Registry

Use Mongo-like filters to query W\&B Registries, Collections, and Artifacts. The following example demonstrates how to filter collections by name using a regular expression.

```python  theme={null}
import wandb

# Initialize wandb API
api = wandb.Api()

# Filter all collections, independent of registry, that 
# contains the string `yolo` in the collection name
collection_filters = {
    "name": {"$regex": "yolo"}
}

# Returns an iterable of all collections that match the filters
collections = api.registries().collections(filter=collection_filters)
```

For more information on how to query a registry, collection, or artifact, see the [Find registry items](/models/registry/search_registry).
