# BBOX Annotation response formats
class Image(BaseModel):
  image_type: str
  short_description: str
  summary: str
```

You can also provide a description for each entry, the description will be used as detailed information and instructions during the annotation; for example:

```python
from pydantic import BaseModel, Field