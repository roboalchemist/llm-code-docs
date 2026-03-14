# Source: https://novita.ai/docs/guides/llm-batch-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch Inference

export const BatchApiModels = () => {
  if (typeof document === "undefined") {
    return null;
  } else {
    let attempts = 0;
    const maxAttempts = 50;
    const INIT_DISPLAY_COUNT = 3;
    const interval = setInterval(() => {
      const clientComponent = document.getElementById("batch-api-models");
      if (clientComponent && window.novitaRemoteData.llmModels.status === 'loaded') {
        const modelList = window.novitaRemoteData.llmModels.data.filter(model => {
          return (model.endpoints || []).includes('batch-api');
        });
        let displayModels = modelList.slice(0, INIT_DISPLAY_COUNT).map(model => {
          return `<li><span class="model-id-item">${model.id}</span></li>`;
        }).join('');
        let showMoreButton = '';
        if (modelList.length > INIT_DISPLAY_COUNT) {
          showMoreButton = `<button id="show-more-batch-api-model-btn" style="margin-left: 32px; color: rgb(40 116 255)">View More</button>`;
        }
        clientComponent.innerHTML = `
          <ul>${displayModels}</ul>
          ${showMoreButton}
        `;
        document.getElementById('show-more-batch-api-model-btn')?.addEventListener('click', () => {
          clientComponent.innerHTML = `
            <ul>${modelList.map(model => {
            return `<li><span class="model-id-item">${model.id}</span></li>`;
          }).join('')}</ul>
          `;
        });
        clearInterval(interval);
      }
      attempts++;
      if (attempts >= maxAttempts) {
        clearInterval(interval);
      }
    }, 200);
    return <div id="batch-api-models"></div>;
  }
};

The Batch API for Large Language Models enables asynchronous processing of numerous inference requests and is fully compatible with the OpenAI API standard.

The Batch API is a cost-effective solution when immediate inference results are unnecessary. It provides a higher rate limits than online calls, ensuring results are delivered within a reasonable timeframe of 48 hours.

This API is ideal for:

* Conducting evaluations and data analysis.
* Classifying extensive datasets.
* Generating document summaries in an offline mode.

Supported Models:

<BatchApiModels />

## Quick Start

### 1. Preparing Batch Files

The Batch API uses .jsonl format files as input, with each line representing the details of an API inference request. Available endpoints include `/v1/chat/completions` and `/v1/completions`.

<Warning>
  Set the `endpoint` parameter to `/v1/chat/completions` or `/v1/completions` for OpenAI API compatibility.
</Warning>

Each request must include a unique `custom_id` to locate inference results in the output file after batch completion. Parameters in the `body` field of each line are sent as actual inference request parameters to the endpoint.

<Warning>
  All requests within a single batch JSONL file must target the same model. Do not mix requests for different models in one batch.
</Warning>

Below is an example input file containing 2 requests:

```JSON  theme={"system"}
{"custom_id": "request-1", "body": {"model": "deepseek/deepseek-v3-0324", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 400}}
{"custom_id": "request-2", "body": {"model": "deepseek/deepseek-v3-0324", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
```

### 2. Upload Batch Input File

Upload the batch input file to ensure it can be accurately referenced when creating a batch. Use the Files API to upload your .jsonl file and set the purpose to `batch`. Note that the file will be retained for 15 days.

<Tip>
  For how to get API key, refer to the [API Key Management](/api-reference/basic-authentication).
</Tip>

Code Example

**Python**

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/openai/v1",
    api_key="<Your API Key>",
)

batch_input_file = client.files.create(
    file=open("batch_input.jsonl", "rb"),
    purpose="batch",
)

print(batch_input_file)
```

**Curl**

```bash  theme={"system"}
export API_KEY="<Your API Key>"

curl --request POST \
  --url https://api.novita.ai/openai/v1/files \
  --header 'Authorization: Bearer ${API_KEY}' \
  --form 'file=@"/your/batch_input.jsonl"' \
  --form 'purpose="batch"'
```

Sample response upon successful file upload:

```
{
    "id": "file_d2co***as73c0cjd0",
    "object": "file",
    "bytes": 238,
    "filename": "batch_input.jsonl",
    "created_at": 1754894162,
    "purpose": "batch",
    "metadata": {
        "total_requests": 2
    }
}
```

### 3. Creating a Batch

Once the input file is successfully uploaded, you can initiate a batch using the ID of the uploaded File object. The completion window is fixed at `48h` and is currently non-adjustable.

Code Example

**Python**

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/openai/v1",
    api_key="<Your API Key>",
)

batch = client.batches.create(
  input_file_id="file_d2cor0es1cas73c0cj60",
  endpoint="/v1/chat/completions",
  completion_window="48h"
)
print(batch)
```

**Curl**

```bash  theme={"system"}
export API_KEY="<Your API Key>"

curl --request POST \
  --url https://api.novita.ai/openai/v1/batches \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer ${API_KEY}' \
  --data '{
      "input_file_id": "file_d2co***as73c0cjd0",
      "endpoint": "/v1/chat/completions",
      "completion_window": "48h"
  }'
```

This request will yield a Batch object that includes metadata about your batch, as illustrated in the example below:

```JSON  theme={"system"}
{
    "id": "batch_d2cq***73a68lu0",
    "object": "batch",
    "endpoint": "/v1/chat/completions",
    "input_file_id": "file_d2co***as73c0cjd0",
    "output_file_id": "",
    "error_file_id": "",
    "completion_window": "48h",
    "in_progress_at": null,
    "expires_at": null,
    "finalizing_at": null,
    "completed_at": null,
    "failed_at": null,
    "expired_at": null,
    "cancelling_at": null,
    "cancelled_at": null,
    "status": "validating",
    "errors": "",
    "version": 0,
    "created_at": "2025-08-11T16:31:52.949816948+08:00",
    "updated_at": null,
    "created_by": "8f242aa1-f725-4a67-8***9-cb68025e0976",
    "created_by_key_id": "key_cc19f96c***e7390644a37da21",
    "remark": "",
    "total": 0,
    "completed": 0,
    "failed": 0,
    "metadata": null,
    "request_counts": {
        "total": 0,
        "completed": 0,
        "failed": 0
    }
}
```

### 4. Check the Status of a Batch

You can check a batch's status at any time to receive the latest batch information.

The status enumeration values of the Batch object are as follows:

<table class="table table-big">
  <thead>
    <tr>
      <th>Status</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>VALIDATING</td>
      <td>The input file is being validated before the batch can begin</td>
    </tr>

    <tr>
      <td>PROGRESS</td>
      <td>Batch is in progress</td>
    </tr>

    <tr>
      <td>COMPLETED</td>
      <td>Batch processing completed successfully</td>
    </tr>

    <tr>
      <td>FAILED</td>
      <td>Batch processing failed</td>
    </tr>

    <tr>
      <td>EXPIRED</td>
      <td>Batch exceeded deadline</td>
    </tr>

    <tr>
      <td>CANCELLING</td>
      <td>Batch is being cancelled</td>
    </tr>

    <tr>
      <td>CANCELLED</td>
      <td>Batch was cancelled</td>
    </tr>
  </tbody>
</table>

Code Example

**Python**

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/openai/v1",
    api_key="<Your API Key>",
)
batch = client.batches.retrieve("batch_d2cq***73a68lu0")
print(batch)
```

**Curl**

```bash  theme={"system"}
export API_KEY="<Your API Key>"

curl --request GET \
  --url https://api.novita.ai/openai/v1/batches/{batch_id} \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer ${API_KEY}'
```

### 5. Retrieve the Results

Once the batch inference is complete, you can download the result output file using the `output_file_id` field from the Batch object.

The result output file will be deleted 30 days after the batch inference concludes, so please retrieve it promptly via the interface.

Code Example

**Python**

```python  theme={"system"}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/openai/v1",
    api_key="<Your API Key>",
)

content = client.files.content("example-250811-1")
print(content.read())
```

**Curl**

```bash  theme={"system"}
export API_KEY="<Your API Key>"

curl --request GET \
  --url https://api.novita.ai/openai/v1/files/{file_id}/content \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer ${API_KEY}'
```

The response returns the raw file content. For batch output files, each line contains a response like this:

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

## Instructions

### Limitations

1. Each batch can contain up to 50,000 requests.<br />
2. The maximum input file size per batch is 100MB.

### Error Handling

Errors encountered during batch processing are recorded in a separate error file, accessible via the error\_file\_id field. Common error codes include:

<table class="table table-big">
  <thead>
    <tr>
      <th>Error Code</th>
      <th>Description</th>
      <th>Solution</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>400</td>
      <td>Invalid request format</td>
      <td>Check JSONL syntax and required fields</td>
    </tr>

    <tr>
      <td>401</td>
      <td>Authentication failed</td>
      <td>Verify API key</td>
    </tr>

    <tr>
      <td>404</td>
      <td>Batch not found</td>
      <td>Check batch ID</td>
    </tr>

    <tr>
      <td>429</td>
      <td>Rate limit exceeded</td>
      <td>Reduce request frequency</td>
    </tr>

    <tr>
      <td>500</td>
      <td>Server error</td>
      <td>Contact us</td>
    </tr>
  </tbody>
</table>

### Batch Expiration

Batches not completed within 48 hours will transition to an EXPIRED state. Unfinished requests will be canceled, while completed requests will be provided through an output file. You only pay for tokens consumed by completed requests. The batch makes every effort to complete within 48 hours.

## All Batch API

1. [Create batch](/api-reference/model-apis-llm-create-batch)
2. [Retrieve batch](/api-reference/model-apis-llm-retrieve-batch)
3. [Cancel batch](/api-reference/model-apis-llm-cancel-batch)
4. [List batch](/api-reference/model-apis-llm-list-batches)
5. [Upload file](/api-reference/model-apis-llm-upload-batch-input-file)
6. [List files](/api-reference/model-apis-llm-list-files)
7. [Retrieve file](/api-reference/model-apis-llm-query-file)
8. [Delete file](/api-reference/model-apis-llm-delete-file)
9. [Retrieve file content](/api-reference/model-apis-llm-retrieve-file-content)


Built with [Mintlify](https://mintlify.com).