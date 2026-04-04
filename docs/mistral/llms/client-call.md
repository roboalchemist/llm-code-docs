# Client call
response = client.ocr.process(
    model="mistral-ocr-latest",
    document=DocumentURLChunk(
      document_url="https://arxiv.org/pdf/2410.07073"
    ),
    bbox_annotation_format=response_format_from_pydantic_model(Image),
    include_image_base64=True
  )
```
  </TabItem>
   <TabItem value="typescript" label="typescript" default>

Here is an example of how to use our Annotation functionalities using the Mistral AI client and Zod:

**Define the Data Model**

First, define the response formats for `BBox Annotation` using Zod schemas:

```typescript


// BBOX Annotation response formats
const ImageSchema = z.object({
  image_type: z.string(),
  short_description: z.string(),
  summary: z.string(),
});
```

You can also provide a description for each entry, the description will be used as detailed information and instructions during the annotation; for example:

```typescript


// Define the schema for the Image type
const ImageSchema = z.object({
  image_type: z.string().describe("The type of the image."),
  short_description: z.string().describe("A description in English describing the image."),
  summary: z.string().describe("Summarize the image."),
});
```


**Start the completion**

Next, use the Mistral AI typescript client to make a request and ensure the response adheres to the defined structure using `bbox_annotation_format` set to the corresponding Zod schema:

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({ apiKey: apiKey });

async function processDocument() {
  try {
    const response = await client.ocr.process({
      model: "mistral-ocr-latest",
      document: {
        type: "document_url",
        documentUrl: "https://arxiv.org/pdf/2410.07073"
      },
      bboxAnnotationFormat: responseFormatFromZodObject(ImageSchema),
      includeImageBase64: true,
    });

    console.log(response);
  } catch (error) {
    console.error("Error processing document:", error);
  }
}

processDocument();

```
  </TabItem>
  <TabItem value="curl" label="curl">

The request is structured to ensure that the response adheres to the specified custom JSON schema. The schema defines the structure of a `bbox_annotation` object with `image_type`, `short_description` and `summary` properties.

```bash
curl --location 'https://api.mistral.ai/v1/ocr' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer ${MISTRAL_API_KEY}" \
--data '{
    "model": "mistral-ocr-latest",
    "document": {"document_url": "https://arxiv.org/pdf/2410.07073"},
    "bbox_annotation_format": {
        "type": "json_schema",
        "json_schema": {
            "schema": {
                "properties": {
                    "document_type": {"title": "Document_Type", "type": "string"},
                    "short_description": {"title": "Short_Description", "type": "string"},
                    "summary": {"title": "Summary", "type": "string"}
                },
                "required": ["document_type", "short_description", "summary"],
                "title": "BBOXAnnotation",
                "type": "object",
                "additionalProperties": false
            },
            "name": "document_annotation",
            "strict": true
        }
    },
    "include_image_base64": true
}'
```

You can also add a `description` key in your `properties` object. The description will be used as detailed information and instructions during the annotation; for example:

```bash
curl --location 'https://api.mistral.ai/v1/ocr' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer ${MISTRAL_API_KEY}" \
--data '{
    "model": "mistral-ocr-latest",
    "document": {"document_url": "https://arxiv.org/pdf/2410.07073"},
    "bbox_annotation_format": {
        "type": "json_schema",
        "json_schema": {
            "schema": {
                "properties": {
                    "document_type": {"title": "Document_Type", "description": "The type of the image.", "type": "string"},
                    "short_description": {"title": "Short_Description", "description": "A description in English describing the image.", "type": "string"},
                    "summary": {"title": "Summary", "description": "Summarize the image.", "type": "string"}
                },
                "required": ["document_type", "short_description", "summary"],
                "title": "BBOXAnnotation",
                "type": "object",
                "additionalProperties": false
            },
            "name": "document_annotation",
            "strict": true
        }
    },
    "include_image_base64": true
}'
```
  </TabItem>
</Tabs>

<details>
<summary><b>Example output</b></summary>

**BBOX Image**
<div style={{ textAlign: 'center' }}>
  <img
    src="/img/img-1.jpeg"
    alt="bbox-image"
    width="800"
    style={{ borderRadius: '15px' }}
  />
</div>

**Image Base 64**
```json
{ 
  "image_base64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGB{LONG_MIDDLE_SEQUENCE}KKACiiigAooooAKKKKACiiigD//2Q==" 
}
```

**BBOX Annotation Output**
```json
{
  "image_type": "scatter plot",
  "short_description": "Comparison of different models based on performance and cost.",
  "summary": "The image consists of two scatter plots comparing various models on two different performance metrics against their cost or number of parameters. The left plot shows performance on the MM-MT-Bench, while the right plot shows performance on the LMSys-Vision ELO. Each point represents a different model, with the x-axis indicating the cost or number of parameters in billions (B) and the y-axis indicating the performance score. The shaded region in both plots highlights the best performance/cost ratio, with Pixtral 12B positioned within this region in both plots, suggesting it offers a strong balance of performance and cost efficiency. Other models like Qwen-2-VL 72B and Qwen-2-VL 7B also show high performance but at varying costs."
}
```
</details>

## Document Annotation

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

Here is an example of how to use our Document Annotation functionality using the Mistral AI client and Pydantic:

**Define the Data Model**

First, define the response format for `Document Annotation` using a Pydantic model:

```python
from pydantic import BaseModel