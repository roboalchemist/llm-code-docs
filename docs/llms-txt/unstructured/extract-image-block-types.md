# Source: https://docs.unstructured.io/open-source/how-to/extract-image-block-types.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/extract-image-block-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Extract images and tables from documents

<Note>
  The following information applies to the legacy Unstructured Partition Endpoint.

  Unstructured recommends that you use the
  [on-demand jobs](/api-reference/workflow/overview#run-an-on-demand-job) functionality in the
  [Unstructured API](/api-reference/overview) instead. Unstructured's on-demand jobs provide
  many benefits over the legacy Unstructured Partition Endpoint, including support for:

  * Production-level usage.
  * Multiple local input files in batches.
  * The latest and highest-performing models.
  * Post-transform enrichments.
  * All of Unstructured's chunking strategies.
  * The generation of vector embeddings.

  The Unstructured API also provides support for processing files and data in remote locations.
</Note>

## Task

You want to get, decode, and show elements, such as images and tables, that are embedded in a PDF document.

## Approach

Extract the Base64-encoded representation of specific elements, such as images and tables, in the document.
For each of these extracted elements, decode the Base64-encoded representation of the element into its original visual representation
and then show it.

## To run this example

You will need a document that is one of the document types supported by the `extract_image_block_types` argument.
See the `extract_image_block_types` entry in [API Parameters](/api-reference/legacy-api/partition/api-parameters).
This example uses a PDF file with embedded images and tables.

## Code

For the [Unstructured Python SDK](/api-reference/legacy-api/partition/sdk-python), you'll need:

These environment variables:

* `UNSTRUCTURED_API_KEY` - Your Unstructured API key value.
* `UNSTRUCTURED_API_URL` - Your Unstructured API URL.

```python Python SDK theme={null}
from unstructured_client import UnstructuredClient
from unstructured_client.models import operations, shared
from unstructured.staging.base import elements_from_dicts, elements_to_json

import os
import base64
from PIL import Image
import io

if __name__ == "__main__":
    client = UnstructuredClient(
        api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")
    )

    # Source: https://github.com/Unstructured-IO/unstructured/blob/main/example-docs/embedded-images-tables.pdf
    
    # Where to get the input file and store the processed data, relative to this .py file.
    local_input_filepath = "local-ingest-input-pdf/embedded-images-tables.pdf"
    local_output_filepath = "local-ingest-output/embedded-images-tables.json"

    with open(local_input_filepath, "rb") as f:
        files = shared.Files(
            content=f.read(),
            file_name=local_input_filepath
        )

    request = operations.PartitionRequest(
        shared.PartitionParameters(
            files=files,
            split_pdf_page=True,
            split_pdf_allow_failed=True,
            split_pdf_concurrency_level=15,
            # Extract the Base64-encoded representation of each
            # processed "Image" and "Table" element. Extract each into
            # an "image_base64" object, as a child of the
            # "metadata" object, for that element in the result.
            # Element type names, such as "Image" and "Table" here,
            # are case-insensitive.
            # Any available Unstructured element type is allowed.
            extract_image_block_types=["Image", "Table"]
        )
    )

    try:
        result = client.general.partition(
            request=request
        )

        for element in result.elements:
            if "image_base64" in element["metadata"]:
                # Decode the Base64-encoded representation of the 
                # processed "Image" or "Table" element into its original
                # visual representation, and then show it.
                image_data = base64.b64decode(element["metadata"]["image_base64"])
                image = Image.open(io.BytesIO(image_data))
                image.show()
        
        # Optionally, prepare to print or save the elements as JSON.
        dict_elements = elements_from_dicts(
            element_dicts=result.elements
        )

        # Print the elements as JSON...
        json_elements = elements_to_json(
            elements=dict_elements,
            indent=2
        )

        print(json_elements)

        # ...or save as JSON.
        elements_to_json(
            elements=dict_elements,
            indent=2,
            filename=local_output_filepath
        )
    except Exception as e:
        print(e)
```

## See also

* [Extract text as HTML](/api-reference/legacy-api/partition/text-as-html)
* [Table extraction from PDF](/examplecode/codesamples/apioss/table-extraction-from-pdf)
