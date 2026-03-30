# Document Annotation response format
class Document(BaseModel):
  language: str
  chapter_titles: list[str]
  urls: list[str]
```

**Start the completion**

Next, use the Mistral AI python client to make a request and ensure the response adheres to the defined structures using `document_annotation_format` set to the corresponding pydantic model:

```python

from mistralai import Mistral, DocumentURLChunk, ImageURLChunk, ResponseFormat
from mistralai.extra import response_format_from_pydantic_model

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)