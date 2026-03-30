# patito.Model.defaults

*property *Model.defaults*: dict[str, Any]*

Return default field values specified on the model.

Returns:

Dictionary containing fields with their respective default values.

Example

```
>>> from typing_extensions import Literal
>>> import patito as pt
>>> class Product(pt.Model):
...     name: str
...     price: int = 0
...     temperature_zone: Literal["dry", "cold", "frozen"] = "dry"
...
>>> Product.defaults
{'price': 0, 'temperature_zone': 'dry'}

```