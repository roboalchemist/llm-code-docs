# Source: https://docs.pinecone.io/guides/assistant/manage-files.md

# Manage files

> List, check status, and delete files from your assistant.

<Note>
  File upload limitations depend on the plan you are using. For more information, see [Pricing and limitations](/guides/assistant/pricing-and-limits#limits).
</Note>

## List files in an assistant

### View all files

You can [get the status, ID, and metadata for each file in your assistant](/reference/api/latest/assistant/list_files), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant.
  files = assistant.list_files()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles();
  console.log(files);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "files": [
    {
      "status": "Available",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "name": "example_file.txt",
      "size": 1073470,
      "metadata": {},
      "updated_on": "2025-07-16T16:46:40.787204651Z",
      "created_on": "2025-07-16T16:45:59.414273474Z",
      "percent_done": 1.0,
      "signed_url": null,
      "error_message": null
    }
  ]
}
```

You can use the `id` value to [check the status of an individual file](#get-the-status-of-a-file).

<Tip>
  You can list file in an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). Select the assistant and view the files in the Assistant playground.
</Tip>

### View a filtered list of files

Metadata filter expressions can be included when listing files. This will limit the list of files to only those matching the filter expression. Use the `filter` parameter to specify the metadata filter expression.

For more information about filtering with metadata, see [Understanding files](/guides/assistant/files-overview#metadata-query-language).

The following example lists files that are a manuscript:

<CodeGroup>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant that match the metadata filter.
  files = assistant.list_files(filter={"document_type":"manuscript"})
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles({
    filter: { document_type: 'manuscript' },
  });
  console.log(files);

  // You can also use filter operators:
  // const files = await assistant.listFiles({
  //   filter: { document_type: { '$ne': 'manuscript' } },
  // });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  ENCODED_METADATA="%7B%22document_type%22%3A%20%22manuscript%22%7D" # URL encoded metadata - See w3schools.com/tags/ref_urlencode.ASP

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME?filter=$ENCODED_METADATA" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

## Get the status of a file

You can [get the status and metadata for your assistant](/reference/api/latest/assistant/describe_file), as in the following example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get an assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `True`.
  file = assistant.describe_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a", include_url=True)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const fileId = "3c90c3cc-0d44-4b50-8888-8dd25736052a";

  // Describe a file. Returns a signed URL by default. 
  const file = await assistant.describeFile(fileId)
  // To exclude signed URL, set `includeUrl` to `false`.
  // const includeUrl = false;
  // const file = await assistant.describeFile(fileId, includeUrl)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `true`.
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</CodeGroup>

This operation returns a response like the following:

```JSON  theme={null}
{
  "status": "Available",
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "name": "example_file.txt",
  "size": 1073470,
  "metadata": {},
  "updated_on": "2025-07-16T16:46:40.787204651Z",
  "created_on": "2025-07-16T16:45:59.414273474Z",
  "percent_done": 1.0,
  "signed_url": "https://storage.googleapis.com/...",
  "error_message": null
}                          
```

<Warning>
  [`signed_url`](https://cloud.google.com/storage/docs/access-control/signed-urls) provides temporary, read-only access to the relevant file. Anyone with the link can access the file, so treat it as sensitive data. Expires in one hour.
</Warning>

<Tip>
  You can check the status a file using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, click the file for more details.
</Tip>

## Delete a file

You can [delete a file](/reference/api/latest/assistant/delete_file) from an assistant.

<Warning>Once a file is deleted, you cannot recover it.</Warning>

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Delete a file from your assistant.
  assistant.delete_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);

  const file = await assistant.deleteFile("070513b3-022f-4966-b583-a9b12e0290ff")
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY"
  ```
</CodeGroup>

<Tip>
  You can delete a file from an assistant using the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/assistant). In the Assistant playground, find the file and click the **ellipsis (...) menu > Delete**.
</Tip>
