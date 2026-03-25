# Source: https://docs.mage.ai/design/data-loading.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Data loader utilities

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

Mage provides data loading clients that simplify loading and exporting data in your pipelines, allowing you to spend more time analyzing and transforming your data for ML tasks. Currently, Mage includes clients for the following data sources:

**File Storage:**

* [AWS S3](#s3)
* [Azure Blob Storage](#azureblobstorage)
* [Azure Data Lake Storage](#azure-data-lake-storage) (Pro only)
* [Filesystem](#fileio)
* [Google Cloud Storage](#googlecloudstorage)

**Databases:**

* [AWS Redshift](#redshift)
* [ClickHouse](#clickhouse)
* [Databricks SQL](#databricks-sql) (Pro only)
* [DuckDB](#duckdb)
* [MySQL](#mysql)
* [MSSQL](#mssql)
* [MongoDB](#mongodb)
* [OracleDB](#oracledb)
* [PostgreSQL](#postgresql)
* [SQLite](#sqlite)
* [Snowflake](#snowflake)
* [Spark](#spark)
* [Trino](#trino)

**Data Warehouses:**

* [Google BigQuery](#bigquery)
* [Microsoft Fabric Warehouse](#microsoft-fabric-warehouse) (Pro only)

**APIs & Services:**

* [Google Sheets](#googlesheets)

Mage's data loading clients fall into two categories:

* **File-Loading Clients** - import/export data between files and your pipeline. Includes both local filesystem storage and external filesystem storage (like AWS S3)
* **Database Clients** - imports data from an external database into your pipeline and exports data frames back into that database. These database clients include the `execute` method which execute your queries in the connected database. The Google BigQuery client follows this structure.
  * A subcategory of database clients are **connection-based clients**, which wrap a connection to the database. This connection is used to execute transactions (sets of queries) on the database, which are either committed (saved to database) or rolled-back (deleted). Clients for PostgreSQL, Redshift, and Snowflake follow this structure.

## Example: Loading data from a file

While traditional Pandas IO procedures can be utilized to load files into your pipeline, Mage provides the `mage_ai.io.file.FileIO` client as a convenience wrapper.

The following code uses the `load` function of the `FileIO` client to load the Titanic survival dataset from a CSV file into a Pandas DataFrame for use in your pipeline. All data loaders can be initialized with the `verbose = True` parameter, which will print the current action the data loading client is performing. This parameter defaults to `False`.

```python  theme={"system"}
loader = FileIO(verbose=True)
df = loader.load(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)
```

Then the `export` function is used to save this data frame back to file, this time in JSON format

```python  theme={"system"}
loader.export(df, './titanic_survival.json', orient='records')
```

Any formatting settings (such as specifying the data frame *orient*) can be passed as keyword arguments to `load` and `export`. These arguments are passed to Pandas IO procedures for the requested file format, enabling fine-grained control over how your data is loaded and exported.

As the data loader was constructed with the verbose parameter set to `True`, the above operations would print the following output describing the actions of the data loader.

```bash  theme={"system"}
FileIO initialized
├─ Loading data frame from 'https://raw.githubusercontent.com/datasciencedojodatasets/master/titanic.csv'...DONE
└─ Exporting data frame to './titanic_survival.json'...DONE
```

See the [FileIO](#fileio) API to learn more about loading data from filesystem.

## Example: Loading data from Snowflake warehouse

Loading data from a Snowflake data warehouse is made easy using the `mage_ai.io.snowflake.Snowflake` data loading client. In order to authenticate access to a Snowflake warehouse, the client requires the associated Snowflake credentials:

* Account Username
* Account Password
* Account ID (including your region) (Ex: *example.us-west-2*)

These parameters can be manually specified as input to the data loading client (see [Snowflake](#snowflake) API). However we recommend using a [Configuration Loader](#configuration-settings) to handle loading these secrets. If you used `mage init` to create your project repository, you can store these values in your `io_config.yaml` file and use `mage_ai.io.config.ConfigFileLoader` to construct the data loader client.

For detailed information about setting up `io_config.yaml`, see the [IO Config Setup documentation](/development/io_config_setup).

An example `io_config.yaml` file in this instance would be:

```yaml  theme={"system"}
default:
    SNOWFLAKE_USER: my_username
    SNOWFLAKE_PASSWORD: my_password
    SNOWFLAKE_ACCOUNT: example.us-west-2
```

with which a Snowflake data loading client can be constructed as:

```python  theme={"system"}
config = ConfigFileLoader('io_config.yaml', 'default')
loader = Snowflake.with_config(config, verbose=True)
```

To learn more about using configuration settings, see [Configuration Settings](#configuration-settings).

Then the following code uses the functions:

* `execute()` - executes an arbitrary query on your data warehouse. In this case, the warehouse, database, and schema to use are selected.
* `load()` - loads the results of a `SELECT` query into a Pandas DataFrame.
* `export()` - stores data frame as a table in your data warehouse. If the table exists, then the data is appended by default (and can be configured with other behavior, see [Snowflake](#snowflake) API). If the table doesn't exist, then the table is created with the given schema name and table name (the table data types are inferred from the Python data type).

```python  theme={"system"}
with loader:
    loader.execute('USE WAREHOUSE my_warehouse;')
    loader.execute('USE DATABASE my_database;')
    loader.execute('USE SCHEMA my_schema;')
    df = loader.load('SELECT * FROM test_table;')
    loader.export(df, 'my_schema', 'test_table')
```

The `loader` object manages a direct connection to your Snowflake data warehouse, so it is important to make sure that your connection is closed once your operations are completed. You can manually use `loader.open()` and `loader.close()` to open and close the connection to your data warehouse or automatically manage the connection with a context manager.

To learn more about loading data from Snowflake, see the [Snowflake](#snowflake) API for more details on member functions and usage.

# Client APIs

This section covers the API for using the following data loaders.

## FileIO

`mage_ai.io.file.FileIO`

Handles data transfer between the filesystem and the Mage app. The `FileIO` client currently supports importing and exporting with the following file formats:

* CSV
* JSON
* Parquet
* HDF5
* XML
* Excel

<h3> Constructor </h3>

`__init__(self, verbose: bool)`

Initializes the FileIO data loading client.

* **Args**
  * `verbose (bool)`: Enables verbose output printing. Defaults to False.

<h3> Methods </h3>

***export*** - `export(df: DataFrame, filepath: os.PathLike, format: FileFormat | str = None, **kwargs) -> None:`

Exports the input data frame to the file specified.

If the format is HDF5, the default key under which the data frame is stored is the stem of the filename. For example, if the file to write the data frame to is 'storage/my\_data\_frame.hdf5', the key would be 'my\_data\_frame'. This can be overridden using the `key` keyword argument.

* **Args**:

  * `df (DataFrame)`: Data frame to export.
  * `filepath (os.PathLike)`: Filepath to export data frame to.
  * `format (FileFormat | str, Optional)`: Format of the file to export data frame to. Defaults to None, in which case the format is inferred.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Writer                                                                                                          |
    | ------- | ---------------------------------------------------------------------------------------------------------------------- |
    | CSV     | [*DataFrame.to\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)         |
    | JSON    | [*DataFrame.to\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)       |
    | Parquet | [*DataFrame.to\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) |
    | HDF5    | [*DataFrame.to\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html)         |
    | XML     | [*DataFrame.to\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_xml.html)         |
    | Excel   | [*DataFrame.to\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)     |

***load*** - `load(filepath: os.PathLike, format: FileFormat | str = None, limit: int = QUERY_ROW_LIMIT **kwargs) -> DataFrame`

Loads the data frame from the filepath specified. This function will load at maximum 10,000,000 rows of data from the specified file (this limit is configurable).

* **Args**:

  * `filepath (os.PathLike)`: Filepath to load data frame from.
  * `format (FileFormat | str, Optional)`: Format of the file to load data frame from. Defaults to None, in which case the format is inferred.
  * `limit (int, optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Reader                                                                                          |
    | ------- | ------------------------------------------------------------------------------------------------------ |
    | CSV     | [*read\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)         |
    | JSON    | [*read\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)       |
    | Parquet | [*read\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) |
    | HDF5    | [*read\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_hdf.html)         |
    | XML     | [*read\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_xml.html)         |
    | Excel   | [*read\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)     |

* **Returns**: (`DataFrame`) Data frame object loaded from data in the specified file.

## S3

`mage_ai.io.s3.S3`

Handles data transfer between an S3 bucket and the Mage app. The `S3` client supports importing and exporting with the following file formats:

* CSV
* JSON
* Parquet
* HDF5
* XML
* Excel

If an IAM profile is not set up using `aws configure`, then AWS credentials for accesses the S3 bucket can be manually specified through either Mage's [configuration loader](#configuration-settings) system or through keyword arguments in the constructor (see constructor).

If using configuration settings, specify the following keys:

```yaml  theme={"system"}
AWS_ACCESS_KEY_ID: AWS Access Key ID credential
AWS_SECRET_ACCESS_KEY: AWS Secret Access Key credential
AWS_REGION: AWS Region
```

<h3> Constructor </h3>

`__init__(self, verbose: bool)`

Initializes the S3 data loading client.

* **Args**
  * `verbose (bool)`: Enables verbose output printing. Defaults to False.
  * If IAM profile is not set up using `aws configure` and Mage's configuration loader is not used, then specify your AWS credentials through the following keyword arguments:
    * `aws_access_key_id (str)`: AWS Access Key ID credential
    * `aws_secret_access_key (str)`: AWS Secret Access Key credential
    * `aws_region (str)`: Region associated with AWS IAM profile

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> S3`

Creates S3 data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`S3`) The constructed dataloader using this method

<h3> Methods </h3>

***export*** - `export(df: DataFrame, bucket_name: str, object_key: str, format: FileFormat | str = None, **kwargs) -> None:`

Exports data frame to an S3 bucket.

If the format is HDF5, the default key under which the data frame is stored is the stem of the filename. For example, if the file to write the data frame to is 'storage/my\_data\_frame.hdf5', the key would be 'my\_data\_frame'. This can be overridden using the `key` keyword argument.

* **Args**:

  * `data (Union[DataFrame, str])`: Data frame or file path to export.
  * `bucket_name (str)`: Name of the bucket to export data frame to.
  * `object_key (str)`: Object key in S3 bucket to export data frame to.
  * `format (FileFormat | str, Optional)`: Format of the file to export data frame to. Defaults to `None`, in which case the format is inferred.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Writer                                                                                                          |
    | ------- | ---------------------------------------------------------------------------------------------------------------------- |
    | CSV     | [*DataFrame.to\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)         |
    | JSON    | [*DataFrame.to\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)       |
    | Parquet | [*DataFrame.to\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) |
    | HDF5    | [*DataFrame.to\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html)         |
    | XML     | [*DataFrame.to\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_xml.html)         |
    | Excel   | [*DataFrame.to\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)     |

***load*** - `load(bucket_name: str, object_key: str, format: FileFormat | str = None, limit: int = QUERY_ROW_LIMIT **kwargs) -> DataFrame`

Loads data from object in S3 bucket into a Pandas data frame. This function will load at maximum 10,000,000 rows of data from the specified file (this limit is configurable).

* **Args**:

  * `bucket_name (str)`: Name of the bucket to load data from.
  * `object_key (str)`: Key of the object in S3 bucket to load data from.
  * `format (FileFormat | str, Optional)`: Format of the file to load data frame from. Defaults to None, in which case the format is inferred.
  * `limit (int, optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Reader                                                                                          |
    | ------- | ------------------------------------------------------------------------------------------------------ |
    | CSV     | [*read\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)         |
    | JSON    | [*read\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)       |
    | Parquet | [*read\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) |
    | HDF5    | [*read\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_hdf.html)         |
    | XML     | [*read\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_xml.html)         |
    | Excel   | [*read\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)     |

* **Returns**: (`DataFrame`) Data frame object loaded from data in the specified file.

## GoogleCloudStorage

`mage_ai.io.google_cloud_storage.GoogleCloudStorage`

Handles data transfer between a Google Cloud Storage bucket and the Mage app. Supports loading files of any of the following types:

* CSV
* JSON
* Parquet
* HDF5
* XML
* Excel

If `GOOGLE_APPLICATION_CREDENTIALS` environment is set, no further arguments are needed other than those specified below. Otherwise, use the factory method `with_config` to construct the data loader using manually specified credentials.

To authenticate (and authorize) access to Google Cloud Storage, credentials must be provided.
Below are the different ways to access those credentials:

* Define the `GOOGLE_APPLICATION_CREDENTIALS` environment variable holding the filepath to your service account key
* Define the `GOOGLE_SERVICE_ACC_KEY_FILEPATH` key with your [configuration loader](#configuration-settings) or the `path_to_credentials` keyword argument with the client constructor holding the filepath to your service account key
* Define the `GOOGLE_SERVICE_ACC_KEY` key with your [configuration loader](#configuration-settings) or the `credentials_mapping` keyword argument with the client constructor holding a mapping sharing the same contents as your service key
  * if using a configuration file, be careful to wrap your service key values in quotes so the YAML parser reads the settings correctly
* Manually pass the `google.oauth2.service_account.Credentials` object with the keyword argument `credentials`

<h3> Constructor </h3>

`__init__(self, verbose: bool = False, **kwargs)`

Initializes the GoogleCloudStorage data loading client.

* **Args**

  * `verbose (bool)`: Enables verbose output printing. Defaults to `False`.
  * `credentials_mapping (Mapping[str, str])` - Mapping object corresponding to your service account key. See instructions above on when to use this keyword argument
  * `path_to_credentials (str)` - Filepath to service account key. See instructions above on when to use this keyword argument.

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> GoogleCloudStorage`

Creates GoogleCloudStorage data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`GoogleCloudStorage`) The constructed dataloader using this method

<h3> Methods </h3>

***export*** - `export(df: DataFrame, bucket_name: str, object_key: str, format: FileFormat | str = None, **kwargs) -> None:`

Exports data frame to a GoogleCloudStorage bucket.

* **Args**:

  * `data (Union[DataFrame, str])`: Data frame or file path to export.
  * `bucket_name (str)`: Name of the bucket to export data frame to.
  * `object_key (str)`: Object key in GoogleCloudStorage bucket to export data frame to.
  * `format (FileFormat | str, Optional)`: Format of the file to export data frame to. Defaults to `None`, in which case the format is inferred.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Writer                                                                                                          |
    | ------- | ---------------------------------------------------------------------------------------------------------------------- |
    | CSV     | [*DataFrame.to\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)         |
    | JSON    | [*DataFrame.to\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)       |
    | Parquet | [*DataFrame.to\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) |
    | HDF5    | [*DataFrame.to\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html)         |
    | XML     | [*DataFrame.to\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_xml.html)         |
    | Excel   | [*DataFrame.to\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)     |

***load*** - `load(bucket_name: str, object_key: str, format: FileFormat | str = None, limit: int = QUERY_ROW_LIMIT, **kwargs) -> DataFrame`

Loads data from object in GoogleCloudStorage bucket into a Pandas data frame. This function will load at maximum 10,000,000 rows of data from the specified file (this limit is configurable).

* **Args**:

  * `bucket_name (str)`: Name of the bucket to load data from.
  * `object_key (str)`: Key of the object in GoogleCloudStorage bucket to load data from.
  * `format (FileFormat | str, Optional)`: Format of the file to load data frame from. Defaults to None, in which case the format is inferred.
  * `limit (int, optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Reader                                                                                          |
    | ------- | ------------------------------------------------------------------------------------------------------ |
    | CSV     | [*read\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)         |
    | JSON    | [*read\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)       |
    | Parquet | [*read\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) |
    | HDF5    | [*read\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_hdf.html)         |
    | XML     | [*read\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_xml.html)         |
    | Excel   | [*read\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)     |

* **Returns**: (`DataFrame`) Data frame object loaded from data in the specified file.

## AzureBlobStorage

`mage_ai.io.azure_blob_storage.AzureBlobStorage`

Handles data transfer between an Azure Blob Storage container and Mage. Supports loading files of the following types:

* CSV
* JSON
* Parquet
* HDF5
* XML
* Excel

To authenticate access to Azure Blob Storage, the following environment variables must be set:

* `AZURE_CLIENT_ID`
* `AZURE_CLIENT_SECRET`
* `AZURE_TENANT_ID`
* `AZURE_STORAGE_ACCOUNT_NAME`

By default, these correspond to variables of the same name in `io_config.yaml`.

<h3> Constructor </h3>

Initializes data loader from an Azure Blob Storage container.

* **Args**

  * `verbose (bool)`: Enables verbose output printing. Defaults to `False`.

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> AzureBlobStorage`

Creates AzureBlobStorage data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`AzureBlobStorage`) The constructed dataloader using this method

<h3> Methods </h3>

***export*** - `export(df: DataFrame, bucket_name: str, object_key: str, format: FileFormat | str = None, **kwargs) -> None:`

Exports data frame to an Azure Blob Storage container.

* **Args**:

  * `df (DataFrame)`: Data frame to export.
  * `container_name (str)`: Name of the Azure container to export data to.
  * `blob_path (str)`: The desired output path of the data in your Azure Blob
  * `format (FileFormat | str, Optional)`: Format of the file to export data frame to. Defaults to `None`, in which case the format is inferred.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats at:

    | Format  | Pandas Writer                                                                                                          |
    | ------- | ---------------------------------------------------------------------------------------------------------------------- |
    | CSV     | [*DataFrame.to\_csv*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)         |
    | JSON    | [*DataFrame.to\_json*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html)       |
    | Parquet | [*DataFrame.to\_parquet*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) |
    | HDF5    | [*DataFrame.to\_hdf*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html)         |
    | XML     | [*DataFrame.to\_xml*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_xml.html)         |
    | Excel   | [*DataFrame.to\_excel*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)     |

***load*** - `load(container_name: str, blob_path: str, format: FileFormat | str = None, limit: int = QUERY_ROW_LIMIT, **kwargs) -> DataFrame`

Loads data from object in Azure Blob Storage into a Pandas data frame. This function will load at maximum 10,000,000 rows of data from the specified file (this limit is configurable).

## GoogleSheets

`mage_ai.io.google_sheets.GoogleSheets`

Handles data transfer between a Google Sheets spreadsheet and the Mage app.

Authentication is the same for our other Google Cloud data loaders. Read more about configuration [here](integrations/databases/GoogleSheets#configuration).

The Google Sheets class is defined [here](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/io/google_sheets.py).

## BigQuery

`mage_ai.io.bigquery.BigQuery`

Handles data transfer between a BigQuery data warehouse and the Mage app.

Authentication with a Google BigQuery warehouse requires specifying the service account key for the service account that has access to the BigQuery warehouse. There are four ways to provide this service key:

* Define the `GOOGLE_APPLICATION_CREDENTIALS` environment variable holding the filepath to your service account key
* Define the `GOOGLE_SERVICE_ACC_KEY_FILEPATH` key with your [configuration loader](#configuration-settings) or the `path_to_credentials` keyword argument with the client constructor holding the filepath to your service account key
* Define the `GOOGLE_SERVICE_ACC_KEY` key with your [configuration loader](#configuration-settings) or the `credentials_mapping` keyword argument with the client constructor holding a mapping sharing the same contents as your service key
  * if using a configuration file, be careful to wrap your service key values in quotes so the YAML parser reads the settings correctly
* Manually pass the `google.oauth2.service_account.Credentials` object with the keyword argument `credentials`

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the BigQuery data loading client.

* **Args**

  * `verbose (bool)`: Enables verbose output printing. Defaults to `False`.
  * `credentials_mapping (Mapping[str, str])` - Mapping object corresponding to your service account key. See instructions above on when to use this keyword argument
  * `path_to_credentials (str)` - Filepath to service account key. See instructions above on when to use this keyword argument.

  All other keyword arguments can be found in the [Google BigQuery Python Client docs](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html?highlight=client#google-cloud-bigquery-client-client)

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> BigQuery`

Creates BigQuery data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`BigQuery`) BigQuery data loading client constructed using this method

***with\_credentials\_file*** - `with_credentials_file(cls, path_to_credentials: str, **kwargs) -> BigQuery`

Constructs BigQuery data loader using the file containing the service account key.

* **Args**:
  * `path_to_credentials (str)`: Path to the credentials file.
  * `**kwargs`: Additional parameters to pass to BigQuery client constructor.
* **Returns**: (`BigQuery`) BigQuery data loading client constructed using this method

***with\_credentials\_object*** - `with_credentials_object(cls, credentials: Mapping[str, str], **kwargs) -> BigQuery`

Constructs BigQuery data loader using manually specified service account key credentials.

* **Args**:
  * `credentials (Mapping[str, str])`: Mapping containing same key-value pairs as a service account key.
  * `**kwargs`: Additional parameters to pass to BigQuery client constructor.
* **Returns**: (`BigQuery`) BigQuery data loading client constructed using this method

<h3> Methods </h3>

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected BigQuery warehouse.

* **Args**:
  * `query_string (str)`: Query to execute on the BigQuery warehouse.
  * `**kwargs`: Additional arguments to pass to query, such as query configurations. See [*Client.query()*](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html?highlight=client#google.cloud.bigquery.client.Client.query) docs for additional arguments.

***export*** - `export(df: DataFrame, table_name: str, database: str, schema: str, if_exists: str, **kwargs) -> None`

Exports a data frame to a Google BigQuery warehouse. If table doesn't exist, the table is automatically created.

* **Args**:
  * `df (DataFrame)`: Data frame to export
  * `table_id (str)`: ID of the table to export the data frame to. If of the format
    `"your-project.your_dataset.your_table_name"`. If this table exists, the table schema must match the data frame schema. If this table doesn't exist, the table schema is automatically inferred.
  * `if_exists (str)`: Specifies export policy if table exists. Either - `'fail'`: throw an error. - `'replace'`: drops existing table and creates new table of same name. - `'append'`: appends data frame to existing table. In this case the schema must match the original table.
    Defaults to `'replace'`. If `write_disposition` is specified as a keyword argument, this parameter
    is ignored (as both define the same functionality).
  * `**configuration_params`: Configuration parameters for export job. See valid configuration parameters at [*LoadJobConfig*](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.LoadJobConfig.html#google.cloud.bigquery.job.LoadJobConfig) docs.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

When a select query is provided, this function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query. See [Google BigQuery Python client](https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html?highlight=client#google.cloud.bigquery.client.Client.query) docs for additional arguments.

***sample*** - `sample(schema: str, table: str, size: int, **kwargs) -> DataFrame`

Sample data from a table in the BigQuery warehouse. Sample is not guaranteed to be random.

* **Args**:

  * `schema (str)`: The schema to select the table from.
  * `size (int)`: The number of rows to sample. Defaults to 10,000,000.
  * `table (str)`: The table to sample from in the connected database.

* **Returns**: (`DataFrame`) Sampled data from the table.

## PostgreSQL

`mage_ai.io.postgres.Postgres`

Handles data transfer between a PostgreSQL database and the Mage app. The `Postgres` client utilizes the following keys to connect the PostgreSQL database.

```yaml  theme={"system"}
POSTGRES_DBNAME: PostgreSQL database name
POSTGRES_USER: PostgreSQL database login username
POSTGRES_PASSWORD: PostgreSQL database login password
POSTGRES_HOST: PostgreSQL database hostname
POSTGRES_PORT: PostgreSQL database port
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the Postgres data loading client.

* **Args**:
  * `dbname (str)`: The name of the database to connect to.
  * `user (str)`: The user with which to connect to the database with.
  * `password (str)`: The login password for the user.
  * `host (str)`: Host address for database.
  * `port (str)`: Port on which the database is running.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `False`.
  * `**kwargs`: Additional settings for creating psycopg2 connection

<h3> Attributes </h3>

* *conn* (`psycopg2.connection.Connection`) - underlying [psycopg2 Connection](https://www.psycopg.org/docs/connection.html) object

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Postgres`

Creates Postgres data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`Postgres`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to PostgreSQL database.

***commit*** - `commit()`

Saves all changes made to the database since the previous transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected PostgreSQL database. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the PostgreSQL database.
  * `**kwargs`: Additional parameters to pass to the query. See [`psycopg2` docs](https://www.psycopg.org/docs/usage.html#query-parameters) for configuring query parameters.

***export*** - `export(df: DataFrame, table_name: str, database: str, schema: str, if_exists: str, index: bool, **kwargs) -> None`

Exports data frame to the PostgreSQL database from a Pandas data frame. If table doesn't exist, the table is automatically created. If the schema doesn't exist, the schema is also created.

Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:

  * `df (DataFrame)`: Data frame to export to the PostgreSQL database.

  * `table_name (str)`: Name of the table to export data to (excluding database and schema).

  * `database (str)`: Name of the database in which the table is located.

  * `schema (str)`: Name of the schema in which the table is located.

  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either

    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.

    Defaults to `'replace'`.

  * `index (bool)`: If `True`, the data frame index is also exported alongside the table. Defaults to `False`.

  * `**kwargs`: Additional arguments to pass to writer. See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) for details on UPSERT (`unique_constraints`, `unique_conflict_method`) and other advanced options like `overwrite_types`, `query_string`, `auto_clean_name`, etc.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query. See [`psycopg2` docs](https://www.psycopg.org/docs/usage.html#query-parameters) for configuring query parameters.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to PostgreSQL database.

***rollback*** - `rollback()`

Rolls back (deletes) all database changes made since the last transaction.

***sample*** - `sample(schema: str, table: str, size: int, **kwargs) -> DataFrame`

Sample data from a table in the PostgreSQL database. Sample is not guaranteed to be random.

* **Args**:

  * `schema (str)`: The schema to select the table from.
  * `size (int)`: The number of rows to sample. Defaults to 10,000,000.
  * `table (str)`: The table to sample from in the connected database.

* **Returns**: (`DataFrame`) Sampled data from the table.

## Advanced Export Parameters for SQL Databases

The following advanced export parameters are available for all SQL database clients (PostgreSQL, MySQL, MSSQL, Snowflake, BigQuery, ClickHouse, Trino, Databricks SQL, SQLite, etc.) that inherit from `BaseSQL`. These parameters provide fine-grained control over how data is exported.

> **Note:** UPSERT (UPDATE or INSERT) functionality is only supported on a subset of SQL databases (e.g., PostgreSQL, MySQL, MSSQL, Snowflake, BigQuery, SQLite). It is **not** supported on Redshift, ClickHouse, Trino or Databricks SQL. See below for details.

### UPSERT (UPDATE or INSERT)

UPSERT allows you to update existing rows when they match unique constraints, or insert new rows if they don't exist. This is useful for maintaining data integrity and avoiding duplicate entries.

To enable UPSERT functionality, you need to specify both `unique_constraints` and `unique_conflict_method` parameters:

* `unique_constraints (List[str])`: A list of column names that form the unique constraint. These columns are used to identify existing rows for updates.
* `unique_conflict_method (str)`: Specifies how to handle conflicts when unique constraints are violated. Can be either:
  * `'UPDATE'` (or use constant `UNIQUE_CONFLICT_METHOD_UPDATE`): Updates existing rows that match the unique constraints with new values from the data frame, and inserts new rows that don't match.
  * `'IGNORE'` (or use constant `UNIQUE_CONFLICT_METHOD_IGNORE`): Ignores rows that would violate unique constraints (does not update or insert).

**Example: UPSERT with PostgreSQL**

```python  theme={"system"}
from mage_ai.io.postgres import Postgres
from mage_ai.io.constants import UNIQUE_CONFLICT_METHOD_UPDATE

loader = Postgres(...)
with loader:
    loader.export(
        df,
        table_name='users',
        schema='public',
        if_exists='append',
        unique_constraints=['user_id', 'email'],  # Columns that form unique constraint
        unique_conflict_method=UNIQUE_CONFLICT_METHOD_UPDATE,  # Update existing, insert new
    )
    loader.commit()
```

In this example:

* If a row with the same `user_id` and `email` already exists, it will be updated with the new values from the data frame.
* If no matching row exists, a new row will be inserted.

**Example: Ignore duplicates**

```python  theme={"system"}
from mage_ai.io.postgres import Postgres
from mage_ai.io.constants import UNIQUE_CONFLICT_METHOD_IGNORE

loader = Postgres(...)
with loader:
    loader.export(
        df,
        table_name='users',
        schema='public',
        if_exists='append',
        unique_constraints=['user_id'],
        unique_conflict_method=UNIQUE_CONFLICT_METHOD_IGNORE,  # Skip rows that already exist
    )
    loader.commit()
```

**Note**: UPSERT functionality is supported on PostgreSQL, MySQL, MSSQL, Snowflake, BigQuery, and SQLite. The exact SQL syntax used may vary by database (e.g., PostgreSQL uses `ON CONFLICT`, MySQL uses `ON DUPLICATE KEY UPDATE`, MSSQL uses `MERGE`), but the interface remains consistent across all supported databases.

UPSERT functionality is **not supported** on Redshift, ClickHouse, Trino and Databricks SQL.

### Additional Export Parameters

The following parameters provide additional control over the export process:

* `allow_reserved_words (bool)`: If `True`, allows column names that are SQL reserved words. Defaults to `False`.
* `auto_clean_name (bool)`: If `True`, automatically cleans column and table names (removes special characters, handles reserved words). Defaults to `True`.
* `case_sensitive (bool)`: If `True`, preserves case sensitivity for identifiers. Defaults to `False`.
* `cascade_on_drop (bool)`: If `True`, adds `CASCADE` when dropping tables. Defaults to `False`.
* `drop_table_on_replace (bool)`: If `True`, drops the table when using `if_exists='replace'` instead of deleting all rows. Defaults to `False`.
* `overwrite_types (Dict[str, str])`: A dictionary mapping column names to SQL data types to override automatic type inference. Example: `{'price': 'DECIMAL(10,2)', 'description': 'TEXT'}`.
* `query_string (str)`: A custom SQL query string to use for creating the table. If provided, the table is created using `CREATE TABLE AS SELECT ...` syntax.
* `skip_check_table_exists (bool)`: If `True`, skips checking if the table exists before export. Defaults to `False`.
* `skip_create_schema (bool)`: If `True`, skips creating the schema if it doesn't exist. Defaults to `False`.
* `skip_semicolon_at_end (bool)`: If `True`, omits the semicolon at the end of SQL statements. Defaults to `False`.

**Example: Using overwrite\_types**

```python  theme={"system"}
loader.export(
    df,
    table_name='products',
    schema='public',
    overwrite_types={
        'price': 'DECIMAL(10,2)',
        'description': 'TEXT',
        'created_at': 'TIMESTAMP',
    }
)
```

**Example: Using query\_string**

```python  theme={"system"}
loader.export(
    df,
    table_name='filtered_data',
    schema='public',
    query_string='SELECT * FROM source_table WHERE status = \'active\'',
)
```

## OracleDB

```yaml  theme={"system"}
ORACLEDB_USER: OracleDB username
ORACLEDB_PASSWORD: OracleDB password
ORACLEDB_HOST: OracleDB host
ORACLEDB_PORT: OracleDB port
ORACLEDB_SERVICE: OracleDB service
ORACLEDB_MODE: OracleDB mode
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the OracleDB data loading client.

* **Args**:
  * `user (str)`: The user for connecting to the database with.
  * `password (str)`: The login password for the user.
  * `host (str)`: Host address for database.
  * `port (int)`: Port on which the database is running Defaults to 3306.
  * `service (str)`: OracleDB service
  * `mode (str)`: switch between OracleDB mode of `thin` or `thick`
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating psycopg2 connection

To switch OracleDB mode to `thick`, it is required to use the customized oracle Dockerfile in `integrations/oracle/Dockerfile`.

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Postgres`

Creates OracleDB data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`OracleDB`) The constructed dataloader using this method

<h3> Methods </h3>

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected OracleDB database. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the OracleDB database.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, schema_name: str, table_name: str, if_exists: str, index: bool, **kwargs) -> None`

Exports data frame to the OracleDB database from a Pandas data frame. If table doesn't exist, the table is automatically created. The `schema_name` can be set as `None` since it is not required for OracleDB loaders.

Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:

  * `df (DataFrame)`: Data frame to export to the OracleDB database.

  * `schema_name (str)`: Not required for OracleDB loaders. Set to `None`.

  * `table_name (str)`: Name of the table to export data to (excluding database).

  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either

    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.

    Defaults to `'replace'`.

  * `index (bool)`: If `True`, the data frame index is also exported alongside the table. Defaults to `False`.

  * `**kwargs`: Additional arguments to pass to writer.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to OracleDB database.

## MySQL

`mage_ai.io.mysql.MySQL`

Handles data transfer between a MySQL database and the Mage app. The `MySQL` client utilizes the following keys to connect the MySQL database.

```yaml  theme={"system"}
MYSQL_DATABASE: MySQL database name
MYSQL_HOST: MySQL database hostname
MYSQL_PASSWORD: MySQL database login password
MYSQL_PORT: MySQL database port
MYSQL_USER: MySQL database login username
MYSQL_ALLOW_LOCAL_INFILE: Pass boolean value to `allow_local_infile` param during connection to enable the capability to load local data file.
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the MySQL data loading client.

* **Args**:
  * `database (str)`: The name of the database to connect to.
  * `user (str)`: The user for connecting to the database with.
  * `password (str)`: The login password for the user.
  * `host (str)`: Host address for database.
  * `port (int)`: Port on which the database is running Defaults to 3306.
  * `allow_local_infile (bool)`: Enables verbose capability to load local file. Defaults to `False`.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating psycopg2 connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> MySQL`

Creates MySQL data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`MySQL`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to MySQL database.

***commit*** - `commit()`

Saves all changes made to the database since the previous transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected MySQL database. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the MySQL database.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, schema_name: str, table_name: str, if_exists: str, index: bool, **kwargs) -> None`

Exports data frame to the MySQL database from a Pandas data frame. If table doesn't exist, the table is automatically created. The `schema_name` can be set as `None` since it is not required for MySQL loaders.

Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:

  * `df (DataFrame)`: Data frame to export to the MySQL database.

  * `schema_name (str)`: Not required for MySQL loaders. Set to `None`.

  * `table_name (str)`: Name of the table to export data to (excluding database).

  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either

    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.

    Defaults to `'replace'`.

  * `index (bool)`: If `True`, the data frame index is also exported alongside the table. Defaults to `False`.

  * `**kwargs`: Additional arguments to pass to writer. See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) for details on UPSERT (`unique_constraints`, `unique_conflict_method`) and other advanced options.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to MySQL database.

***sample*** - `sample(database: str, table: str, size: int, **kwargs) -> DataFrame`

Sample data from a table in the MySQL database. Sample is not guaranteed to be random.

* **Args**:

  * `database (str)`: The database to select the table from.
  * `table (str)`: The table to sample from in the connected database.
  * `size (int)`: The number of rows to sample. Defaults to 10,000,000.

* **Returns**: (`DataFrame`) Sampled data from the table.

## DuckDB

`mage_ai.io.duckdb`

Handles data transfer between DuckDB database and the Mage app.
DuckDB client utilizes the following keys to connect:

```yaml  theme={"system"}
DUCKDB_DATABASE: database # Database name
DUCKDB_SCHEMA: main # Schema name. Default is main.
```

<h3> Constructor </h3>

```
__init__(self,
         database: str
         schema: str = None,
         verbose: bool = True,
         **kwargs
        )
```

Initializes the DuckDB data loading client.

* **Args**:
  * `database (str)`: The name of the database to connect to.
  * `schema`: Schema to use.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating psycopg2 connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> DuckDB`

Creates DuckDB data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`DuckDB`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to DuckDB database.

***open*** - `open()`

Opens a connection to DuckDB database.

***table\_exists*** - `table_exists()`

Build query to check if a table existing in the DB.

* **Args**:
  * `schema_name`: Name of the schema to use.
  * `table_name`: Name of the table.
* **Returns**: true or false.

***upload\_dataframe*** - `upload_dataframe()`

Build query to insert data into table.

* **Args**:
  * `df`: Data in dataframe type.

***get\_type*** - `get_type()`

Convert data from input type into DuckDB type.

* **Args**:
  * `column`: Metadata associated with the column.
  * `dtype`: Input data type.
* **Returns**: DuckDB data type in string format.

## Snowflake

`mage_ai.io.snowflake.Snowflake`

Handles data transfer between a Snowflake data warehouse and the Mage app. The `Snowflake` client utilizes the following keys to authenticate access and connect to Snowflake servers.

```yaml  theme={"system"}
SNOWFLAKE_USER: username
SNOWFLAKE_PASSWORD: password
SNOWFLAKE_ACCOUNT: account_id.region
SNOWFLAKE_DEFAULT_WH: null                  # Optional default warehouse
SNOWFLAKE_DEFAULT_DB: null                  # Optional default database
SNOWFLAKE_DEFAULT_SCHEMA: null              # Optional default schema
SNOWFLAKE_PRIVATE_KEY_PASSPHRASE: null      # Optional private key passphrase
SNOWFLAKE_PRIVATE_KEY_PATH: null            # Optional private key path
SNOWFLAKE_ROLE: null                        # Optional role name
SNOWFLAKE_TIMEOUT: null                     # Optional timeout in seconds
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes settings for connecting to Snowflake data warehouse.
The following arguments must be provided to the connector, all other
arguments are optional.

*Required Arguments*:

* `user (str)`: Username for the Snowflake user.
* `password (str)`: Login Password for the user.
* `account (str)`: Snowflake account identifier (including region, excluding `snowflake-computing.com` suffix).

*Optional Arguments*:

* `verbose (bool)`: Specify whether to print verbose output.
* `database (str)`: Name of the default database to use. If unspecified no database is selected on login.
* `schema (str)`: Name of the default schema to use. If unspecified no schema is selected on login.
* `warehouse (str)`: Name of the default warehouse to use. If unspecified no warehouse is selected on login.

<h3> Attributes </h3>

* *conn* (`snowflake.connector.Connection`) - underlying [Snowflake Connection](https://docs.snowflake.com/en/user-guide/python-connector-api.html#object-connection) object

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Snowflake`
Creates Snowflake data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `verbose (bool)`: Enables verbose output printing. Defaults to False.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`Snowflake`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to Snowflake server.

***commit*** - `commit()`

Saves all changes made to the warehouse since the previous transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected Snowflake warehouse. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the Snowflake warehouse.
  * `**kwargs`: Additional parameters to pass to the query. See [Snowflake Connector Docs](https://docs.snowflake.com/en/user-guide/python-connector-api.html#execute) for additional parameters.

***export*** - `export(df: DataFrame, table_name: str, database: str, schema: str, if_exists: str, **kwargs) -> None`

Exports a Pandas data frame to a Snowflake warehouse based on the table name. If table doesn't exist, the table is automatically created.

Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:

  * `df (DataFrame)`: Data frame to export to a Snowflake warehouse.

  * `table_name (str)`: Name of the table to export data to (excluding database and schema).

  * `database (str)`: Name of the database in which the table is located.

  * `schema (str)`: Name of the schema in which the table is located.

  * `if_exists (str, optional)`: Specifies export policy if table exists. Either

    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.

    Defaults to `'append'`.

  * `**kwargs`: Additional arguments to pass to writer. See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) for details on UPSERT (`unique_constraints`, `unique_conflict_method`) and other advanced options.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from Snowflake into a Pandas data frame based on the query given. This will fail unless a `SELECT` query is provided.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse using `execute`.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `*args, **kwargs`: Additional parameters to pass to the query. See [Snowflake Connector Docs](https://docs.snowflake.com/en/user-guide/python-connector-api.html#execute) for additional parameters.
* **Returns**: (`DataFrame`) Data frame containing the queried data

***open*** - `open()`

Opens a connection to Snowflake servers.

***rollback*** - `rollback()`

Rolls back (deletes) all database changes made since the last transaction.

***sample*** - `sample(schema: str, table: str, size: int, **kwargs) -> DataFrame`

Sample data from a table in the Snowflake warehouse. Sample is not guaranteed to be random.

* **Args**:

  * `schema (str)`: The schema to select the table from.
  * `size (int)`: The number of rows to sample. Defaults to 10,000,000.
  * `table (str)`: The table to sample from in the connected database.

* **Returns**: (`DataFrame`) Sampled data from the data frame.

## Redshift

`mage_ai.io.redshift.Redshift`

Handles data transfer between a Redshift cluster and the Mage app. Mage uses temporary credentials to authenticate access to a Redshift cluster. There are two ways to specify these credentials:

1. Pre-generate temporary credentials and specify them in the configuration settings. Add the following keys to the configuration settings for `Redshift` to use the temporary credentials:
   ```yaml  theme={"system"}
   REDSHIFT_DBNAME: Name of Redshift database to connect to
   REDSHIFT_HOST: Redshift Cluster hostname
   REDSHIFT_PORT: Redshift Cluster port. Optional, defaults to 5439
   REDSHIFT_TEMP_CRED_USER: Redshift temp credentials username
   REDSHIFT_TEMP_CRED_PASSWORD: Redshift temp credentials password
   ```
2. Provide an IAM Profile to automatically generate temporary credentials for connection. The IAM profile is read from `~/.aws/` and is used with the `GetClusterCredentials` endpoint to generate temporary credentials. Add the following keys to the configuration settings for `Redshift` to generate temporary credentials

   ```yaml  theme={"system"}
   REDSHIFT_DBNAME: Name of Redshift database to connect to
   REDSHIFT_DBUSER: Redshift database user to generate credentials for
   REDSHIFT_CLUSTER_ID: Redshift cluster ID
   REDSHIFT_IAM_PROFILE: Name of the IAM profile to generate temp credentials with
   ```

   If an IAM profile is not setup using `aws configure`, manually specify the AWS credentials in the configuration settings as well.

   ```yaml  theme={"system"}
   AWS_ACCESS_KEY_ID: AWS Access Key ID credential
   AWS_SECRET_ACCESS_KEY: AWS Secret Access Key credential
   AWS_SESSION_TOKEN: AWS Session Token (used to generate temp DB credentials)
   AWS_REGION: AWS Region
   ```

<h3> Constructor </h3>

`__init__(**kwargs)`

* **Args**

  * `verbose`: Enables verbose output. Defaults to `False`.

  See other keyword arguments in [Redshift's Python connector](https://docs.aws.amazon.com/redshift/latest/mgmt/python-configuration-options.html) docs.

<h3> Attributes </h3>

* *conn* (`redshift_connector.Connection`) - the underlying [Redshift Connection](https://docs.aws.amazon.com/redshift/latest/mgmt/python-api-reference.html#python-api-connection) object.

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Redshift`

Initializes Redshift client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor.
* **Returns**: (`Redshift`) Redshift data loading client constructed using this method

***with\_temporary\_credentials*** - `with_temporary_credentials(database: str, host: str, user: str, password: str, port: int = 5439, **kwargs) -> Redshift`

Creates a Redshift data loader with temporary database credentials.

* **Args**:
  * `database (str)`: Name of the database to connect to.
  * `host (str)`: The hostname of the Redshift cluster which the database belongs to.
  * `user (str)`: Temporary credentials username for use in authentication.
  * `password (str)`: Temporary credentials password for use in authentication.
  * `port (int, optional)`: Port number of the Redshift cluster. Defaults to 5439.
  * `**kwargs`: Additional parameters passed to the loader constructor.
* **Returns**: (`Redshift`) Redshift data loading client constructed using this method

***with\_iam*** - `with_iam(cluster_identifier: str, database: str, db_user: str, profile: str, **kwargs) -> Redshift`

Creates a Redshift data loader using an IAM profile from `~/.aws`.

The IAM Profile settings can also be manually specified as keyword arguments to this constructor, but is not recommended. If credentials are manually specified, the region of the Redshift cluster must also be specified.

* **Args**:
  * `cluster_identifier (str)`: Identifier of the cluster to connect to.
  * `database (str)`: The database to connect to within the specified cluster.
  * `db_user (str)`: Database username
  * `profile (str, optional)`: The profile to use from stored credentials file.
    Defaults to 'default'.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`Redshift`) Redshift data loading client constructed using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to the Redshift cluster specified in the loader configuration.

***commit*** - `commit()`

Saves all changes made to the database since the last transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected Redshift cluster. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the Redshift cluster.
  * `**kwargs`: Additional parameters to pass to the query. See [`redshift-connector` docs](https://github.com/aws/amazon-redshift-python-driver#configuring-cursor-paramstyle) for configuring query parameters.

***export*** - `export(df: DataFrame, table_name: str) -> None`

Exports a Pandas data frame to a Redshift cluster under the specified table. The changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `df (DataFrame)`: Data frame to export to database in Redshift cluster.
  * `table_name (str)`: Name of the table to export the data to. Table must already exist.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse using `execute`.

* **Args**:

  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `*args, **kwargs`: Additional parameters to send to query, including parameters
    for use with format strings. See [`redshift-connector` docs](https://github.com/aws/amazon-redshift-python-driver#configuring-cursor-paramstyle) for configuring query parameters.

* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to the Redshift cluster specified in the loader configuration.

***rollback*** - `rollback()`

Rolls back (deletes) all database changes made since the last transaction.

***sample*** - `sample(schema: str, table: str, size: int, **kwargs) -> DataFrame`

Sample data from a table in the selected database in the Redshift cluster. Sample is not guaranteed to be random.

* **Args**:

  * `schema (str)`: The schema to select the table from.
  * `size (int)`: The number of rows to sample. Defaults to 10,000,000.
  * `table (str)`: The table to sample from in the connected database.

* **Returns**: (`DataFrame`) Sampled data from the table.

## MSSQL

`mage_ai.io.mssql.MSSQL`

Handles data transfer between a Microsoft SQL Server database and the Mage app. The `MSSQL` client utilizes the following keys to connect to the database.

```yaml  theme={"system"}
MSSQL_DATABASE: MSSQL database name
MSSQL_USER: MSSQL database login username
MSSQL_PASSWORD: MSSQL database login password
MSSQL_HOST: MSSQL database hostname
MSSQL_PORT: MSSQL database port (defaults to 1433)
MSSQL_SCHEMA: MSSQL database schema (defaults to 'dbo')
MSSQL_AUTHENTICATION: Authentication method (optional)
MSSQL_CONNECTION_METHOD: Connection method ('direct' or 'ssh_tunnel')
MSSQL_SSH_HOST: SSH tunnel host (if using SSH tunnel)
MSSQL_SSH_PORT: SSH tunnel port
MSSQL_SSH_USERNAME: SSH tunnel username
MSSQL_SSH_PASSWORD: SSH tunnel password
MSSQL_SSH_PKEY: SSH tunnel private key path
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the MSSQL data loading client.

* **Args**:
  * `database (str)`: The name of the database to connect to.
  * `user (str)`: The user for connecting to the database with.
  * `password (str)`: The login password for the user.
  * `host (str)`: Host address for database.
  * `port (int)`: Port on which the database is running. Defaults to 1433.
  * `schema (str)`: Schema name. Defaults to 'dbo'.
  * `authentication (str, optional)`: Authentication method.
  * `connection_method (str)`: Connection method ('direct' or 'ssh\_tunnel'). Defaults to 'direct'.
  * `ssh_host (str, optional)`: SSH tunnel host.
  * `ssh_port (int, optional)`: SSH tunnel port.
  * `ssh_username (str, optional)`: SSH tunnel username.
  * `ssh_password (str, optional)`: SSH tunnel password.
  * `ssh_pkey (str, optional)`: SSH tunnel private key path.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> MSSQL`

Creates MSSQL data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`MSSQL`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to MSSQL database.

***commit*** - `commit()`

Saves all changes made to the database since the previous transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected MSSQL database. Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the MSSQL database.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, schema_name: str, table_name: str, if_exists: str, index: bool, **kwargs) -> None`

Exports data frame to the MSSQL database from a Pandas data frame. If table doesn't exist, the table is automatically created.

Any changes made to the database will not be saved unless `commit()` is called afterward.

* **Args**:
  * `df (DataFrame)`: Data frame to export to the MSSQL database.
  * `schema_name (str)`: Name of the schema in which the table is located. Defaults to 'dbo'.
  * `table_name (str)`: Name of the table to export data to.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `index (bool)`: If `True`, the data frame index is also exported alongside the table. Defaults to `False`.
  * `**kwargs`: Additional arguments to pass to the writer. See the [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) section for details on using options such as `unique_constraints`, `unique_conflict_method`, and other advanced export options.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to MSSQL database.

***rollback*** - `rollback()`

Rolls back (deletes) all database changes made since the last transaction.

## ClickHouse

`mage_ai.io.clickhouse.ClickHouse`

Handles data transfer between a ClickHouse data warehouse and the Mage app. The `ClickHouse` client utilizes the following keys to authenticate access and connect to ClickHouse servers.

```yaml  theme={"system"}
CLICKHOUSE_HOST: ClickHouse hostname
CLICKHOUSE_PORT: ClickHouse port
CLICKHOUSE_USERNAME: ClickHouse username
CLICKHOUSE_PASSWORD: ClickHouse password
CLICKHOUSE_DATABASE: ClickHouse database name
CLICKHOUSE_INTERFACE: ClickHouse interface (optional)
CLICKHOUSE_SSL_CA_CERT: Path to CA certificate for SSL (optional)
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the ClickHouse data loading client.

* **Args**:
  * `host (str)`: ClickHouse hostname.
  * `port (int)`: ClickHouse port.
  * `username (str)`: ClickHouse username.
  * `password (str)`: ClickHouse password.
  * `database (str)`: Database name. Defaults to 'default'.
  * `interface (str, optional)`: ClickHouse interface.
  * `secure (bool, optional)`: Enable SSL.
  * `ca_cert (str, optional)`: Path to CA certificate.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings passed to ClickHouse client

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> ClickHouse`

Creates ClickHouse data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`ClickHouse`) The constructed dataloader using this method

<h3> Methods </h3>

***execute*** - `execute(command_string: str, **kwargs) -> None`

Sends command to the connected ClickHouse warehouse.

* **Args**:
  * `command_string (str)`: Command to execute on the ClickHouse warehouse.
  * `**kwargs`: Additional arguments to pass to command.

***load*** - `load(query_string: str, limit: int, **kwargs) -> DataFrame`

Loads data from ClickHouse into a Pandas data frame based on the query given. This will fail if the query returns no data from the database. When a select query is provided, this function will load at maximum 10,000,000 rows of data. To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded dataframe to. Defaults to 10,000,000.
  * `**kwargs`: Additional arguments to pass to query.
* **Returns**: (`DataFrame`) Data frame associated with the given query.

***export*** - `export(df: DataFrame, table_name: str, database: str, if_exists: str, **kwargs) -> None`

Exports a Pandas data frame to a ClickHouse warehouse. If table doesn't exist, the table is automatically created.

* **Args**:
  * `df (DataFrame)`: Data frame to export to ClickHouse warehouse.
  * `table_name (str)`: Name of the table to export data to.
  * `database (str)`: Name of the database in which the table is located.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `**kwargs`: Advanced export parameters. See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases). (UPSERT not supported.)

## SQLite

`mage_ai.io.sqlite.SQLite`

Handles data transfer between a SQLite database and the Mage app.

<h3> Constructor </h3>

`__init__(self, database: str, verbose: bool = True, **kwargs)`

Initializes the SQLite data loading client.

* **Args**:
  * `database (str)`: Path to the SQLite database file.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> SQLite`

Creates SQLite data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`SQLite`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to SQLite database.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected SQLite database.

* **Args**:
  * `query_string (str)`: The query to execute on the SQLite database.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, table_name: str, if_exists: str, index: bool, **kwargs) -> None`

Exports data frame to the SQLite database from a Pandas data frame. If table doesn't exist, the table is automatically created.

* **Args**:
  * `df (DataFrame)`: Data frame to export to the SQLite database.
  * `table_name (str)`: Name of the table to export data to.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `index (bool)`: If `True`, the data frame index is also exported alongside the table. Defaults to `False`.
  * `**kwargs`: Advanced export options such as `unique_constraints`, `unique_conflict_method`, `overwrite_types`, `auto_clean_name`, etc. See the [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) section for details.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from the results of a query into a Pandas data frame. This will fail if the query returns no data from the database.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to SQLite database.

## Trino

`mage_ai.io.trino.Trino`

Handles data transfer between a Trino data warehouse and the Mage app. The `Trino` client utilizes the following keys to authenticate access and connect to Trino servers.

```yaml  theme={"system"}
TRINO_CATALOG: Trino catalog name
TRINO_HOST: Trino hostname
TRINO_PORT: Trino port (defaults to 8080)
TRINO_USER: Trino username
TRINO_PASSWORD: Trino password
TRINO_SCHEMA: Trino schema name
```

<h3> Constructor </h3>

`__init__(self, catalog: str, host: str, user: str, password: str = None, port: int = 8080, schema: str = None, verbose: bool = True, **kwargs)`

Initializes the Trino data loading client.

* **Args**:
  * `catalog (str)`: Trino catalog name.
  * `host (str)`: Trino hostname.
  * `user (str)`: Trino username.
  * `password (str, optional)`: Trino password.
  * `port (int)`: Trino port. Defaults to 8080.
  * `schema (str, optional)`: Trino schema name.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Trino`

Creates Trino data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`Trino`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to Trino warehouse.

***commit*** - `commit()`

Saves all changes made to the warehouse since the previous transaction.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected Trino warehouse. Any changes made to the warehouse will not be saved unless `commit()` is called afterward.

* **Args**:
  * `query_string (str)`: The query to execute on the Trino warehouse.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, table_name: str, schema: str, if_exists: str, **kwargs) -> None`

Exports a Pandas data frame to a Trino warehouse. If table doesn't exist, the table is automatically created.

Any changes made to the warehouse will not be saved unless `commit()` is called afterward.

* **Args**:
  * `df (DataFrame)`: Data frame to export to Trino warehouse.
  * `table_name (str)`: Name of the table to export data to.
  * `schema (str)`: Name of the schema in which the table is located.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `**kwargs`: Advanced export parameters. See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases). (UPSERT not supported.)

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from Trino into a Pandas data frame based on the query given. This will fail if the query returns no data from the warehouse.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to Trino warehouse.

***rollback*** - `rollback()`

Rolls back (deletes) all warehouse changes made since the last transaction.

## MongoDB

`mage_ai.io.mongodb.MongoDB`

Handles data transfer between a MongoDB database and the Mage app. The `MongoDB` client utilizes the following keys to connect to the database.

```yaml  theme={"system"}
MONGODB_CONNECTION_STRING: MongoDB connection string (alternative to individual settings)
MONGODB_HOST: MongoDB hostname
MONGODB_PORT: MongoDB port (defaults to 27017)
MONGODB_USER: MongoDB username
MONGODB_PASSWORD: MongoDB password
MONGODB_DATABASE: MongoDB database name
MONGODB_COLLECTION: MongoDB collection name
```

<h3> Constructor </h3>

`__init__(self, connection_string: str = None, host: str = None, port: int = 27017, user: str = None, password: str = None, database: str = None, collection: str = None, verbose: bool = True, **kwargs)`

Initializes the MongoDB data loading client.

* **Args**:
  * `connection_string (str, optional)`: MongoDB connection string. If provided, other connection parameters are ignored.
  * `host (str, optional)`: MongoDB hostname.
  * `port (int, optional)`: MongoDB port. Defaults to 27017.
  * `user (str, optional)`: MongoDB username.
  * `password (str, optional)`: MongoDB password.
  * `database (str, optional)`: MongoDB database name.
  * `collection (str, optional)`: MongoDB collection name.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> MongoDB`

Creates MongoDB data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`MongoDB`) The constructed dataloader using this method

<h3> Methods </h3>

***load*** - `load(collection: str = None, query: Dict = None, **kwargs) -> DataFrame`

Loads the data frame from the MongoDB collection.

* **Args**:
  * `collection (str, optional)`: MongoDB collection name. Defaults to collection specified in constructor.
  * `query (Dict, optional)`: Filter the result by using a query object. Examples:
    `{ "address": "Park Lane 38" }`, `{ "address": { "$gt": "S" } }`
* **Returns**: (`DataFrame`) Data frame object loaded from the MongoDB collection.

***export*** - `export(data: Union[DataFrame, List[Dict]], collection: str = None, **kwargs) -> None`

Exports the input dataframe to the MongoDB collection.

* **Args**:
  * `data (Union[DataFrame, List[Dict]])`: Data frame or List of Dictionary to export.
  * `collection (str, optional)`: MongoDB collection name. Defaults to collection specified in constructor.

## Databricks SQL

<ProOnly source="databricks" />

`mage_ai.io.databricks_sql.DatabricksSQL`

Handles data transfer between a Databricks SQL warehouse and the Mage app. The `DatabricksSQL` client utilizes the following keys to authenticate access and connect to Databricks.

```yaml  theme={"system"}
DATABRICKS_ACCESS_TOKEN: Databricks access token
DATABRICKS_HOST: Databricks workspace hostname
DATABRICKS_HTTP_PATH: Databricks SQL warehouse HTTP path
DATABRICKS_DATABASE: Databricks database/catalog name
DATABRICKS_SCHEMA: Databricks schema name
```

<h3> Constructor </h3>

`__init__(self, verbose: bool = True, **kwargs)`

Initializes the Databricks SQL data loading client.

* **Args**:
  * `access_token (str)`: Databricks access token (required).
  * `host (str)`: Databricks workspace hostname (required).
  * `http_path (str)`: Databricks SQL warehouse HTTP path (required).
  * `database (str, optional)`: Database/catalog name.
  * `schema (str, optional)`: Schema name.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating connection

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> DatabricksSQL`

Creates Databricks SQL data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`DatabricksSQL`) The constructed dataloader using this method

<h3> Methods </h3>

***close*** - `close()`

Closes connection to Databricks SQL warehouse.

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected Databricks SQL warehouse.

* **Args**:
  * `query_string (str)`: The query to execute on the Databricks SQL warehouse.
  * `**kwargs`: Additional parameters to pass to the query.

***export*** - `export(df: DataFrame, table_name: str, database: str, schema: str, if_exists: str, **kwargs) -> None`

Exports a Pandas data frame to a Databricks SQL warehouse. If table doesn't exist, the table is automatically created.

* **Args**:
  * `df (DataFrame)`: Data frame to export to Databricks SQL warehouse.
  * `table_name (str)`: Name of the table to export data to.
  * `database (str)`: Name of the database/catalog in which the table is located.
  * `schema (str)`: Name of the schema in which the table is located.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `**kwargs`: See [Advanced Export Parameters](#advanced-export-parameters-for-sql-databases) for available options.

***load*** - `load(query_string: str, limit: int, *args, **kwargs) -> DataFrame`

Loads data from Databricks SQL into a Pandas data frame based on the query given. This will fail if the query returns no data from the warehouse.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in warehouse.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional parameters to pass to the query.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***open*** - `open()`

Opens a connection to Databricks SQL warehouse.

## Spark

`mage_ai.io.spark.Spark`

Handles data transfer between a Spark session and the Mage app. The `Spark` client utilizes the following keys to connect to Spark.

```yaml  theme={"system"}
SPARK_HOST: Spark host/master URL
SPARK_METHOD: Spark connection method
SPARK_SCHEMA: Spark database/schema name
```

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the Spark data loading client.

* **Args**:
  * `host (str)`: Spark master URL (e.g., 'local', 'spark://host:port').
  * `method (str, optional)`: Spark connection method.
  * `database (str, optional)`: Database/schema name.
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings for creating Spark session

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> Spark`

Creates Spark data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`Spark`) The constructed dataloader using this method

<h3> Methods </h3>

***execute*** - `execute(query_string: str, **kwargs) -> None`

Sends query to the connected Spark session.

* **Args**:
  * `query_string (str)`: Query to execute on the Spark session.
  * `**kwargs`: Additional arguments to pass to query.

***load*** - `load(query_string: str, limit: int, **kwargs) -> DataFrame`

Loads data from Spark into a Pandas data frame based on the query given. This will fail if the query returns no data.

This function will load at maximum 10,000,000 rows of data (this limit is configurable). To operate on more data, consider performing data transformations in Spark.

* **Args**:
  * `query_string (str)`: Query to fetch a table or subset of a table.
  * `limit (int, Optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs`: Additional arguments to pass to query.
* **Returns**: (`DataFrame`) Data frame containing the queried data.

***export*** - `export(df: DataFrame, table_name: str, database: str, if_exists: str, **kwargs) -> None`

Exports a Pandas data frame to a Spark session. If table doesn't exist, the table is automatically created.

* **Args**:
  * `df (DataFrame)`: Data frame to export to Spark session.
  * `table_name (str)`: Name of the table to export data to.
  * `database (str)`: Name of the database in which the table is located.
  * `if_exists (ExportWritePolicy)`: Specifies export policy if table exists. Either
    * `'fail'`: throw an error.
    * `'replace'`: drops existing table and creates new table of same name.
    * `'append'`: appends data frame to existing table.
      Defaults to `'replace'`.
  * `**kwargs`: Additional arguments to pass to writer.

## Azure Data Lake Storage

<ProOnly source="azure-data-lake-storage" />

`mage_ai.io.azure_data_lake_storage.AzureDataLakeStorage`

Handles data transfer between an Azure Data Lake Storage Gen2 container and the Mage app. Supports loading files of the following types:

* CSV
* JSON
* Parquet

To authenticate access to Azure Data Lake Storage, the following environment variables must be set:

* `AZURE_CLIENT_ID`
* `AZURE_CLIENT_SECRET`
* `AZURE_TENANT_ID`
* `AZURE_STORAGE_ACCOUNT_NAME`

By default, these correspond to variables of the same name in `io_config.yaml`.

<h3> Constructor </h3>

`__init__(self, verbose: bool = True, **kwargs)`

Initializes data loader from an Azure Data Lake Storage Gen2 container.

* **Args**:
  * `storage_account_name (str)`: Azure Storage account name (required).
  * `verbose (bool)`: Enables verbose output printing. Defaults to `True`.
  * `**kwargs`: Additional settings. If `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, and `AZURE_TENANT_ID` are provided, they will be used for authentication. Otherwise, DefaultAzureCredential will be used.

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> AzureDataLakeStorage`

Creates AzureDataLakeStorage data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`AzureDataLakeStorage`) The constructed dataloader using this method

<h3> Methods </h3>

***export*** - `export(df: DataFrame, container_name: str, file_path: str, format: FileFormat | str = None, **kwargs) -> None`

Exports data frame to an Azure Data Lake Storage Gen2 container.

* **Args**:
  * `df (DataFrame)`: Data frame to export.
  * `container_name (str)`: Name of the Azure container to export data to.
  * `file_path (str)`: The desired output path of the data in your Azure Data Lake Storage.
  * `format (FileFormat | str, Optional)`: Format of the file to export data frame to. Defaults to `None`, in which case the format is inferred.
  * `**kwargs` - Additional keyword arguments to pass to the file writer. See possible arguments by file formats in [FileIO](#fileio) section.

***load*** - `load(container_name: str, file_path: str, format: FileFormat | str = None, limit: int = QUERY_ROW_LIMIT, **kwargs) -> DataFrame`

Loads data from object in Azure Data Lake Storage Gen2 into a Pandas data frame. This function will load at maximum 10,000,000 rows of data from the specified file (this limit is configurable).

* **Args**:
  * `container_name (str)`: Name of the container to load data from.
  * `file_path (str)`: Path of the file in Azure Data Lake Storage to load data from.
  * `format (FileFormat | str, Optional)`: Format of the file to load data frame from. Defaults to None, in which case the format is inferred.
  * `limit (int, optional)`: The number of rows to limit the loaded data frame to. Defaults to 10,000,000.
  * `**kwargs` - Additional keyword arguments to pass to the file reader. See possible arguments by file formats in [FileIO](#fileio) section.
* **Returns**: (`DataFrame`) Data frame object loaded from data in the specified file.

## Microsoft Fabric Warehouse

<ProOnly source="microsoft-fabric-warehouse" />

`mage_ai.io.microsoft_fabric_warehouse.MicrosoftFabricWarehouse`

Handles data transfer between a Microsoft Fabric Warehouse and the Mage app. This client extends the MSSQL client and uses the same connection methods.

<h3> Constructor </h3>

`__init__(self, **kwargs)`

Initializes the Microsoft Fabric Warehouse data loading client. Uses the same parameters as [MSSQL](#mssql).

<h3> Factory Methods </h3>

***with\_config*** - `with_config(config: BaseConfigLoader, **kwargs) -> MicrosoftFabricWarehouse`

Creates Microsoft Fabric Warehouse data loading client from configuration settings.

* **Args**:
  * `config (BaseConfigLoader)`: Configuration loader object.
  * `**kwargs`: Additional parameters passed to the loader constructor
* **Returns**: (`MicrosoftFabricWarehouse`) The constructed dataloader using this method

# Configuration Settings

Connections to third-party data storage require you to specify confidential information such as login information or access keys. While you can manually specify this information code while constructing data loading clients, it is recommended to not store the secrets directly in code.

Instead, Mage provides **configuration loaders** which allow data loading clients to use your secrets without explicitly writing them in code.

<Warning>
  Currently Mage only supports AWS Secrets Manager as a configuration loader. If you need to use secrets from Azure Key Vault
  or GCP Secret Manager, you can reference the following docs:

  * [Azure Key Vault](https://docs.mage.ai/production/deploying-to-cloud/secrets/Azure)
  * [GCP Secret Manager](https://docs.mage.ai/production/deploying-to-cloud/secrets/GCP)
</Warning>

Currently, the following sources (and their corresponding configuration loader) can be used to load configuration settings:

* Configuration File - `ConfigFileLoader`
* Environment Variables - `EnvironmentVariableLoader`
* AWS Secrets Manager - `AWSSecretLoader`

For example, the code below constructs a Redshift data loading client using secrets stored in AWS Secrets Manager

```python  theme={"system"}
from mage_ai.io.config import AWSSecretLoader
from mage_ai.io.redshift import Redshift

config = AWSSecretLoader()
loader = Redshift.from_config(config)
```

The following are the set of allowed key names that you must name your secrets with in order for Mage's configuration loaders to recognize your secrets. In code you can refer to these keys by their string name or using the `mage_ai.io.config.ConfigKey` enum. Not all keys need be specified at once - only use the keys related to the services you utilize.

| Key Name                               | Service                                         | Client Constructor Parameter | Description                                                             | Notes                                                                                                |
| -------------------------------------- | ----------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **AWS General**                        |                                                 |                              |                                                                         |                                                                                                      |
| AWS\_ACCESS\_KEY\_ID                   | AWS General                                     | -                            | AWS Access Key ID credential                                            | Used by [Redshift](#redshift) and [S3](#s3)                                                          |
| AWS\_SECRET\_ACCESS\_KEY               | AWS General                                     | -                            | AWS Secret Access Key credential                                        | Used by [Redshift](#redshift) and [S3](#s3)                                                          |
| AWS\_SESSION\_TOKEN                    | AWS General                                     | -                            | AWS Session Token (used to generate temporary DB credentials)           | Used by Redshift                                                                                     |
| AWS\_REGION                            | AWS General                                     | -                            | AWS Region                                                              | Used by [Redshift](#redshift) and [S3](#s3)                                                          |
| AWS\_ENDPOINT                          | AWS General                                     | -                            | AWS endpoint URL                                                        | Used by [S3](#s3). Optional                                                                          |
| **AWS Redshift**                       |                                                 |                              |                                                                         |                                                                                                      |
| REDSHIFT\_DBNAME                       | [AWS Redshift](#redshift)                       | database                     | Name of Redshift database to connect to                                 |                                                                                                      |
| REDSHIFT\_HOST                         | [AWS Redshift](#redshift)                       | host                         | Redshift Cluster hostname                                               | Use with temporary credentials                                                                       |
| REDSHIFT\_PORT                         | [AWS Redshift](#redshift)                       | port                         | Redshift Cluster port. Optional, defaults to 5439.                      | Use with temporary credentials                                                                       |
| REDSHIFT\_SCHEMA                       | [AWS Redshift](#redshift)                       | schema                       | Redshift schema name                                                    | Optional                                                                                             |
| REDSHIFT\_TEMP\_CRED\_USER             | [AWS Redshift](#redshift)                       | user                         | Redshift temporary credentials username.                                | Use with temporary credentials                                                                       |
| REDSHIFT\_TEMP\_CRED\_PASSWORD         | [AWS Redshift](#redshift)                       | password                     | Redshift temporary credentials password.                                | Use with temporary credentials                                                                       |
| REDSHIFT\_DBUSER                       | [AWS Redshift](#redshift)                       | db\_user                     | Redshift database user to generate credentials for.                     | Use to generate temporary credentials                                                                |
| REDSHIFT\_CLUSTER\_ID                  | [AWS Redshift](#redshift)                       | cluster\_identifier          | Redshift cluster ID                                                     | Use to generate temporary credentials                                                                |
| REDSHIFT\_IAM\_PROFILE                 | [AWS Redshift](#redshift)                       | profile                      | Name of the IAM profile to generate temporary credentials with          | Use to generate temporary credentials                                                                |
| **PostgreSQL**                         |                                                 |                              |                                                                         |                                                                                                      |
| POSTGRES\_DBNAME                       | [PostgreSQL](#postgresql)                       | dbname                       | Database name                                                           |                                                                                                      |
| POSTGRES\_USER                         | [PostgreSQL](#postgresql)                       | user                         | Database login username                                                 |                                                                                                      |
| POSTGRES\_PASSWORD                     | [PostgreSQL](#postgresql)                       | password                     | Database login password                                                 |                                                                                                      |
| POSTGRES\_HOST                         | [PostgreSQL](#postgresql)                       | host                         | Database hostname                                                       |                                                                                                      |
| POSTGRES\_PORT                         | [PostgreSQL](#postgresql)                       | port                         | PostgreSQL database port                                                |                                                                                                      |
| POSTGRES\_SCHEMA                       | [PostgreSQL](#postgresql)                       | schema                       | PostgreSQL schema name                                                  | Optional                                                                                             |
| POSTGRES\_CONNECTION\_METHOD           | [PostgreSQL](#postgresql)                       | connection\_method           | Connection method ('direct' or 'ssh\_tunnel')                           | Optional                                                                                             |
| POSTGRES\_SSH\_HOST                    | [PostgreSQL](#postgresql)                       | ssh\_host                    | SSH tunnel host                                                         | Optional                                                                                             |
| POSTGRES\_SSH\_PORT                    | [PostgreSQL](#postgresql)                       | ssh\_port                    | SSH tunnel port                                                         | Optional                                                                                             |
| POSTGRES\_SSH\_USERNAME                | [PostgreSQL](#postgresql)                       | ssh\_username                | SSH tunnel username                                                     | Optional                                                                                             |
| POSTGRES\_SSH\_PASSWORD                | [PostgreSQL](#postgresql)                       | ssh\_password                | SSH tunnel password                                                     | Optional                                                                                             |
| POSTGRES\_SSH\_PKEY                    | [PostgreSQL](#postgresql)                       | ssh\_pkey                    | SSH tunnel private key path                                             | Optional                                                                                             |
| POSTGRES\_SSL\_MODE                    | [PostgreSQL](#postgresql)                       | sslmode                      | SSL mode                                                                | Optional                                                                                             |
| POSTGRES\_SSL\_ROOTCERT                | [PostgreSQL](#postgresql)                       | sslrootcert                  | SSL root certificate path                                               | Optional                                                                                             |
| POSTGRES\_SSL\_CERT                    | [PostgreSQL](#postgresql)                       | sslcert                      | SSL certificate path                                                    | Optional                                                                                             |
| POSTGRES\_SSL\_KEY                     | [PostgreSQL](#postgresql)                       | sslkey                       | SSL key path                                                            | Optional                                                                                             |
| POSTGRES\_CONNECT\_TIMEOUT             | [PostgreSQL](#postgresql)                       | connect\_timeout             | Connection timeout in seconds                                           | Optional                                                                                             |
| **Snowflake**                          |                                                 |                              |                                                                         |                                                                                                      |
| SNOWFLAKE\_USER                        | [Snowflake](#snowflake)                         | user                         | Snowflake username                                                      |                                                                                                      |
| SNOWFLAKE\_PASSWORD                    | [Snowflake](#snowflake)                         | password                     | Snowflake password                                                      |                                                                                                      |
| SNOWFLAKE\_ACCOUNT                     | [Snowflake](#snowflake)                         | account                      | Snowflake account ID (including region)                                 |                                                                                                      |
| SNOWFLAKE\_DEFAULT\_DB                 | [Snowflake](#snowflake)                         | database                     | Default database to use. Optional, no database chosen if unspecified.   |                                                                                                      |
| SNOWFLAKE\_DEFAULT\_SCHEMA             | [Snowflake](#snowflake)                         | schema                       | Default schema to use. Optional, no schema chosen if unspecified.       |                                                                                                      |
| SNOWFLAKE\_DEFAULT\_WH                 | [Snowflake](#snowflake)                         | warehouse                    | Default warehouse to use. Optional, no warehouse chosen if unspecified. |                                                                                                      |
| SNOWFLAKE\_PRIVATE\_KEY\_PASSPHRASE    | [Snowflake](#snowflake)                         | private\_key\_passphrase     | Private key passphrase for key pair authentication                      | Optional                                                                                             |
| SNOWFLAKE\_PRIVATE\_KEY\_PATH          | [Snowflake](#snowflake)                         | private\_key\_path           | Path to private key file for key pair authentication                    | Optional                                                                                             |
| SNOWFLAKE\_ROLE                        | [Snowflake](#snowflake)                         | role                         | Snowflake role name                                                     | Optional                                                                                             |
| SNOWFLAKE\_TIMEOUT                     | [Snowflake](#snowflake)                         | timeout                      | Query timeout in seconds                                                | Optional                                                                                             |
| **Google BigQuery**                    |                                                 |                              |                                                                         |                                                                                                      |
| GOOGLE\_SERVICE\_ACC\_KEY              | [Google BigQuery](#bigquery)                    | credentials\_mapping         | Service account key                                                     |                                                                                                      |
| GOOGLE\_SERVICE\_ACC\_KEY\_FILEPATH    | [Google BigQuery](#bigquery)                    | path\_to\_credentials        | Path to service account key                                             |                                                                                                      |
| GOOGLE\_LOCATION                       | [Google BigQuery](#bigquery)                    | location                     | Google Cloud location                                                   | Optional                                                                                             |
| **MySQL**                              |                                                 |                              |                                                                         |                                                                                                      |
| MYSQL\_DATABASE                        | [MySQL](#mysql)                                 | database                     | MySQL database name                                                     |                                                                                                      |
| MYSQL\_USER                            | [MySQL](#mysql)                                 | user                         | MySQL username                                                          |                                                                                                      |
| MYSQL\_PASSWORD                        | [MySQL](#mysql)                                 | password                     | MySQL password                                                          |                                                                                                      |
| MYSQL\_HOST                            | [MySQL](#mysql)                                 | host                         | MySQL hostname                                                          |                                                                                                      |
| MYSQL\_PORT                            | [MySQL](#mysql)                                 | port                         | MySQL port. Defaults to 3306.                                           |                                                                                                      |
| MYSQL\_CONNECTION\_METHOD              | [MySQL](#mysql)                                 | connection\_method           | Connection method ('direct' or 'ssh\_tunnel')                           | Optional                                                                                             |
| MYSQL\_SSH\_HOST                       | [MySQL](#mysql)                                 | ssh\_host                    | SSH tunnel host                                                         | Optional                                                                                             |
| MYSQL\_SSH\_PORT                       | [MySQL](#mysql)                                 | ssh\_port                    | SSH tunnel port                                                         | Optional                                                                                             |
| MYSQL\_SSH\_USERNAME                   | [MySQL](#mysql)                                 | ssh\_username                | SSH tunnel username                                                     | Optional                                                                                             |
| MYSQL\_SSH\_PASSWORD                   | [MySQL](#mysql)                                 | ssh\_password                | SSH tunnel password                                                     | Optional                                                                                             |
| MYSQL\_SSH\_PKEY                       | [MySQL](#mysql)                                 | ssh\_pkey                    | SSH tunnel private key path                                             | Optional                                                                                             |
| **MSSQL**                              |                                                 |                              |                                                                         |                                                                                                      |
| MSSQL\_DATABASE                        | [MSSQL](#mssql)                                 | database                     | MSSQL database name                                                     |                                                                                                      |
| MSSQL\_USER                            | [MSSQL](#mssql)                                 | user                         | MSSQL username                                                          |                                                                                                      |
| MSSQL\_PASSWORD                        | [MSSQL](#mssql)                                 | password                     | MSSQL password                                                          |                                                                                                      |
| MSSQL\_HOST                            | [MSSQL](#mssql)                                 | host                         | MSSQL hostname                                                          |                                                                                                      |
| MSSQL\_PORT                            | [MSSQL](#mssql)                                 | port                         | MSSQL port. Defaults to 1433.                                           |                                                                                                      |
| MSSQL\_SCHEMA                          | [MSSQL](#mssql)                                 | schema                       | MSSQL schema name. Defaults to 'dbo'.                                   |                                                                                                      |
| MSSQL\_AUTHENTICATION                  | [MSSQL](#mssql)                                 | authentication               | Authentication method                                                   | Optional                                                                                             |
| MSSQL\_CONNECTION\_METHOD              | [MSSQL](#mssql)                                 | connection\_method           | Connection method ('direct' or 'ssh\_tunnel')                           | Optional                                                                                             |
| MSSQL\_SSH\_HOST                       | [MSSQL](#mssql)                                 | ssh\_host                    | SSH tunnel host                                                         | Optional                                                                                             |
| MSSQL\_SSH\_PORT                       | [MSSQL](#mssql)                                 | ssh\_port                    | SSH tunnel port                                                         | Optional                                                                                             |
| MSSQL\_SSH\_USERNAME                   | [MSSQL](#mssql)                                 | ssh\_username                | SSH tunnel username                                                     | Optional                                                                                             |
| MSSQL\_SSH\_PASSWORD                   | [MSSQL](#mssql)                                 | ssh\_password                | SSH tunnel password                                                     | Optional                                                                                             |
| MSSQL\_SSH\_PKEY                       | [MSSQL](#mssql)                                 | ssh\_pkey                    | SSH tunnel private key path                                             | Optional                                                                                             |
| MSSQL\_DRIVER                          | [MSSQL](#mssql)                                 | driver                       | ODBC driver name                                                        | Optional                                                                                             |
| **ClickHouse**                         |                                                 |                              |                                                                         |                                                                                                      |
| CLICKHOUSE\_HOST                       | [ClickHouse](#clickhouse)                       | host                         | ClickHouse hostname                                                     |                                                                                                      |
| CLICKHOUSE\_PORT                       | [ClickHouse](#clickhouse)                       | port                         | ClickHouse port                                                         |                                                                                                      |
| CLICKHOUSE\_USERNAME                   | [ClickHouse](#clickhouse)                       | username                     | ClickHouse username                                                     |                                                                                                      |
| CLICKHOUSE\_PASSWORD                   | [ClickHouse](#clickhouse)                       | password                     | ClickHouse password                                                     |                                                                                                      |
| CLICKHOUSE\_DATABASE                   | [ClickHouse](#clickhouse)                       | database                     | ClickHouse database name                                                |                                                                                                      |
| CLICKHOUSE\_INTERFACE                  | [ClickHouse](#clickhouse)                       | interface                    | ClickHouse interface                                                    | Optional                                                                                             |
| CLICKHOUSE\_SSL\_CA\_CERT              | [ClickHouse](#clickhouse)                       | ca\_cert                     | Path to CA certificate for SSL                                          | Optional                                                                                             |
| **Trino**                              |                                                 |                              |                                                                         |                                                                                                      |
| TRINO\_CATALOG                         | [Trino](#trino)                                 | catalog                      | Trino catalog name                                                      |                                                                                                      |
| TRINO\_HOST                            | [Trino](#trino)                                 | host                         | Trino hostname                                                          |                                                                                                      |
| TRINO\_PORT                            | [Trino](#trino)                                 | port                         | Trino port. Defaults to 8080.                                           |                                                                                                      |
| TRINO\_USER                            | [Trino](#trino)                                 | user                         | Trino username                                                          |                                                                                                      |
| TRINO\_PASSWORD                        | [Trino](#trino)                                 | password                     | Trino password                                                          | Optional                                                                                             |
| TRINO\_SCHEMA                          | [Trino](#trino)                                 | schema                       | Trino schema name                                                       | Optional                                                                                             |
| **Databricks SQL**                     |                                                 |                              |                                                                         |                                                                                                      |
| DATABRICKS\_ACCESS\_TOKEN              | [Databricks SQL](#databricks-sql)               | access\_token                | Databricks access token                                                 |                                                                                                      |
| DATABRICKS\_HOST                       | [Databricks SQL](#databricks-sql)               | host                         | Databricks workspace hostname                                           |                                                                                                      |
| DATABRICKS\_HTTP\_PATH                 | [Databricks SQL](#databricks-sql)               | http\_path                   | Databricks SQL warehouse HTTP path                                      |                                                                                                      |
| DATABRICKS\_DATABASE                   | [Databricks SQL](#databricks-sql)               | database                     | Databricks database/catalog name                                        | Optional                                                                                             |
| DATABRICKS\_SCHEMA                     | [Databricks SQL](#databricks-sql)               | schema                       | Databricks schema name                                                  | Optional                                                                                             |
| **Spark**                              |                                                 |                              |                                                                         |                                                                                                      |
| SPARK\_HOST                            | [Spark](#spark)                                 | host                         | Spark master URL                                                        |                                                                                                      |
| SPARK\_METHOD                          | [Spark](#spark)                                 | method                       | Spark connection method                                                 | Optional                                                                                             |
| SPARK\_SCHEMA                          | [Spark](#spark)                                 | database                     | Spark database/schema name                                              | Optional                                                                                             |
| **MongoDB**                            |                                                 |                              |                                                                         |                                                                                                      |
| MONGODB\_CONNECTION\_STRING            | [MongoDB](#mongodb)                             | connection\_string           | MongoDB connection string                                               | Alternative to individual settings                                                                   |
| MONGODB\_HOST                          | [MongoDB](#mongodb)                             | host                         | MongoDB hostname                                                        |                                                                                                      |
| MONGODB\_PORT                          | [MongoDB](#mongodb)                             | port                         | MongoDB port. Defaults to 27017.                                        |                                                                                                      |
| MONGODB\_USER                          | [MongoDB](#mongodb)                             | user                         | MongoDB username                                                        |                                                                                                      |
| MONGODB\_PASSWORD                      | [MongoDB](#mongodb)                             | password                     | MongoDB password                                                        |                                                                                                      |
| MONGODB\_DATABASE                      | [MongoDB](#mongodb)                             | database                     | MongoDB database name                                                   |                                                                                                      |
| MONGODB\_COLLECTION                    | [MongoDB](#mongodb)                             | collection                   | MongoDB collection name                                                 | Optional                                                                                             |
| **OracleDB**                           |                                                 |                              |                                                                         |                                                                                                      |
| ORACLEDB\_USER                         | [OracleDB](#oracledb)                           | user                         | OracleDB username                                                       |                                                                                                      |
| ORACLEDB\_PASSWORD                     | [OracleDB](#oracledb)                           | password                     | OracleDB password                                                       |                                                                                                      |
| ORACLEDB\_HOST                         | [OracleDB](#oracledb)                           | host                         | OracleDB hostname                                                       |                                                                                                      |
| ORACLEDB\_PORT                         | [OracleDB](#oracledb)                           | port                         | OracleDB port                                                           |                                                                                                      |
| ORACLEDB\_SERVICE                      | [OracleDB](#oracledb)                           | service                      | OracleDB service name                                                   |                                                                                                      |
| ORACLEDB\_MODE                         | [OracleDB](#oracledb)                           | mode                         | OracleDB mode ('thin' or 'thick')                                       | Optional                                                                                             |
| **DuckDB**                             |                                                 |                              |                                                                         |                                                                                                      |
| DUCKDB\_DATABASE                       | [DuckDB](#duckdb)                               | database                     | DuckDB database path                                                    |                                                                                                      |
| DUCKDB\_SCHEMA                         | [DuckDB](#duckdb)                               | schema                       | DuckDB schema name. Defaults to 'main'.                                 | Optional                                                                                             |
| MOTHERDUCK\_TOKEN                      | [DuckDB](#duckdb)                               | -                            | MotherDuck authentication token                                         | Optional                                                                                             |
| **SQLite**                             |                                                 |                              |                                                                         |                                                                                                      |
| SQLITE                                 | [SQLite](#sqlite)                               | database                     | SQLite database file path                                               |                                                                                                      |
| **Azure**                              |                                                 |                              |                                                                         |                                                                                                      |
| AZURE\_CLIENT\_ID                      | Azure Services                                  | client\_id                   | Azure AD application client ID                                          | Used by [Azure Blob Storage](#azureblobstorage), [Azure Data Lake Storage](#azure-data-lake-storage) |
| AZURE\_CLIENT\_SECRET                  | Azure Services                                  | client\_secret               | Azure AD application client secret                                      | Used by [Azure Blob Storage](#azureblobstorage), [Azure Data Lake Storage](#azure-data-lake-storage) |
| AZURE\_TENANT\_ID                      | Azure Services                                  | tenant\_id                   | Azure AD tenant ID                                                      | Used by [Azure Blob Storage](#azureblobstorage), [Azure Data Lake Storage](#azure-data-lake-storage) |
| AZURE\_STORAGE\_ACCOUNT\_NAME          | Azure Services                                  | storage\_account\_name       | Azure Storage account name                                              | Used by [Azure Blob Storage](#azureblobstorage), [Azure Data Lake Storage](#azure-data-lake-storage) |
| **Microsoft Fabric**                   |                                                 |                              |                                                                         |                                                                                                      |
| MICROSOFT\_FABRIC\_WAREHOUSE\_NAME     | [Microsoft Fabric](#microsoft-fabric-warehouse) | warehouse\_name              | Microsoft Fabric warehouse name                                         |                                                                                                      |
| MICROSOFT\_FABRIC\_WAREHOUSE\_ENDPOINT | [Microsoft Fabric](#microsoft-fabric-warehouse) | endpoint                     | Microsoft Fabric warehouse endpoint                                     |                                                                                                      |
| MICROSOFT\_FABRIC\_WAREHOUSE\_SCHEMA   | [Microsoft Fabric](#microsoft-fabric-warehouse) | schema                       | Microsoft Fabric warehouse schema                                       | Optional                                                                                             |

## Configuration Loader APIs

This section contains the exact APIs and more detailed information on the configuration loaders. Every configuration loader has two functions:

* `contains` - checks if the configuration source contains the requested key. Commonly, the `in` operation is used to check for setting existence (but is not always identical as `contains` can accept multiple parameters while the `in` keyword only accepts the key).

  ```python  theme={"system"}
  if config.contains(ConfigKey.POSTGRES_PORT):
      ...
  # alternatively
  if ConfigKey.POSTGRES_PORT in config:
      ...
  ```

* `get` - gets the configuration setting associated with the given key. If the key doesn't exist, returns None. Commonly, the data model overload `__getitem__` is used to fetch a configuration setting (but is not always identical as `get` can accept multiple parameters while `__getitem__` does not).

  ```python  theme={"system"}
  user = config.get(ConfigKey.REDSHIFT_DBUSER)
  # alternatively
  user = config[ConfigKey.REDSHIFT_DBUSER]
  ```

These functions are shared among all configuration loaders, but depending on the source some function signatures may differ.

### Configuration File

Loads configuration settings from a configuration file.

For detailed information about creating and managing `io_config.yaml` files, see the [IO Config Setup documentation](/development/io_config_setup).

**Example**:

```python  theme={"system"}
from mage_ai.io.config import ConfigKey, ConfigFileLoader

config = ConfigFileLoader('path/to/my/io_config.yaml', 'my_profile')
postgres_db = config[ConfigKey.POSTGRES_DBNAME]
```

**Constructor**: `__init__(filepath: os.PathLike, profile: str)`
Initializes IO Configuration loader. Input configuration file can have two formats:

* *Standard*: contains a subset of the configuration keys specified in `ConfigKey`. This
  is the default and recommended format. Below is an example configuration file using this format.
  ```yaml  theme={"system"}
  version: 0.1.0
  default:
      AWS_ACCESS_KEY_ID: AWS Access Key ID credential
      AWS_SECRET_ACCESS_KEY: AWS Secret Access Key credential
      AWS_REGION: AWS Region
      REDSHIFT_DBNAME: Name of Redshift database to connect to
      REDSHIFT_HOST: Redshift Cluster hostname
      REDSHIFT_PORT: Redshift Cluster port. Optional, defaults to 5439
      REDSHIFT_TEMP_CRED_USER: Redshift temp credentials username
      REDSHIFT_TEMP_CRED_PASSWORD: Redshift temp credentials password
  ```
  The above configuration file has a single **profile** named `'default'`. Each profile organizes a set of keys to use (for example, distinguishing production keys versus development keys). A configuration file can have multiple profiles.
* *Verbose*: Instead of configuration keys, each profile stores an object of settings associated with
  each data migration client. This format was used in previous versions of this tool, and exists
  for backwards compatibility. Below is an example configuration file using this format.
  ```yaml  theme={"system"}
  version: 0.0.0
  default:
      AWS:
          Redshift:
              database: Name of Redshift database to connect to
              host: Redshift Cluster hostname
              port: Redshift Cluster port. Optional, defaults to 5439
              user: Redshift temp credentials username
              password: Redshift temp credentials password
          access_key_id: AWS Access Key ID credential
          secret_access_key: AWS Secret Access Key credential
          region: AWS Region
  ```

Use handlebars and `env_var` syntax to reference environment variables in either configuration file format.

```yaml  theme={"system"}
version: 0.1.0
default:
    GOOGLE_SERVICE_ACC_KEY_FILEPATH: "{{ env_var('GOOGLE_APPLICATION_CREDENTIALS') }}"
```

**Args**:

* `filepath (os.PathLike, optional)`: Path to IO configuration file. Defaults to `'[repo_path]/io_config.yaml'`
* `profile (str, optional)`: Profile to load configuration settings from. Defaults to `'default'`.

**Methods**

***contains*** - `contains(self, key: ConfigKey | str) -> Any`

Checks if the configuration setting stored under `key` is contained.

* **Args**:
  * `key (str)`: Name of the configuration setting to check.
* **Returns** (`bool`) Returns `True` if configuration setting exists, otherwise returns `False`.

***get*** - `get(self, key: ConfigKey | str) -> Any`

Loads the configuration setting stored under `key`.

* **Args**:
  * `key (str)`: Key name of the configuration setting to load
* **Returns**: (`Any`) Configuration setting corresponding to the given key

### Environment Variables

Loads configuration settings from environment variables in your current environment.

**Example**:

```python  theme={"system"}
from mage_ai.io.config import ConfigKey, EnvironmentVariableLoader

config = EnvironmentVariableLoader()
postgres_db = config[ConfigKey.POSTGRES_DBNAME]
```

**Constructor** : `__init__(self)` - no parameters for construction.

**Methods**:

***contains*** - `contains(env_var: ConfigKey | str) -> bool`

Checks if the environment variable given by `env_var` exists.

* **Args**:

  * `key (ConfigKey | str)`: Name of the configuration setting to check existence of.

* **Returns** (`bool`) Returns `True` if configuration setting exists, otherwise returns `False`.

***get*** - `get(env_var: ConfigKey | str) -> Any`

Loads the config setting stored under the environment variable `env_var`.

* **Args**:

  * `env_var (str)`: Name of the environment variable to load configuration setting from

* **Returns**: (`Any`) The configuration setting stored under `env_var`

### AWS Secret Loader

Loads secrets from AWS Secrets Manager. To authenticate access to AWS Secrets Manager, either

* Configure your AWS profile using the AWS CLI
  ```bash  theme={"system"}
  aws configure
  ```
* Manually specify your AWS Credentials when constructing the configuration loader
  `python config = AWSSecretLoader( aws_access_key_id = 'your access key id', aws_secret_access_key = 'your secret key', region_name = 'your region' ) `

**Example**:

```python  theme={"system"}
from mage_ai.io.config import ConfigKey, AWSSecretLoader

config = AWSSecretLoader()
postgres_db = config[ConfigKey.POSTGRES_DBNAME]
# with finer control on version
postgres_db = config.get(ConfigKey.POSTGRES_DBNAME, version_id='my_version_id')
```

**Constructor** : `__init__(self, **kwargs)`:

* **Keyword Arguments**:
  * `aws_access_key_id (str, Optional)`: AWS access key ID credential.
  * `aws_secret_access_key (str, Optional)`: AWS secret access key credential.
  * `region_name (str, Optional)`: AWS region which Secrets Manager is created in.

**Methods**:

***contains*** - `contains( secret_id: ConfigKey | str, version_id: str, version_stage_label : str) -> bool`
Check if there is a secret with ID `secret_id` contained. Can also specify the version of the
secret to check. If

* both `version_id` and `version_stage_label` are specified, both must agree on the secret version.
* neither of `version_id` or `version_stage_label` are specified, any version is checked.
* one of `version_id` and `version_stage_label` are specified, the associated version is checked.

When using the `in` operator, comparisons to specific versions are not allowed.

* **Args**:
  * `secret_id (str)`: ID of the secret to load
  * `version_id (str, Optional)`: ID of the version of the secret to load. Defaults to `None`.
  * `version_stage_label (str, Optional)`: Staging label of the version of the secret to load. Defaults to `None`.
* **Returns**: (`bool`) Returns true if secret exists, otherwise returns false.

***get*** - `get(secret_id: ConfigKey | str, version_id: str, version_stage_label : str) -> bytes | str`
Loads the secret stored under `secret_id`. Can also specify the version of the
secret to fetch. If

* both `version_id` and `version_stage_label` are specified, both must agree on the secret version.
* neither of `version_id` or `version_stage_label` are specified, the current version is loaded.
* one of `version_id` and `version_stage_label` are specified, the associated version is loaded.

When using the `__getitem__` overload, comparisons to specific versions are not allowed.

* **Args**:

  * `secret_id (str)`: ID of the secret to load
  * ` version_id (str, Optional)`: ID of the version of the secret to load. Defaults to `None`.
  * `version_stage_label (str, Optional)`: Staging label of the version of the secret to load. Defaults to `None`.

* **Returns**: (`bytes | str`) The secret stored under `secret_id` in AWS secret manager. If secret is a binary value, returns a `bytes` object; else returns a `string` object


Built with [Mintlify](https://mintlify.com).