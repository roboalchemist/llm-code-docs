# Client call
response = client.ocr.process(
    model="mistral-ocr-latest",
    pages=list(range(8)),
    document=DocumentURLChunk(
      document_url="https://arxiv.org/pdf/2410.07073"
    ),
    bbox_annotation_format=response_format_from_pydantic_model(Image),
    document_annotation_format=response_format_from_pydantic_model(Document),
    include_image_base64=True
  )
```
  </TabItem>
   <TabItem value="typescript" label="typescript" default>

Here is an example of how to use our Annotation functionalities using the Mistral AI client and Zod:

**Define the Data Model**

First, define the response formats for both `BBox Annotation` and `Document Annotation` using Zod schemas:

```typescript


// BBOX Annotation response format
const ImageSchema = z.object({
  image_type: z.string(),
  short_description: z.string(),
  summary: z.string(),
});

// Document Annotation response format
const DocumentSchema = z.object({
  language: z.string(),
  chapter_titles: z.array(z.string()),
  urls: z.array(z.string()),
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

// Document Annotation response format
const DocumentSchema = z.object({
  language: z.string(),
  chapter_titles: z.array(z.string()),
  urls: z.array(z.string()),
});
```

**Start the completion**

Next, use the Mistral AI typescript client to make a request and ensure the response adheres to the defined structures using `bbox_annotation_format` and `document_annotation_format` set to the corresponding Zod schemas:

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
      bboxAnnotationFormat: responseFormatFromZodObject(ImageSchema),
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

The request is structured to ensure that the response adheres to the specified custom JSON schema. The schema defines the structure of a `bbox_annotation` object with `image_type`, `short_description` and `summary` properties and a `document_annotation` object with with `language`, `chapter_titles` and `urls` properties.

```bash
curl --location 'https://api.mistral.ai/v1/ocr' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer ${MISTRAL_API_KEY}" \
--data '{
    "model": "mistral-ocr-latest",
    "document": {"document_url": "https://arxiv.org/pdf/2410.07073"},
    "pages": [0, 1, 2, 3, 4, 5, 6, 7],
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


You can also add a `description` key in you `properties` object. The description will be used as detailed information and instructions during the annotation; for example:

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

## Cookbooks
For more information and guides on how to make use of OCR, we have the following cookbooks:
- [Data Extraction with Structured Outputs](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/ocr/data_extraction.ipynb)

## FAQ
**Q: Are there any limits regarding the Document Intelligence API?**\
A: Yes, there are certain limitations for the Document Intelligence API. Uploaded document files must not exceed 50 MB in size and should be no longer than 1,000 pages.

**Q: Are there any limits regarding the Annotations?**\
A: When using Document Annotations, the file cannot have more than 8 pages. BBox Annotations does not have the same limit.


[Basic OCR]
Source: https://docs.mistral.ai/docs/capabilities/document_ai/basic_ocr

## Document AI OCR processor 

Mistral Document AI API comes with a Document OCR (Optical Character Recognition) processor, powered by our latest OCR model `mistral-ocr-latest`, which enables you to extract text and structured content from PDF documents. 

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/basic_ocr_graph.png"
    alt="Basic OCR Graph"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>

**Key features**:
- Extracts text content while maintaining document structure and hierarchy
- Preserves formatting like headers, paragraphs, lists and tables
- Returns results in markdown format for easy parsing and rendering
- Handles complex layouts including multi-column text and mixed content
- Processes documents at scale with high accuracy
- Supports multiple document formats including:
    - `image_url`: png, jpeg/jpg, avif and more...
    - `document_url`: pdf, pptx, docx and more...

The OCR processor returns the extracted **text content**, **images bboxes** and metadata about the document structure, making it easy to work with the recognized content programmatically.

### OCR with PDF

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": "https://arxiv.org/pdf/2201.04234"
    },
    include_image_base64=True
)
```

Or passing a Base64 encoded pdf:
```python


from mistralai import Mistral

def encode_pdf(pdf_path):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None