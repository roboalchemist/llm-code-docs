# Source: https://docs.unstructured.io/open-source/how-to/get-chunked-elements.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/get-chunked-elements.md

# Source: https://docs.unstructured.io/open-source/how-to/get-chunked-elements.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/get-chunked-elements.md

# Source: https://docs.unstructured.io/open-source/how-to/get-chunked-elements.md

# Source: https://docs.unstructured.io/api-reference/partition/get-chunked-elements.md

# Get chunked elements

## Task

You want to get, and print or save, the contents of elements that have been chunked.

## Approach

Chunked elements are typically represented in this format:

```json  theme={null}
{
  "type": "CompositeElement",
  "element_id": "3800f7ff047e97cbf0a5f7df7ad52c80",
  "text": "4,5 Exception noted in \u201cSpecial Considerations for Promotional Labeling and Advertising Material\u201d\n\n3",
  "metadata": {
    "filetype": "application/pdf",
    "languages": ["eng"],
    "page_number": 6,
    "orig_elements": "eJy ... Full content omitted for brevity ... x8=",
    "filename": "Portable-Document-Format-Specifications.pdf"
  }
}
```

```json  theme={null}
{
  "type": "Table",
  "element_id": "758127b42c51b93b59abf08640d1ccab",
  "text": "Gels and karyotypes High pressure liquid chromatography 600 dpi (8 bit grayscale depth) 300 dpi",
  "metadata": {
    "text_as_html": "<table><tbody><tr><td>Gels and karyotypes</td><td>600 dpi (8 bit grayscale depth)</td></tr><tr><td>High pressure liquid chromatography</td><td>300</td></tr></tbody></table>",
    "filetype": "application/pdf",
    "languages": ["eng"],
    "page_number": 8,
    "orig_elements": "eJy ... Full content omitted for brevity ... MnD",
    "filename": "Portable-Document-Format-Specifications.pdf"
}
```

To get the element's chunked content, extract the contents of the element's `text` field.

The chunked content might not contain all of its associated content. To get all of the elements that were used to derive this chunked content, extract the contents of the element's `orig_elements` field, which is nested inside of its parent `metadata` field.

The contents of the `orig_elements` field is in compressed Base64 gzipped format. To get the content, Base64-decode the bytes, decompress them, and then decode them using UTF-8.

## To run this example

You will need to chunk a document during processing. This example uses a PDF file chunked into 200- to 300-character elements.

## Code

For the [Unstructured Python SDK](/api-reference/partition/sdk-python), you'll need:

These environment variables:

* `UNSTRUCTURED_API_KEY` - Your Unstructured API key value.
* `UNSTRUCTURED_API_URL` - Your Unstructured API URL.

```python  theme={null}
from unstructured_client import UnstructuredClient
from unstructured_client.models import operations, shared
from unstructured.staging.base import elements_from_dicts, elements_to_json

import os, base64, zlib
from typing import List, Dict, Any

# Extract the contents of an orig_elements field.
def extract_orig_elements(orig_elements):
    decoded_orig_elements = base64.b64decode(orig_elements)
    decompressed_orig_elements = zlib.decompress(decoded_orig_elements)
    return decompressed_orig_elements.decode('utf-8')

# Source file: https://www.fda.gov/files/drugs/published/Portable-Document-Format-Specifications.pdf
input_filepath = "local-ingest-input-pdf/Portable-Document-Format-Specifications.pdf"
output_filepath = "local-ingest-output-json/Portable-Document-Format-Specifications.json"

client = UnstructuredClient(
    api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")
)

with open(input_filepath, "rb") as f:
    files = shared.Files(
        content=f.read(),
        file_name=input_filepath
    )

# Chunk the document with a basic chunking strategy.
# Create chunks that are at least around 200 characters (soft limit)
# but never more than 300 characters (hard maximum).
req = operations.PartitionRequest(
    shared.PartitionParameters(
        files=files,
        strategy=shared.Strategy.VLM,
        vlm_model="gpt-4o",
        vlm_model_provider="openai",
        split_pdf_page=True,
        split_pdf_allow_failed=True,
        split_pdf_concurrency_level=15,
        chunking_strategy="basic",
        new_after_n_chars=200,
        max_characters=300
    )
)

try:
    res = await client.general.partition_async(
        request=req
    )

    # Create a dictionary that will hold only
    # a transposed version of the returned elements. 
    # For instance, we just want to capture each element's ID,
    # the chunk's text, and the chunk's associated elements in context.
    orig_elements_dict: List[Dict[str, Any]] = []

    for element in res.elements:
        # For each chunk that has an "orig_elements" field...
        if "orig_elements" in element["metadata"]:
            # ...get the chunk's associated elements in context...
            orig_elements = extract_orig_elements(element["metadata"]["orig_elements"])
            # ...and then transpose it and other associated fields into a separate dictionary.
            orig_elements_dict.append({
                "element_id": element["element_id"],
                "text": element["text"],
                "orig_elements": json.loads(orig_elements)
            })
    
    # Convert the elements into a JSON object.
    orig_elements_json = json.dumps(orig_elements_dict, indent=2)

    # Write the JSON to a file.
    with open(output_filepath, "w") as file:
        file.write(orig_elements_json)
except Exception as e:
    print(e)
```

## See also

* [Recovering chunk elements](/open-source/core-functionality/chunking#recovering-chunk-elements)
* [Chunking strategies](/api-reference/partition/chunking)
