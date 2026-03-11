# Source: https://docs.aurelio.ai/graphai/client-reference/utils.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# graphai.utils

## StrEnum Objects

```python  theme={null}
class StrEnum(str, Enum)
```

Backport of StrEnum for Python \< 3.11

## ColoredFormatter Objects

```python  theme={null}
class ColoredFormatter(logging.Formatter)
```

Custom colored formatter for the logger using ANSI escape codes.

#### add\_coloured\_handler

```python  theme={null}
def add_coloured_handler(logger)
```

Add a coloured handler to the logger.

#### setup\_custom\_logger

```python  theme={null}
def setup_custom_logger(name)
```

Setup a custom logger.

## Parameter Objects

```python  theme={null}
class Parameter(BaseModel)
```

Parameter for a function.

**Arguments**:

* `name` (`str`): The name of the parameter.
* `description` (`str | None`): The description of the parameter.
* `type` (`str`): The type of the parameter.
* `default` (`Any`): The default value of the parameter.
* `required` (`bool`): Whether the parameter is required.

#### to\_dict

```python  theme={null}
def to_dict() -> dict[str, Any]
```

Convert the parameter to a dictionary for an standard dictionary-based function schema.

This is the most common format used by LLM providers, including OpenAI, Ollama, and others.

**Returns**:

`dict[str, Any]`: The parameter in dictionary format.

## FunctionSchema Objects

```python  theme={null}
class FunctionSchema(BaseModel)
```

Class that consumes a function and can return a schema required by
different LLMs for function calling.

#### from\_callable

```python  theme={null}
@classmethod
def from_callable(cls, function: Callable) -> "FunctionSchema"
```

Initialize the FunctionSchema.

**Arguments**:

* `function` (`Callable`): The function to consume.

#### from\_pydantic

```python  theme={null}
@classmethod
def from_pydantic(cls, model: type[BaseModel]) -> "FunctionSchema"
```

Create a FunctionSchema from a Pydantic model class.

**Arguments**:

* `model` (`type[BaseModel]`): The Pydantic model class to convert

**Returns**:

`FunctionSchema`: FunctionSchema instance

#### to\_openai

```python  theme={null}
def to_openai(api: OpenAIAPI = OpenAIAPI.COMPLETIONS) -> dict[str, Any]
```

Convert the function schema into OpenAI-compatible formats. Supports

both completions and responses APIs.

**Arguments**:

* `api` (`OpenAIAPI`): The API to convert to.

**Returns**:

`dict`: The function schema in OpenAI-compatible format.


Built with [Mintlify](https://mintlify.com).