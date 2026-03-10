# Document Annotation response format
class Document(BaseModel):
  language: str
  chapter_titles: list[str]
  urls: list[str]
```

You can also provide a description for each entry, the description will be used as detailed information and instructions during the annotation; for example:

```python
from pydantic import BaseModel, Field