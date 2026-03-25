# Source: https://docs.aurelio.ai/semantic-router/client-reference/llms/llamacpp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.llms.llamacpp

## LlamaCppLLM Objects

```python  theme={null}
class LlamaCppLLM(BaseLLM)
```

LLM for LlamaCPP. Enables fully local LLM use, helpful for local implementation of
dynamic routes.

#### \_\_init\_\_

```python  theme={null}
def __init__(llm: Any,
             name: str = "llama.cpp",
             temperature: float = 0.2,
             max_tokens: Optional[int] = 200,
             grammar: Optional[Any] = None)
```

Initialize the LlamaCPPLLM.

**Arguments**:

* `llm` (`Any`): The LLM to use.
* `name` (`str`): The name of the LLM.
* `temperature` (`float`): The temperature of the LLM.
* `max_tokens` (`Optional[int]`): The maximum number of tokens to generate.
* `grammar` (`Optional[Any]`): The grammar to use.

#### \_\_call\_\_

```python  theme={null}
def __call__(messages: List[Message]) -> str
```

Call the LlamaCPPLLM.

**Arguments**:

* `messages` (`List[Message]`): The messages to pass to the LlamaCPPLLM.

**Returns**:

`str`: The response from the LlamaCPPLLM.

#### extract\_function\_inputs

```python  theme={null}
def extract_function_inputs(
        query: str, function_schemas: List[Dict[str,
                                                Any]]) -> List[Dict[str, Any]]
```

Extract the function inputs from the query.

**Arguments**:

* `query` (`str`): The query to extract the function inputs from.
* `function_schemas` (`List[Dict[str, Any]]`): The function schemas to extract the function inputs from.

**Returns**:

`List[Dict[str, Any]]`: The function inputs.


Built with [Mintlify](https://mintlify.com).