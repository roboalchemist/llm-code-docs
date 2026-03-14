# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/post_processing_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.post_processing_api

## Classes

### PostProcessingApi

```python  theme={"system"}
edgeimpulse_api.api.post_processing_api.PostProcessingApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### generate\_post\_processing\_features\_for\_sample

```python  theme={"system"}
edgeimpulse_api.api.post_processing_api.PostProcessingApi.generate_post_processing_features_for_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	post_processing_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	post_processing_features_for_sample_request: edgeimpulse_api.models.post_processing_features_for_sample_request.PostProcessingFeaturesForSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generate_post_processing_features_for_sample200_response.GeneratePostProcessingFeaturesForSample200Response
```

Classify sample with post-processing

Classify a sample using post-processing parameters. Sample should be in the post-processing dataset.

| Parameters                                    |                                                                                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                        | ` `                                                                                                                                                                        |
| `project_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                             |
| `post_processing_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')]` |
| `sample_id`                                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                              |
| `post_processing_features_for_sample_request` | `edgeimpulse_api.models.post_processing_features_for_sample_request.PostProcessingFeaturesForSampleRequest`                                                                |
| `**kwargs`                                    | ` `                                                                                                                                                                        |

| Returns                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.generate_post_processing_features_for_sample200_response.GeneratePostProcessingFeaturesForSample200Response` |

#### get\_post\_processing\_config

```python  theme={"system"}
edgeimpulse_api.api.post_processing_api.PostProcessingApi.get_post_processing_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	post_processing_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.post_processing_config_response.PostProcessingConfigResponse
```

Get post-processing block config

Retrieve the configuration parameters for a post-processing block. Use the impulse functions to retrieve all post-processing blocks.

| Parameters           |                                                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                                                                                        |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                             |
| `post_processing_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`           | ` `                                                                                                                                                                        |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.post_processing_config_response.PostProcessingConfigResponse` |

#### get\_post\_processing\_results\_for\_sample

```python  theme={"system"}
edgeimpulse_api.api.post_processing_api.PostProcessingApi.get_post_processing_results_for_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	post_processing_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	post_processing_features_for_sample_request: edgeimpulse_api.models.post_processing_features_for_sample_request.PostProcessingFeaturesForSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse
```

Check post-processing results for sample

Retrieve post-processing results for a specific sample, e.g. whether it has generated features already.

| Parameters                                    |                                                                                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                        | ` `                                                                                                                                                                        |
| `project_id`                                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                             |
| `post_processing_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')]` |
| `sample_id`                                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                              |
| `post_processing_features_for_sample_request` | `edgeimpulse_api.models.post_processing_features_for_sample_request.PostProcessingFeaturesForSampleRequest`                                                                |
| `**kwargs`                                    | ` `                                                                                                                                                                        |

| Returns                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_post_processing_results_for_sample_response.GetPostProcessingResultsForSampleResponse` |

#### set\_post\_processing\_config

```python  theme={"system"}
edgeimpulse_api.api.post_processing_api.PostProcessingApi.set_post_processing_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	post_processing_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')],
	post_processing_config_request: edgeimpulse_api.models.post_processing_config_request.PostProcessingConfigRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set post-processing block config

Set configuration parameters for a post-processing block. Only values set in the body will be overwritten.

| Parameters                       |                                                                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                                                                                        |
| `project_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                             |
| `post_processing_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Post-processing Block ID, use the impulse functions to retrieve the ID')]` |
| `post_processing_config_request` | `edgeimpulse_api.models.post_processing_config_request.PostProcessingConfigRequest`                                                                                        |
| `**kwargs`                       | ` `                                                                                                                                                                        |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).