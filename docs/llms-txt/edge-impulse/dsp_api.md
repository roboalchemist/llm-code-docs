# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/dsp_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.dsp_api

## Classes

### DSPApi

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### clear\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.clear_dsp_block(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear DSP block

Clear generated features for a DSP block (used in tests).

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_dsp\_data

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.download_dsp_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')],
	raw: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to download raw data or processed data. Processed data is the default.')] = None,
	**kwargs
) ‑> str
```

Download DSP data

Download output from a DSP block over all data in the training set, already sliced in windows. In Numpy binary format.

| Parameters   |                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                           |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                |
| `category`   | `Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')]`           |
| `raw`        | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to download raw data or processed data. Processed data is the default.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                           |

| Returns |
| ------- |
| `str`   |

#### download\_dsp\_labels

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.download_dsp_labels(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')],
	**kwargs
) ‑> str
```

Download DSP labels

Download labels for a DSP block over all data in the training set, already sliced in windows.

| Parameters   |                                                                                                                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                 |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                      |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                      |
| `category`   | `Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')]` |
| `**kwargs`   | ` `                                                                                                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### dsp\_get\_features\_for\_sample

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.dsp_get_features_for_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_sample_features_response.DspSampleFeaturesResponse
```

Features for sample

Runs the DSP block against a sample. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and run the DSP function for every window that is extracted.

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                  |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_sample_features_response.DspSampleFeaturesResponse` |

#### dsp\_sample\_trained\_features

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.dsp_sample_trained_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	feature_ax1: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 1')],
	feature_ax2: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 2')],
	feature_ax3: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 3')],
	category: Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_trained_features_response.DspTrainedFeaturesResponse
```

Sample of trained features

Get a sample of trained features, this extracts a number of samples and their labels. Used to visualize the current training set.

| Parameters    |                                                                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`        | ` `                                                                                                                                                                                                 |
| `project_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                      |
| `dsp_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                      |
| `feature_ax1` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 1')]`                                                                                  |
| `feature_ax2` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 2')]`                                                                                  |
| `feature_ax3` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 3')]`                                                                                  |
| `category`    | `Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')]` |
| `**kwargs`    | ` `                                                                                                                                                                                                 |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_trained_features_response.DspTrainedFeaturesResponse` |

#### get\_autotuner\_results

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_autotuner_results(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_autotuner_results.DspAutotunerResults
```

Get results from DSP autotuner

Get a set of parameters, found as a result of running the DSP autotuner.

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_autotuner_results.DspAutotunerResults` |

#### get\_dsp\_config

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_config_response.DSPConfigResponse
```

Get config

Retrieve the configuration parameters for the DSP block. Use the impulse functions to retrieve all DSP blocks.

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_config_response.DSPConfigResponse` |

#### get\_dsp\_feature\_importance

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_feature_importance(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_feature_importance_response.DspFeatureImportanceResponse
```

Feature importance

Retrieve the feature importance for a DSP block (only available for blocks where dimensionalityReduction is not enabled)

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_feature_importance_response.DspFeatureImportanceResponse` |

#### get\_dsp\_feature\_labels

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_feature_labels(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_feature_labels_response.DspFeatureLabelsResponse
```

Feature labels

Retrieve the names of the features the DSP block generates

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_feature_labels_response.DspFeatureLabelsResponse` |

#### get\_dsp\_metadata

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	exclude_included_samples: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Whether to exclude 'includedSamples' in the response (as these can slow down requests significantly).")] = None,
	category: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Which of the acquisition categories to get metadata from')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.dsp_metadata_response.DSPMetadataResponse
```

Get metadata

Retrieve the metadata from a generated DSP block.

| Parameters                 |                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                     | ` `                                                                                                                                                                                                                                  |
| `project_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                       |
| `dsp_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                                       |
| `exclude_included_samples` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Whether to exclude 'includedSamples' in the response (as these can slow down requests significantly).")] = None` |
| `category`                 | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Which of the acquisition categories to get metadata from')] = None`                                               |
| `**kwargs`                 | ` `                                                                                                                                                                                                                                  |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_metadata_response.DSPMetadataResponse` |

#### get\_dsp\_raw\_sample

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_raw_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	limit_payload_values: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	use_cached_upsampled_data: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, upsampled data will be fetched from cache, returning the original sample data when limitPayloadValues > sample length.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get raw sample

Get raw sample data, but with only the axes selected by the DSP block. E.g. if you have selected only accX and accY as inputs for the DSP block, but the raw sample also contains accZ, accZ is filtered out. If you pass dspId = 0 this will return a raw graph without any processing.

| Parameters                   |                                                                                                                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                                                                            |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                 |
| `dsp_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                                                                 |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                                  |
| `limit_payload_values`       | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None`                                                                               |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                              |
| `use_cached_upsampled_data`  | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, upsampled data will be fetched from cache, returning the original sample data when limitPayloadValues > sample length.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                            |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |

#### get\_dsp\_sample\_slice

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_dsp_sample_slice(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	slice_start: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')],
	slice_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get raw sample (slice)

Get slice of raw sample data, but with only the axes selected by the DSP block. E.g. if you have selected only accX and accY as inputs for the DSP block, but the raw sample also contains accZ, accZ is filtered out.

| Parameters                   |                                                                                                                                                                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                                                                        |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                             |
| `dsp_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                                                             |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                              |
| `slice_start`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')]`                                                                                                                               |
| `slice_end`                  | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None` |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                          |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                        |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |

#### get\_performance\_all\_variants

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.get_performance_all_variants(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.dsp_performance_all_variants_response.DspPerformanceAllVariantsResponse
```

Get DSP block performance for all latency devices

Get estimated performance (latency and RAM) for the DSP block, for all supported project latency devices.

| Parameters   |                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                            |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_performance_all_variants_response.DspPerformanceAllVariantsResponse` |

#### run\_dsp\_on\_features\_array

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.run_dsp_on_features_array(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	dsp_run_request_with_features: edgeimpulse_api.models.dsp_run_request_with_features.DspRunRequestWithFeatures,
	**kwargs
) ‑> edgeimpulse_api.models.dsp_run_response.DspRunResponse
```

Get processed sample (from features array)

Takes in a features array and runs it through the DSP block. This data should have the same frequency as set in the input block in your impulse.

| Parameters                      |                                                                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                            |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `dsp_run_request_with_features` | `edgeimpulse_api.models.dsp_run_request_with_features.DspRunRequestWithFeatures`                                                                               |
| `**kwargs`                      | ` `                                                                                                                                                            |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.dsp_run_response.DspRunResponse` |

#### run\_dsp\_sample\_slice

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.run_dsp_sample_slice(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	slice_start: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')],
	dsp_run_request_without_features: edgeimpulse_api.models.dsp_run_request_without_features.DspRunRequestWithoutFeatures,
	slice_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample
```

Get processed sample (slice)

Get slice of sample data, and run it through the DSP block. This only the axes selected by the DSP block. E.g. if you have selected only accX and accY as inputs for the DSP block, but the raw sample also contains accZ, accZ is filtered out.

| Parameters                         |                                                                                                                                                                                                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                                                                                                                                                                        |
| `project_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                             |
| `dsp_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                                                             |
| `sample_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                              |
| `slice_start`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')]`                                                                                                                               |
| `dsp_run_request_without_features` | `edgeimpulse_api.models.dsp_run_request_without_features.DspRunRequestWithoutFeatures`                                                                                                                                                                     |
| `slice_end`                        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None` |
| `**kwargs`                         | ` `                                                                                                                                                                                                                                                        |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample` |

#### run\_dsp\_sample\_slice\_read\_only

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.run_dsp_sample_slice_read_only(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	slice_start: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')],
	slice_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample
```

Get processed sample (slice)

Get slice of sample data, and run it through the DSP block. This only the axes selected by the DSP block. E.g. if you have selected only accX and accY as inputs for the DSP block, but the raw sample also contains accZ, accZ is filtered out.

| Parameters    |                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`        | ` `                                                                                                                                                                                                                                                        |
| `project_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                             |
| `dsp_id`      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]`                                                                                             |
| `sample_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                              |
| `slice_start` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')]`                                                                                                                               |
| `slice_end`   | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None` |
| `**kwargs`    | ` `                                                                                                                                                                                                                                                        |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.dsp_run_response_with_sample.DspRunResponseWithSample` |

#### set\_dsp\_config

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.set_dsp_config(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	dsp_config_request: edgeimpulse_api.models.dsp_config_request.DSPConfigRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set config

Set configuration parameters for the DSP block. Only values set in the body will be overwritten.

| Parameters           |                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`               | ` `                                                                                                                                                            |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `dsp_config_request` | `edgeimpulse_api.models.dsp_config_request.DSPConfigRequest`                                                                                                   |
| `**kwargs`           | ` `                                                                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_profile\_custom\_dsp\_block

```python  theme={"system"}
edgeimpulse_api.api.dsp_api.DSPApi.start_profile_custom_dsp_block(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	dsp_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')],
	dsp_run_request_without_features_read_only: edgeimpulse_api.models.dsp_run_request_without_features_read_only.DspRunRequestWithoutFeaturesReadOnly,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Profile custom DSP block

Returns performance characteristics for a custom DSP block (needs `hasTfliteImplementation`). Updates are streamed over the websocket API (or can be retrieved through the /stdout endpoint). Use getProfileTfliteJobResult to get the results when the job is completed.

| Parameters                                   |                                                                                                                                                                |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                       | ` `                                                                                                                                                            |
| `project_id`                                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                 |
| `dsp_id`                                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='DSP Block ID, use the impulse functions to retrieve the ID')]` |
| `dsp_run_request_without_features_read_only` | `edgeimpulse_api.models.dsp_run_request_without_features_read_only.DspRunRequestWithoutFeaturesReadOnly`                                                       |
| `**kwargs`                                   | ` `                                                                                                                                                            |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |


Built with [Mintlify](https://mintlify.com).