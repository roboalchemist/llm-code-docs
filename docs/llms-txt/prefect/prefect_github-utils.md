# Source: https://docs.prefect.io/integrations/prefect-github/api-ref/prefect_github-utils.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# utils

# `prefect_github.utils`

Utilities to assist with using generated collections.

## Functions

### `camel_to_snake_case` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/utils.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
camel_to_snake_case(string: str) -> str
```

Converts CamelCase and lowerCamelCase to snake\_case.
Args:
string: The string in CamelCase or lowerCamelCase to convert.
Returns:
A snake\_case version of the string.

### `initialize_return_fields_defaults` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/utils.py#L25" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
initialize_return_fields_defaults(config_path: Union[Path, str]) -> List
```

Reads config\_path to parse out the desired default fields to return.
Args:
config\_path: The path to the config file.

### `strip_kwargs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-github/prefect_github/utils.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
strip_kwargs(**kwargs: Dict) -> Dict
```

Drops keyword arguments if value is None because sgqlc.Operation
errors out if a keyword argument is provided, but set to None.

**Args:**

* `**kwargs`: Input keyword arguments.

**Returns:**

* Stripped version of kwargs.


Built with [Mintlify](https://mintlify.com).