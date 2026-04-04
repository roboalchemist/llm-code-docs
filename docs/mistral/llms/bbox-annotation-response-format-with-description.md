# BBOX Annotation response format with description
class Image(BaseModel):
  image_type: str = Field(..., description="The type of the image.")
  short_description: str = Field(..., description="A description in english describing the image.")
  summary: str = Field(..., description="Summarize the image.")