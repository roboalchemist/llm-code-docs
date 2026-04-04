# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/experimental/impulse/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.experimental.impulse

## Functions

### build

```python  theme={"system"}
edgeimpulse.experimental.impulse.build(
	deploy_model_type: str | None = None,
	engine: str = 'tflite',
	deploy_target: str = 'zip',
	output_directory: str | None = None,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> _io.BytesIO
```

Build and download an impulse from Edge Impulse.

Build a model and download it from Edge Impulse. The model can be built for a specific target
and engine. The model can be saved to a file if `output_directory` is provided and the file name
will be derived from the deployment target.

| Parameters          |                        |
| ------------------- | ---------------------- |
| `deploy_model_type` | `str \| None = None`   |
| `engine`            | `str = 'tflite'`       |
| `deploy_target`     | `str = 'zip'`          |
| `output_directory`  | `str \| None = None`   |
| `api_key`           | `str \| None = None`   |
| `timeout_sec`       | `float \| None = None` |

| Returns       |
| ------------- |
| `_io.BytesIO` |


Built with [Mintlify](https://mintlify.com).