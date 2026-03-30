# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/devices_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.devices_api

## Classes

### DevicesApi

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### create\_device

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.create_device(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	create_device_request: edgeimpulse_api.models.create_device_request.CreateDeviceRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Create device

Create a new device. If you set `ifNotExists` to `false` and the device already exists, the `deviceType` will be overwritten.

| Parameters              |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                       |
| `project_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `create_device_request` | `edgeimpulse_api.models.create_device_request.CreateDeviceRequest`                                        |
| `**kwargs`              | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_device

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.delete_device(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete device

Delete a device. When this device sends a new message to ingestion or connects to remote management the device will be recreated.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`  | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_device

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.get_device(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_device_response.GetDeviceResponse
```

Get device

Retrieves a single device

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`  | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_device_response.GetDeviceResponse` |

#### get\_impulse\_records

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.get_impulse_records(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	get_impulse_records_request: edgeimpulse_api.models.get_impulse_records_request.GetImpulseRecordsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Get impulse records

Retrieve impulse records from the device.

| Parameters                    |                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                       |
| `project_id`                  | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`                   | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `get_impulse_records_request` | `edgeimpulse_api.models.get_impulse_records_request.GetImpulseRecordsRequest`                             |
| `**kwargs`                    | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### keep\_device\_debug\_stream\_alive

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.keep_device_debug_stream_alive(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	keep_device_debug_stream_alive_request: edgeimpulse_api.models.keep_device_debug_stream_alive_request.KeepDeviceDebugStreamAliveRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Keep debug stream alive

If you have opened a debug stream, ping this interface every 10 seconds to let us know to keep the debug stream open.

| Parameters                               |                                                                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                                   | ` `                                                                                                       |
| `project_id`                             | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`                              | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `keep_device_debug_stream_alive_request` | `edgeimpulse_api.models.keep_device_debug_stream_alive_request.KeepDeviceDebugStreamAliveRequest`         |
| `**kwargs`                               | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### list\_devices

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.list_devices(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.list_devices_response.ListDevicesResponse
```

Lists devices

List all devices for this project. Devices get included here if they connect to the remote management API or if they have sent data to the ingestion API and had the `device_id` field set.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_devices_response.ListDevicesResponse` |

#### rename\_device

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.rename_device(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	rename_device_request: edgeimpulse_api.models.rename_device_request.RenameDeviceRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Rename device

Set the current name for a device.

| Parameters              |                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                       |
| `project_id`            | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`             | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `rename_device_request` | `edgeimpulse_api.models.rename_device_request.RenameDeviceRequest`                                        |
| `**kwargs`              | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_device\_model\_update

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.request_device_model_update(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Trigger model update request

Trigger a model update request, this only works for devices connected to remote management server in inference mode.

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`  | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_device\_inference\_debug\_stream

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.start_device_inference_debug_stream(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.start_device_debug_stream_response.StartDeviceDebugStreamResponse
```

Start inference debug stream

Start an inference debug stream for this device with inference results (and images if a camera is attached). Updates are streamed through the websocket API. A keep-alive token is returned, you'll need to ping the API (with keepDeviceDebugStreamAlive) every 10 seconds (so we know when the client is disconnected).

| Parameters   |                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                       |
| `project_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`  | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `**kwargs`   | ` `                                                                                                       |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.start_device_debug_stream_response.StartDeviceDebugStreamResponse` |

#### start\_device\_snapshot\_debug\_stream

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.start_device_snapshot_debug_stream(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	start_device_snapshot_debug_stream_request: edgeimpulse_api.models.start_device_snapshot_debug_stream_request.StartDeviceSnapshotDebugStreamRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_device_debug_stream_response.StartDeviceDebugStreamResponse
```

Start snapshot debug stream

Start a snapshot debug stream for this device with a current camera view. Updates are streamed through the websocket API. A keep-alive token is returned, you'll need to ping the API (with keepDeviceDebugStreamAlive) every 10 seconds (so we know when the client is disconnected).

| Parameters                                   |                                                                                                           |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                                       | ` `                                                                                                       |
| `project_id`                                 | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`                                  | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `start_device_snapshot_debug_stream_request` | `edgeimpulse_api.models.start_device_snapshot_debug_stream_request.StartDeviceSnapshotDebugStreamRequest` |
| `**kwargs`                                   | ` `                                                                                                       |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.start_device_debug_stream_response.StartDeviceDebugStreamResponse` |

#### start\_sampling

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.start_sampling(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	start_sampling_request: edgeimpulse_api.models.start_sampling_request.StartSamplingRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_sampling_response.StartSamplingResponse
```

Start sampling

Start sampling on a device. This function returns immediately. Updates are streamed through the websocket API.

| Parameters               |                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                       |
| `project_id`             | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`              | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `start_sampling_request` | `edgeimpulse_api.models.start_sampling_request.StartSamplingRequest`                                      |
| `**kwargs`               | ` `                                                                                                       |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_sampling_response.StartSamplingResponse` |

#### stop\_device\_debug\_stream

```python  theme={"system"}
edgeimpulse_api.api.devices_api.DevicesApi.stop_device_debug_stream(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	device_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})],
	stop_device_debug_stream_request: edgeimpulse_api.models.stop_device_debug_stream_request.StopDeviceDebugStreamRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Stop debug stream

If you have opened a debug stream, close it.

| Parameters                         |                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                       |
| `project_id`                       | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `device_id`                        | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Device ID', extra={})]`  |
| `stop_device_debug_stream_request` | `edgeimpulse_api.models.stop_device_debug_stream_request.StopDeviceDebugStreamRequest`                    |
| `**kwargs`                         | ` `                                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).