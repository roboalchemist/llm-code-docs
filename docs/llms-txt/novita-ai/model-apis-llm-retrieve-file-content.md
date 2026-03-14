# Source: https://novita.ai/docs/api-reference/model-apis-llm-retrieve-file-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve file content

Retrieves the content of a specific file using its file ID. This is commonly used to download batch output files or error files.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Path Parameters

<ParamField path="file_id" type="string" required={true}>
  The unique identifier of the file to retrieve content for.
</ParamField>

## Response

The response returns the raw file content. For batch output files, this will be in JSONL format where each line contains a batch request result.

**Example Response**

For batch output files, each line contains a response like this:

```json  theme={"system"}
{
  "custom_id": "request-2589",
  "error": null,
  "id": "batch_req_task_d2c",
  "response": {
    "body": {
      "id": "29e1432c-edfb-44a4-b531-c23c600abfae",
      "object": "chat.completion",
      "created": 1754902266,
      "model": "deepseek-test",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Hello! 👋 How can I assist you today? 😊"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 13,
        "total_tokens": 18
      }
    },
    "request_id": "request-2589",
    "status_code": 200
  }
}
```


Built with [Mintlify](https://mintlify.com).