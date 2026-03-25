# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/util.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.util

## Functions

### check\_response\_errors

```python  theme={"system"}
edgeimpulse.util.check_response_errors(
	request
)
```

Check for standard errors and raise an exception with the details if found.

| Parameters |     |
| ---------- | --- |
| `request`  | ` ` |

### configure\_generic\_client

```python  theme={"system"}
edgeimpulse.util.configure_generic_client(
	key: str,
	key_type: str | None = 'api',
	host: str | None = 'https://studio.edgeimpulse.com/v1'
) ‑> edgeimpulse_api.api_client.ApiClient
```

Configure generic api client which the right key.

| Parameters |                        |
| ---------- | ---------------------- |
| `key`      | `str`                  |
| `key_type` | `str \| None = 'api'`  |
| `host`     | `str \| None = 'https` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.api_client.ApiClient` |

### connect\_websocket

```python  theme={"system"}
edgeimpulse.util.connect_websocket(
	token,
	host: str = None
) ‑> socketio.client.Client
```

Connects to the websocket server.

Parameters:
token (str): The authentication token.
host (str, optional): The hostname. If None, API\_ENDPOINT will be used.

Returns:
object: Websocket object.

| Parameters |              |
| ---------- | ------------ |
| `token`    | ` `          |
| `host`     | `str = None` |

| Returns                  |
| ------------------------ |
| `socketio.client.Client` |

### default\_project\_id\_for

```python  theme={"system"}
edgeimpulse.util.default_project_id_for(
	client: edgeimpulse_api.api_client.ApiClient
) ‑> int
```

Derive project id from api\_key used to configure generic client.

| Parameters |                                        |
| ---------- | -------------------------------------- |
| `client`   | `edgeimpulse_api.api_client.ApiClient` |

| Returns |
| ------- |
| `int`   |

### encode\_file\_as\_base64

```python  theme={"system"}
edgeimpulse.util.encode_file_as_base64(
	filename: str
)
```

Encode a file as base64.

| Parameters |       |
| ---------- | ----- |
| `filename` | `str` |

### get\_organization\_websocket

```python  theme={"system"}
edgeimpulse.util.get_organization_websocket(
	client,
	organization_id: int,
	host: str = None
) ‑> socketio.client.Client
```

Gets a websocket to listen to organization events.

| Parameters        |              |
| ----------------- | ------------ |
| `client`          | ` `          |
| `organization_id` | `int`        |
| `host`            | `str = None` |

| Returns                  |
| ------------------------ |
| `socketio.client.Client` |

### get\_profile\_devices

```python  theme={"system"}
edgeimpulse.util.get_profile_devices(
	client: edgeimpulse_api.api_client.ApiClient,
	project_id: int | None = None
) ‑> List[str]
```

Pull a list of profile devices.

| Parameters   |                                        |
| ------------ | -------------------------------------- |
| `client`     | `edgeimpulse_api.api_client.ApiClient` |
| `project_id` | `int \| None = None`                   |

| Returns     |
| ----------- |
| `List[str]` |

### get\_project\_deploy\_targets

```python  theme={"system"}
edgeimpulse.util.get_project_deploy_targets(
	client: edgeimpulse_api.api_client.ApiClient,
	project_id: int | None = None
) ‑> List[str]
```

Pull a list of deploy targets.

| Parameters   |                                        |
| ------------ | -------------------------------------- |
| `client`     | `edgeimpulse_api.api_client.ApiClient` |
| `project_id` | `int \| None = None`                   |

| Returns     |
| ----------- |
| `List[str]` |

### get\_project\_websocket

```python  theme={"system"}
edgeimpulse.util.get_project_websocket(
	client,
	project_id: int,
	host: str = None
) ‑> socketio.client.Client
```

Gets a websocket to listen to project events.

| Parameters   |              |
| ------------ | ------------ |
| `client`     | ` `          |
| `project_id` | `int`        |
| `host`       | `str = None` |

| Returns                  |
| ------------------------ |
| `socketio.client.Client` |

### get\_user\_agent

```python  theme={"system"}
edgeimpulse.util.get_user_agent(
	add_platform_info=False
)
```

Get user agent string for API calls so we can track usage.

| Parameters                |     |
| ------------------------- | --- |
| `add_platform_info=False` | ` ` |

### inspect\_model

```python  theme={"system"}
edgeimpulse.util.inspect_model(
	model: pathlib.Path | str | bytes | Any,
	tempdir: str
) ‑> Tuple[str, str]
```

Load tflite model.

| Parameters |                                       |
| ---------- | ------------------------------------- |
| `model`    | `pathlib.Path \| str \| bytes \| Any` |
| `tempdir`  | `str`                                 |

| Returns           |
| ----------------- |
| `Tuple[str, str]` |

### inspect\_representative\_data

```python  theme={"system"}
edgeimpulse.util.inspect_representative_data(
	data: pathlib.Path | str | bytes | Any
) ‑> str | None
```

Ensure representative data is saved to disk for upload.

| Parameters |                                       |
| ---------- | ------------------------------------- |
| `data`     | `pathlib.Path \| str \| bytes \| Any` |

| Returns       |
| ------------- |
| `str \| None` |

### is\_keras\_model

```python  theme={"system"}
edgeimpulse.util.is_keras_model(
	model
)
```

Check if model is a keras model.

| Parameters |     |
| ---------- | --- |
| `model`    | ` ` |

### is\_numpy\_array

```python  theme={"system"}
edgeimpulse.util.is_numpy_array(
	array
)
```

Check if array is a numpy array.

| Parameters |     |
| ---------- | --- |
| `array`    | ` ` |

### is\_onnx\_model

```python  theme={"system"}
edgeimpulse.util.is_onnx_model(
	model
)
```

Check if given model is an onnx model.

| Parameters |     |
| ---------- | --- |
| `model`    | ` ` |

### is\_path\_to\_numpy\_file

```python  theme={"system"}
edgeimpulse.util.is_path_to_numpy_file(
	path
)
```

Check if given path is a numpy file.

| Parameters |     |
| ---------- | --- |
| `path`     | ` ` |

### is\_path\_to\_onnx\_model

```python  theme={"system"}
edgeimpulse.util.is_path_to_onnx_model(
	path
)
```

Check if given path is a onnx file.

| Parameters |     |
| ---------- | --- |
| `path`     | ` ` |

### is\_path\_to\_tf\_saved\_model\_directory

```python  theme={"system"}
edgeimpulse.util.is_path_to_tf_saved_model_directory(
	model_dir
)
```

Check if directory contains a saved model.

| Parameters  |     |
| ----------- | --- |
| `model_dir` | ` ` |

### is\_path\_to\_tf\_saved\_model\_zipped

```python  theme={"system"}
edgeimpulse.util.is_path_to_tf_saved_model_zipped(
	model
)
```

Check if path is poiting to a zipped model.

| Parameters |     |
| ---------- | --- |
| `model`    | ` ` |

### is\_type\_accepted\_by\_open

```python  theme={"system"}
edgeimpulse.util.is_type_accepted_by_open(
	path
)
```

Check if given path is a. string or a `Path`.

| Parameters |     |
| ---------- | --- |
| `path`     | ` ` |

### make\_zip\_archive

```python  theme={"system"}
edgeimpulse.util.make_zip_archive(
	saved_model_path
)
```

Create zip archive from a model path.

| Parameters         |     |
| ------------------ | --- |
| `saved_model_path` | ` ` |

### numpy\_installed

```python  theme={"system"}
edgeimpulse.util.numpy_installed(
	
) ‑> bool
```

Return True if NumPy is installed, otherwise False.

| Returns |
| ------- |
| `bool`  |

### onnx\_installed

```python  theme={"system"}
edgeimpulse.util.onnx_installed(
	
) ‑> bool
```

Return True if ONNX is installed, otherwise False.

| Returns |
| ------- |
| `bool`  |

### pandas\_installed

```python  theme={"system"}
edgeimpulse.util.pandas_installed(
	
) ‑> bool
```

Return True if pandas is installed, otherwise False.

| Returns |
| ------- |
| `bool`  |

### poll

```python  theme={"system"}
edgeimpulse.util.poll(
	jobs_client: edgeimpulse_api.api.jobs_api.JobsApi,
	project_id: int,
	job_id: int,
	timeout_sec: float | None = None
) ‑> edgeimpulse_api.models.get_job_response.GetJobResponse
```

Poll a specific job within a project until done or timmeout is reached.

| Parameters    |                                        |
| ------------- | -------------------------------------- |
| `jobs_client` | `edgeimpulse_api.api.jobs_api.JobsApi` |
| `project_id`  | `int`                                  |
| `job_id`      | `int`                                  |
| `timeout_sec` | `float \| None = None`                 |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_job_response.GetJobResponse` |

### run\_job\_until\_completion

```python  theme={"system"}
edgeimpulse.util.run_job_until_completion(
	ws,
	job_id: int,
	data_cb=None,
	timeout_sec: int | None = None
)
```

Runs a project or organization job until completion.

| Parameters     |                      |
| -------------- | -------------------- |
| `ws`           | ` `                  |
| `job_id`       | `int`                |
| `data_cb=None` | ` `                  |
| `timeout_sec`  | `int \| None = None` |

### run\_organization\_job\_until\_completion

```python  theme={"system"}
edgeimpulse.util.run_organization_job_until_completion(
	organization_id: int,
	job_id: int,
	data_cb=None,
	client=None,
	timeout_sec: int | None = None
) ‑> None
```

Runs an organization job until completion.

| Parameters        |                      |
| ----------------- | -------------------- |
| `organization_id` | `int`                |
| `job_id`          | `int`                |
| `data_cb=None`    | ` `                  |
| `client=None`     | ` `                  |
| `timeout_sec`     | `int \| None = None` |

| Returns |
| ------- |
| `None`  |

### run\_project\_job\_until\_completion

```python  theme={"system"}
edgeimpulse.util.run_project_job_until_completion(
	job_id: int,
	data_cb=None,
	client=None,
	project_id: int | None = None,
	timeout_sec: int | None = None
) ‑> None
```

Runs a project job until completion.

| Parameters     |                      |
| -------------- | -------------------- |
| `job_id`       | `int`                |
| `data_cb=None` | ` `                  |
| `client=None`  | ` `                  |
| `project_id`   | `int \| None = None` |
| `timeout_sec`  | `int \| None = None` |

| Returns |
| ------- |
| `None`  |

### save\_model

```python  theme={"system"}
edgeimpulse.util.save_model(
	model: pathlib.Path | str | bytes,
	directory: str
) ‑> str
```

Save a machine learning model to the specified directory.

| Parameters  |                                |
| ----------- | ------------------------------ |
| `model`     | `pathlib.Path \| str \| bytes` |
| `directory` | `str`                          |

| Returns |
| ------- |
| `str`   |

### save\_representative\_data

```python  theme={"system"}
edgeimpulse.util.save_representative_data(
	data: pathlib.Path | str | bytes,
	directory: str
) ‑> str
```

Save the representive data to a directory.

| Parameters  |                                |
| ----------- | ------------------------------ |
| `data`      | `pathlib.Path \| str \| bytes` |
| `directory` | `str`                          |

| Returns |
| ------- |
| `str`   |

### tensorflow\_installed

```python  theme={"system"}
edgeimpulse.util.tensorflow_installed(
	
) ‑> bool
```

Return True if TensorFlow is installed, otherwise False.

| Returns |
| ------- |
| `bool`  |

### upload\_pretrained\_model\_and\_data

```python  theme={"system"}
edgeimpulse.util.upload_pretrained_model_and_data(
	tempdir: str,
	client: edgeimpulse_api.api_client.ApiClient,
	project_id: int,
	model: pathlib.Path | str | bytes | Any,
	representative_data: pathlib.Path | str | bytes | Any | None = None,
	device: str | None = None,
	timeout_sec: float | None = None
) ‑> edgeimpulse_api.models.get_job_response.GetJobResponse
```

Upload a model and data to Edge Impulse servers.

| Parameters            |                                                      |
| --------------------- | ---------------------------------------------------- |
| `tempdir`             | `str`                                                |
| `client`              | `edgeimpulse_api.api_client.ApiClient`               |
| `project_id`          | `int`                                                |
| `model`               | `pathlib.Path \| str \| bytes \| Any`                |
| `representative_data` | `pathlib.Path \| str \| bytes \| Any \| None = None` |
| `device`              | `str \| None = None`                                 |
| `timeout_sec`         | `float \| None = None`                               |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_job_response.GetJobResponse` |


Built with [Mintlify](https://mintlify.com).