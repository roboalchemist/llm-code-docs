# Client call
response = client.ocr.process(
    model="mistral-ocr-latest",
    pages=list(range(8)),
    document=DocumentURLChunk(
      document_url="https://arxiv.org/pdf/2410.07073"
    ),
    document_annotation_format=response_format_from_pydantic_model(Document),
    include_image_base64=True
  )
```
  </TabItem>
   <TabItem value="typescript" label="typescript" default>

Here is an example of how to use our Document Annotation functionality using the Mistral AI client and Zod:

**Define the Data Model**

First, define the response formats for `Document Annotation` using a Zod schema:

```typescript


// Document Annotation response format
const DocumentSchema = z.object({
  language: z.string(),
  chapter_titles: z.array(z.string()),
  urls: z.array(z.string()),
});
```

**Start the completion**

Next, use the Mistral AI typescript client to make a request and ensure the response adheres to the defined structures using `document_annotation_format` set to the corresponding Zod schema:

```typescript


const apiKey = process.env.MISTRAL_API_KEY;

const client = new Mistral({ apiKey: apiKey });

async function processDocument() {
  try {
    const response = await client.ocr.process({
      model: "mistral-ocr-latest",
      pages: Array.from({ length: 8 }, (_, i) => i), // Creates an array [0, 1, 2, ..., 7]
      document: {
        type: "document_url",
        documentUrl: "https://arxiv.org/pdf/2410.07073"
      },
      documentAnnotationFormat: responseFormatFromZodObject(DocumentSchema),
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

The request is structured to ensure that the response adheres to the specified custom JSON schema. The schema defines the structure of a `document_annotation` object with with `language`, `chapter_titles` and `urls` properties.

```bash
curl --location 'https://api.mistral.ai/v1/ocr' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer ${MISTRAL_API_KEY}" \
--data '{
    "model": "mistral-ocr-latest",
    "document": {"document_url": "https://arxiv.org/pdf/2410.07073"},
    "pages": [0, 1, 2, 3, 4, 5, 6, 7],
    "document_annotation_format": {
        "type": "json_schema",
        "json_schema": {
            "schema": {
                "properties": {
                    "language": {"title": "Language", "type": "string"},
                    "chapter_titles": {"title": "Chapter_Titles", "type": "string"},
                    "urls": {"title": "urls", "type": "string"}
                },
                "required": ["language", "chapter_titles", "urls"],
                "title": "DocumentAnnotation",
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

**Document Annotation Output**
```json
{
  "language": "English",
  "chapter_titles": [
    "Abstract",
    "1 Introduction",
    "2 Architectural details",
    "2.1 Multimodal Decoder",
    "2.2 Vision Encoder",
    "2.3 Complete architecture",
    "3 MM-MT-Bench: A benchmark for multi-modal instruction following",
    "4 Results",
    "4.1 Main Results",
    "4.2 Prompt selection",
    "4.3 Sensitivity to evaluation metrics",
    "4.4 Vision Encoder Ablations"
  ],
  "urls": [
    "https://mistral.ai/news/pixtal-12b/",
    "https://github.com/mistralai/mistral-inference/",
    "https://github.com/mistralai/mistral-evals/",
    "https://huggingface.co/datasets/mistralai/MM-MT-Bench"
  ]
} 
```
</details>

## BBoxes Annotation and Document Annotation

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

Here is an example of how to use our Annotation functionalities using the Mistral AI client and Pydantic:

**Define the Data Model**

First, define the response formats for both `BBox Annotation` and `Document Annotation` using Pydantic models:

```python
from pydantic import BaseModel