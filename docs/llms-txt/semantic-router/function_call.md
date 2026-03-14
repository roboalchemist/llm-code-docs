# Source: https://docs.aurelio.ai/semantic-router/client-reference/utils/function_call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.utils.function_call

## Parameter Objects

```python  theme={null}
class Parameter(BaseModel)
```

Parameter for a function.

**Arguments**:

* `name` (`str`): The name of the parameter.
* `description` (`Optional[str]`): The description of the parameter.
* `type` (`str`): The type of the parameter.
* `default` (`Any`): The default value of the parameter.
* `required` (`bool`): Whether the parameter is required.

#### to\_ollama

```python  theme={null}
def to_ollama()
```

Convert the parameter to a dictionary for an Ollama-compatible function schema.

**Returns**:

`Dict[str, Any]`: The parameter in dictionary format.

## FunctionSchema Objects

```python  theme={null}
class FunctionSchema()
```

Class that consumes a function and can return a schema required by
different LLMs for function calling.

#### \_\_init\_\_

```python  theme={null}
def __init__(function: Union[Callable, BaseModel])
```

Initialize the FunctionSchema.

**Arguments**:

* `function` (`Union[Callable, BaseModel]`): The function to consume.

#### to\_ollama

```python  theme={null}
def to_ollama()
```

Convert the FunctionSchema to an Ollama-compatible function schema dictionary.

**Returns**:

`Dict[str, Any]`: The function schema in dictionary format.

#### get\_schema\_list

```python  theme={null}
def get_schema_list(
        items: List[Union[BaseModel, Callable]]) -> List[Dict[str, Any]]
```

Get a list of function schemas from a list of functions or Pydantic BaseModels.

**Arguments**:

* `items` (`List[Union[BaseModel, Callable]]`): The functions or BaseModels to get the schemas for.

**Returns**:

`List[Dict[str, Any]]`: A list of function schemas.

#### get\_schema

```python  theme={null}
def get_schema(item: Union[BaseModel, Callable]) -> Dict[str, Any]
```

Get a function schema from a function or Pydantic BaseModel.

**Arguments**:

* `item` (`Union[BaseModel, Callable]`): The function or BaseModel to get the schema for.

**Returns**:

`Dict[str, Any]`: The function schema.

#### convert\_python\_type\_to\_json\_type

```python  theme={null}
def convert_python_type_to_json_type(param_type: str) -> str
```

Convert a Python type to a JSON type.

**Arguments**:

* `param_type` (`str`): The type of the parameter.

**Returns**:

`str`: The JSON type.

#### route\_and\_execute

```python  theme={null}
async def route_and_execute(query: str, llm: BaseLLM,
                            functions: List[Callable], layer) -> Any
```

Route and execute a function.

**Arguments**:

* `query` (`str`): The query to route and execute.
* `llm` (`BaseLLM`): The LLM to use.
* `functions` (`List[Callable]`): The functions to execute.
* `layer` (`Layer`): The layer to use.

**Returns**:

`Any`: The result of the function.


Built with [Mintlify](https://mintlify.com).