# Source: https://docs.aurelio.ai/semantic-router/client-reference/routers/semantic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.routers.semantic

## SemanticRouter Objects

```python  theme={null}
class SemanticRouter(BaseRouter)
```

A router that uses a dense encoder to encode routes and utterances.

#### add

```python  theme={null}
def add(routes: List[Route] | Route)
```

Add a route to the local SemanticRouter and index.

**Arguments**:

* `route` (`Route`): The route to add.

#### aadd

```python  theme={null}
async def aadd(routes: List[Route] | Route)
```

Asynchronously add a route to the local SemanticRouter and index.

**Arguments**:

* `routes` (`List[Route] | Route`): The route(s) to add.


Built with [Mintlify](https://mintlify.com).