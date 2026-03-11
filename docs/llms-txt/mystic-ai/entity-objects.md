# Source: https://docs.mystic.ai/docs/entity-objects.md

# Entity objects

# entity - class decorator

[Source on GitHub](https://github.com/mystic-ai/pipeline/blob/main/pipeline/objects/decorators.py#L114)

```python Py
pipeline.objects.decorators.entity(
	model_class: Any = None
)
```

## Description

The `entity` decorator is used on classes to allow the `Pipeline` context manager to treat them as model objects. A model can contain `pipe` decorated functions and allows for persistent logic to be present inside of the wrapped class (for caching etc).

## Parameters

* `model_class` (`Any`, optional) - The model class to be wrapped, this is implicitly passed in you do not manually pass this.

## Examples

```python Python
from pipeline import Pipeline, entity

...

@entity
class MyModel:
	def __init__(self, ...):
  	...
 
...


with Pipeline() as builder:
	...
  
  my_model = MyModel()
  
  ...
```