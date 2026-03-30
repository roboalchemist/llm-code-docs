# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/model/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.model

## Modules

* [edgeimpulse.model.input\_type](/tools/libraries/sdks/studio/python/edgeimpulse/model/input_type)
* [edgeimpulse.model.model\_info](/tools/libraries/sdks/studio/python/edgeimpulse/model/model_info)
* [edgeimpulse.model.output\_type](/tools/libraries/sdks/studio/python/edgeimpulse/model/output_type)

## Functions

### deploy

```python  theme={"system"}
edgeimpulse.model.deploy(
	model: pathlib.Path | str | bytes | Any,
	model_output_type: edgeimpulse.model.output_type.Classification | edgeimpulse.model.output_type.Regression | edgeimpulse.model.output_type.ObjectDetection,
	model_input_type: edgeimpulse.model.input_type.ImageInput | edgeimpulse.model.input_type.AudioInput | edgeimpulse.model.input_type.TimeSeriesInput | edgeimpulse.model.input_type.OtherInput | None = None,
	representative_data_for_quantization: pathlib.Path | str | bytes | Any | None = None,
	deploy_model_type: str | None = None,
	engine: str = 'tflite',
	deploy_target: str = 'zip',
	output_directory: str | None = None,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> _io.BytesIO
```

Transform a machine learning model into a library for an edge device.

Transforms a trained model into a library, package, or firmware ready to deploy on an embedded
device. Can optionally apply post-training quantization if a representative data sample is
uploaded.

Supported model formats:

* `Keras Model instance <https://www.tensorflow.org/api_docs/python/tf/keras/Model>`\_
* `TensorFlow SavedModel <https://www.tensorflow.org/guide/saved_model>`\_ (as path to directory
  or `.zip` file)
* `ONNX model file <https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-onnx-model>`\_
  (as path to `.onnx` file)
* `TensorFlow Lite file <https://www.tensorflow.org/lite/guide>`\_ (as bytes, or path to any file
  that is not `.zip` or `.onnx`)

Representative data for quantization:

* Must be a numpy array or `.npy` file.
* Each element must have the same shape as your model's input.
* Must be representative of the range (maximum and minimum) of values in your training data.

Note: the available deployment options will change depending on the values given
for `model`, `model_output_type`, and `model_input_type`. For example, the `openmv`
deployment option is only available if `model_input_type` is set to `ImageInput`. If
you attempt to deploy to an unavailable target, you will receive the error `Could
not deploy: deploy_target: ...`.

| Parameters                             |                                                                                                                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                | `pathlib.Path \| str \| bytes \| Any`                                                                                                                                                          |
| `model_output_type`                    | `edgeimpulse.model.output_type.Classification \| edgeimpulse.model.output_type.Regression \| edgeimpulse.model.output_type.ObjectDetection`                                                    |
| `model_input_type`                     | `edgeimpulse.model.input_type.ImageInput \| edgeimpulse.model.input_type.AudioInput \| edgeimpulse.model.input_type.TimeSeriesInput \| edgeimpulse.model.input_type.OtherInput \| None = None` |
| `representative_data_for_quantization` | `pathlib.Path \| str \| bytes \| Any \| None = None`                                                                                                                                           |
| `deploy_model_type`                    | `str \| None = None`                                                                                                                                                                           |
| `engine`                               | `str = 'tflite'`                                                                                                                                                                               |
| `deploy_target`                        | `str = 'zip'`                                                                                                                                                                                  |
| `output_directory`                     | `str \| None = None`                                                                                                                                                                           |
| `api_key`                              | `str \| None = None`                                                                                                                                                                           |
| `timeout_sec`                          | `float \| None = None`                                                                                                                                                                         |

| Returns       |
| ------------- |
| `_io.BytesIO` |

### list\_deployment\_targets

```python  theme={"system"}
edgeimpulse.model.list_deployment_targets(
	api_key: str | None = None
) ‑> List[str]
```

List suitable deployment targets for the project associated with configured or provided api key.

| Parameters |                      |
| ---------- | -------------------- |
| `api_key`  | `str \| None = None` |

| Returns     |
| ----------- |
| `List[str]` |

### list\_engines

```python  theme={"system"}
edgeimpulse.model.list_engines(
	
) ‑> List[str]
```

List all the engines that can be passed to `deploy()`'s `engine` parameter.

Returns:
List\[str]: List of engines

| Returns     |
| ----------- |
| `List[str]` |

### list\_model\_types

```python  theme={"system"}
edgeimpulse.model.list_model_types(
	
) ‑> List[str]
```

List all the model types that can passed to `deploy()`'s `deploy_model_type` parameter.

Returns:
List\[str]: List of model types

| Returns     |
| ----------- |
| `List[str]` |

### list\_profile\_devices

```python  theme={"system"}
edgeimpulse.model.list_profile_devices(
	api_key: str | None = None
) ‑> List[str]
```

List possible values for the `device` field when calling `edgeimpulse.model.profile()`.

| Parameters |                      |
| ---------- | -------------------- |
| `api_key`  | `str \| None = None` |

| Returns     |
| ----------- |
| `List[str]` |

### profile

```python  theme={"system"}
edgeimpulse.model.profile(
	model: pathlib.Path | str | bytes | Any,
	device: str | None = None,
	api_key: str | None = None,
	timeout_sec: float | None = None
) ‑> edgeimpulse.model._functions.profile.ProfileResponse
```

Profile the performance of a trained model on a range of embedded targets, or a specific device.

The response includes estimates of memory usage and latency for the model across a range of
targets, including low-end MCU, high-end MCU, high-end MCU with accelerator, microprocessor unit
(MPU), and a GPU or neural network accelerator. It will also include details of any conditions
that preclude operation on a given type of device.

If you request a specific `device`, the results will also include estimates for that specific
device. A list of devices can be obtained from `edgeimpulse.model.list_profile_devices()`.

You can call `.summary()` on the response to obtain a more readable version of the most relevant
information.

| Parameters    |                                       |
| ------------- | ------------------------------------- |
| `model`       | `pathlib.Path \| str \| bytes \| Any` |
| `device`      | `str \| None = None`                  |
| `api_key`     | `str \| None = None`                  |
| `timeout_sec` | `float \| None = None`                |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse.model._functions.profile.ProfileResponse` |


Built with [Mintlify](https://mintlify.com).