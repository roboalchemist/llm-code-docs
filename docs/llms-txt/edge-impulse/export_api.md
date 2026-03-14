# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/export_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.export_api

## Classes

### ExportApi

```python  theme={"system"}
edgeimpulse_api.api.export_api.ExportApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### get\_export\_url

```python  theme={"system"}
edgeimpulse_api.api.export_api.ExportApi.get_export_url(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.export_get_url_response.ExportGetUrlResponse
```

Get URL of export

Get the URL to the exported artefacts for an export job of a project.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                               |
| --------------------------------------------------------------------- |
| `edgeimpulse_api.models.export_get_url_response.ExportGetUrlResponse` |


Built with [Mintlify](https://mintlify.com).