# Source: https://dev.writer.com/home/parse-pdf.md

# Parse a PDF

<Warning>
  **Deprecation notice**: The [parse PDF API endpoint](/api-reference/tool-api/pdf-parser) at `/v1/tools/pdf-parser/{file_id}` is deprecated and will be removed on **December 22, 2025**.

  **Migration path**: We plan to introduce a prebuilt PDF parsing tool for chat completions that will provide similar functionality. This tool will work similarly to other prebuilt tools like the [Vision tool](/home/vision-tool) or [LLM tool](/home/model-delegation). We will provide more details about this alternative when it becomes available.
</Warning>

The [PDF parser endpoint](/api-reference/tool-api/pdf-parser) converts PDF documents into other formats. This is useful when you need to extract and process text content from PDF files for further analysis or integration into your workflow.

## Use cases

* Converting research papers from PDF to searchable text for analysis
* Extracting content from business reports for data processing
* Converting PDF documentation into markdown format for web publishing
* Making archived PDF documents searchable and analyzable
* Automating data extraction from PDF forms and invoices

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Endpoint overview

**URL:** `POST https://api.writer.com/v1/tools/pdf-parser`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/tools/pdf-parser/<file-id>' \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --data '{
    "format": "markdown"
  }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.tools.parse_pdf(
      file_id="file_id",
      format="text",
  )
  print(response.content)
  ```

  ```javascript JavaScript theme={null}
  import Writer from 'writer-sdk';

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  async function main() {
    const response = await client.tools.parsePdf('file_id', { format: 'text' });

    console.log(response.content);
  }

  main();
  ```
</CodeGroup>

### Path parameters

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| `file_id` | The ID of the uploaded PDF file to parse. |

Before using the PDF parser, you'll need to upload your PDF file to the Writer API and obtain its file ID. Learn more about how to upload files with the [Files API](/home/files).

### Request body

The request body includes the following parameters:

| Parameter | Type     | Description                                             |
| --------- | -------- | ------------------------------------------------------- |
| `format`  | `string` | The desired output format. Can be `text` or `markdown`. |

### Response parameters

Returns an object with a `content` field containing the extracted text in the specified format.

```json JSON theme={null}
{
  "content": "..."
}
```
