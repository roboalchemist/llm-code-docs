# Source: https://docs.unstructured.io/open-source/how-to/text-as-html.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/text-as-html.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Extract tables as HTML

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

You want to get, save, or show the contents of elements that are represented as HTML, such as tables that are embedded in a PDF document.

## Approach

Extract the contents of an element's `text_as_html` JSON object, which is nested inside of its parent `metadata` object.

## To run this example

You will need a document that is one of the document types that can output the `text_as_html` JSON object. For the list of applicable document types, see the entries in the table at the beginning of [Partitioning](/open-source/core-functionality/partitioning) where "Table Support" is "Yes."

This example uses a PDF file with an embedded table.

## Code

For the [Unstructured Python SDK](/api-reference/legacy-api/partition/sdk-python), you'll need:

These environment variables:

* `UNSTRUCTURED_API_KEY` - Your Unstructured API key value.
* `UNSTRUCTURED_API_URL` - Your Unstructured API URL.

```python Python SDK theme={null}
from unstructured_client import UnstructuredClient
from unstructured_client.models import operations, shared
from unstructured.staging.base import elements_from_dicts, elements_to_json

import os, webbrowser

if __name__ == "__main__":
    client = UnstructuredClient(
        api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")
    )

    # Source: https://github.com/Unstructured-IO/unstructured-ingest/blob/main/example-docs/pdf/embedded-images-tables.pdf

    # Where to get the local file, relative to this .py file.
    local_input_filepath = "local-ingest-input-pdf/embedded-images-tables.pdf"

    # Where to store the retrieved HTML (and the processed JSON), relative to this .py file.
    local_output_filepath = "local-ingest-output"

    with open(local_input_filepath, "rb") as f:
        files = shared.Files(
            content=f.read(),
            file_name=local_input_filepath
        )

    request = operations.PartitionRequest(
        shared.PartitionParameters(
            files=files,
            strategy=shared.Strategy.VLM,
            vlm_model="gpt-4o",
            vlm_model_provider="openai",
            split_pdf_page=True,
            split_pdf_allow_failed=True,
            split_pdf_concurrency_level=15
        )
    )

    try:
        result = await client.general.partition_async(
            request=request
        )

        # Provide some minimal CSS for better table readability.
        table_css = "<head><style>table, th, td { border: 1px solid; }</style></head>"

        for element in result.elements:
            if "text_as_html" in element["metadata"]:
                # Surround the element's HTML with basic <html> and <body> tags, and add the minimal CSS.
                html_string = f"<!DOCTYPE html><html>{table_css}<body>{element["metadata"]["text_as_html"]}</body></html>"

                # Save the element's HTML to a local file.
                save_path = f"{local_output_path}/{element["element_id"]}.html"
                file = open(save_path, 'w')
                file.write(html_string)
                file.close()

                # View the locally saved file in the local default web browser.
                webbrowser.open_new(f"file:///{os.getcwd()}/{save_path}")

        # Also get the elements for inspection and validation.
        dict_elements = elements_from_dicts(
            element_dicts=result.elements
        )

        # Save the elements as JSON.
        elements_to_json(
            elements=dict_elements,
            indent=2,
            filename=f"{local_output_filepath}/embedded-images-tables.json"
        )
    except Exception as e:
        print(e)
```

## See also

* [Extract images and tables from documents](/api-reference/legacy-api/partition/extract-image-block-types)
* [Table Extraction from PDF](/examplecode/codesamples/apioss/table-extraction-from-pdf)
