# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/dsp_group_item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.dsp_group_item

## Classes

### DSPGroupItem

```python  theme={"system"}
edgeimpulse_api.models.dsp_group_item.DSPGroupItem(
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

| Class variables     |                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| `Config`            | ` `                                                                                                       |
| `default_value`     | `pydantic.v1.types.StrictStr`                                                                             |
| `help`              | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `hint`              | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `invalid_text`      | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `items`             | `Dict[str, Any] \| None`                                                                                  |
| `max_val`           | `float \| None`                                                                                           |
| `min_val`           | `float \| None`                                                                                           |
| `multiline`         | `pydantic.v1.types.StrictBool \| None`                                                                    |
| `name`              | `pydantic.v1.types.StrictStr`                                                                             |
| `param`             | `pydantic.v1.types.StrictStr`                                                                             |
| `placeholder`       | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `properties`        | `Dict[str, Any] \| None`                                                                                  |
| `readonly`          | `pydantic.v1.types.StrictBool`                                                                            |
| `required`          | `pydantic.v1.types.StrictBool`                                                                            |
| `section`           | `pydantic.v1.types.StrictStr \| None`                                                                     |
| `select_options`    | `List[edgeimpulse_api.models.dsp_group_item_select_options_inner.DSPGroupItemSelectOptionsInner] \| None` |
| `should_show`       | `pydantic.v1.types.StrictBool`                                                                            |
| `show_click_to_set` | `pydantic.v1.types.StrictBool`                                                                            |
| `show_if`           | `edgeimpulse_api.models.dsp_group_item_show_if.DSPGroupItemShowIf \| None`                                |
| `type`              | `pydantic.v1.types.StrictStr`                                                                             |
| `valid`             | `List[Dict[str, Any]] \| None`                                                                            |
| `value`             | `pydantic.v1.types.StrictStr \| None`                                                                     |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.dsp_group_item.DSPGroupItem
```

Create an instance of DSPGroupItem from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse_api.models.dsp_group_item.DSPGroupItem` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.dsp_group_item.DSPGroupItem
```

Create an instance of DSPGroupItem from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                              |
| ---------------------------------------------------- |
| `edgeimpulse_api.models.dsp_group_item.DSPGroupItem` |

#### section\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.section_validate_enum(
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
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.to_json(
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
edgeimpulse_api.models.dsp_group_item.DSPGroupItem.to_str(
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