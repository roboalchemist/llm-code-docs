# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/data/sample_type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.data.sample_type

## Classes

### DataAcquisition

```python  theme={"system"}
edgeimpulse.data.sample_type.DataAcquisition(
	protected: edgeimpulse.data.sample_type.Protected,
	payload: edgeimpulse.data.sample_type.Payload,
	signature: str | None = None
)
```

Wrapper class for the Edge Impulse data acquisition format.

See here for more information: [https://docs.edgeimpulse.com/reference/data-acquisition-format](https://docs.edgeimpulse.com/reference/data-acquisition-format).

| Parameters  |                                          |
| ----------- | ---------------------------------------- |
| `protected` | `edgeimpulse.data.sample_type.Protected` |
| `payload`   | `edgeimpulse.data.sample_type.Payload`   |
| `signature` | `str \| None = None`                     |

| Instance variables |                                          |
| ------------------ | ---------------------------------------- |
| `payload`          | `edgeimpulse.data.sample_type.Payload`   |
| `protected`        | `edgeimpulse.data.sample_type.Protected` |
| `signature`        | `str \| None`                            |

### Payload

```python  theme={"system"}
edgeimpulse.data.sample_type.Payload(
	device_type: str,
	sensors: List[edgeimpulse.data.sample_type.Sensor],
	values: List[List[float]],
	interval_ms: int | None = 0,
	device_name: str | None = None
)
```

Wrapper class for the sensor data.

Information about the data acquisition format can be found here: [https://docs.edgeimpulse.com/reference/data-acquisition-format](https://docs.edgeimpulse.com/reference/data-acquisition-format).

| Parameters    |                                             |
| ------------- | ------------------------------------------- |
| `device_type` | `str`                                       |
| `sensors`     | `List[edgeimpulse.data.sample_type.Sensor]` |
| `values`      | `List[List[float]]`                         |
| `interval_ms` | `int \| None = 0`                           |
| `device_name` | `str \| None = None`                        |

| Instance variables |                                             |
| ------------------ | ------------------------------------------- |
| `device_name`      | `str \| None`                               |
| `device_type`      | `str`                                       |
| `interval_ms`      | `int \| None`                               |
| `sensors`          | `List[edgeimpulse.data.sample_type.Sensor]` |
| `values`           | `List[List[float]]`                         |

### Protected

```python  theme={"system"}
edgeimpulse.data.sample_type.Protected(
	ver: str = 'v1',
	alg: Literal['HS256', 'none'] = 'none',
	iat: int | None = None
)
```

Wrapper class for information about the signature format.

More information can be found here: [https://docs.edgeimpulse.com/reference/data-acquisition-format](https://docs.edgeimpulse.com/reference/data-acquisition-format).

| Parameters |                                     |
| ---------- | ----------------------------------- |
| `ver`      | `str = 'v1'`                        |
| `alg`      | `Literal['HS256', 'none'] = 'none'` |
| `iat`      | `int \| None = None`                |

| Instance variables |                            |
| ------------------ | -------------------------- |
| `alg`              | `Literal['HS256', 'none']` |
| `iat`              | `int \| None`              |
| `ver`              | `str`                      |

### Sample

```python  theme={"system"}
edgeimpulse.data.sample_type.Sample(
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

### SampleInfo

```python  theme={"system"}
edgeimpulse.data.sample_type.SampleInfo(
	sample_id: int | None = None,
	filename: str | None = None,
	category: str | None = None,
	label: str | None = None
)
```

Wrapper for the response from the Edge Impulse ingestion service when retrieving sample information.

| Parameters  |                      |
| ----------- | -------------------- |
| `sample_id` | `int \| None = None` |
| `filename`  | `str \| None = None` |
| `category`  | `str \| None = None` |
| `label`     | `str \| None = None` |

| Instance variables |               |
| ------------------ | ------------- |
| `category`         | `str \| None` |
| `filename`         | `str \| None` |
| `label`            | `str \| None` |
| `sample_id`        | `int \| None` |

### SampleIngestionResponse

```python  theme={"system"}
edgeimpulse.data.sample_type.SampleIngestionResponse(
	sample: edgeimpulse.data.sample_type.Sample,
	response: dict
)
```

Wrapper for the response from the Edge Impulse ingestion service when uploading a sample along with the sample that was uploaded.

| Parameters |                                       |
| ---------- | ------------------------------------- |
| `sample`   | `edgeimpulse.data.sample_type.Sample` |
| `response` | `dict`                                |

### Sensor

```python  theme={"system"}
edgeimpulse.data.sample_type.Sensor(
	name: str,
	units: Literal['m', 'kg', 'g', 's', 'A', 'K', 'cd', 'mol', 'Hz', 'rad', 'sr', 'N', 'Pa', 'J', 'W', 'C', 'V', 'F', 'Ohm', 'S', 'Wb', 'T', 'H', 'Cel', 'lm', 'lx', 'Bq', 'Gy', 'Sv', 'kat', 'm2', 'm3', 'l', 'm/s', 'm/s2', 'm3/s', 'l/s', 'W/m2', 'cd/m2', 'bit', 'bit/s', 'lat', 'lon', 'pH', 'dB', 'dBW', 'Bspl', 'count', '/', '%', '%RH', '%EL', 'EL', '1/s', '1/min', 'beat/min', 'beats', 'S/m', 'B', 'VA', 'VAs', 'var', 'vars', 'J/m', 'kg/m3', 'deg', 'NTU', 'rgba'] = 'm/s'
)
```

Represents a sensor in the Edge Impulse data acquisition format.

Note:
The units must comply with the SenML units list:
[https://www.iana.org/assignments/senml/senml.xhtml](https://www.iana.org/assignments/senml/senml.xhtml)

| Parameters |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`     | `str`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `units`    | `Literal['m', 'kg', 'g', 's', 'A', 'K', 'cd', 'mol', 'Hz', 'rad', 'sr', 'N', 'Pa', 'J', 'W', 'C', 'V', 'F', 'Ohm', 'S', 'Wb', 'T', 'H', 'Cel', 'lm', 'lx', 'Bq', 'Gy', 'Sv', 'kat', 'm2', 'm3', 'l', 'm/s', 'm/s2', 'm3/s', 'l/s', 'W/m2', 'cd/m2', 'bit', 'bit/s', 'lat', 'lon', 'pH', 'dB', 'dBW', 'Bspl', 'count', '/', '%', '%RH', '%EL', 'EL', '1/s', '1/min', 'beat/min', 'beats', 'S/m', 'B', 'VA', 'VAs', 'var', 'vars', 'J/m', 'kg/m3', 'deg', 'NTU', 'rgba'] = 'm/s'` |

| Instance variables |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | `str`                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `units`            | `Literal['m', 'kg', 'g', 's', 'A', 'K', 'cd', 'mol', 'Hz', 'rad', 'sr', 'N', 'Pa', 'J', 'W', 'C', 'V', 'F', 'Ohm', 'S', 'Wb', 'T', 'H', 'Cel', 'lm', 'lx', 'Bq', 'Gy', 'Sv', 'kat', 'm2', 'm3', 'l', 'm/s', 'm/s2', 'm3/s', 'l/s', 'W/m2', 'cd/m2', 'bit', 'bit/s', 'lat', 'lon', 'pH', 'dB', 'dBW', 'Bspl', 'count', '/', '%', '%RH', '%EL', 'EL', '1/s', '1/min', 'beat/min', 'beats', 'S/m', 'B', 'VA', 'VAs', 'var', 'vars', 'J/m', 'kg/m3', 'deg', 'NTU', 'rgba']` |

### UploadSamplesResponse

```python  theme={"system"}
edgeimpulse.data.sample_type.UploadSamplesResponse(
	successes: List[edgeimpulse.data.sample_type.SampleIngestionResponse],
	fails: List[edgeimpulse.data.sample_type.SampleIngestionResponse]
)
```

Response from the Edge Impulse server when uploading multiple samples.

| Parameters  |                                                              |
| ----------- | ------------------------------------------------------------ |
| `successes` | `List[edgeimpulse.data.sample_type.SampleIngestionResponse]` |
| `fails`     | `List[edgeimpulse.data.sample_type.SampleIngestionResponse]` |

***

**METHODS**

#### extend

```python  theme={"system"}
edgeimpulse.data.sample_type.UploadSamplesResponse.extend(
	self,
	successes: List[edgeimpulse.data.sample_type.SampleIngestionResponse],
	fails: List[edgeimpulse.data.sample_type.SampleIngestionResponse]
)
```

Add new responses to the existing responses.

| Parameters  |                                                              |
| ----------- | ------------------------------------------------------------ |
| `self`      | ` `                                                          |
| `successes` | `List[edgeimpulse.data.sample_type.SampleIngestionResponse]` |
| `fails`     | `List[edgeimpulse.data.sample_type.SampleIngestionResponse]` |


Built with [Mintlify](https://mintlify.com).