# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/tfidf.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.tfidf

## TfidfEncoder Objects

```python  theme={null}
class TfidfEncoder(SparseEncoder, FittableMixin)
```

#### fit

```python  theme={null}
def fit(routes: List[Route])
```

Trains the encoder weights on the provided routes.

**Arguments**:

* `routes` (`List[Route]`): List of routes to train the encoder on.


Built with [Mintlify](https://mintlify.com).