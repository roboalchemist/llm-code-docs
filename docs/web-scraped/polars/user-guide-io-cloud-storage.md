# Source: https://docs.pola.rs/user-guide/io/cloud-storage/

Title: Cloud storage - Polars user guide

URL Source: https://docs.pola.rs/user-guide/io/cloud-storage/

Markdown Content:
Polars can read and write to AWS S3, Azure Blob Storage and Google Cloud Storage. The API is the same for all three storage providers.

To read from cloud storage, additional dependencies may be needed depending on the use case and cloud storage provider:

Python  Rust

```
$ pip install fsspec s3fs adlfs gcsfs
```

```
$ cargo add aws_sdk_s3 aws_config tokio --features tokio/full
```

Reading from cloud storage
--------------------------

Polars supports reading Parquet, CSV, IPC and NDJSON files from cloud storage:

Python  Rust

[`ParquetReader`](https://docs.pola.rs/api/rust/dev/polars/prelude/struct.ParquetReader.html) ·[`CsvReader`](https://docs.pola.rs/api/rust/dev/polars/prelude/struct.CsvReader.html) ·[`IpcReader`](https://docs.pola.rs/api/rust/dev/polars/prelude/struct.IpcReader.html) ·[Available on feature ipc](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag ipc") ·[Available on feature csv](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag csv") ·[Available on feature parquet](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag parquet")

```
use aws_config::BehaviorVersion;
use polars::prelude::*;

#[tokio::main]
async fn main() {
    let bucket = "<YOUR_BUCKET>";
    let path = "<YOUR_PATH>";

    let config = aws_config::load_defaults(BehaviorVersion::latest()).await;
    let client = aws_sdk_s3::Client::new(&config);

    let object = client
        .get_object()
        .bucket(bucket)
        .key(path)
        .send()
        .await
        .unwrap();

    let bytes = object.body.collect().await.unwrap().into_bytes();

    let cursor = std::io::Cursor::new(bytes);
    let df = CsvReader::new(cursor).finish().unwrap();

    println!("{df:?}");
}
```

Scanning from cloud storage with query optimisation
---------------------------------------------------

Using `pl.scan_*` functions to read from cloud storage can benefit from [predicate and projection pushdowns](https://docs.pola.rs/user-guide/lazy/optimizations/), where the query optimizer will apply them before the file is downloaded. This can significantly reduce the amount of data that needs to be downloaded. The query evaluation is triggered by calling `collect`.

Python  Rust

```
import polars as pl

source = "s3://bucket/*.parquet"

df = pl.scan_parquet(source).filter(pl.col("id") < 100).select("id","value").collect()
```

Cloud authentication
--------------------

Polars is able to automatically load default credential configurations for some cloud providers. For cases when this does not happen, it is possible to manually configure the credentials for Polars to use for authentication. This can be done in a few ways:

### Using `storage_options`:

*   Credentials can be passed as configuration keys in a dict with the `storage_options` parameter:

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html)

```
import polars as pl

source = "s3://bucket/*.parquet"

storage_options = {
    "aws_access_key_id": "<secret>",
    "aws_secret_access_key": "<secret>",
    "aws_region": "us-east-1",
}
df = pl.scan_parquet(source, storage_options=storage_options).collect()
```

### Using one of the available `CredentialProvider*` utility classes

*   There may be a utility class `pl.CredentialProvider*` that provides the required authentication functionality. For example, `pl.CredentialProviderAWS` supports selecting AWS profiles, as well as assuming an IAM role:

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html) ·[`CredentialProviderAWS`](https://docs.pola.rs/api/python/stable/reference/api/polars.CredentialProviderAWS.html)

```
lf = pl.scan_parquet(
    "s3://.../...",
    credential_provider=pl.CredentialProviderAWS(
        profile_name="...",
        assume_role={
            "RoleArn": f"...",
            "RoleSessionName": "...",
        }
    ),
)

df = lf.collect()
```

### Using a custom `credential_provider` function

*   Some environments may require custom authentication logic (e.g. AWS IAM role-chaining). For these cases a Python function can be provided for Polars to use to retrieve credentials:

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html)

```
def get_credentials() -> pl.CredentialProviderFunctionReturn:
    expiry = None

    return {
        "aws_access_key_id": "...",
        "aws_secret_access_key": "...",
        "aws_session_token": "...",
    }, expiry

lf = pl.scan_parquet(
    "s3://.../...",
    credential_provider=get_credentials,
)

df = lf.collect()
```

*   Example for Azure:

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html) ·[`CredentialProviderAzure`](https://docs.pola.rs/api/python/stable/reference/api/polars.CredentialProviderAzure.html)

```
def credential_provider():
    credential = DefaultAzureCredential(exclude_managed_identity_credential=True)
    token = credential.get_token("https://storage.azure.com/.default")

    return {"bearer_token": token.token}, token.expires_on

pl.scan_parquet(
    "abfss://...@.../...",
    credential_provider=credential_provider,
)

# Note that for the above case, this shortcut is also available:

pl.scan_parquet(
    "abfss://...@.../...",
    credential_provider=pl.CredentialProviderAzure(
        credential=DefaultAzureCredential(exclude_managed_identity_credential=True)
    ),
)
```

### Set a default credential provider to use

*   It is possible to globally configure a default credential provider, so that it does not need to be passed to every I/O function call. This can be convenient in the case where there are many cloud I/O operations that use the same credential provider.

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html) ·[`CredentialProviderAWS`](https://docs.pola.rs/api/python/stable/reference/api/polars.CredentialProviderAWS.html)

```
pl.Config.set_default_credential_provider(
    pl.CredentialProviderAWS(
        profile_name="...",
        assume_role={
            "RoleArn": f"...",
            "RoleSessionName": "...",
        },
    )
)
```

Cloud retry configuration
-------------------------

*   Retry behavior such as maximum retries and backoff can be configured via `storage_options`:

Python  Rust

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html)

```
import polars as pl

pl.scan_parquet(
    "s3://bucket/*.parquet",
    storage_options={
        "max_retries": 3,
        "retry_timeout_ms": 9873,
        "retry_init_backoff_ms": 9874,
        "retry_max_backoff_ms": 9875,
        "retry_base_multiplier": 3.14159,
    },
)
```

Scanning with PyArrow
---------------------

We can also scan from cloud storage using PyArrow. This is particularly useful for partitioned datasets such as Hive partitioning.

We first create a PyArrow dataset and then create a `LazyFrame` from the dataset.

Python  Rust

[`scan_pyarrow_dataset`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_pyarrow_dataset.html)

```
import polars as pl
import pyarrow.dataset as ds

dset = ds.dataset("s3://my-partitioned-folder/", format="parquet")
(
    pl.scan_pyarrow_dataset(dset)
    .filter(pl.col("foo") == "a")
    .select(["foo", "bar"])
    .collect()
)
```

Writing to cloud storage
------------------------

`DataFrame`s can also be written to cloud storage by passing a cloud URL:

Python  Rust

[`write_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_parquet.html)

```
import polars as pl

df = pl.DataFrame(
    {
        "foo": ["a", "b", "c", "d", "d"],
        "bar": [1, 2, 3, 4, 5],
    }
)

destination = "s3://bucket/my_file.parquet"

df.write_parquet(destination)
```

Note that `DataFrame`s can also be written to any Python file object that supports writes. This can be helpful for performing operations that are not yet natively supported, e.g. writing a compressed CSV directly to cloud:

Python  Rust

[`write_csv`](https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_csv.html)

```
import polars as pl
import s3fs
import gzip

df = pl.DataFrame(
    {
        "foo": ["a", "b", "c", "d", "d"],
        "bar": [1, 2, 3, 4, 5],
    }
)

destination = "s3://bucket/my_file.csv.gz"

fs = s3fs.S3FileSystem()

with fs.open(destination, "wb") as cloud_f:
    with gzip.open(cloud_f, "w") as f:
        df.write_csv(f)
```
