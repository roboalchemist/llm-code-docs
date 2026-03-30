# patito.Model.DataFrame

Model.DataFrame(*data=None*, *schema=None*, ***, *schema_overrides=None*, *orient=None*, *infer_schema_length=100*, *nan_to_null=False*)

A sub-class of polars.DataFrame with additional functionality related to Model.

Two different methods are available for constructing model-aware data frames.
Assume a simple model with two fields:

```
>>> import patito as pt
>>> class Product(pt.Model):
...     name: str
...     price_in_cents: int
...

```