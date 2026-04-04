# Source: https://docs.fiddler.ai/api/rest-api/rest-api/model.md

# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model.md

# Model

Represents a machine learning model in the Fiddler platform.

The Model class is the central entity for ML model monitoring and management. It encapsulates the model's schema, specification, and metadata, and provides methods for data publishing, artifact management, and monitoring operations.

Key Concepts:

* **Schema** ([`ModelSchema`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-schema)): Defines the structure and data types of model inputs/outputs
* **Spec** ([`ModelSpec`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-spec)): Defines how columns are used (features, targets, predictions, etc.)
* **Task** ([`ModelTask`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-task)): The ML task type (classification, regression, ranking, etc.)
* **Artifacts** (`ModelArtifact`): Deployable model code and dependencies
* **Surrogates** (`Surrogate`): Simplified models for fast explanations

Lifecycle:

1. Create model with schema/spec (from data or manual definition)
2. Upload model artifacts for serving (optional)
3. Publish baseline/training data for drift detection
4. Publish production data for monitoring
5. Set up alerts and monitoring rules

Common Use Cases:

* **Tabular Models**: Traditional ML models with structured data
* **Text Models**: NLP models with text inputs and embeddings
* **Mixed Models**: Models combining tabular and unstructured data
* **Ranking Models**: Recommendation and search ranking systems
* **LLM Models**: Large language model monitoring

## Example

```python
# Create model from DataFrame with automatic schema detection
import pandas as pd
df = pd.DataFrame({
    'age': [25, 35, 45],
    'income': [50000, 75000, 100000],
    'approved': [0, 1, 1]  # target
})

model = Model.from_data(
    source=df,
    name="credit_approval",
    project_id=project.id,
    task=ModelTask.BINARY_CLASSIFICATION,
    description="Credit approval model v1.0"
)
model.create()

# Publish production events
events = [
    {'age': 30, 'income': 60000, 'prediction': 0.8},
    {'age': 40, 'income': 80000, 'prediction': 0.9}
]
event_ids = model.publish(source=events)

# Get model info
print(f"Model: {model.name} (Task: {model.task})")
print(f"Columns: {len(model.schema.columns)}")
print(f"Features: {model.spec.inputs}")
```

Initialize a Model instance.

Creates a new Model object with the specified configuration. The model is not created on the Fiddler platform until .create() is called.

## Parameters

| Parameter         | Type                                                                                        | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`            | `str`                                                                                       | ✗        | `None`  | Model name, must be unique within the project version. Should be descriptive and follow naming conventions.                                                                                                                                                                                                                                                                                                        |
| `project_id`      | \`UUID                                                                                      | str\`    | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `schema`          | [`ModelSchema`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-schema) | ✗        | `None`  | [`ModelSchema`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-schema) defining column structure and data types. Can be created manually or generated from data.                                                                                                                                                                                                                              |
| `spec`            | [`ModelSpec`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-spec)     | ✗        | `None`  | [`ModelSpec`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-spec) defining how columns are used (inputs, outputs, targets). Specifies the model's interface and column roles.                                                                                                                                                                                                                |
| `version`         | \`str                                                                                       | None\`   | ✗       | `v1`                                                                                                                                                                                                                                                                                                                                                                                                               |
| `input_type`      | `str`                                                                                       | ✗        | `None`  | [`ModelInputType`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-input-type) - Type of input data the model processes.; `TABULAR`: Structured/tabular data (default); `TEXT`: Natural language text data; `MIXED`: Combination of structured and unstructured data                                                                                                                         |
| `task`            | `str`                                                                                       | ✗        | `None`  | [`ModelTask`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-task) - Machine learning task type.; `BINARY_CLASSIFICATION`: Binary classification (0/1, True/False); `MULTICLASS_CLASSIFICATION`: Multi-class classification; `REGRESSION`: Continuous value prediction; `RANKING`: Ranking/recommendation tasks; `LLM`: Large language model tasks; `NOT_SET`: Task not specified (default) |
| `task_params`     | \`ModelTaskParams                                                                           | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `description`     | \`str                                                                                       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `event_id_col`    | \`str                                                                                       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `event_ts_col`    | \`str                                                                                       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `event_ts_format` | \`str                                                                                       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |
| `xai_params`      | \`XaiParams                                                                                 | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                             |

## Example

```python
from fiddler.schemas import ModelSchema, ModelSpec, Column
from fiddler.constants import DataType, ModelTask

# Manual schema/spec creation
schema = ModelSchema(columns=[
    Column(name='age', data_type=DataType.INTEGER),
    Column(name='income', data_type=DataType.FLOAT),
    Column(name='prediction', data_type=DataType.FLOAT)
])

spec = ModelSpec(
    inputs=['age', 'income'],
    outputs=['prediction']
)

model = Model(
    name="manual_model",
    project_id="project-uuid",
    schema=schema,
    spec=spec,
    task=ModelTask.REGRESSION,
    description="Manually defined regression model"
)
```

{% hint style="info" %}
The model exists only locally until .create() is called. Use Model.from\_data() for automatic schema/spec generation from DataFrames or files.
{% endhint %}

## *classmethod* get(id\_)

Retrieve a model by its unique identifier.

Fetches a model from the Fiddler platform using its UUID. This is the most direct way to retrieve a model when you know its ID.

## Parameters

| Parameter | Type   | Required | Default | Description |
| --------- | ------ | -------- | ------- | ----------- |
| `id_`     | \`UUID | str\`    | ✗       | `None`      |

## Returns

The model instance with all its configuration and metadata.

**Return type:** [Model](#model)

## Raises

* **NotFound** -- If no model exists with the specified ID.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get model by UUID
model = Model.get(id_="550e8400-e29b-41d4-a716-446655440000")
print(f"Retrieved model: {model.name} (Task: {model.task})")

# Access model properties
print(f"Project ID: {model.project_id}")
print(f"Input columns: {model.spec.inputs}")
print(f"Created: {model.created_at}")
```

{% hint style="info" %}
This method makes an API call to fetch the latest model state from the server. The returned model instance reflects the current state in Fiddler.
{% endhint %}

## *classmethod* from\_name(name, project\_id, version=None, latest=False)

Retrieve a model by name within a project.

Finds and returns a model using its name and project context. This is useful when you know the model name but not its UUID. Supports version-specific retrieval and latest version lookup.

## Parameters

| Parameter    | Type   | Required | Default | Description                                                                                                                                                |
| ------------ | ------ | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`       | `str`  | ✗        | `None`  | The name of the model to retrieve. Model names are unique within a project but may have multiple versions.                                                 |
| `project_id` | \`UUID | str\`    | ✗       | `None`                                                                                                                                                     |
| `version`    | \`str  | None\`   | ✗       | `None`                                                                                                                                                     |
| `latest`     | `bool` | ✗        | `None`  | If True and version is None, retrieves the most recently created version. If False, retrieves the first (oldest) version. Ignored if version is specified. |

## Returns

The model instance matching the specified criteria.

**Return type:** [Model](#model)

## Raises

* **NotFound** -- If no model exists with the specified name/version in the project.
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Get specific version
model = Model.from_name(
    name="fraud_detector",
    project_id=project.id,
    version="v2.1"
)

# Get latest version
latest_model = Model.from_name(
    name="fraud_detector",
    project_id=project.id,
    latest=True
)

# Get first version (default behavior)
first_model = Model.from_name(
    name="fraud_detector",
    project_id=project.id
)

print(f"Model versions: {first_model.version} -> {latest_model.version}")
```

{% hint style="info" %}
When version is None and latest=False, returns the first version created. This provides consistent behavior for accessing the "original" model version.
{% endhint %}

## create()

Create the model on the Fiddler platform.

Persists this model instance to the Fiddler platform, making it available for monitoring, data publishing, and other operations. The model must have a valid schema, spec, and be associated with an existing project.

## Returns

This model instance, updated with server-assigned fields like : ID, creation timestamp, and other metadata.

**Return type:** [Model](#model)

## Raises

* **Conflict** -- If a model with the same name and version already exists in the project.
* **ValidationError** -- If the model configuration is invalid (e.g., invalid schema, spec, or task parameters).
* **ApiError** -- If there's an error communicating with the Fiddler API.

## Example

```python
# Create model from DataFrame
model = Model.from_data(
    source=training_df,
    name="churn_predictor",
    project_id=project.id,
    task=ModelTask.BINARY_CLASSIFICATION
)

# Create on platform
created_model = model.create()
print(f"Created model with ID: {created_model.id}")
print(f"Created at: {created_model.created_at}")

# Model is now available for monitoring
assert created_model.id is not None

# Can now publish data, set up alerts, etc.
job = created_model.publish(source=production_data)
```

{% hint style="info" %}
After successful creation, the model instance is updated in-place with server-assigned metadata. The same instance can be used for subsequent operations without needing to fetch it again.
{% endhint %}

## update()

Update an existing model.

**Return type:** None

## add\_column()

Add a new column to the model schema.

Updates both the schema and spec to include the new column. This allows you to extend your model with additional columns after initial creation.

**New in version 3.11.0**

## Parameters

| Parameter     | Type                                                                             | Required | Default    | Description                                                                  |
| ------------- | -------------------------------------------------------------------------------- | -------- | ---------- | ---------------------------------------------------------------------------- |
| `column`      | [`Column`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/column) | ✗        | `None`     | Column object defining the new column's properties (name, data\_type, etc.)  |
| `column_type` | `str`                                                                            | ✗        | `metadata` | Type of column in spec. One of: 'inputs', 'outputs', 'targets', 'decisions', |

## Raises

* **ValueError** -- If column already exists or column\_type is invalid
* **BadRequest** -- If column definition is invalid per backend validation **Return type:** None

## Example

```python
# Add a numeric metadata column
new_col = Column(
    name="customer_segment",
    data_type=DataType.INTEGER,
    min=1,
    max=5
)
model.add_column(column=new_col, column_type='metadata')

# Add a categorical feature
category_col = Column(
    name="region",
    data_type=DataType.CATEGORY,
    categories=["US", "EU", "APAC"]
)
model.add_column(column=category_col, column_type='inputs')
```

{% hint style="info" %}

* Adding a column doesn't populate historical data; new column will be null for past events
* Column names must be unique within the model
* After adding a column, include it in future event publishing
  {% endhint %}

## *classmethod* list(project\_id, name=None)

List models in a project with optional filtering.

Retrieves all models or model versions within a project. Returns lightweight ModelCompact objects that can be used to fetch full Model instances when needed.

## Parameters

| Parameter    | Type   | Required | Default | Description |
| ------------ | ------ | -------- | ------- | ----------- |
| `project_id` | \`UUID | str\`    | ✗       | `None`      |
| `name`       | \`str  | None\`   | ✗       | `None`      |

## Yields

*ModelCompact* --

Lightweight model objects containing id, name, and version. : Call .fetch() on any ModelCompact to get the full Model instance. **Return type:** *Iterator*\[*ModelCompact*]

## Example

```python
# List all models in project
for model_compact in Model.list(project_id=project.id):

    print(f"Model: {model_compact.name} v{model_compact.version}")
    print(f"  ID: {model_compact.id}")

    # List all versions of a specific model
    for version in Model.list(project_id=project.id, name="fraud_detector"):

        print(f"Version: {version.version}")

        # Get full model details if needed
        full_model = version.fetch()
        print(f"  Task: {full_model.task}")
        print(f"  Created: {full_model.created_at}")

        # Convert to list for counting
        models = list(Model.list(project_id=project.id))
        print(f"Total models in project: {len(models)}")
```

{% hint style="info" %}
This method returns an iterator for memory efficiency when dealing with many models. The ModelCompact objects are lightweight and don't include full schema/spec information - use .fetch() when you need complete details.
{% endhint %}

## duplicate()

Duplicate the model instance with the given version name.

This call will not save the model on server. After making changes to the model instance call .create() to add the model version to Fiddler Platform.

## Parameters

| Parameter | Type  | Required | Default | Description |
| --------- | ----- | -------- | ------- | ----------- |
| `version` | \`str | None\`   | ✗       | `None`      |

## Returns

Model instance

**Return type:** [*Model*](#model)

## *property* datasets *: Iterator\[Dataset]*

Get all datasets associated with this model.

Returns an iterator over all datasets that have been published to this model, including both production data and pre-production datasets used for baselines and drift comparison.

## Yields

[`Dataset`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/dataset) --

Dataset objects containing metadata and data access methods. : Each dataset represents a collection of events published to the model.

## Example

```python
# List all datasets for the model
for dataset in model.datasets:

    print(f"Dataset: {dataset.name}")
    print(f"  Environment: {dataset.environment}")
    print(f"  Size: {dataset.size} events")
    print(f"  Created: {dataset.created_at}")

    # Find specific dataset
    baseline_datasets = [
        ds for ds in model.datasets
        if ds.environment == EnvType.PRE_PRODUCTION
    ]
    print(f"Found {len(baseline_datasets)} baseline datasets")
```

{% hint style="info" %}
This includes both production event data and named pre-production datasets. Use the Dataset objects to download data, analyze distributions, or set up baseline comparisons for drift detection.
{% endhint %}

## *property* baselines *: Iterator\[Baseline]*

Get all baselines configured for this model.

Returns an iterator over all baseline configurations used for drift detection and performance monitoring. Baselines define reference distributions and metrics for comparison with production data.

## Yields

[`Baseline`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/baseline) --

Baseline objects containing configuration and reference data. : Each baseline defines how drift and performance should be measured against historical or reference datasets.

## Example

```python
# List all baselines
for baseline in model.baselines:

    print(f"Baseline: {baseline.name}")
    print(f"  Type: {baseline.type}")  # STATIC or ROLLING
    print(f"  Dataset: {baseline.dataset_name}")
    print(f"  Created: {baseline.created_at}")

    # Find production baseline
    prod_baselines = [
        bl for bl in model.baselines
        if "production" in bl.name.lower()
    ]

    # Use baseline for drift comparison
    if prod_baselines:

        baseline = prod_baselines[0]
        drift_metrics = baseline.compute_drift(recent_data)
```

{% hint style="info" %}
Baselines are essential for drift detection and alerting. They define the "normal" behavior against which production data is compared. Static baselines use fixed reference data, while rolling baselines update automatically with recent data.
{% endhint %}

## *property* deployment *: ModelDeployment*

Fetch model deployment instance of this model.

## Returns

The deployment configuration for this model.

**Return type:** [`ModelDeployment`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model-deployment)

## *classmethod* from\_data(source, name, project\_id, spec=None, version=None, input\_type=ModelInputType.TABULAR, task=ModelTask.NOT\_SET, task\_params=None, description=None, event\_id\_col=None, event\_ts\_col=None, event\_ts\_format=None, xai\_params=None, max\_cardinality=None, sample\_size=None)

Create a Model instance with automatic schema generation from data.

This is the most convenient way to create models when you have training data or representative samples. The method automatically analyzes the data to generate appropriate schema (column types) and spec (column roles) definitions.

## Parameters

| Parameter         | Type              | Required | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ----------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`          | \`DataFrame       | Path     | str\`   | ✗                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `name`            | `str`             | ✗        | `None`  | Model name, must be unique within the project version. Use descriptive names like "fraud\_detector\_v1" or "churn\_model".                                                                                                                                                                                                                                                                                        |
| `project_id`      | \`UUID            | str\`    | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `spec`            | \`ModelSpec       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `version`         | \`str             | None\`   | ✗       | `v1`                                                                                                                                                                                                                                                                                                                                                                                                              |
| `input_type`      | `str`             | ✗        | `None`  | [`ModelInputType`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-input-type) - Type of input data the model processes.; `TABULAR`: Structured/tabular data (default); `TEXT`: Natural language text data; `MIXED`: Combination of structured and unstructured data                                                                                                                        |
| `task`            | `str`             | ✗        | `None`  | [`ModelTask`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-task) - Machine learning task type: `BINARY_CLASSIFICATION`: Binary classification (0/1, True/False); `MULTICLASS_CLASSIFICATION`: Multi-class classification; `REGRESSION`: Continuous value prediction; `RANKING`: Ranking/recommendation tasks; `LLM`: Large language model tasks; `NOT_SET`: Task not specified (default) |
| `task_params`     | \`ModelTaskParams | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `description`     | \`str             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `event_id_col`    | \`str             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `event_ts_col`    | \`str             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `event_ts_format` | \`str             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `xai_params`      | \`XaiParams       | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `max_cardinality` | \`int             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `sample_size`     | \`int             | None\`   | ✗       | `None`                                                                                                                                                                                                                                                                                                                                                                                                            |

## Returns

A new Model instance with automatically generated schema and spec. : The model is not yet created on the platform - call .create() to persist.

**Return type:** `Model`

## Raises

* **ValueError** -- If the data source is invalid or cannot be processed.
* **FileNotFoundError** -- If source is a file path that doesn't exist.
* **ValidationError** -- If the generated schema/spec is invalid.

## Example

```python
import pandas as pd

# Create from DataFrame
df = pd.DataFrame({
    'age': [25, 35, 45, 55],
    'income': [30000, 50000, 70000, 90000],
    'credit_score': [650, 700, 750, 800],
    'approved': [0, 1, 1, 1],  # target
    'prediction': [0.2, 0.8, 0.9, 0.95],  # model output
    'prediction_score': [0.2, 0.8, 0.9, 0.95]  # alternative output
})

model = Model.from_data(
    source=df,
    name="credit_approval_v1",
    project_id=project.id,
    task=ModelTask.BINARY_CLASSIFICATION,
    description="Credit approval model trained on 2024 data",
    event_id_col="application_id",  # if present in real data
    event_ts_col="timestamp"        # if present in real data
)

# Review generated schema
print(f"Columns detected: {len(model.schema.columns)}")
for col in model.schema.columns:

    print(f"  {col.name}: {col.data_type}")

    # Review generated spec
    print(f"Inputs: {model.spec.inputs}")
    print(f"Outputs: {model.spec.outputs}")
    print(f"Targets: {model.spec.targets}")

    # Create on platform
    model.create()

    # Create from file
    model = Model.from_data(
        source="training_data.csv",
        name="file_based_model",
        project_id=project.id,
        task=ModelTask.REGRESSION,
        sample_size=10000  # Sample large files
    )
```

{% hint style="info" %}
The automatic schema generation uses heuristics to detect column types and roles. Review the generated schema and spec before calling .create() to ensure they match your model's actual interface. You can modify the schema and spec after creation if needed.
{% endhint %}

## delete()

Delete a model and it's associated resources.

## Returns

model deletion job instance

**Return type:** *Job*

## remove\_column()

Remove a column from the model schema and spec

This method is only to modify model object before creating and will not save the model on Fiddler Platform. After making changes to the model instance, call .create() to add the model to Fiddler Platform.

## Parameters

| Parameter     | Type   | Required | Default | Description                                               |
| ------------- | ------ | -------- | ------- | --------------------------------------------------------- |
| `column_name` | `str`  | ✗        | `None`  | Column name to be removed                                 |
| `missing_ok`  | `bool` | ✗        | `True`  | If True, do not raise an error if the column is not found |

## Returns

None

## Raises

**KeyError** -- If the column name is not found and missing\_ok is False

**Return type:** None

## publish()

Publish data to the model for monitoring and analysis.

Uploads prediction events, training data, or reference datasets to Fiddler for monitoring, drift detection, and performance analysis. This is how you send your model's real-world data to the platform.

## Parameters

| Parameter      | Type                                                                                  | Required | Default              | Description                                                                                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------- | -------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`       | \`list\[dict\[str, Any]] \| str                                                       | Path     | DataFrame\`          | ✗                                                                                                                                                                                                                                                                                                                             |
| `environment`  | [`EnvType`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/env-type) | ✗        | `EnvType.PRODUCTION` | [`EnvType`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/env-type) - Data environment type: **`PRODUCTION`**: Live production prediction data.; Used for real-time monitoring and alerting.; **`PRE_PRODUCTION`**: Training, validation, or baseline data. Used for drift comparison and model evaluation. |
| `dataset_name` | \`str                                                                                 | None\`   | ✗                    | `None`                                                                                                                                                                                                                                                                                                                        |
| `update`       | `bool`                                                                                | ✗        | `False`              | Whether these events update previously published data. Set to True when republishing corrected predictions or adding ground truth labels to existing events.                                                                                                                                                                  |

## Returns

Event IDs when source is list of dicts or DataFrame. : Use these IDs to reference specific events later.

* [`Job`](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/job): Async job object when source is a file path. Use job.wait() to wait for completion or check job.status.

**Return type:** - **list\[UUID]**

## Raises

* **ValidationError** -- If the data doesn't match the model's schema or contains invalid values.
* **ApiError** -- If there's an error uploading the data to Fiddler.
* **ValueError** -- If the source format is unsupported or parameters are incompatible (e.g., dataset\_name with PRODUCTION).

## Example

```python
# Publish production events from DataFrame
import pandas as pd
prod_df = pd.DataFrame({
    'age': [30, 25, 45],
    'income': [60000, 45000, 80000],
    'prediction': [0.8, 0.3, 0.9],
    'timestamp': ['2024-01-01 10:00:00', '2024-01-01 11:00:00', '2024-01-01 12:00:00']
})

# Returns list of event UUIDs
event_ids = model.publish(
    source=prod_df,
    environment=EnvType.PRODUCTION
)
print(f"Published {len(event_ids)} events")

# Publish baseline data for drift comparison
baseline_df = pd.read_csv("training_data.csv")
job = model.publish(
    source="training_data.csv",  # File path
    environment=EnvType.PRE_PRODUCTION,
    dataset_name="training_baseline_2024"
)
job.wait()  # Wait for upload to complete
print(f"Baseline upload status: {job.status}")

# Publish real-time streaming events
events = [
    {
        'age': 35,
        'income': 70000,
        'prediction': 0.75,
        'event_id': 'pred_001',
        'timestamp': '2024-01-01 13:00:00'
    },
    {
        'age': 28,
        'income': 55000,
        'prediction': 0.45,
        'event_id': 'pred_002',
        'timestamp': '2024-01-01 13:01:00'
    }
]
event_ids = model.publish(source=events)
print(f"Published {len(events)} streaming events")

# Update existing events with ground truth
corrected_events = [
    {
        'event_id': 'pred_001',
        'ground_truth': 1,  # Actual outcome
        'timestamp': '2024-01-01 13:00:00'
    }
]
model.publish(source=corrected_events, update=True)
```

{% hint style="warning" %}

* **Schema Validation**: All published data must match the model's schema. Column names, types, and value ranges are validated.
* **Event IDs**: Include event\_id\_col if specified in model config for event tracking and updates.
* **Timestamps**: Include event\_ts\_col for time-based analysis and drift detection.
* **Batch Limits**: List of dicts is limited to 1000 events per call. Use files or multiple calls for larger datasets.

{% hint style="info" %}
Production data publishing enables real-time monitoring, alerting, and drift detection. Pre-production data creates reference datasets for comparison and model evaluation.
{% endhint %}
{% endhint %}

## add\_artifact()

Upload and deploy model artifact.

## Parameters

| Parameter           | Type               | Required | Default | Description |
| ------------------- | ------------------ | -------- | ------- | ----------- |
| `model_dir`         | \`str              | Path\`   | ✗       | `None`      |
| `deployment_params` | \`DeploymentParams | None\`   | ✗       | `None`      |

## Returns

Async job instance

**Return type:** *Job*

## update\_artifact()

Update existing model artifact.

## Parameters

| Parameter           | Type               | Required | Default | Description |
| ------------------- | ------------------ | -------- | ------- | ----------- |
| `model_dir`         | \`str              | Path\`   | ✗       | `None`      |
| `deployment_params` | \`DeploymentParams | None\`   | ✗       | `None`      |

## Returns

Async job instance

**Return type:** *Job*

## download\_artifact()

Download existing model artifact.

## Parameters

| Parameter    | Type  | Required | Default | Description |
| ------------ | ----- | -------- | ------- | ----------- |
| `output_dir` | \`str | Path\`   | ✗       | `None`      |

## add\_surrogate()

Add a new surrogate model

## Parameters

| Parameter           | Type               | Required | Default | Description |
| ------------------- | ------------------ | -------- | ------- | ----------- |
| `dataset_id`        | \`UUID             | str\`    | ✗       | `None`      |
| `deployment_params` | \`DeploymentParams | None\`   | ✗       | `None`      |

## Returns

Async job

**Return type:** *Job*

## update\_surrogate()

Update an existing surrogate model

## Parameters

| Parameter           | Type               | Required | Default | Description |
| ------------------- | ------------------ | -------- | ------- | ----------- |
| `dataset_id`        | \`UUID             | str\`    | ✗       | `None`      |
| `deployment_params` | \`DeploymentParams | None\`   | ✗       | `None`      |

## Returns

Async job

**Return type:** *Job*
