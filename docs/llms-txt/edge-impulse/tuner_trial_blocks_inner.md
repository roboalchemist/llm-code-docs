# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/tuner_trial_blocks_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.tuner_trial_blocks_inner

## Classes

### TunerTrialBlocksInner

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner(
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

| Class variables     |                                       |
| ------------------- | ------------------------------------- |
| `Config`            | ` `                                   |
| `id`                | `pydantic.v1.types.StrictInt`         |
| `last_active`       | `datetime.datetime \| None`           |
| `model_block_index` | `pydantic.v1.types.StrictInt \| None` |
| `retries`           | `pydantic.v1.types.StrictInt`         |
| `status`            | `pydantic.v1.types.StrictStr`         |
| `type`              | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner
```

Create an instance of TunerTrialBlocksInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner
```

Create an instance of TunerTrialBlocksInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                 |
| ----------------------------------------------------------------------- |
| `edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner` |

#### status\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.status_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.to_json(
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
edgeimpulse_api.models.tuner_trial_blocks_inner.TunerTrialBlocksInner.to_str(
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