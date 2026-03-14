# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/integrations_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.integrations_api

## Classes

### IntegrationsApi

```python  theme={"system"}
edgeimpulse_api.api.integrations_api.IntegrationsApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### get\_tensor\_board\_session\_status

```python  theme={"system"}
edgeimpulse_api.api.integrations_api.IntegrationsApi.get_tensor_board_session_status(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	resource_id: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Unique resource ID for an integration session. When an integration is launched we create a new session for it. Each session is uniquely identifiable by the project ID and resource ID. ', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.get_integration_session_status_response.GetIntegrationSessionStatusResponse
```

Get TensorBoard session status

Get the status of a TensorBoard session

| Parameters    |                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`        | ` `                                                                                                                                                                                                                                                                                     |
| `project_id`  | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]`                                                                                                                                                                               |
| `resource_id` | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Unique resource ID for an integration session. When an integration is launched we create a new session for it. Each session is uniquely identifiable by the project ID and resource ID. ', extra={})]` |
| `**kwargs`    | ` `                                                                                                                                                                                                                                                                                     |

| Returns                                                                                              |
| ---------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_integration_session_status_response.GetIntegrationSessionStatusResponse` |

#### start\_tensor\_board\_session

```python  theme={"system"}
edgeimpulse_api.api.integrations_api.IntegrationsApi.start_tensor_board_session(
	self,
	project_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})],
	start_tensor_board_session_request: edgeimpulse_api.models.start_tensor_board_session_request.StartTensorBoardSessionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_integration_session_response.StartIntegrationSessionResponse
```

Start TensorBoard integration

Start a TensorBoard session for the requested learn blocks

| Parameters                           |                                                                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                       |
| `project_id`                         | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Project ID', extra={})]` |
| `start_tensor_board_session_request` | `edgeimpulse_api.models.start_tensor_board_session_request.StartTensorBoardSessionRequest`                |
| `**kwargs`                           | ` `                                                                                                       |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_integration_session_response.StartIntegrationSessionResponse` |


Built with [Mintlify](https://mintlify.com).