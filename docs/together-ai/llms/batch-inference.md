# Source: https://docs.together.ai/docs/batch-inference.md

> Process jobs asynchronously with the Batch API.

# Batch

Learn how to use the Batch API to send asynchronous groups of requests with up to 50% lower costs, higher rate limits, and flexible completion windows. The service is ideal for processing jobs that don't require immediate responses.

## Overview

The Batch API enables you to process large volumes of requests asynchronously at up to 50% lower cost compared to real-time API calls. It's perfect for workloads that don't need immediate responses such as:

* Running evaluations and data analysis
* Classifying large datasets
* Offline summarization
* Synthetic data generation
* Content generation for marketing
* Dataset processing and transformations

Compared to using standard endpoints directly, Batch API offers:

* **Better cost efficiency**: 50% cost discount compared to synchronous APIs
* **Higher rate limits**: Substantially more headroom with separate rate limit pools
* **Large-scale support**: Process thousands of requests per batch
* **Flexible completion**: Best-effort completion with progress tracking

## Getting started

**Note:** Make sure your `together` version number is **>1.5.13**. Run `pip install together --upgrade` to upgrade if needed.

### 1. Prepare your batch file

Batches start with a `.jsonl` file where each line contains the details of an individual request to the API. The available endpoint is `/v1/chat/completions` (Chat Completions API). Each request must include a unique `custom_id` value, which you can use to reference results after completion. Here's an example of an input file with 2 requests:

```json batch_input.jsonl theme={null}
{"custom_id": "request-1", "body": {"model": "deepseek-ai/DeepSeek-V3", "messages": [{"role": "user", "content": "Hello, world!"}], "max_tokens": 200}}
{"custom_id": "request-2", "body": {"model": "deepseek-ai/DeepSeek-V3", "messages": [{"role": "user", "content": "Explain quantum computing"}], "max_tokens": 200}}
```

Each line in your batch file must follow this schema:

| Field       | Type   | Required | Description                                     |
| ----------- | ------ | -------- | ----------------------------------------------- |
| `custom_id` | string | Yes      | Unique identifier for tracking (max 64 chars)   |
| `body`      | object | Yes      | The request body matching the endpoint's schema |

### 2. Upload your batch input file

You must first upload your input file so that you can reference it correctly when creating batches. Upload your `.jsonl` file using the Files API with `purpose=batch-api`.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Uploads batch job file
  file_resp = client.files.upload(
      file="batch_input.jsonl", purpose="batch-api", check=False
  )
  ```

  ```shell CLI theme={null}
  together files upload batch_input.jsonl --purpose "batch-api"
  ```
</CodeGroup>

This will return a file object with `id` and other details:

```json  theme={null}
{
  "id": "file-b35b03e9-154e-429f-bdef-5bd3d8f596c3",
  "bytes": 174,
  "created_at": 1765175491,
  "filename": "mini_batch.jsonl",
  "file_type": "jsonl",
  "line_count": 0,
  "object": "file",
  "processed": true,
  "purpose": "batch-api"
}
```

### 3. Create the batch

Once you've successfully uploaded your input file, you can use the input File object's ID to create a batch. For now, the completion window defaults to `24h` which is a best efforts estimate and cannot be changed. You can also provide custom metadata.

<CodeGroup>
  ```python Python theme={null}
  file_id = file_resp.id

  batch = client.batches.create_batch(file_id, endpoint="/v1/chat/completions")

  print(batch.id)
  ```

  ```python Python v2 theme={null}
  file_id = file_resp.id

  batch = client.batches.create(
      input_file_id=file_id, endpoint="/v1/chat/completions"
  )

  print(batch.job.id)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // The file id from the previous step
  const fileId = file_resp.id;

  const batch = await client.batches.create({
    endpoint: "/v1/chat/completions",
    input_file_id: fileId,
  });

  console.log(batch);
  ```
</CodeGroup>

This request will return a Batch object with metadata about your batch:

```json JSON theme={null}
{
  "id": "batch-xyz789",
  "status": "VALIDATING",
  "endpoint": "/v1/chat/completions",
  "input_file_id": "file-abc123",
  "created_at": "2024-01-15T10:00:00Z",
  "request_count": 0,
  "model_id": null
}
```

### 4. Check the status of a batch

You can check the status of a batch at any time, which will return updated batch information.

<CodeGroup>
  ```python Python theme={null}
  batch_stat = client.batches.get_batch(batch.id)

  print(batch_stat.status)
  ```

  ```python Python(v2) theme={null}
  batch_stat = client.batches.retrieve(batch.job.id)

  print(batch_stat.status)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // The batch id from the previous step
  const batchId = batch.job?.id;

  let batchInfo = await client.batches.retrieve(batchId);

  console.log(batchInfo.status);
  ```
</CodeGroup>

The status of a given Batch object can be any of the following:

| Status        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `VALIDATING`  | The input file is being validated before the batch can begin |
| `IN_PROGRESS` | Batch is in progress                                         |
| `COMPLETED`   | Batch processing completed successfully                      |
| `FAILED`      | Batch processing failed                                      |
| `CANCELLED`   | Batch was cancelled                                          |

### 5. Retrieve the results

Once the batch is complete, you can download the output by making a request to retrieve the output file using the `output_file_id` field from the Batch object.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Get the batch status to find output_file_id
  batch = client.batches.get_batch("batch-xyz789")

  if batch.status == "COMPLETED":
      # Download the output file
      client.files.retrieve_content(
          id=batch_stat.output_file_id,
          output="batch_output.jsonl",
      )
  ```

  ```python Python(v2) theme={null}
  from together import Together

  client = Together()

  ## Get the batch status to find output_file_id
  batch = client.batches.retrieve("batch-xyz789")

  if batch.status == "COMPLETED":
      # Download the output file using streaming response
      with client.files.with_streaming_response.content(
          id=batch.output_file_id
      ) as response:
          with open("batch_output.jsonl", "wb") as f:
              for chunk in response.iter_bytes():
                  f.write(chunk)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  // The batch id from the previous step
  const batchInfo = await client.batches.retrieve(batchId);

  if (batchInfo.status === "COMPLETED" && batchInfo.output_file_id) {
    const resp = await client.files.content(batchInfo.output_file_id);
    const result = await resp.text();
    console.log(result);
  }
  ```
</CodeGroup>

The output `.jsonl` file will have one response line for every successful request line in the input file. Any failed requests will have their error information in a separate error file accessible via `error_file_id`.

Note that the output line order may not match the input line order. Use the `custom_id` field to map requests to results.

### 6. Cancel a batch

You can cancel a batch job as follows:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  # Cancel a specific batch by ID
  batch_id = "your-batch-id-here"
  cancelled_batch = client.batches.cancel_batch(batch_id)

  print(cancelled_batch)
  ```

  ```python Python(v2) theme={null}
  from together import Together

  client = Together()

  # Cancel a specific batch by ID
  batch_id = "your-batch-id-here"
  cancelled_batch = client.batches.cancel(batch_id)

  print(cancelled_batch)
  ```
</CodeGroup>

### 7. Get a list of all batches

At any time, you can see all your batches.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## List all batches
  batches = client.batches.list_batches()

  for batch in batches:
      print(batch)
  ```

  ```python Python(v2) theme={null}
  from together import Together

  client = Together()

  ## List all batches
  batches = client.batches.list()

  for batch in batches:
      print(batch)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const allBatches = await client.batches.list();

  for (const batch of allBatches) {
    console.log(batch);
  }
  ```
</CodeGroup>

## Model availability & Pricing

The following models are supported for batch processing:

| Model ID                                          | Discount |
| ------------------------------------------------- | -------- |
| deepseek-ai/DeepSeek-R1-0528-tput                 | 50%      |
| deepseek-ai/DeepSeek-V3                           | 50%      |
| meta-llama/Llama-3-70b-chat-hf                    | 50%      |
| meta-llama/Llama-3.3-70B-Instruct-Turbo           | 50%      |
| meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 50%      |
| meta-llama/Llama-4-Scout-17B-16E-Instruct         | 50%      |
| meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo     | 50%      |
| meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo      | 50%      |
| meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo       | 50%      |
| mistralai/Mistral-7B-Instruct-v0.1                | 50%      |
| mistralai/Mixtral-8x7B-Instruct-v0.1              | 50%      |
| Qwen/Qwen2.5-72B-Instruct-Turbo                   | 50%      |
| Qwen/Qwen2.5-7B-Instruct-Turbo                    | 50%      |
| Qwen/Qwen3-235B-A22B-fp8-tput                     | 50%      |
| openai/whisper-large-v3                           | 50%      |
| google/gemma-3n-E4B-it                            | 0%       |
| marin-community/marin-8b-instruct                 | 0%       |
| meta-llama/Meta-Llama-3-70B-Instruct-Turbo        | 50%      |
| Qwen/Qwen2.5-VL-72B-Instruct                      | 50%      |
| Qwen/Qwen3-235B-A22B-Instruct-2507-tput           | 0%       |
| togethercomputer/Refuel-Llm-V2                    | 0%       |
| togethercomputer/Refuel-Llm-V2-Small              | 0%       |
| Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8           | 0%       |
| openai/gpt-oss-120b                               | 0%       |
| zai-org/GLM-4.5-Air-FP8                           | 50%      |
| Qwen/Qwen3-235B-A22B-Thinking-2507                | 50%      |
| openai/gpt-oss-20b                                | 0%       |

## Rate limits

Batch API rate limits are separate from existing per-model rate limits. The Batch API has specific rate limits:

* **Max Token limits**: A maximum of 30B tokens can be ***enqueued per model***
* **Per-batch limits**: A single batch may include up to 50,000 requests
* **Batch file size**: Maximum 100MB per batch input file
* **Separate pool**: Batch API usage doesn't consume tokens from standard rate limits

## Error handling

When errors occur during batch processing, they are recorded in a separate error file accessible via the `error_file_id` field. Common error codes include:

| Error Code | Description            | Solution                               |
| ---------- | ---------------------- | -------------------------------------- |
| 400        | Invalid request format | Check JSONL syntax and required fields |
| 401        | Authentication failed  | Verify API key                         |
| 404        | Batch not found        | Check batch ID                         |
| 429        | Rate limit exceeded    | Reduce request frequency               |
| 500        | Server error           | Retry with exponential backoff         |

**Error File Format:**

```jsonl Jsonl theme={null}
{"custom_id": "req-1", "error": {"message": "Invalid model specified", "code": "invalid_model"}}
{"custom_id": "req-5", "error": {"message": "Request timeout", "code": "timeout"}}
```

## Best practices

### Optimal Batch Size

* Aim for 1,000-10,000 requests per batch for best performance
* Maximum 50,000 requests per batch
* Keep file size under 100MB

### Error Handling

* Always check the `error_file_id` for partial failures
* Implement retry logic for failed requests
* Use unique `custom_id` values for easy tracking

### Model Selection

* Choose models based on your quality/cost requirements
* Smaller models (7B-17B) for simple tasks
* Larger models (70B+) for complex reasoning

### Request Formatting

* Validate JSON before submission
* Use consistent schema across requests
* Include all required fields

### Monitoring

* Poll status endpoint every 30-60 seconds
* Set up notifications for completion (if available)

## FAQ

**Q: How long do batches take to complete?**\
A: Processing time depends on the batch size and model complexity. Most batch jobs typically complete (or partially complete) within 24 hours.

**Q: What should I do if my batch job has been**`IN_PROGRESS` **for more than 24 hours?**\
A: If your batch is scheduled on a particularly complex and/or popular model your job may not be able to be completed within the standard 24 hour time frame. In these cases we request that you wait at least 72 hours before contacting our support team. As long as the batch is still showing as being `IN_PROGRESS` it will be processed.

**Q: Can I cancel a running batch?**\
A: Currently, batches cannot be cancelled once processing begins.

**Q: Are results returned in the same order as requests?**\
A: No, results may be in any order. Use `custom_id` to match requests with responses.

**Q: Can I use the same file for multiple batches?**\
A: Yes, uploaded files can be reused for multiple batch jobs.

**Q: How are batch jobs billed?**\
A: Batch requests are billed when a succesful response is returned. If a batch job terminates early, or is cancelled, you will still be billed for all successful responses up to that point. You can find all successful responses are included in the resulting output\_file.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt