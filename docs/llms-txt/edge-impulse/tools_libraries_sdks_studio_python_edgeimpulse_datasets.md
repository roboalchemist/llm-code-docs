# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/datasets/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.datasets

## Functions

### download\_dataset

```python  theme={"system"}
edgeimpulse.datasets.download_dataset(
	name: str,
	force_redownload: bool = False,
	overwrite_existing: bool = False,
	show_progress: bool = False,
	extract_dir: str | None = None
)
```

Download and extract a dataset from the Edge Impulse CDN for tutorials, and quick prototyping.

Saves the dataset in the `datasets/<name>` folder.
Use `list_datasets` to show available datasets for download.

| Parameters           |                      |
| -------------------- | -------------------- |
| `name`               | `str`                |
| `force_redownload`   | `bool = False`       |
| `overwrite_existing` | `bool = False`       |
| `show_progress`      | `bool = False`       |
| `extract_dir`        | `str \| None = None` |

### list\_datasets

```python  theme={"system"}
edgeimpulse.datasets.list_datasets(
	
) ‑> List[dict]
```

List the available datasets on the Edge Impulse CDN.

| Returns      |
| ------------ |
| `List[dict]` |


Built with [Mintlify](https://mintlify.com).