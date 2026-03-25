# Source: https://docs.mage.ai/integrations/databases/Iceberg.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Iceberg

> Connect to Apache Iceberg tables stored in Amazon S3 using various catalog types

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="iceberg" />

## Add credentials

To access **Apache Iceberg tables stored in Amazon S3**, you'll need to configure your AWS credentials.

1. Create a new pipeline or open an existing pipeline.
2. Expand the left side of your screen to view the file browser.
3. Scroll down and click on a file named `io_config.yaml`.
4. Enter the following keys and values under the key named `default` (or the profile you are using):

   ```yaml  theme={"system"}
   version: 0.1.1
   default:
     AWS_ACCESS_KEY_ID: ...
     AWS_SECRET_ACCESS_KEY: ...
     AWS_REGION: us-west-2  # or the region where your S3 bucket is located
   ```

   > These credentials must have read/write access to the S3 bucket that contains your Iceberg tables.

## Using Python block

You can use Mage to load data from Iceberg tables stored in S3 or export data to Iceberg tables using a configurable Python block.

### Steps

1. **Create or open a pipeline** in your Mage Pro cluster.
2. **Add a block** of type **Data Loader** or **Data Exporter**.
3. From the block template list, choose:\
   **Data lakes → Apache Iceberg**
4. In the generated code block, update the following configuration parameters:
   * `base_uri`: Base S3 URI for the Iceberg warehouse (e.g., `s3://your-bucket-name/warehouse/`) - required for SQL catalog
   * `namespace`: Namespace for the Iceberg catalog (default: `'default'`)
   * `catalog_type`: Type of catalog to use - `'sql'` (default) or `'glue'`
   * `table_name`: Name of the Iceberg table
   * `bucket_name`: Name of your S3 bucket (for exports)
   * `mode`: Write mode for exports - `'append'` (default) or `'overwrite'`
   * `metadata_file`: Optional - used to directly access S3 metadata file when table is not in catalog
5. If you're using a non-default profile, update the `config_profile` field accordingly.
6. **Run the block** to load or export data from your Iceberg table stored on S3.

### Configuration Options

#### Catalog Types

Mage supports multiple catalog types for Iceberg, including:

* **SQL Catalog (default)**: Uses a Postgres-backed catalog to store table metadata
  * Requires `base_uri` to specify the warehouse location
  * Tables can be registered in the catalog or accessed directly via metadata files

* **AWS Glue Catalog**: Uses AWS Glue as the catalog
  * No `base_uri` required
  * Tables must be registered in AWS Glue

Additional catalog types are also supported. Set `catalog_type` to the appropriate value for your catalog implementation.

#### Loading Data

When loading data, you can:

* Load from catalog: If the table is registered in the catalog, just provide `table_name`
* Load from metadata file: If the table is not in the catalog, provide `metadata_file` to access the S3 metadata file directly
  * The metadata file path will be: `{base_uri}{table_name}/metadata/{metadata_file}`

Additional kwargs (e.g., `row_filter`, `selected_fields`, `case_sensitive`, `snapshot_id`) can be passed into the `load()` method to customize the data retrieval. These parameters are passed through to pyiceberg's scan method.

#### Scan Parameters

The following parameters can be passed to the `load()` method to customize data retrieval. These parameters are passed through to pyiceberg's `scan()` method. For the complete method signature, see the [pyiceberg source code](https://github.com/apache/iceberg-python/blob/main/pyiceberg/table/__init__.py#L1133-L1135).

| Parameter         | Type                         | Default        | Description                                                                                                   | Example                                |
| ----------------- | ---------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `row_filter`      | `str` or `BooleanExpression` | `AlwaysTrue()` | A string or BooleanExpression that describes the desired rows                                                 | `'id > 100'` or `'status == "active"'` |
| `selected_fields` | `tuple[str]`                 | `("*",)`       | A tuple of strings representing the column names to return in the output dataframe                            | `('id', 'name', 'created_at')`         |
| `case_sensitive`  | `bool`                       | `True`         | If `True`, column matching is case sensitive                                                                  | `True`                                 |
| `snapshot_id`     | `int` or `None`              | `None`         | Optional Snapshot ID to time travel to. If `None`, scans the table as of the current snapshot ID              | `12345`                                |
| `limit`           | `int` or `None`              | `None`         | An integer representing the number of rows to return in the scan result. If `None`, fetches all matching rows | `1000`                                 |

#### Exporting Data

When exporting data, you can:

* **Append mode** (default): Adds new data to the existing table
* **Overwrite mode**: Replaces all data in the table with the new data

### Example: Loading Data

<CodeGroup>
  ```python SQL Catalog theme={"system"}
  from mage_ai.io.iceberg_s3 import Iceberg
  from mage_ai.io.config import ConfigFileLoader

  # Using SQL catalog
  iceberg = Iceberg.with_config(
      ConfigFileLoader(config_path, config_profile),
      base_uri='s3://my-bucket/warehouse/',
      namespace='analytics',
      catalog_type='sql',
  )

  # Load from catalog
  df = iceberg.load('my_table')

  # Or load from metadata file (if not in catalog)
  df = iceberg.load('my_table', metadata_file='00000-abc123.metadata.json')
  ```

  ```python AWS Glue Catalog theme={"system"}
  from mage_ai.io.iceberg_s3 import Iceberg
  from mage_ai.io.config import ConfigFileLoader

  # Using AWS Glue catalog
  iceberg = Iceberg.with_config(
      ConfigFileLoader(config_path, config_profile),
      namespace='analytics',
      catalog_type='glue',
  )

  df = iceberg.load('my_table')
  ```

  ```python With Scan Parameters theme={"system"}
  from mage_ai.io.iceberg_s3 import Iceberg
  from mage_ai.io.config import ConfigFileLoader

  iceberg = Iceberg.with_config(
      ConfigFileLoader(config_path, config_profile),
      base_uri='s3://my-bucket/warehouse/',
      namespace='analytics',
      catalog_type='sql',
  )

  # Loading with additional scan parameters
  df = iceberg.load(
      'my_table',
      row_filter='id > 100',  # Filter rows
      selected_fields=['id', 'name', 'created_at'],  # Select specific fields
      case_sensitive=True,  # Case-sensitive field matching
      snapshot_id=12345,  # Read from specific snapshot
      limit=1000,  # Limit number of rows
  )
  ```
</CodeGroup>

### Example: Exporting Data

<CodeGroup>
  ```python Append Mode theme={"system"}
  from mage_ai.io.iceberg_s3 import Iceberg
  from mage_ai.io.config import ConfigFileLoader

  iceberg = Iceberg.with_config(
      ConfigFileLoader(config_path, config_profile),
      namespace='analytics',
      catalog_type='sql',
  )

  # Append data to table
  iceberg.export(
      df,
      bucket_name='my-bucket',
      table_name='my_table',
      mode='append',
  )
  ```

  ```python Overwrite Mode theme={"system"}
  from mage_ai.io.iceberg_s3 import Iceberg
  from mage_ai.io.config import ConfigFileLoader

  iceberg = Iceberg.with_config(
      ConfigFileLoader(config_path, config_profile),
      namespace='analytics',
      catalog_type='sql',
  )

  # Overwrite table with new data
  iceberg.export(
      df,
      bucket_name='my-bucket',
      table_name='my_table',
      mode='overwrite',
  )
  ```
</CodeGroup>

### Additional Methods

The Iceberg integration also provides methods for managing tables and namespaces:

* `list_namespaces()`: List all namespaces in the catalog
* `list_tables(namespace)`: List all tables in a namespace
* `get_table_schema(table_name, namespace)`: Get the schema of a table
* `drop_table(table_name, namespace)`: Drop (delete) a table
* `drop_namespace(namespace)`: Drop (delete) a namespace

### Notes

* The Iceberg integration supports direct access to tables through metadata stored in S3 when tables are not registered in the catalog.
* For SQL catalog, `base_uri` should point to your warehouse location and include a trailing slash (e.g., `s3://bucket/warehouse/`).
* For AWS Glue catalog, tables must be registered in AWS Glue.
* When using `metadata_file`, the path is constructed as: `{base_uri}{table_name}/metadata/{metadata_file}`.
* Additional scan parameters (e.g., `row_filter`, `selected_fields`, `case_sensitive`, `snapshot_id`) can be passed to the `load()` method.

## Using Iceberg with PySpark

Mage Pro supports reading from and writing to [Apache Iceberg](https://iceberg.apache.org/) tables using PySpark, enabling scalable and efficient data lake operations.

### Example code

Using Iceberg with Google Cloud Storage (GCS)

```python  theme={"system"}
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("IcebergWithGCS") \
    .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.1") \
    .config("spark.jars", "/opt/spark/jars/gcs-connector-hadoop3-2.2.5-shaded.jar") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.iceberg", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.iceberg.type", "hadoop") \
    .config("spark.sql.catalog.iceberg.warehouse", "gs://mage_icerberg_test/test") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/home/src/default_repo/your_google_service_account_key.json") \
    .getOrCreate()
```

Create and Write an Iceberg Table

```python  theme={"system"}
# Sample DataFrame
df = spark.createDataFrame([
    (1, "apple"),
    (2, "banana"),
    (3, "banana"),
], ["id", "fruit"])

# Create the database if it doesn't exist
spark.sql("CREATE DATABASE IF NOT EXISTS iceberg.db_name")

# Write data to an Iceberg table
df.writeTo("iceberg.db_name.iceberg_table") \
  .using("iceberg") \
  .createOrReplace()
```

### Notes

* `iceberg.db_name.iceberg_table` uses the Hadoop catalog type and stores metadata in the specified GCS path.
* You can modify the catalog configs to use **Hive**, **Glue**, or **Nessie** depending on your architecture.
* For AWS S3, update the warehouse path and authentication configurations accordingly.
* The Google service account key file path must be accessible inside the Mage Pro cluster.
* You can run this code inside a block in Mage Pro batch pipeline.


Built with [Mintlify](https://mintlify.com).