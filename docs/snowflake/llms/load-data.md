# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/load-data.md

# Load and write data

Use Snowflake ML to efficiently load data from Snowflake tables and stages into your machine learning workflows. Snowflake ML provides optimized data loading capabilities that take advantage of Snowflake’s distributed processing to accelerate data ingestion for your training and inference workflows.

You can load and process data using:

* **Snowflake Notebooks**: Interactive development environment for exploring data and building ML models. For more information, see [Notebooks on Container Runtime](notebooks-on-spcs.md).
* **Snowflake ML Jobs**: Run your ML workloads asynchronously from any development environment. For more information, see [Snowflake ML Jobs](ml-jobs/overview.md).

Both Notebooks and ML Jobs run on the Container Runtime, which provides preconfigured environments optimized for machine learning workloads with distributed processing capabilities. The Container Runtime uses Ray, an open-source framework for distributed computing, to efficiently process data across multiple compute nodes. For more information about the Container Runtime, see [Snowflake Container Runtime](container-runtime-ml.md).

Snowflake ML provides different APIs for loading structured and unstructured data:

**Structured data (tables and datasets)**

* **DataConnector**: Load data from Snowflake tables and Snowflake Datasets. For more information, see Load structured data from Snowflake tables.
* **DataSink**: Write data back to Snowflake tables. For more information, see Write structured data back to Snowflake tables.

**Unstructured data (files in stages)**

* **DataSource APIs**: Load data from various file formats (CSV, Parquet, images, and more) from Snowflake stages. For more information, see Load unstructured data from Snowflake stages.

The following table can help you choose the right API for your use case:

Data Sources and APIs

| Data Type | Data Source | API for Loading | API for Writing |
| --- | --- | --- | --- |
| Structured | Snowflake Tables | DataConnector | DataSink |
| Structured | Snowflake Datasets | DataConnector | DataSink |
| Unstructured | CSV Files (Stage) | DataSource API | N/A |
| Unstructured | Parquet Files (Stage) | DataSource API | N/A |
| Unstructured | Other Staged Files | DataSource API | N/A |

## Load structured data from Snowflake tables

Use the Snowflake DataConnector to load structured data from Snowflake tables and Snowflake Datasets into a Snowflake Notebook or Snowflake ML Job. The DataConnector accelerates data loading by parallelizing the reads across multiple compute nodes.

The DataConnector works with either Snowpark DataFrames or Snowflake Datasets:

* **Snowpark DataFrames**: Provide direct access to the data in your Snowflake tables. Best used during development.
* **Snowflake Datasets**: Versioned schema-level objects. Best used for production workflows. For more information, see [Snowflake Datasets](dataset.md).

After parallelizing the reads, the DataConnector can convert the data into one of following data structures:

* pandas dataframe
* PyTorch dataset
* TensorFlow dataset

### Create a DataConnector

You can create a DataConnector from a Snowpark DataFrame or a Snowflake Dataset.

Use the following code to create a DataConnector from a Snowpark DataFrame:

```python
from snowflake.ml.data.data_connector import DataConnector
from snowflake.snowpark.context import get_active_session

session = get_active_session()

# Create DataConnector from a Snowflake table
data_connector = DataConnector.from_dataframe(session.table("example-table-name"))
```

Use the following code to create a DataConnector from a Snowflake Dataset:

```python
from snowflake.ml.data.data_connector import DataConnector

# Create DataConnector from a Snowflake Dataset
data_connector = DataConnector.from_dataset(snowflake_dataset)
```

### Convert DataConnector to other formats

After creating a DataConnector, you can convert it to different data structures for use with various ML frameworks.

pandas dataframePyTorch datasetTensorFlow dataset

You can convert a DataConnector to a pandas dataframe for use with scikit-learn and other pandas-compatible libraries.

The following example loads data from a Snowflake table into a pandas dataframe and trains an XGBoost classifier:

```python
from snowflake.ml.data.data_connector import DataConnector
from snowflake.snowpark.context import get_active_session
import xgboost as xgb

session = get_active_session()

# Specify training table location
table_name = "TRAINING_TABLE"

# Load table into DataConnector
data_connector = DataConnector.from_dataframe(session.table(table_name))

# Convert to pandas dataframe
pandas_df = data_connector.to_pandas()

# Prepare features and labels
label_column_name = 'TARGET'
X, y = pandas_df.drop(label_column_name, axis=1), pandas_df[label_column_name]

# Train classifier
clf = xgb.Classifier()
clf.fit(X, y)
```

You can convert a DataConnector to a PyTorch dataset for use with PyTorch models and data loaders.

The following example loads data from a Snowflake table into a PyTorch dataset:

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from snowflake.ml.data.data_connector import DataConnector

# Create DataConnector (see previous examples)
# data_connector = DataConnector.from_dataframe(...)

# Convert to PyTorch dataset
torch_dataset = data_connector.to_torch_dataset(batch_size=32)
dataloader = DataLoader(torch_dataset, batch_size=None)

label_col = 'TARGET'
feature_cols = ['FEATURE1', 'FEATURE2']

for batch_idx, batch in enumerate(dataloader):
    y = batch_data.pop(label_col).squeeze()
    X = torch.stack(
        [tensor.squeeze() for key, tensor in batch.items() if key in feature_cols]
    )
```

You can convert a DataConnector to a TensorFlow dataset for use with TensorFlow models. Data is loaded in a streaming fashion for maximum efficiency.

The following example converts a DataConnector to a TensorFlow dataset:

```python
from snowflake.ml.data.data_connector import DataConnector

# Create DataConnector (see previous examples)
# data_connector = DataConnector.from_dataframe(...)

# Convert to TensorFlow dataset
tf_ds = data_connector.to_tf_dataset(
    batch_size=4,
    shuffle=True,
    drop_last_batch=True
)

for batch in tf_ds:
    print(batch)
```

### Use with Snowflake’s distributed training APIs

For best performance, you can pass a DataConnector directly to Snowflake’s optimized distributed training APIs instead of converting to pandas, PyTorch, or TensorFlow datasets first.

The following example trains an XGBoost model using Snowflake’s distributed XGBoost estimator:

```python
from snowflake.ml.data.data_connector import DataConnector
from snowflake.ml.modeling.distributors.xgboost.xgboost_estimator import (
    XGBEstimator,
    XGBScalingConfig,
)
from snowflake.snowpark.context import get_active_session

session = get_active_session()

# Create DataConnector from a Snowpark dataframe
snowflake_df = session.table("TRAINING_TABLE")
data_connector = DataConnector.from_dataframe(snowflake_df)

# Create Snowflake XGBoost estimator
snowflake_est = XGBEstimator(
    n_estimators=1,
    objective="reg:squarederror",
    scaling_config=XGBScalingConfig(use_gpu=False),
)

# Train using the data connector
# When using a data connector, input_cols and label_col must be provided
fit_booster = snowflake_est.fit(
    data_connector,
    input_cols=NUMERICAL_COLS,
    label_col=LABEL_COL
)
```

### Use sharding with PyTorch distributor

You can use the ShardedDataConnector to shard your data across multiple nodes for distributed training with the Snowflake PyTorch distributor.

The following example trains a PyTorch model on the digits dataset using sharded data across multiple processes:

```python
from sklearn import datasets
from snowflake.ml.data.sharded_data_connector import ShardedDataConnector
from snowflake.ml.modeling.pytorch import (
    PyTorchTrainer,
    ScalingConfig,
    WorkerResourceConfig,
    getContext,
)
from torch import nn
from snowflake.snowpark.context import get_active_session

session = get_active_session()

# Create the Snowflake data from a Snowpark dataframe
digits = datasets.load_digits(as_frame=True).frame
digits_df = session.create_dataframe(digits)

# Create sharded data connector
sharded_data_connector = ShardedDataConnector.from_dataframe(digits_df)

# Define the PyTorch model
class DigitsModel(nn.Module):
    def __init__(self):
        super(DigitsModel, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(8 * 8, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

# Define training function that runs across multiple nodes or devices
# Each process receives a unique data shard
def train_func():
    import os
    import torch
    import torch.distributed as dist
    from torch.utils.data import DataLoader
    from torch import nn
    from torch.nn.parallel import DistributedDataParallel as DDP

    # Get context with data shards and model directory
    context = getContext()
    dataset_map = context.get_dataset_map()
    model_dir = context.get_model_dir()
    training_data = dataset_map["train"].get_shard().to_torch_dataset()
    train_dataloader = DataLoader(training_data, batch_size=batch_size, drop_last=True)

    dist.init_process_group()
    device = "cpu"
    label_col = '"target"'
    batch_size = 64

    model = DDP(DigitsModel())
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    # Training loop
    for epoch in range(5):
        for batch, batch_data in enumerate(train_dataloader):
            y = batch_data.pop(label_col).flatten().type(torch.LongTensor).to(device)
            X = torch.concat(
                [tensor.to(torch.float32) for tensor in batch_data.values()],
                dim=-1,
            ).to(device)
            pred = model(X)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch % 100 == 0:
                print(f"Epoch {epoch}, Batch {batch}, Loss: {loss.item()}")

    # Save the model
    if dist.get_rank() == 0:
        torch.save(model.state_dict(), os.path.join(model_dir, "digits_model.pth"))

# Create PyTorch trainer with scaling configuration
pytorch_trainer = PyTorchTrainer(
    train_func=train_func,
    scaling_config=ScalingConfig(
        num_nodes=1,
        num_workers_per_node=4,
        resource_requirements_per_worker=WorkerResourceConfig(num_cpus=1, num_gpus=0),
    ),
)

# Run distributed training
response = pytorch_trainer.run(
    dataset_map=dict(
        train=sharded_data_connector,
    )
)
```

## Load unstructured data from Snowflake stages

Use the Snowflake DataSource APIs to read unstructured data from Snowflake stages. Each file format has a corresponding datasource class that defines how to read the data.

The following shows the file formats and corresponding APIs that you use to load the data:

* **Binary files**: `SFStageBinaryFileDataSource`
* **Text files**: `SFStageTextDataSource`
* **CSV files**: `SFStageCSVDataSource`
* **Parquet files**: `SFStageParquetDataSource`
* **Image files**: `SFStageImageDataSource`

### Load and process data

When you create a Snowflake Datasource, you must provide the following:

* The name of the stage from which you’re reading the data
* The database that has the stage (defaults to current session)
* The schema that has the stage (defaults to current session)
* The pattern to the filter files being read from the datasource (optional)

The Data API or the Data Connector retrieves all files within the provided path that matches the file pattern.

After you define the Snowflake Datasource, you can load data into a Ray dataset. With the Ray dataset, you can do the following:

* Use the dataset with Ray APIs
* Pass the dataset to DataConnector
* Convert to pandas or PyTorch datasets if needed.

The following example does the following:

* Reads Parquet files from a Snowflake stage into a Ray dataset
* Converts the dataset to a DataConnector

```python
import ray
from snowflake.ml.ray.datasource.stage_parquet_file_datasource import SFStageParquetDataSource
from snowflake.ml.data.data_connector import DataConnector

data_source = SFStageParquetDataSource(
    stage_location="@stage/path/",
    database="DB_NAME", # optional
    schema="SCHEMA_NAME", # optional
    file_pattern='*.parquet', # optional
)

# Build Ray dataset from provided datasources
ray_ds = ray.data.read_datasource(data_source)

dc = DataConnector.from_ray_dataset(ray_ds)
```

## Write structured data back to Snowflake tables

Use the Snowflake DataSink API to write structured data from your Notebook or ML Job back to a Snowflake table. You can write transformed or prediction datasets to Snowflake for further analysis or storage.

To define a data sink, provide the following:

* Stage name
* Database name (defaults to current session)
* Schema name (defaults to current session)
* File pattern to match specific files (optional)

The following example defines a data sink:

```python
from snowflake.ml.ray.datasink import SnowflakeTableDatasink
datasink = SnowflakeTableDatasink(
    table_name="table_name",
    database="db_name",
    schema="schema_name",
    auto_create_table=True, # create table if not exists
    override=True # replace vs insert to table
)
```

After you define a data sink, you can use the following code to write the Ray dataset to a Snowflake table.

```python
import ray

# Get Ray dataset from sources
ray_ds = ray.data.read_datasource(data_source)

# Setup transform operations, not executed yet
transformed_ds = ray_ds.map_batches(example_transform_batch_function)

# Start writing to Snowflake distributedly
transformed_ds.write_datasink(datasink)
```

## Best Practices and Considerations

For optimal performance and resource utilization, consider the following best practices:

**Parallelism**: Design your data source implementations to leverage Ray’s distributed nature. Customize the parallelism and concurrency arguments to better suit your use case. You can manually define how many resources you’re allocating per task in each step.

**Partitioning**: By default, Ray’s internal logic will partition the dataset based on resources and data size. You can customize number of partitions to choose between large number of small tasks vs small number of big tasks based on use case with `ray_ds.repartition(X)`.

**Best practices**: Follow [Ray Data User Guide](https://docs.ray.io/en/latest/data/user-guide.html) for additional guidance.

**Ray API details**:

* [Ray Datasource](https://docs.ray.io/en/latest/data/api/doc/ray.data.read_datasource.html)
* [Ray Map Batches (batch transformation)](https://docs.ray.io/en/latest/data/api/doc/ray.data.Dataset.map_batches.html)

## Next steps

After loading your data, you can:

* [Transform and engineer features](transform-data.md)
* [Train models](modeling.md)
* [Use the Feature Store](feature-store/overview.md) for feature management
