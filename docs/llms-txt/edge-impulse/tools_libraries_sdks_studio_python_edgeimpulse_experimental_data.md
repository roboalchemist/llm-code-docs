# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/experimental/data/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.experimental.data

## Functions

### delete\_all\_samples

```python  theme={"system"}
edgeimpulse.experimental.data.delete_all_samples(
	category: str | None = None,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse | None
```

Delete all samples in a given category.

If category is set to `None`, all samples in the project are deleted.

| Parameters    |                        |
| ------------- | ---------------------- |
| `category`    | `str \| None = None`   |
| `api_key`     | `str \| None = None`   |
| `timeout_sec` | `float \| None = None` |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse \| None` |

### delete\_sample\_by\_id

```python  theme={"system"}
edgeimpulse.experimental.data.delete_sample_by_id(
	sample_id: int,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse | None
```

Delete a particular sample from a project given the sample ID.

| Parameters    |                        |
| ------------- | ---------------------- |
| `sample_id`   | `int`                  |
| `api_key`     | `str \| None = None`   |
| `timeout_sec` | `float \| None = None` |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse \| None` |

### delete\_samples\_by\_filename

```python  theme={"system"}
edgeimpulse.experimental.data.delete_samples_by_filename(
	filename: str,
	category: str | None = None,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> Tuple[Any | None, ...]
```

Delete any samples from an Edge Impulse project that match the given filename.

Note: the `filename` argument must not include the original extension. For example,
if you uploaded a file named `my-image.01.png`, you must provide the `filename` as
`my-image.01`.

| Parameters    |                        |
| ------------- | ---------------------- |
| `filename`    | `str`                  |
| `category`    | `str \| None = None`   |
| `api_key`     | `str \| None = None`   |
| `timeout_sec` | `float \| None = None` |

| Returns                   |
| ------------------------- |
| `Tuple[Any \| None, ...]` |

### download\_samples\_by\_ids

```python  theme={"system"}
edgeimpulse.experimental.data.download_samples_by_ids(
	sample_ids: int | List[int],
	api_key: str | None = None,
	timeout_sec: float | None = None,
	max_workers: int | None = None,
	show_progress: bool | None = False,
	pool_maxsize: int | None = 20,
	pool_connections: int | None = 20
) ‑> List[edgeimpulse.data.sample_type.Sample]
```

Download samples by their associated IDs from an Edge Impulse project.

Downloaded sample data is returned as a `DownloadSample` object, which contains the raw data in
a BytesIO object along with associated metadata.

**Important!** All time series data is returned as a JSON file (in BytesIO format)
with a timestamp column. This includes files originally uploaded as CSV, JSON, and
CBOR. Edge Impulse Studio removes the timestamp column from any uploaded CSV
files and computes an estimated sample rate. The timestamps are computed based on
the sample rate, will always start at 0, and will be in milliseconds. These
timestamps may not be the same as the original timestamps in the uploaded file.

| Parameters         |                        |
| ------------------ | ---------------------- |
| `sample_ids`       | `int \| List[int]`     |
| `api_key`          | `str \| None = None`   |
| `timeout_sec`      | `float \| None = None` |
| `max_workers`      | `int \| None = None`   |
| `show_progress`    | `bool \| None = False` |
| `pool_maxsize`     | `int \| None = 20`     |
| `pool_connections` | `int \| None = 20`     |

| Returns                                     |
| ------------------------------------------- |
| `List[edgeimpulse.data.sample_type.Sample]` |

### get\_filename\_by\_id

```python  theme={"system"}
edgeimpulse.experimental.data.get_filename_by_id(
	sample_id: int,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> str | None
```

Given an ID for a sample in a project, return the filename associated with that sample.

Note that while multiple samples can have the same filename, each sample has a
unique sample ID that is provided by Studio when the sample is uploaded.

| Parameters    |                        |
| ------------- | ---------------------- |
| `sample_id`   | `int`                  |
| `api_key`     | `str \| None = None`   |
| `timeout_sec` | `float \| None = None` |

| Returns       |
| ------------- |
| `str \| None` |

### get\_sample\_ids

```python  theme={"system"}
edgeimpulse.experimental.data.get_sample_ids(
	filename: str | None = None,
	category: str | None = None,
	labels: str | None = None,
	api_key: str | None = None,
	num_workers: int | None = 4,
	timeout_sec: float | None = None
) ‑> List[edgeimpulse.data.sample_type.SampleInfo]
```

Get the sample IDs and filenames for all samples in a project, filtered by category, labels, or filename.

Note that filenames are given by the root of the filename when uploaded.
For example, if you upload `my-image.01.png`, it will be stored in your project with
a hash such as `my-image.01.png.4f262n1b.json`. To find the ID(s) that match this
sample, you must provide the argument `filename=my-image.01`. Notice the lack of
extension and hash.

Because of the potential for multiple samples (i.e., different sample IDs) with the
same filename, we recommend providing unique filenames for your samples when
uploading.

| Parameters    |                        |
| ------------- | ---------------------- |
| `filename`    | `str \| None = None`   |
| `category`    | `str \| None = None`   |
| `labels`      | `str \| None = None`   |
| `api_key`     | `str \| None = None`   |
| `num_workers` | `int \| None = 4`      |
| `timeout_sec` | `float \| None = None` |

| Returns                                         |
| ----------------------------------------------- |
| `List[edgeimpulse.data.sample_type.SampleInfo]` |

### infer\_category\_and\_label\_from\_filename

```python  theme={"system"}
edgeimpulse.experimental.data.infer_category_and_label_from_filename(
	sample: edgeimpulse.data.sample_type.Sample,
	file: str
) ‑> None
```

Extract label and category information from the filename and assigns them to the sample object.

Files should look like this `my-dataset/training/wave.1.cbor` where `wave` is the label and `training` is the category.
It checks if there is `training`, `testing` or `anomaly` in the filename to determine the sample category.

| Parameters |                                       |
| ---------- | ------------------------------------- |
| `sample`   | `edgeimpulse.data.sample_type.Sample` |
| `file`     | `str`                                 |

| Returns |
| ------- |
| `None`  |

### numpy\_timeseries\_to\_sample

```python  theme={"system"}
edgeimpulse.experimental.data.numpy_timeseries_to_sample(
	values,
	sensors: List[edgeimpulse.data.sample_type.Sensor],
	sample_rate_ms: int
) ‑> edgeimpulse.data.sample_type.Sample
```

Convert numpy values to a sample that can be uploaded to Edge Impulse.

| Parameters       |                                             |
| ---------------- | ------------------------------------------- |
| `values`         | ` `                                         |
| `sensors`        | `List[edgeimpulse.data.sample_type.Sensor]` |
| `sample_rate_ms` | `int`                                       |

| Returns                               |
| ------------------------------------- |
| `edgeimpulse.data.sample_type.Sample` |

### pandas\_dataframe\_to\_sample

```python  theme={"system"}
edgeimpulse.experimental.data.pandas_dataframe_to_sample(
	df,
	sample_rate_ms: int | None = None,
	label: str | None = None,
	filename: str | None = None,
	axis_columns: List[str] | None = None,
	metadata: dict | None = None,
	label_col: str | None = None,
	category: Literal['training', 'testing', 'split'] = 'split'
) ‑> edgeimpulse.data.sample_type.Sample
```

Convert a dataframe to a single sample. Can handle both *timeseries* and *non-timeseries* data.

In order to be inferred as timeseries it must have:

* More than one row
* A sample rate or an index from which the sample rate can be inferred
  * Therefore must be monotonically increasing
  * And int or a date

| Parameters       |                                                     |
| ---------------- | --------------------------------------------------- |
| `df`             | ` `                                                 |
| `sample_rate_ms` | `int \| None = None`                                |
| `label`          | `str \| None = None`                                |
| `filename`       | `str \| None = None`                                |
| `axis_columns`   | `List[str] \| None = None`                          |
| `metadata`       | `dict \| None = None`                               |
| `label_col`      | `str \| None = None`                                |
| `category`       | `Literal['training', 'testing', 'split'] = 'split'` |

| Returns                               |
| ------------------------------------- |
| `edgeimpulse.data.sample_type.Sample` |

### stream\_samples\_by\_ids

```python  theme={"system"}
edgeimpulse.experimental.data.stream_samples_by_ids(
	sample_ids: int | Sequence[int],
	api_key: str | None = None,
	timeout_sec: float | None = None,
	max_workers: int | None = None,
	show_progress: bool | None = False,
	pool_maxsize: int | None = 20,
	pool_connections: int | None = 20
) ‑> Generator[edgeimpulse.data.sample_type.Sample, None, None]
```

Download samples by their associated IDs from an Edge Impulse project.

| Parameters         |                        |
| ------------------ | ---------------------- |
| `sample_ids`       | `int \| Sequence[int]` |
| `api_key`          | `str \| None = None`   |
| `timeout_sec`      | `float \| None = None` |
| `max_workers`      | `int \| None = None`   |
| `show_progress`    | `bool \| None = False` |
| `pool_maxsize`     | `int \| None = 20`     |
| `pool_connections` | `int \| None = 20`     |

| Returns                                                      |
| ------------------------------------------------------------ |
| `Generator[edgeimpulse.data.sample_type.Sample, None, None]` |

### upload\_directory

```python  theme={"system"}
edgeimpulse.experimental.data.upload_directory(
	directory: str,
	category: str | None = None,
	label: str | None = None,
	metadata: dict | None = None,
	transform: <built-in function callable> | None = None,
	allow_duplicates: bool | None = False,
	show_progress: bool | None = False,
	batch_size: int | None = 1024
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload a directory of files to Edge Impulse.

Tries to autodetect whether it's an Edge Impulse exported dataset, or a standard directory. The files can be in CBOR, JSON, image, or
WAV file formats. You can read more about the different file formats accepted by the Edge Impulse ingestion service here:

[https://docs.edgeimpulse.com/reference/ingestion-api](https://docs.edgeimpulse.com/reference/ingestion-api)

| Parameters         |                                               |
| ------------------ | --------------------------------------------- |
| `directory`        | `str`                                         |
| `category`         | `str \| None = None`                          |
| `label`            | `str \| None = None`                          |
| `metadata`         | `dict \| None = None`                         |
| `transform`        | `<built-in function callable> \| None = None` |
| `allow_duplicates` | `bool \| None = False`                        |
| `show_progress`    | `bool \| None = False`                        |
| `batch_size`       | `int \| None = 1024`                          |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_exported\_dataset

```python  theme={"system"}
edgeimpulse.experimental.data.upload_exported_dataset(
	directory: str,
	transform: <built-in function callable> | None = None,
	allow_duplicates: bool | None = False,
	show_progress: bool | None = False,
	batch_size: int | None = 1024
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload samples from a downloaded Edge Impulse dataset and preserve the `info.labels` information.

Use this when you've exported your data in the studio, via the `export` functionality.

| Parameters         |                                               |
| ------------------ | --------------------------------------------- |
| `directory`        | `str`                                         |
| `transform`        | `<built-in function callable> \| None = None` |
| `allow_duplicates` | `bool \| None = False`                        |
| `show_progress`    | `bool \| None = False`                        |
| `batch_size`       | `int \| None = 1024`                          |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_numpy

```python  theme={"system"}
edgeimpulse.experimental.data.upload_numpy(
	data,
	labels: List[str],
	sensors: List[edgeimpulse.data.sample_type.Sensor],
	sample_rate_ms: int,
	metadata: dict | None = None,
	category: Literal['training', 'testing', 'split', 'anomaly'] = 'split'
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload numpy arrays as timeseries using the Edge Impulse data acquisition format.

| Parameters       |                                                                |
| ---------------- | -------------------------------------------------------------- |
| `data`           | ` `                                                            |
| `labels`         | `List[str]`                                                    |
| `sensors`        | `List[edgeimpulse.data.sample_type.Sensor]`                    |
| `sample_rate_ms` | `int`                                                          |
| `metadata`       | `dict \| None = None`                                          |
| `category`       | `Literal['training', 'testing', 'split', 'anomaly'] = 'split'` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_pandas\_dataframe

```python  theme={"system"}
edgeimpulse.experimental.data.upload_pandas_dataframe(
	df,
	feature_cols: List[str],
	label_col: str | None = None,
	category_col: str | None = None,
	metadata_cols: List[str] | None = None
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload non-timeseries data to Edge Impulse where each dataframe row becomes a sample.

| Parameters      |                            |
| --------------- | -------------------------- |
| `df`            | ` `                        |
| `feature_cols`  | `List[str]`                |
| `label_col`     | `str \| None = None`       |
| `category_col`  | `str \| None = None`       |
| `metadata_cols` | `List[str] \| None = None` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_pandas\_dataframe\_wide

```python  theme={"system"}
edgeimpulse.experimental.data.upload_pandas_dataframe_wide(
	df,
	sample_rate_ms: int,
	data_col_start: int | None = None,
	label_col: str | None = None,
	category_col: str | None = None,
	metadata_cols: List[str] | None = None,
	data_col_length: int | None = None,
	data_axis_cols: List[str] | None = None
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload a dataframe to Edge Impulse where each column represents a value in the timeseries data and the rows become the individual samples.

| Parameters        |                            |
| ----------------- | -------------------------- |
| `df`              | ` `                        |
| `sample_rate_ms`  | `int`                      |
| `data_col_start`  | `int \| None = None`       |
| `label_col`       | `str \| None = None`       |
| `category_col`    | `str \| None = None`       |
| `metadata_cols`   | `List[str] \| None = None` |
| `data_col_length` | `int \| None = None`       |
| `data_axis_cols`  | `List[str] \| None = None` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_pandas\_dataframe\_with\_group

```python  theme={"system"}
edgeimpulse.experimental.data.upload_pandas_dataframe_with_group(
	df,
	timestamp_col: str,
	group_by: str,
	feature_cols: List[str],
	label_col: str | None = None,
	category_col: str | None = None,
	metadata_cols: List[str] | None = None
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload a dataframe where the rows contain multiple samples and timeseries data for those samples.

It uses a `group_by` in order to detect what timeseries value belongs
to which sample.

| Parameters      |                            |
| --------------- | -------------------------- |
| `df`            | ` `                        |
| `timestamp_col` | `str`                      |
| `group_by`      | `str`                      |
| `feature_cols`  | `List[str]`                |
| `label_col`     | `str \| None = None`       |
| `category_col`  | `str \| None = None`       |
| `metadata_cols` | `List[str] \| None = None` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_pandas\_sample

```python  theme={"system"}
edgeimpulse.experimental.data.upload_pandas_sample(
	df,
	label: str | None = None,
	sample_rate_ms: int | None = None,
	filename: str | None = None,
	axis_columns: List[str] | None = None,
	metadata: dict | None = None,
	label_col: str | None = None,
	category: Literal['training', 'testing', 'split'] = 'split'
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload a single dataframe sample.

Upload a single dataframe sample to Edge Impulse.

| Parameters       |                                                     |
| ---------------- | --------------------------------------------------- |
| `df`             | ` `                                                 |
| `label`          | `str \| None = None`                                |
| `sample_rate_ms` | `int \| None = None`                                |
| `filename`       | `str \| None = None`                                |
| `axis_columns`   | `List[str] \| None = None`                          |
| `metadata`       | `dict \| None = None`                               |
| `label_col`      | `str \| None = None`                                |
| `category`       | `Literal['training', 'testing', 'split'] = 'split'` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_plain\_directory

```python  theme={"system"}
edgeimpulse.experimental.data.upload_plain_directory(
	directory: str,
	category: str | None = None,
	label: str | None = None,
	metadata: dict | None = None,
	transform: <built-in function callable> | None = None,
	allow_duplicates: bool | None = False,
	show_progress: bool | None = False,
	batch_size: int | None = 1024
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload a directory of files to Edge Impulse.

The samples can be in CBOR, JSON, image, or WAV file formats.

| Parameters         |                                               |
| ------------------ | --------------------------------------------- |
| `directory`        | `str`                                         |
| `category`         | `str \| None = None`                          |
| `label`            | `str \| None = None`                          |
| `metadata`         | `dict \| None = None`                         |
| `transform`        | `<built-in function callable> \| None = None` |
| `allow_duplicates` | `bool \| None = False`                        |
| `show_progress`    | `bool \| None = False`                        |
| `batch_size`       | `int \| None = 1024`                          |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

### upload\_samples

```python  theme={"system"}
edgeimpulse.experimental.data.upload_samples(
	samples: edgeimpulse.data.sample_type.Sample | List[edgeimpulse.data.sample_type.Sample],
	allow_duplicates: bool | None = False,
	api_key: str | None = None,
	timeout_sec: float | None = None,
	max_workers: int | None = None,
	show_progress: bool | None = False,
	pool_maxsize: int | None = 20,
	pool_connections: int | None = 20
) ‑> edgeimpulse.data.sample_type.UploadSamplesResponse
```

Upload one or more samples to an Edge Impulse project using the ingestion service.

Each sample must be wrapped in a `Sample` object, which contains metadata about that sample.
Give this function a single `Sample` or a List of `Sample` objects to upload to your
project. The `data` field of the `Sample` must be a raw binary stream, such as a BufferedIOBase
object (which you can create with the `open(..., "rb")` function).

| Parameters         |                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------- |
| `samples`          | `edgeimpulse.data.sample_type.Sample \| List[edgeimpulse.data.sample_type.Sample]` |
| `allow_duplicates` | `bool \| None = False`                                                             |
| `api_key`          | `str \| None = None`                                                               |
| `timeout_sec`      | `float \| None = None`                                                             |
| `max_workers`      | `int \| None = None`                                                               |
| `show_progress`    | `bool \| None = False`                                                             |
| `pool_maxsize`     | `int \| None = 20`                                                                 |
| `pool_connections` | `int \| None = 20`                                                                 |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse.data.sample_type.UploadSamplesResponse` |

## Classes

### Sample

```python  theme={"system"}
edgeimpulse.experimental.data.Sample(
	data: io.BufferedIOBase | _io.StringIO | str,
	filename: str | None = None,
	category: Literal['training', 'testing', 'anomaly', 'split'] | None = 'split',
	label: str | None = None,
	bounding_boxes: List[dict] | None = None,
	metadata: dict | None = None,
	sample_id: int | None = None,
	structured_labels: List[dict] | None = None
)
```

Wrapper class for sample data, labels, and associated metadata.

Sample data should be contained in a file or file-like object, for example, as the return from `open(..., "rb")`. The
`upload_samples()` function expects Sample objects as input.

| Parameters          |                                                                        |
| ------------------- | ---------------------------------------------------------------------- |
| `data`              | `io.BufferedIOBase \| _io.StringIO \| str`                             |
| `filename`          | `str \| None = None`                                                   |
| `category`          | `Literal['training', 'testing', 'anomaly', 'split'] \| None = 'split'` |
| `label`             | `str \| None = None`                                                   |
| `bounding_boxes`    | `List[dict] \| None = None`                                            |
| `metadata`          | `dict \| None = None`                                                  |
| `sample_id`         | `int \| None = None`                                                   |
| `structured_labels` | `List[dict] \| None = None`                                            |

| Instance variables  |                                                              |
| ------------------- | ------------------------------------------------------------ |
| `bounding_boxes`    | `List[dict] \| None`                                         |
| `category`          | `Literal['training', 'testing', 'anomaly', 'split'] \| None` |
| `data`              | `io.BufferedIOBase \| _io.StringIO \| str`                   |
| `filename`          | `str \| None`                                                |
| `label`             | `str \| None`                                                |
| `metadata`          | `dict \| None`                                               |
| `sample_id`         | `int \| None`                                                |
| `structured_labels` | `List[dict] \| None`                                         |


Built with [Mintlify](https://mintlify.com).