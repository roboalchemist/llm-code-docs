# Source: https://docs.fiddler.ai/api/fiddler-evals-sdk/entities/dataset.md

# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/dataset.md

# Dataset

Represents a dataset containing data published to a Fiddler model.

A Dataset is a collection of data records that have been published to a specific model in the Fiddler platform. Datasets are automatically created when data is published using Model.publish() and serve as the foundation for monitoring, drift detection, and baseline creation.

Key Features:

* **Data Collection**: Organized storage of model input/output data
* **Environment Separation**: Distinct handling of production vs. pre-production data
* **Baseline Source**: Reference data for drift detection and monitoring
* **Analysis Support**: Data download and statistical analysis capabilities
* **Model Integration**: Tight coupling with specific models for context

Dataset Characteristics:

* **Automatic Creation**: Created by Model.publish() operations
* **Model-Scoped**: Each dataset belongs to exactly one model
* **Named Collections**: Unique names within a model for identification
* **Row Tracking**: Automatic counting of data records
* **Environment Typed**: Classified as production or pre-production data

## Example

```python
# Retrieve a specific dataset
dataset = Dataset.from_name(
    name="training_data_v1",
    model_id=model.id
)
print(f"Dataset: {dataset.name}")
print(f"Rows: {dataset.row_count}")
print(f"Model: {dataset.model_id}")

# List all datasets for a model
datasets = list(Dataset.list(model_id=model.id))
print(f"Found {len(datasets)} datasets")

# Find datasets by characteristics
large_datasets = [
    ds for ds in Dataset.list(model_id=model.id)
    if ds.row_count and ds.row_count > 10000
]
```

{% hint style="info" %}
Datasets cannot be created directly through the Dataset class. They are automatically created when data is published to models using Model.publish(). Use the Dataset class for retrieval, listing, and analysis operations.
{% endhint %}

Initialize a Dataset instance.

Creates a dataset object representing data published to a model. This constructor is typically used internally when deserializing API responses rather than for direct dataset creation.

## Parameters

| Parameter    | Type   | Required | Default | Description                                                                                           |
| ------------ | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------- |
| `name`       | `str`  | ✗        | `None`  | Dataset name, must be unique within the model. Should be descriptive of the data contents or purpose. |
| `model_id`   | \`str  | UUID\`   | ✗       | `None`                                                                                                |
| `project_id` | \`UUID | str\`    | ✗       | `None`                                                                                                |

## Example

```python
# Internal usage - typically not called directly
dataset = Dataset(
    name="training_baseline_v1",
    model_id="550e8400-e29b-41d4-a716-446655440000",
    project_id="660e8400-e29b-41d4-a716-446655440000"
)
```

{% hint style="info" %}
Datasets are typically retrieved using Dataset.get(), Dataset.from\_name(), or Dataset.list() rather than created directly. Direct creation is mainly used internally by the Fiddler client.
{% endhint %}

## *classmethod* get(id\_)

Retrieve a dataset by its unique identifier.

Fetches a dataset from the Fiddler platform using its UUID. This is the most direct way to retrieve a dataset when you know its ID.

## Parameters

| Parameter | Type   | Required | Default | Description |
| --------- | ------ | -------- | ------- | ----------- |
| `id_`     | \`UUID | str\`    | ✗       | `None`      |

## Returns

The dataset instance with all metadata and row count information.

**Return type:** `Dataset`

## Raises

* **NotFound** -- If no dataset exists with the specified ID.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get dataset by UUID
dataset = Dataset.get(id_="550e8400-e29b-41d4-a716-446655440000")
print(f"Retrieved dataset: {dataset.name}")
print(f"Rows: {dataset.row_count}")
print(f"Model: {dataset.model_id}")

# Use dataset for analysis
if dataset.row_count and dataset.row_count > 1000:

    print("Large dataset suitable for baseline creation")
```

{% hint style="info" %}
This method makes an API call to fetch the latest dataset state from the server. The returned dataset instance reflects the current state in Fiddler.
{% endhint %}

## *classmethod* from\_name(name, model\_id)

Retrieve a dataset by name within a specific model.

Finds and returns a dataset using its name and model context. Dataset names are unique within a model, making this a reliable lookup method when you know both the dataset name and model ID.

## Parameters

| Parameter  | Type   | Required | Default | Description                                                                                          |
| ---------- | ------ | -------- | ------- | ---------------------------------------------------------------------------------------------------- |
| `name`     | `str`  | ✗        | `None`  | The name of the dataset to retrieve. Dataset names are unique within a model and are case-sensitive. |
| `model_id` | \`UUID | str\`    | ✗       | `None`                                                                                               |

## Returns

The dataset instance matching the specified name and model.

**Return type:** `Dataset`

## Raises

* **NotFound** -- If no dataset exists with the specified name in the given model.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get dataset by name for a specific model
dataset = Dataset.from_name(
    name="training_baseline",
    model_id=model.id
)
print(f"Found dataset: {dataset.name}")
print(f"Rows: {dataset.row_count}")

# Get validation dataset
val_dataset = Dataset.from_name(
    name="validation_set_v2",
    model_id=model.id
)

# Use for baseline creation
baseline = Baseline.create_from_dataset(
    dataset_id=dataset.id,
    name="training_baseline"
)
```

{% hint style="info" %}
Dataset names are case-sensitive and must match exactly. This method is useful when you know the dataset name from configuration or when working with named datasets created during model training workflows.
{% endhint %}

## *classmethod* list(model\_id)

List all pre-production datasets for a specific model.

Retrieves all datasets that have been published to a model in the pre-production environment. These datasets are typically used for baselines, training data analysis, and validation purposes.

## Parameters

| Parameter  | Type   | Required | Default | Description |
| ---------- | ------ | -------- | ------- | ----------- |
| `model_id` | \`UUID | str\`    | ✗       | `None`      |

## Yields

`Dataset` -- Dataset instances for all pre-production datasets in the model.

## Raises

**ApiError** -- If there's an error communicating with the Fiddler API. **Return type:** *Iterator*\[[*Dataset*](#dataset)]

## Example

```python
# List all datasets for a model
for dataset in Dataset.list(model_id=model.id):

    print(f"Dataset: {dataset.name}")
    print(f"  Rows: {dataset.row_count}")
    print(f"  ID: {dataset.id}")

    # Convert to list for analysis
    datasets = list(Dataset.list(model_id=model.id))
    print(f"Found {len(datasets)} datasets")

    # Find datasets by characteristics
    large_datasets = [
        ds for ds in Dataset.list(model_id=model.id)
        if ds.row_count and ds.row_count > 10000
    ]
    print(f"Large datasets: {len(large_datasets)}")

    # Get dataset summary statistics
    total_rows = sum(
        ds.row_count or 0
        for ds in Dataset.list(model_id=model.id)
    )
    print(f"Total rows across all datasets: {total_rows}")
```

{% hint style="info" %}
This method returns an iterator for memory efficiency and only includes pre-production datasets. Production data is handled separately through the monitoring system. Convert to a list with list(Dataset.list(...)) if you need to iterate multiple times.
{% endhint %}
