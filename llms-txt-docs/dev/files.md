# Source: https://dev.writer.com/home/files.md

# Manage files

> Upload, download, list, and delete files with the File API. Use files in Knowledge Graphs and no-code agents.

The File API allows you to manage files in your account. You can upload, download, list, and delete files.

After you upload a file, you can use it to perform actions such as attaching it to a [Knowledge Graph](/home/knowledge-graph) or using it as an input in a [no-code agent](/home/applications).

This guide shows you how to perform the following actions:

* [Upload a file](#upload-a-file)
* [Get a file](#get-a-file)
* [List all files](#list-all-files)
* [Delete a file](#delete-a-file)

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Upload a file

**Endpoint**: `POST /v1/files`

<Info>A file persists in your account until you [delete it](#delete-a-file).</Info>

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST "https://api.writer.com/v1/files" \
    --header "Content-Type: text/plain" \
    --header "Content-Disposition: attachment; filename=<FILE_NAME>" \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --data-binary "@<FILE_PATH>"

  # Example:
  #   <FILE_NAME> = test.txt
  #   <FILE_PATH> = /path/to/test.txt
  ```

  ```python Python theme={null}
  from pathlib import Path
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  # Read the file contents
  file_path = Path("<FILE_PATH>")  # Replace with your file path, for example: /path/to/test.txt
  file_name = file_path.name  # Get the filename from the path

  file_ = client.files.upload(
    content=file_path.read_bytes(),  # Read the actual file contents
    content_disposition=f"attachment; filename={file_name}",
    content_type="text/plain"
  )

  print(file_.id)
  ```

  ```javascript JavaScript theme={null}
  import fs from 'fs';
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const file = await client.files.upload({
    content: fs.createReadStream("<FILE_PATH>"),  // Replace with your file path, for example: /path/to/test.txt
    "Content-Disposition": "attachment; filename=<FILE_NAME>",  // Replace with your file name, for example: test.txt
    "Content-Type": "text/plain"
  });

  console.log(file.id)
  ```
</CodeGroup>

### Request body

| Parameter             | Type     | Description                                                                                                                                                                                                                                                                  |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content`             | `string` | The content of the file. See the [Python SDK](https://github.com/writer/writer-python?tab=readme-ov-file#file-uploads) and the [JavaScript SDK](https://github.com/writer/writer-node?tab=readme-ov-file#file-uploads) for more details about how to pass the file contents. |
| `content_disposition` | `string` | The [content disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) of the file.                                                                                                                                                        |
| `content_type`        | `string` | The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types) of the file. The file upload supports `txt`, `doc`, `docx`, `ppt`, `pptx`, `jpg`, `png`, `eml`, `html`, `pdf`, `srt`, `csv`, `xls`, and `xlsx` file extensions.            |

### Response format

| Field        | Type            | Description                                                |
| ------------ | --------------- | ---------------------------------------------------------- |
| `id`         | `string`        | The ID of the file.                                        |
| `created_at` | `string`        | The date and time the file was created in ISO 8601 format. |
| `name`       | `string`        | The name of the file.                                      |
| `graph_ids`  | `array[string]` | The IDs of the Knowledge Graphs the file is attached to.   |
| `status`     | `string`        | The processing status of the file.                         |

```json  theme={null}
{
  "id": "1862f090-a281-48f3-8838-26c1e78b605e",
  "created_at": "2024-06-24T12:34:56Z",
  "name": "test.txt",
  "graph_ids": [],
  "status": "in_progress"
}
```

## List all files

**Endpoint**: `GET /v1/files`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request GET "https://api.writer.com/v1/files" \
    --header "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()
  page = client.files.list()

  for file in page.data:
      print(file.id, file.name, file.graph_ids, file.status)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();
  const files = await client.files.list();

  for (const file of files.data) {
      console.log(file.id, file.name, file.graph_ids, file.status);
  }
  ```
</CodeGroup>

### Query parameters

In addition to the [pagination parameters](/api-reference/file-api/get-all-files), this endpoint supports the following query parameters:

| Parameter    | Type     | Description                                                                                      |
| ------------ | -------- | ------------------------------------------------------------------------------------------------ |
| `graph_id`   | `string` | Filter files by the graph they are attached to.                                                  |
| `status`     | `string` | Filter files by status.                                                                          |
| `file_types` | `string` | Filter files by extension type. Separate multiple values by commas. For example, `txt,pdf,docx`. |

<Warning>
  The `file_types` parameter is not yet available in the Python and Node SDKs. It will be available in version 2.3.0.
</Warning>

### Response format

The response has the following structure:

| Field               | Type            | Description                                                |
| ------------------- | --------------- | ---------------------------------------------------------- |
| `data`              | `array[object]` | An array of file objects.                                  |
| `data[].id`         | `string`        | The ID of the file.                                        |
| `data[].created_at` | `string`        | The date and time the file was created in ISO 8601 format. |
| `data[].name`       | `string`        | The name of the file.                                      |
| `data[].graph_ids`  | `array[string]` | The IDs of the Knowledge Graphs the file is attached to.   |
| `data[].status`     | `string`        | The status of the file.                                    |
| `has_more`          | `boolean`       | Whether there are more files to fetch.                     |
| `first_id`          | `string`        | The ID of the first file in the response.                  |
| `last_id`           | `string`        | The ID of the last file in the response.                   |

```json  theme={null}
{
  "data": [
    {
      "id": "f1234-abcd-1234",
      "created_at": "2025-03-07T23:20:50.978908Z",
      "name": "my_file.pdf",
      "graph_ids": [],
      "status": "completed"
    },
    {
      "id": "1234-abcd-5678",
      "created_at": "2025-03-07T23:20:44.047604Z",
      "name": "my_second_file.pdf",
      "graph_ids": [],
      "status": "completed"
    }
  ],
  "has_more": false,
  "first_id": "f1234-abcd-1234",
  "last_id": "1234-abcd-5678"
}
```

## Get a file

**Endpoint**: `GET /v1/files/{fileId}`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request GET "https://api.writer.com/v1/files/<FILE_ID>" \
    --header "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()
  file = client.files.retrieve("<FILE_ID>")

  print(file.id, file.name, file.graph_ids, file.status)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();
  const file = await client.files.retrieve('<FILE_ID>');

  console.log(file.id, file.name, file.graph_ids, file.status)
  ```
</CodeGroup>

### Response format

```json  theme={null}
{
  "id": "f1234-abcd-1234",
  "created_at": "2025-03-07T23:20:50.978908Z",
  "name": "test.txt",
  "graph_ids": [],
  "status": "completed"
}
```

## Delete a file

**Endpoint**: `DELETE /v1/files/{fileId}`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request DELETE "https://api.writer.com/v1/files/<FILE_ID>" \
    --header "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()
  file = client.files.delete("<FILE_ID>")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();
  const fileDeleteResponse = await client.files.delete('<FILE_ID>');
  ```
</CodeGroup>

### Response format

The response has the following structure:

```json  theme={null}
{
  "id": "f1234-abcd-1234",
  "deleted": true
}
```
