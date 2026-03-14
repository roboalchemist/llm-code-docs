# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/image-extraction.md

# Cortex AI Functions: Image extraction with AI_PARSE_DOCUMENT

AI_PARSE_DOCUMENT is a Cortex AI
function that extracts text, data, layout elements, and images, from PDFs, Word documents, and images. Use this
high-fidelity image extraction capability to power advanced, multimodal document processing workflows, such as:

* *Enrich data*: Extract images from documents to add visual context for deeper insights.
* *Multimodal RAG*: Combine images and text for retrieval-augmented generation (RAG) to improve model responses.
* *Image classification*: Use extracted images with AI_EXTRACT or AI_COMPLETE for automatic tagging and analysis.
* *Knowledge bases*: Build richer repositories by including both text and images for better search and reasoning.
* *Compliance*: Extract and analyze images (e.g., charts, signatures) for regulatory and audit workflows.

For an introduction to AI_PARSE_DOCUMENT, see [Parsing documents with AI_PARSE_DOCUMENT](parse-document.md).

## Using AI_PARSE_DOCUMENT to extract images

To extract images from a document using AI_PARSE_DOCUMENT:

* Set the `'mode'` option to `'LAYOUT'`. Image extraction requires LAYOUT mode.
* Set the `'extract_images'` option to TRUE.

AI_PARSE_DOCUMENT image extraction returns an array, `images`, in the JSON output. Each element of `images` contains a
field, `image_base64`, with the extracted image data encoded as a base64 string. Image OBJECT_CONSTRUCT also contains fields
for a unique ID and image bounding boxes.

```sqlexample
SELECT AI_PARSE_DOCUMENT(
    TO_FILE('@my_stage', 'my_document.pdf'),
    {'mode': 'LAYOUT', 'extract_images': true})
AS layout_wƒith_images;
```

You can decode the images using BASE64_DECODE_BINARY, then pass them directly to AI_EXTRACT to process or describe the
image contents. Alternatively, you can store them in a stage for processing using multimodal AI_COMPLETE. (AI_COMPLETE
does not currently support direct image input.)

## Examples

### Extract and describe images

After extracting image data, you can use AI_EXTRACT to process or describe the image content. The following example
generates a description for the first extracted image after converting it to binary from base64. (AI_EXTRACT requires
binary input.) The query uses a regular expression to strip the metadata (schema and format) from the base64 string.

```sqlexample
SELECT AI_EXTRACT(
file_data => BASE64_DECODE_BINARY(
    REGEXP_REPLACE(
    (
        SELECT (
            AI_PARSE_DOCUMENT(
                TO_FILE('@image_docs', 'my_document.pdf'),
                {'mode': 'LAYOUT', 'extract_images': true}
            ):images[0]['image_base64']
            )::STRING
        ),
    '^data:image/[^;]+;base64,', '')
    ),
responseFormat => {'Image Name': 'Describe the image'}
);
```

### Store extracted images in a stage

You can store extracted images from documents in a Snowflake stage for reuse, auditing, or additional processing with
other Cortex AI functions. This example creates and uses a Python stored procedure to decode base64
image data from AI_PARSE_DOCUMENT and upload the resulting image files to a specified stage.

```sqlexample-python
CREATE OR REPLACE PROCEDURE SAVE_EXTRACTED_IMAGES(r VARIANT)
RETURNS ARRAY
LANGUAGE PYTHON
RUNTIME_VERSION = '3.9'
PACKAGES = ('pillow', 'snowflake-snowpark-python')
HANDLER = 'run'
AS
$$
import base64
import io
import os
import tempfile
from PIL import Image

def process_parse_document_result(data: dict) -> tuple[str, str, str]:
    images = data["images"]
    for image in images:
        id = image["id"]
        data, image_base64 = image["image_base64"].split(";", 1)
        extension = data.split("/")[1]
        base64 = image_base64.split(",")[1]
        yield id, extension, base64

def decode_base64(encoded_image: str) -> bytes:
    return base64.b64decode(encoded_image)

def run(session, r):
    destination_path = r["DESTINATION_PATH"]
    parse_document_result = r["PARSE_DOCUMENT_RESULT"]

    if not destination_path:
        return ["Error: destination_path parameter is required"]
    if not destination_path.startswith("@"):
        return ["Error: destination_path must start with @ (e.g. @output_stage/path"]
    if destination_path == "@":
        return ["Error: destination_path must include a stage name after @"]

    # Clean the result directory
    session.sql(f"RM destination_path")

    uploaded_files = []
    with tempfile.TemporaryDirectory() as temp_dir:
        for image_id, extension, encoded_image in process_parse_document_result(parse_document_result):
            image_bytes = decode_base64(encoded_image)
            image: Image = Image.open(io.BytesIO(image_bytes))

            image_path = os.path.join(temp_dir, image_id)
            image.save(image_path)

            # Use session.file.put with source file path and auto_compress=False
            session.file.put(
                image_path, destination_path, auto_compress=False, overwrite=True
            )
            uploaded_files.append(f"{destination_path}/{image_id}")

            # Cleanup
            os.remove(image_path)
    return uploaded_files
$$;
```

After creating the SAVE_EXTRACTED_IMAGES procedure, you can call it to extract images from a document and store them in
a stage, as shown in the following code snippet:

```sqlexample
CALL SAVE_EXTRACTED_IMAGES(
(
SELECT OBJECT_CONSTRUCT(*)
FROM ( SELECT
    '@image_docs/output' as destination_path,
    AI_PARSE_DOCUMENT(
    TO_FILE('@image_docs/my_document.pdf'),
    {'mode': 'LAYOUT', 'extract_images': true}
    ) as parse_document_result
) LIMIT 1
));
```

The output of this query is a list of file paths for the images stored in the specified stage, such as:

```output
image_docs/output/img-0.jpeg
image_docs/output/img-1.jpeg
image_docs/output/img-10.jpeg
image_docs/output/img-11.jpeg
image_docs/output/img-12.jpeg
image_docs/output/img-13.jpeg
```

Now you can process the stored images using other Cortex AI functions, such as AI_COMPLETE for multimodal analysis or generation.

```sqlexample
SELECT AI_COMPLETE(
    'pixtral-large',
    'Describe the image in 10 words.',
    TO_FILE('@image_docs/output/img-0.jpeg')
);
```

Response:

```output
The image shows central bank policy rates for various countries from 2000 to 2025.
```

## Cost considerations

AI_PARSE_DOCUMENT uses billing based on the number of pages processed. A single image file is considered to be a page
for billing purposes. Extracting images does not incur additional costs.

## Current limitations

* No more than fifty images can be extracted from a single document. Additional images are ignored.
* Images smaller than 4x4 pixels are not extracted.
* If the size of a response exceeds the account parameter EXTERNAL_FUNCTION_MAx_RESPONSE_SIZE, the function returns an
  error. Increase the value of this parameter if necessary.
