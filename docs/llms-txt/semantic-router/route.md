# Source: https://docs.aurelio.ai/semantic-router/client-reference/route.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.route

#### is\_valid

```python  theme={null}
def is_valid(route_config: str) -> bool
```

Check if the route config is valid.

**Arguments**:

* `route_config` (`str`): The route config to check.

**Returns**:

`bool`: Whether the route config is valid.

## Route Objects

```python  theme={null}
class Route(BaseModel)
```

A route for the semantic router.

**Arguments**:

* `name` (`str`): The name of the route.
* `utterances` (`Union[List[str], List[Any]]`): The utterances of the route.
* `description` (`Optional[str]`): The description of the route.
* `function_schemas` (`Optional[List[Dict[str, Any]]]`): The function schemas of the route.
* `llm` (`Optional[BaseLLM]`): The LLM to use.
* `str`0 (`str`1): The score threshold of the route.
* `str`2 (`str`3): The metadata of the route.

#### \_\_call\_\_

```python  theme={null}
def __call__(query: Optional[str] = None) -> RouteChoice
```

Call the route. If dynamic routes have been provided the query must have been

provided and the llm attribute must be set.

**Arguments**:

* `query` (`Optional[str]`): The query to pass to the route.

**Returns**:

`RouteChoice`: The route choice.

#### acall

```python  theme={null}
async def acall(query: Optional[str] = None) -> RouteChoice
```

Asynchronous call the route. If dynamic routes have been provided the query

must have been provided and the llm attribute must be set.

**Arguments**:

* `query` (`Optional[str]`): The query to pass to the route.

**Returns**:

`RouteChoice`: The route choice.

#### to\_dict

```python  theme={null}
def to_dict() -> Dict[str, Any]
```

Convert the route to a dictionary.

**Returns**:

`Dict[str, Any]`: The dictionary representation of the route.

#### from\_dict

```python  theme={null}
@classmethod
def from_dict(cls, data: Dict[str, Any])
```

Create a Route object from a dictionary.

**Arguments**:

* `data` (`Dict[str, Any]`): The dictionary to create the route from.

**Returns**:

`Route`: The created route.

#### from\_dynamic\_route

```python  theme={null}
@classmethod
def from_dynamic_route(cls, llm: BaseLLM, entities: List[Union[BaseModel,
                                                               Callable]],
                       route_name: str)
```

Generate a dynamic Route object from a list of functions or Pydantic models

using an LLM.

**Arguments**:

* `llm` (`BaseLLM`): The LLM to use.
* `entities` (`List[Union[BaseModel, Callable]]`): The entities to use.
* `route_name`: The name of the route.


Built with [Mintlify](https://mintlify.com).