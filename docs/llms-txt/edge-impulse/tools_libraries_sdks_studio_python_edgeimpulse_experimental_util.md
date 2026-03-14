# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/experimental/util/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.experimental.util

## Functions

### add\_labels\_to\_dataframe

```python  theme={"system"}
edgeimpulse.experimental.util.add_labels_to_dataframe(
	df,
	labels,
	label_col_name='label'
)
```

Adds labels to a DataFrame based on provided label information.

| Parameters               |     |
| ------------------------ | --- |
| `df`                     | ` ` |
| `labels`                 | ` ` |
| `label_col_name='label'` | ` ` |

### convert\_json\_cbor\_to\_dataframe

```python  theme={"system"}
edgeimpulse.experimental.util.convert_json_cbor_to_dataframe(
	data,
	ts_col_name=None
)
```

Converts JSON CBOR data to a pandas DataFrame.

| Parameters         |     |
| ------------------ | --- |
| `data`             | ` ` |
| `ts_col_name=None` | ` ` |

### convert\_sample\_to\_dataframe

```python  theme={"system"}
edgeimpulse.experimental.util.convert_sample_to_dataframe(
	sample,
	label_col_name: str | None = 'label',
	ts_col_name: str | None = None
)
```

Converts a sample to a DataFrame and adds labels if provided.

| Parameters       |                         |
| ---------------- | ----------------------- |
| `sample`         | ` `                     |
| `label_col_name` | `str \| None = 'label'` |
| `ts_col_name`    | `str \| None = None`    |

### fetch\_samples

```python  theme={"system"}
edgeimpulse.experimental.util.fetch_samples(
	filename: str | None = None,
	category: str | None = None,
	labels: str | None = None,
	max_workers=None
)
```

Fetch samples based on the provided parameters and stream them by their IDs.

| Parameters         |                      |
| ------------------ | -------------------- |
| `filename`         | `str \| None = None` |
| `category`         | `str \| None = None` |
| `labels`           | `str \| None = None` |
| `max_workers=None` | ` `                  |

### generate\_labels\_from\_dataframe

```python  theme={"system"}
edgeimpulse.experimental.util.generate_labels_from_dataframe(
	df,
	label_col='label',
	file_name=None
)
```

Generates structured labels from a DataFrame based on transitions in the specified label column.

This function iterates over the rows of a pandas DataFrame and detects changes in the values of
a specified label column. It groups consecutive rows with the same label value, and for each group,
it returns a dictionary containing the start index, end index, and the label. Optionally, the result
can be returned in a dictionary format, compatible with file saving, including the file name.

| Parameters          |     |
| ------------------- | --- |
| `df`                | ` ` |
| `label_col='label'` | ` ` |
| `file_name=None`    | ` ` |


Built with [Mintlify](https://mintlify.com).