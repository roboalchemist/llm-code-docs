# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/classify_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.classify_api

## Classes

### ClassifyApi

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### classify\_image

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_image(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	image: Annotated[str, Strict(strict=True)],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse
```

Classify an image

Test out a trained impulse (using a posted image).

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `image`      | `Annotated[str, Strict(strict=True)]`                                                                                                                                                        |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse` |

#### classify\_sample

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	include_debug_info: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse
```

Classify sample (deprecated)

This API is deprecated, use classifySampleV2 instead (`/v1/api/{projectId}/classify/v2/{sampleId}`). Classify a complete file against the current impulse. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and classify for every window that is extracted.

| Parameters           |                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                              |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                   |
| `sample_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                    |
| `include_debug_info` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None` |
| `impulse_id`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`     |
| `**kwargs`           | ` `                                                                                                                                                                                              |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse` |

#### classify\_sample\_by\_learn\_block

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_sample_by_learn_block(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	block_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Block ID')],
	**kwargs
) ‑> edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse
```

Classify sample by learn block

This API is deprecated, use classifySampleByLearnBlockV2 (`/v1/api/{projectId}/classify/anomaly-gmm/v2/{blockId}/{sampleId}`) instead. Classify a complete file against the specified learn block. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and classify for every window that is extracted.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `block_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Block ID')]`   |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                  |
| ------------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_sample_response.ClassifySampleResponse` |

#### classify\_sample\_by\_learn\_block\_v2

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_sample_by_learn_block_v2(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	block_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Block ID')],
	variant: Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum | None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response
```

Classify sample by learn block

Classify a complete file against the specified learn block. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and classify for every window that is extracted. Depending on the size of your file, whether your sample is resampled, and whether the result is cached you'll get either the result or a job back. If you receive a job, then wait for the completion of the job, and then call this function again to receive the results. The unoptimized (float32) model is used by default, and classification with an optimized (int8) model can be slower.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                     |
| `block_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Block ID')]`                                                                                                      |
| `variant`                    | `Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None`                               |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response` |

#### classify\_sample\_for\_variants

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_sample_for_variants(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	variants: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='List of keras model variants, given as a JSON string')],
	include_debug_info: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_sample_for_variants200_response.ClassifySampleForVariants200Response
```

Classify sample for the given set of variants

Classify a complete file against the current impulse, for all given variants. Depending on the size of your file and whether the sample is resampled, you may get a job ID in the response.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                     |
| `variants`                   | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='List of keras model variants, given as a JSON string')]`                                                          |
| `include_debug_info`         | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None`                  |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                      |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_sample_for_variants200_response.ClassifySampleForVariants200Response` |

#### classify\_sample\_v2

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.classify_sample_v2(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	include_debug_info: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None,
	variant: Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum | None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response
```

Classify sample

Classify a complete file against the current impulse. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and classify for every window that is extracted. Depending on the size of your file, whether your sample is resampled, and whether the result is cached you'll get either the result or a job back. If you receive a job, then wait for the completion of the job, and then call this function again to receive the results. The unoptimized (float32) model is used by default, and classification with an optimized (int8) model can be slower.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                     |
| `include_debug_info`         | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to return the debug information from FOMO classification.')] = None`                  |
| `variant`                    | `Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None`                               |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                      |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_sample_v2200_response.ClassifySampleV2200Response` |

#### get\_classify\_job\_result

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.get_classify_job_result(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	feature_explorer_only: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to get only the classification results relevant to the feature explorer.')] = None,
	variant: Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum | None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_job_response.ClassifyJobResponse
```

Classify job result

Get classify job result, containing the result for the complete testing dataset.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `feature_explorer_only`      | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to get only the classification results relevant to the feature explorer.')] = None`   |
| `variant`                    | `Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None`                               |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                      |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.classify_job_response.ClassifyJobResponse` |

#### get\_classify\_job\_result\_page

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.get_classify_job_result_page(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	variant: Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum | None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	min_label: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None,
	max_label: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None,
	search: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None,
	data_type: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None,
	min_id: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None,
	max_id: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None,
	metadata: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties:     - "key": Metadata key to filter on.     - "op": Operator ("eq" for positive match, "neq" for negative match).     - "values": (optional) Array of values to match/exclude. If omitted or empty, matches/excludes all values for the key. In addition to filter objects, the following option objects can be specified:     - { "no_metadata": boolean } - If true, include samples without any metadata     - { "filters_combinator": ("and" | "or") } - Specifies the combinator and matching mode:         - "and": All filter items must match (logical AND).         - "or": Any filter item may match (logical OR); samples with metadata keys not present in the filters are included. ')] = None,
	min_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None,
	max_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage
```

Single page of a classify job result

Get classify job result, containing the predictions for a given page.

| Parameters                   |                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                       | ` `                                                                                                                                                                                                                                                                |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `limit`                      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                                            |
| `offset`                     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                                        |
| `variant`                    | `Annotated[edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum \| None, FieldInfo(annotation=NoneType, required=True, description='Keras model variant')] = None`                                                                                |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                       |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                                  |
| `labels`                     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `min_label`                  | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`                  | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`                   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`                   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage` |

#### get\_sample\_window\_from\_cache

```python  theme={"system"}
edgeimpulse_api.api.classify_api.ClassifyApi.get_sample_window_from_cache(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	window_index: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample window index')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get a window of raw sample features from cache, after a live classification job has completed.

Get raw sample features for a particular window. This is only available after a live classification job has completed and raw features have been cached.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                     |
| `window_index`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample window index')]`                                                                                           |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                      |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |


Built with [Mintlify](https://mintlify.com).