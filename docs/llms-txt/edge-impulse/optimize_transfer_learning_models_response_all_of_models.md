# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of_models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models

## Classes

### OptimizeTransferLearningModelsResponseAllOfModels

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels(
	**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

| Parameters |       |
| ---------- | ----- |
| `**data`   | `Any` |

| Bases                              |
| ---------------------------------- |
| `pydantic.v1.main.BaseModel`       |
| `pydantic.v1.utils.Representation` |

| Class variables    |                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------ |
| `Config`           | ` `                                                                                  |
| `anomaly`          | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel] \| None` |
| `classification`   | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`         |
| `image`            | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`         |
| `kws`              | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`         |
| `object_detection` | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`         |
| `regression`       | `List[edgeimpulse_api.models.transfer_learning_model.TransferLearningModel]`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels
```

Create an instance of OptimizeTransferLearningModelsResponseAllOfModels from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels
```

Create an instance of OptimizeTransferLearningModelsResponseAllOfModels from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.optimize_transfer_learning_models_response_all_of_models.OptimizeTransferLearningModelsResponseAllOfModels.to_str(
	self
) ‑> str
```

Returns the string representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).