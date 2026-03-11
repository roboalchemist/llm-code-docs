# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/raw_data_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.raw_data_api

## Classes

### RawDataApi

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### batch\_add\_metadata

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_add_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	batch_add_metadata_request: edgeimpulse_api.models.batch_add_metadata_request.BatchAddMetadataRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Add metadata (multiple samples)

Add specific metadata for multiple samples.

| Parameters                   |                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                       | ` `                                                                                                                                                                                                                                                                |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`                   | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `batch_add_metadata_request` | `edgeimpulse_api.models.batch_add_metadata_request.BatchAddMetadataRequest`                                                                                                                                                                                        |
| `labels`                     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
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

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_back\_to\_labeling

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_back_to_labeling(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	back_to_labeling_request: edgeimpulse_api.models.back_to_labeling_request.BackToLabelingRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Put samples back into the object detection labeling queue

Batch operation to put multiple samples back into the object detection labeling queue. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters                 |                                                                                                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                     | ` `                                                                                                                                                                                                                                                                |
| `project_id`               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`                 | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `back_to_labeling_request` | `edgeimpulse_api.models.back_to_labeling_request.BackToLabelingRequest`                                                                                                                                                                                            |
| `labels`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                 | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`               | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`               | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`            | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`            | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                      | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`              | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`                | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`                | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                   | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                   | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`                 | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`                 | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`                 | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`                 | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_clear\_metadata

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_clear_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear all metadata (multiple samples)

Clears all metadata for multiple samples.

| Parameters           |                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                                                                                                |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`           | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `labels`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`           | ` `                                                                                                                                                                                                                                                                |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### batch\_clear\_metadata\_by\_key

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_clear_metadata_by_key(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	batch_clear_metadata_by_key_request: edgeimpulse_api.models.batch_clear_metadata_by_key_request.BatchClearMetadataByKeyRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Clear metadata by key (multiple samples)

Clears a specific metadata field (by key) for multiple samples.

| Parameters                            |                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                                | ` `                                                                                                                                                                                                                                                                |
| `project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`                            | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `batch_clear_metadata_by_key_request` | `edgeimpulse_api.models.batch_clear_metadata_by_key_request.BatchClearMetadataByKeyRequest`                                                                                                                                                                        |
| `labels`                              | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`                          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`                          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`                       | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`                       | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`                    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                                 | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`                         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`                           | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`                           | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                              | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`                           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`                            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`                            | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`                            | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`                            | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_delete

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_delete(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Remove multiple samples

Deletes samples. Note that this does not delete the data from cold storage. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters           |                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                                                                                                |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`           | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `labels`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`           | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_disable

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_disable(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Disable multiple samples

Disables samples, ensuring that they are excluded from the dataset. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters           |                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                                                                                                |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`           | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `labels`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`           | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_edit\_bounding\_boxes

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_edit_bounding_boxes(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	batch_edit_bounding_boxes_request: edgeimpulse_api.models.batch_edit_bounding_boxes_request.BatchEditBoundingBoxesRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Edit bounding boxes for multiple samples

Relabels (or removes) bounding boxes for multiple samples. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters                          |                                                                                                                                                                                                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                              | ` `                                                                                                                                                                                                                                                                |
| `project_id`                        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`                          | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `batch_edit_bounding_boxes_request` | `edgeimpulse_api.models.batch_edit_bounding_boxes_request.BatchEditBoundingBoxesRequest`                                                                                                                                                                           |
| `labels`                            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`                        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`                        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                               | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`                       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`                         | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`                         | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                            | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`                         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                            | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                            | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`                          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`                          | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`                          | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`                          | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_edit\_labels

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_edit_labels(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	edit_sample_label_request: edgeimpulse_api.models.edit_sample_label_request.EditSampleLabelRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Edit labels for multiple samples

Sets the label (also known as class) of multiple samples. If you want to relabel bounding boxes, use "batchEditBoundingBoxes" instead. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters                  |                                                                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                      | ` `                                                                                                                                                                                                                                                                |
| `project_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`                  | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `edit_sample_label_request` | `edgeimpulse_api.models.edit_sample_label_request.EditSampleLabelRequest`                                                                                                                                                                                          |
| `labels`                    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`                | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                       | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`               | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`                 | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`                 | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`                 | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                    | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                    | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`                  | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`                  | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`                  | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_enable

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_enable(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Enable multiple samples

Enables samples, ensuring that they are not excluded from the dataset. Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters           |                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                                                                                                |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`           | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `labels`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`        | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`           | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### batch\_move

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.batch_move(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	move_raw_data_request: edgeimpulse_api.models.move_raw_data_request.MoveRawDataRequest,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None,
	exclude_ids: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None,
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
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Move multiple samples

Move multiple samples to another category (e.g. from test to training). Depending on the number of affected samples this will either execute immediately or return the ID of a job that will perform this action in batches.

| Parameters              |                                                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                  | ` `                                                                                                                                                                                                                                                                |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`              | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `move_raw_data_request` | `edgeimpulse_api.models.move_raw_data_request.MoveRawDataRequest`                                                                                                                                                                                                  |
| `labels`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`              | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`            | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`            | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`         | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`         | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity`    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`      | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `ids`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                 |
| `exclude_ids`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Exclude samples with an ID within the given list of IDs, given as a JSON string')] = None`                                                      |
| `min_label`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`                | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`                | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`              | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`              | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`              | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`              | ` `                                                                                                                                                                                                                                                                |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### classify\_using\_autolabel

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.classify_using_autolabel(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	object_detection_auto_label_request: edgeimpulse_api.models.object_detection_auto_label_request.ObjectDetectionAutoLabelRequest,
	**kwargs
) ‑> edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse
```

Auto-label an image

Classify an image using another neural network.

| Parameters                            |                                                                                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                            |
| `project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `object_detection_auto_label_request` | `edgeimpulse_api.models.object_detection_auto_label_request.ObjectDetectionAutoLabelRequest`                   |
| `**kwargs`                            | ` `                                                                                                            |

| Returns                                                                                        |
| ---------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse` |

#### clear\_all\_object\_detection\_labels

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.clear_all_object_detection_labels(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear all object detection labels

Clears all object detection labels for this dataset, and places all images back in the labeling queue.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### clear\_data\_explorer

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.clear_data_explorer(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Clear data explorer

Remove the current data explorer state

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### count\_samples

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.count_samples(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
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
) ‑> edgeimpulse_api.models.count_samples_response.CountSamplesResponse
```

Count samples

Count all raw data by category.

| Parameters           |                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`               | ` `                                                                                                                                                                                                                                                                |
| `project_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                     |
| `category`           | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                   |
| `labels`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                            |
| `filename`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                      |
| `max_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                  |
| `min_length`         | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                   |
| `min_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                          |
| `max_frequency`      | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                           |
| `signature_validity` | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                              |
| `include_disabled`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                   |
| `min_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                    |
| `max_label`          | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                     |
| `search`             | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                         |
| `data_type`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                     |
| `min_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                      |
| `max_id`             | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                       |
| `metadata`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties` |
| `min_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                             |
| `max_date`           | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                             |
| `**kwargs`           | ` `                                                                                                                                                                                                                                                                |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.count_samples_response.CountSamplesResponse` |

#### crop\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.crop_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	crop_sample_request: edgeimpulse_api.models.crop_sample_request.CropSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.crop_sample_response.CropSampleResponse
```

Crop sample

Crop a sample to within a new range.

| Parameters            |                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                | ` `                                                                                                            |
| `project_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `crop_sample_request` | `edgeimpulse_api.models.crop_sample_request.CropSampleRequest`                                                 |
| `**kwargs`            | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.crop_sample_response.CropSampleResponse` |

#### delete\_all\_samples

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.delete_all_samples(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove all samples

Deletes all samples for this project over all categories. This also invalidates all DSP and learn blocks. Note that this does not delete the data from cold storage.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_all\_samples\_by\_category

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.delete_all_samples_by_category(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove all samples by category

Deletes all samples for this project over a single category. Note that this does not delete the data from cold storage.

| Parameters   |                                                                                                                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                 |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                      |
| `category`   | `Annotated[edgeimpulse_api.models.raw_data_category.RawDataCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to download data from')]` |
| `**kwargs`   | ` `                                                                                                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.delete_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove sample

Deletes the sample. Note that this does not delete the data from cold storage.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### disable\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.disable_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Disable sample

Disable a sample, ensuring that it is excluded from the dataset.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### edit\_label

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.edit_label(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	edit_sample_label_request: edgeimpulse_api.models.edit_sample_label_request.EditSampleLabelRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Edit label

Sets the label (also known as class) of the sample. Use the same label for similar types of data, as they are used during training.

| Parameters                  |                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                            |
| `project_id`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `edit_sample_label_request` | `edgeimpulse_api.models.edit_sample_label_request.EditSampleLabelRequest`                                      |
| `**kwargs`                  | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### enable\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.enable_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Enable sample

Enable a sample, ensuring that it is not excluded from the dataset.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### find\_segments\_in\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.find_segments_in_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	find_segment_sample_request: edgeimpulse_api.models.find_segment_sample_request.FindSegmentSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.find_segment_sample_response.FindSegmentSampleResponse
```

Find segments

Find start and end times for all non-noise events in a sample

| Parameters                    |                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                            |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `find_segment_sample_request` | `edgeimpulse_api.models.find_segment_sample_request.FindSegmentSampleRequest`                                  |
| `**kwargs`                    | ` `                                                                                                            |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.find_segment_sample_response.FindSegmentSampleResponse` |

#### get\_ai\_actions\_proposed\_changes

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_ai_actions_proposed_changes(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	job_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_ai_actions_proposed_changes_response.GetAIActionsProposedChangesResponse
```

Get AI Actions proposed changes

Get proposed changes from an AI Actions job.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `job_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Job ID')]`     |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_ai_actions_proposed_changes_response.GetAIActionsProposedChangesResponse` |

#### get\_all\_imported\_from

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_all_imported_from(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_all_imported_from_response.GetAllImportedFromResponse
```

List data with "imported from" metadata key

Lists all data with an 'imported from' metadata key. Used to check in a data source which items are already in a project.

| Parameters   |                                                                                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                         |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                              |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                                         |

| Returns                                                                            |
| ---------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_all_imported_from_response.GetAllImportedFromResponse` |

#### get\_data\_explorer\_features

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_data_explorer_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse
```

Get data explorer features

t-SNE2 output of the raw dataset

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse` |

#### get\_data\_explorer\_predictions

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_data_explorer_predictions(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.data_explorer_predictions_response.DataExplorerPredictionsResponse
```

Get data explorer predictions

Predictions for every data explorer point (only available when using current impulse to populate data explorer)

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.data_explorer_predictions_response.DataExplorerPredictionsResponse` |

#### get\_data\_explorer\_settings

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_data_explorer_settings(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse
```

Get data explorer settings

Get data explorer configuration, like the type of data, and the input / dsp block to use.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse` |

#### get\_dataset\_ratio

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_dataset_ratio(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_dataset_ratio_response.GetDatasetRatioResponse
```

Get dataset ratio

Retrieve number of samples in train and test set.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_dataset_ratio_response.GetDatasetRatioResponse` |

#### get\_diversity\_data

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_diversity_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_diversity_data_response.GetDiversityDataResponse
```

Get diversity metrics data

Obtain metrics that describe the similarity and diversity of a dataset. To calculate these metrics, use the `calculateDataQualityMetrics` endpoint.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                       |
| ----------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_diversity_data_response.GetDiversityDataResponse` |

#### get\_label\_noise\_data

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_label_noise_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_label_noise_data_response.GetLabelNoiseDataResponse
```

Get label noise data

Obtain metrics that describe potential label noise issues in the dataset. To calculate these metrics, use the `calculateDataQualityMetrics` endpoint.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                          |
| -------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_label_noise_data_response.GetLabelNoiseDataResponse` |

#### get\_object\_detection\_label\_queue

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_object_detection_label_queue(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.object_detection_label_queue_response.ObjectDetectionLabelQueueResponse
```

Object detection label queue

Get all unlabeled items from the object detection queue.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.object_detection_label_queue_response.ObjectDetectionLabelQueueResponse` |

#### get\_object\_detection\_label\_queue\_count

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_object_detection_label_queue_count(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.object_detection_label_queue_count_response.ObjectDetectionLabelQueueCountResponse
```

Object detection label queue count

Get count for unlabeled items from the object detection queue.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.object_detection_label_queue_count_response.ObjectDetectionLabelQueueCountResponse` |

#### get\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	limit_payload_values: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None,
	cache_key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	proposed_actions_job_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Pass this parameter when querying samples from inside an AI Action job. If you pass this parameter in a multi-stage AI Action, previous proposed changes (from an earlier step) will be applied to the returned dataset.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get sample

Get a sample.

| Parameters                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                       | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                                                                                                                                     |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                                                                                                                                                                                                                                      |
| `limit_payload_values`       | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None`                                                                                                                                                                                                                                                                                   |
| `cache_key`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None` |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                                                                                                                                                                                                                       |
| `proposed_actions_job_id`    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Pass this parameter when querying samples from inside an AI Action job. If you pass this parameter in a multi-stage AI Action, previous proposed changes (from an earlier step) will be applied to the returned dataset.')] = None`                                                                                                             |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                                                                                                                                                                                                                                  |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |

#### get\_sample\_as\_audio

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_as_audio(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	axis_ix: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Axis index')],
	slice_start: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice. If not given, the whole sample is used.')] = None,
	slice_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the whole sample is used.')] = None,
	cache_key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None,
	**kwargs
) ‑> str
```

Get WAV file

Get a sample as a WAV file. This only applies to samples with an audio axis.

| Parameters    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`        | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `project_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                                                                                                                                     |
| `sample_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                                                                                                                                                                                                                                      |
| `axis_ix`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Axis index')]`                                                                                                                                                                                                                                                                                                                                                     |
| `slice_start` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice. If not given, the whole sample is used.')] = None`                                                                                                                                                                                                                                                                    |
| `slice_end`   | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the whole sample is used.')] = None`                                                                                                                                                                                                                                                                      |
| `cache_key`   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None` |
| `**kwargs`    | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

| Returns |
| ------- |
| `str`   |

#### get\_sample\_as\_image

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_as_image(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	after_input_block: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to process the image through the input block first')] = None,
	cache_key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> str
```

Get image file

Get a sample as an image file. This only applies to samples with RGBA data.

| Parameters          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`              | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `project_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                                                                                                                                     |
| `sample_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                                                                                                                                                                                                                                      |
| `after_input_block` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to process the image through the input block first')] = None`                                                                                                                                                                                                                                                                          |
| `cache_key`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None` |
| `impulse_id`        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                                                                                                                                                                                                                       |
| `**kwargs`          | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

| Returns |
| ------- |
| `str`   |

#### get\_sample\_as\_raw

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_as_raw(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> str
```

Download file

Download a sample in it's original format as uploaded to the ingestion service.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns |
| ------- |
| `str`   |

#### get\_sample\_as\_video

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_as_video(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	after_input_block: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to process the image through the input block first')] = None,
	cache_key: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> str
```

Get video file

Get a sample as an video file. This only applies to samples with video data.

| Parameters          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`              | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `project_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                                                                                                                                     |
| `sample_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                                                                                                                                                                                                                                      |
| `after_input_block` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to process the image through the input block first')] = None`                                                                                                                                                                                                                                                                          |
| `cache_key`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set, then a long cache header is sent. If this is omitted then a no-cache header is sent. You can use this if you f.e. know the last modified date of a sample. Stick the last modified date in the cache key, so the sample can be stored in browser cache (and will automatically be invalidated if the modified date changes).')] = None` |
| `impulse_id`        | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                                                                                                                                                                                                                       |
| `**kwargs`          | ` `                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

| Returns |
| ------- |
| `str`   |

#### get\_sample\_metadata

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_metadata_response.GetSampleMetadataResponse
```

Get project sample metadata

Get metadata for all samples in a project.

| Parameters   |                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                   |
| `category`   | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]` |
| `**kwargs`   | ` `                                                                                                                                                                                                              |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_metadata_response.GetSampleMetadataResponse` |

#### get\_sample\_metadata\_filter\_options

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_metadata_filter_options(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_metadata_filter_options_response.GetSampleMetadataFilterOptionsResponse
```

Get project sample metadata filter options

Get a list of unique key value pairs across all samples in a project that can be applied as filters to the /api/`{projectId}`/raw-data endpoint

| Parameters   |                                                                                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                                                         |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                              |
| `category`   | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`            |
| `limit`      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                                                         |

| Returns                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_metadata_filter_options_response.GetSampleMetadataFilterOptionsResponse` |

#### get\_sample\_slice

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_sample_slice(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	slice_start: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')],
	slice_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get sample slice

Get a slice of a sample.

| Parameters                   |                                                                                                                                                                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                                                                        |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                             |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                                                              |
| `slice_start`                | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Begin index of the slice')]`                                                                                                                               |
| `slice_end`                  | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='End index of the slice. If not given, the sample will be sliced to the same length as the impulse input block window length.')] = None` |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                               |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                          |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                        |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |

#### get\_uncropped\_downsampled\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.get_uncropped_downsampled_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	limit_payload_values: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None,
	zoom_start: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Zoom into the sample, with the focus starting at this index')] = None,
	zoom_end: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Zoom into the sample, with the focus ending at this index')] = None,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_sample_response.GetSampleResponse
```

Get the original downsampled data

Get the original, uncropped, downsampled data.

| Parameters                   |                                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                                                                                                               |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                    |
| `sample_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                                                                     |
| `limit_payload_values`       | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Limit the number of payload values in the response')] = None`                                  |
| `zoom_start`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Zoom into the sample, with the focus starting at this index')] = None`                         |
| `zoom_end`                   | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Zoom into the sample, with the focus ending at this index')] = None`                           |
| `impulse_id`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                      |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None` |
| `**kwargs`                   | ` `                                                                                                                                                                                                               |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sample_response.GetSampleResponse` |

#### has\_data\_explorer\_features

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.has_data_explorer_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse
```

Check data explorer features

t-SNE2 output of the raw dataset

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse` |

#### has\_diversity\_data

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.has_diversity_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse
```

Check if data diversity metrics exist

Determine if data diversity metrics have been calculated. To calculate these metrics, use the `calculateDataQualityMetrics` endpoint.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse` |

#### has\_label\_noise\_data

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.has_label_noise_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse
```

Check if label noise metrics exist

Determine if label noise metrics have been calculated. To calculate these metrics, use the `calculateDataQualityMetrics` endpoint.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.has_data_explorer_features_response.HasDataExplorerFeaturesResponse` |

#### list\_samples

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.list_samples(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	category: Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	exclude_sensors: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude sensors in the response (as these can slow down requests when you have large pages).')] = None,
	labels: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None,
	filename: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None,
	max_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None,
	min_length: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None,
	min_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None,
	max_frequency: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None,
	signature_validity: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None,
	include_disabled: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None,
	min_label: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None,
	max_label: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None,
	search: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None,
	proposed_actions_job_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Pass this parameter when querying samples from inside an AI Action job. If you pass this parameter in a multi-stage AI Action, previous proposed changes (from an earlier step) will be applied to the returned dataset.')] = None,
	truncate_structured_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None,
	sort_by: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If not specified, "id-desc" is used.')] = None,
	data_type: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None,
	min_id: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None,
	max_id: Annotated[float | None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None,
	metadata: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties:     - "key": Metadata key to filter on.     - "op": Operator ("eq" for positive match, "neq" for negative match).     - "values": (optional) Array of values to match/exclude. If omitted or empty, matches/excludes all values for the key. In addition to filter objects, the following option objects can be specified:     - { "no_metadata": boolean } - If true, include samples without any metadata     - { "filters_combinator": ("and" | "or") } - Specifies the combinator and matching mode:         - "and": All filter items must match (logical AND).         - "or": Any filter item may match (logical OR); samples with metadata keys not present in the filters are included. ')] = None,
	min_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None,
	max_date: Annotated[datetime.datetime | None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_samples_response.ListSamplesResponse
```

List samples

Retrieve all raw data by category.

| Parameters                   |                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                       | ` `                                                                                                                                                                                                                                                                                                                                                    |
| `project_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                         |
| `category`                   | `Annotated[edgeimpulse_api.models.raw_data_filter_category.RawDataFilterCategory, FieldInfo(annotation=NoneType, required=True, description='Which of the three acquisition categories to retrieve data from')]`                                                                                                                                       |
| `limit`                      | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                                                                                                                                |
| `offset`                     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                                                                                                                            |
| `exclude_sensors`            | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Whether to exclude sensors in the response (as these can slow down requests when you have large pages).')] = None`                                                                                                                 |
| `labels`                     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label within the given list of labels, given as a JSON string')] = None`                                                                                                                                |
| `filename`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples whose filename includes the given filename')] = None`                                                                                                                                                          |
| `max_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples shorter than the given length, in milliseconds')] = None`                                                                                                                                                      |
| `min_length`                 | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples longer than the given length, in milliseconds')] = None`                                                                                                                                                       |
| `min_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with higher frequency than given frequency, in hertz')] = None`                                                                                                                                                                              |
| `max_frequency`              | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with lower frequency than given frequency, in hertz')] = None`                                                                                                                                                                               |
| `signature_validity`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include samples with either valid or invalid signatures')] = None`                                                                                                                                                                  |
| `include_disabled`           | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only enabled or disabled samples (or both)')] = None`                                                                                                                                                                       |
| `min_label`                  | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label >= this value')] = None`                                                                                                                                                                                                        |
| `max_label`                  | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples with a label < this value')] = None`                                                                                                                                                                                                         |
| `search`                     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Search query')] = None`                                                                                                                                                                                                             |
| `proposed_actions_job_id`    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Pass this parameter when querying samples from inside an AI Action job. If you pass this parameter in a multi-stage AI Action, previous proposed changes (from an earlier step) will be applied to the returned dataset.')] = None` |
| `truncate_structured_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If true, only a slice of labels will be returned for samples with multiple labels.')] = None`                                                                                                                                      |
| `sort_by`                    | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If not specified, "id-desc" is used.')] = None`                                                                                                                                                                                     |
| `data_type`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with a particular data type')] = None`                                                                                                                                                                         |
| `min_id`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID >= this value')] = None`                                                                                                                                                                                                          |
| `max_id`                     | `Annotated[float \| None, FieldInfo(annotation=NoneType, required=True, description='Include only samples with an ID < this value')] = None`                                                                                                                                                                                                           |
| `metadata`                   | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Filter samples by metadata key-value pairs, provided as a JSON string. Each item in the filter list is an object with the following properties`                                                                                     |
| `min_date`                   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that where added after the date given')] = None`                                                                                                                                                                                 |
| `max_date`                   | `Annotated[datetime.datetime \| None, FieldInfo(annotation=NoneType, required=True, description='Only include samples that were added before the date given')] = None`                                                                                                                                                                                 |
| `**kwargs`                   | ` `                                                                                                                                                                                                                                                                                                                                                    |

| Returns                                                            |
| ------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_samples_response.ListSamplesResponse` |

#### move\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.move_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	move_raw_data_request: edgeimpulse_api.models.move_raw_data_request.MoveRawDataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Move sample

Move a sample to another category (e.g. from test to training).

| Parameters              |                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                            |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `move_raw_data_request` | `edgeimpulse_api.models.move_raw_data_request.MoveRawDataRequest`                                              |
| `**kwargs`              | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### move\_to\_labeling\_queue

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.move_to_labeling_queue(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Move sample to labeling queue

Clears the bounding box labels and moves item back to labeling queue

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### rebalance\_dataset

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.rebalance_dataset(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.rebalance_dataset_response.RebalanceDatasetResponse
```

Rebalance dataset

This API is deprecated, use rebalanceDatasetV2 instead (`/v1/api/{projectId}/v2/rebalance`). Rebalances the dataset over training / testing categories. This resets the category for all data and splits it 80%/20% between training and testing. This is a deterministic process based on the hash of the name of the data.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                      |
| ---------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_response.RebalanceDatasetResponse` |

#### rebalance\_dataset\_v2

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.rebalance_dataset_v2(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	**kwargs
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Rebalance dataset

Rebalances the dataset over training / testing categories. This resets the category for all data and splits it 80%/20% between training and testing. This is a deterministic process based on the hash of the name of the data. Returns immediately on small datasets, or starts a job on larger datasets. To get the dataset ratio (as returned by the v1 endpoint), use getDatasetRatio.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### rename\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.rename_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	rename_sample_request: edgeimpulse_api.models.rename_sample_request.RenameSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Rename sample

Sets the file name of the sample. This name does not need to be unique, but it's highly recommended to do so.

| Parameters              |                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                            |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `rename_sample_request` | `edgeimpulse_api.models.rename_sample_request.RenameSampleRequest`                                             |
| `**kwargs`              | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### retry\_processing

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.retry_processing(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Retry processing

If a sample failed processing, retry the processing operation.

| Parameters   |                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                            |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `**kwargs`   | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### segment\_sample

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.segment_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	segment_sample_request: edgeimpulse_api.models.segment_sample_request.SegmentSampleRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Segment sample

Slice a sample into multiple segments. The original file will be marked as deleted, but you can crop any created segment to retrieve the original file.

| Parameters               |                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                            |
| `project_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `segment_sample_request` | `edgeimpulse_api.models.segment_sample_request.SegmentSampleRequest`                                           |
| `**kwargs`               | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_data\_explorer\_settings

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_data_explorer_settings(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	data_explorer_settings: edgeimpulse_api.models.data_explorer_settings.DataExplorerSettings,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set data explorer settings

Set data explorer configuration, like the type of data, and the input / dsp block to use.

| Parameters               |                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                   | ` `                                                                                                            |
| `project_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `data_explorer_settings` | `edgeimpulse_api.models.data_explorer_settings.DataExplorerSettings`                                           |
| `**kwargs`               | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_sample\_bounding\_boxes

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_sample_bounding_boxes(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	sample_bounding_boxes_request: edgeimpulse_api.models.sample_bounding_boxes_request.SampleBoundingBoxesRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set bounding boxes

Set the bounding boxes for a sample

| Parameters                      |                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                            |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `sample_bounding_boxes_request` | `edgeimpulse_api.models.sample_bounding_boxes_request.SampleBoundingBoxesRequest`                              |
| `**kwargs`                      | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_sample\_metadata

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_sample_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	set_sample_metadata_request: edgeimpulse_api.models.set_sample_metadata_request.SetSampleMetadataRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set sample metadata

Adds or updates the metadata associated to a sample.

| Parameters                    |                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                            |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `set_sample_metadata_request` | `edgeimpulse_api.models.set_sample_metadata_request.SetSampleMetadataRequest`                                  |
| `**kwargs`                    | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_sample\_proposed\_changes

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_sample_proposed_changes(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	set_sample_proposed_changes_request: edgeimpulse_api.models.set_sample_proposed_changes_request.SetSampleProposedChangesRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Propose changes

Queue up changes to an object as part of the AI Actions flow. This overwrites any previous proposed changes.

| Parameters                            |                                                                                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                            |
| `project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `set_sample_proposed_changes_request` | `edgeimpulse_api.models.set_sample_proposed_changes_request.SetSampleProposedChangesRequest`                   |
| `**kwargs`                            | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_sample\_structured\_labels

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_sample_structured_labels(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	set_sample_structured_labels_request: edgeimpulse_api.models.set_sample_structured_labels_request.SetSampleStructuredLabelsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update structured labels

Set structured labels for a sample. If a sample has structured labels the `label` column is ignored, and the sample is allowed to have multiple labels. An array of `{ startIndex, endIndex, label }` needs to be passed in with labels for the complete sample (see `valuesCount` to get the upper bound). endIndex is *inclusive*. If you pass in an incorrect array (e.g. missing values) you'll get an error back.

| Parameters                             |                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                 | ` `                                                                                                            |
| `project_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `set_sample_structured_labels_request` | `edgeimpulse_api.models.set_sample_structured_labels_request.SetSampleStructuredLabelsRequest`                 |
| `**kwargs`                             | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_sample\_video\_dimensions

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.set_sample_video_dimensions(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	set_sample_video_dimensions_request: edgeimpulse_api.models.set_sample_video_dimensions_request.SetSampleVideoDimensionsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set sample video dimensions

Update the video dimensions for a sample. This is only available for video files that do not have dimensions set yet.

| Parameters                            |                                                                                                                |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                            |
| `project_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `set_sample_video_dimensions_request` | `edgeimpulse_api.models.set_sample_video_dimensions_request.SetSampleVideoDimensionsRequest`                   |
| `**kwargs`                            | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### split\_sample\_in\_frames

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.split_sample_in_frames(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	split_sample_in_frames_request: edgeimpulse_api.models.split_sample_in_frames_request.SplitSampleInFramesRequest,
	**kwargs
) ‑> edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response
```

Split sample into frames

Split a video sample into individual frames. Depending on the length of the video sample this will either execute immediately or return the ID of a job that will perform this action.

| Parameters                       |                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                            |
| `project_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `sample_id`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`  |
| `split_sample_in_frames_request` | `edgeimpulse_api.models.split_sample_in_frames_request.SplitSampleInFramesRequest`                             |
| `**kwargs`                       | ` `                                                                                                            |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.rebalance_dataset_v2200_response.RebalanceDatasetV2200Response` |

#### store\_segment\_length

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.store_segment_length(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	store_segment_length_request: edgeimpulse_api.models.store_segment_length_request.StoreSegmentLengthRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Store the last segment length

When segmenting a sample into smaller segments, store the segment length to ensure uniform segment lengths.

| Parameters                     |                                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                            |
| `project_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `store_segment_length_request` | `edgeimpulse_api.models.store_segment_length_request.StoreSegmentLengthRequest`                                |
| `**kwargs`                     | ` `                                                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### track\_objects

```python  theme={"system"}
edgeimpulse_api.api.raw_data_api.RawDataApi.track_objects(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	track_objects_request: edgeimpulse_api.models.track_objects_request.TrackObjectsRequest,
	**kwargs
) ‑> edgeimpulse_api.models.track_objects_response.TrackObjectsResponse
```

Track objects

Track objects between two samples. Source sample should have bounding boxes set.

| Parameters              |                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| `self`                  | ` `                                                                                                            |
| `project_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]` |
| `track_objects_request` | `edgeimpulse_api.models.track_objects_request.TrackObjectsRequest`                                             |
| `**kwargs`              | ` `                                                                                                            |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.track_objects_response.TrackObjectsResponse` |


Built with [Mintlify](https://mintlify.com).