# BBOX Annotation response formats
class Image(BaseModel):
  image_type: str = Field(..., description="The type of the image.")
  short_description: str = Field(..., description="A description in english describing the image.")
  summary: str = Field(..., description="Summarize the image.")
```

**Start the completion**

Next, use the Mistral AI python client to make a request and ensure the response adheres to the defined structures using `bbox_annotation_format` set to the corresponding pydantic models:

```python

from mistralai import Mistral, DocumentURLChunk, ImageURLChunk, ResponseFormat
from mistralai.extra import response_format_from_pydantic_model

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)