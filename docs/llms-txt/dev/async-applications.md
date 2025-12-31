# Source: https://dev.writer.com/home/async-applications.md

# Run agents asynchronously

> Process no-code agent requests asynchronously or in batches with the async applications API. Generate content for multiple items efficiently.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>

With asynchronous agents, your team can build and deploy [no-code agents in AI Studio](/no-code/introduction) and use the [async applications API](/api-reference/application-api/generate-application-job) to generate content asynchronously or in batches.

For example, your product team can build a no-code agent that creates product description pages, and then you can use the async applications API to generate pages in batches for multiple products.

This guide helps you understand how to run async jobs. The API is similar to the [applications API](/home/applications), but it allows you to process batches of requests asynchronously.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Endpoint overview

**URL:** `POST https://api.writer.com/v1/applications/{application_id}/jobs`

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.writer.com/v1/applications/<application-id>/jobs' \
  -X POST \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $WRITER_API_KEY" \
  --data-raw '{
    "inputs": [
      {
        "id": "Input name",
        "value": [
          "Input value"
        ]
      }
    ]
  }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  job_response = client.applications.jobs.create(
      application_id="<application-id>",
      inputs=[
          {
              "id": "Input name",
              "value": [
                  "Input value"
              ]
          }
      ]
  )
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.applications.jobs.create(
    "<application-id>",
    {
      inputs: [
        {
          id: "Input name",
          value: [
            "Input value"
          ]
        }
      ]
    }
  )
  ```
</CodeGroup>

### Path parameters

| Parameter        | Type     | Description                 |
| ---------------- | -------- | --------------------------- |
| `application_id` | `string` | The ID of the no-code agent |

### Request body

The async applications API has the same request body structure as the [no-code agents API](/home/applications#request-body). It should contain an array of input objects matching the no-code agent's input schema.

### Response format

A successful job creation request returns a JSON object with the following structure:

| Parameter    | Type     | Description                                                            |
| ------------ | -------- | ---------------------------------------------------------------------- |
| `job_id`     | `string` | The ID of the job                                                      |
| `status`     | `string` | The status of the job. Can be `in_progress`, `completed`, or `failed`. |
| `created_at` | `string` | The date and time the job was created                                  |

```json  theme={null}
{
  "job_id": "123-456-789",
  "status": "in_progress",
  "created_at": "2024-03-15T10:00:00Z"
}
```

## Usage example

The following example demonstrates using the async applications API to generate content asynchronously with a hypothetical product description generation agent.

### Create and deploy a no-code agent

First, create and deploy a no-code agent in [AI Studio](https://app.writer.com/aistudio). If you don't already have a no-code agent, follow the [text generation guide](/no-code/text-generation) to get started.

### Create an async job

Send a `POST` request with the inputs for the agent to create an async job.

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.writer.com/v1/applications/<application-id>/jobs' \
  -X POST \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $WRITER_API_KEY" \
  --data-raw '{
    "inputs": [
      {
        "id": "Product descriptions",
        "value": [
          "Terra running shoe",
          "Aqua swim goggles",
          "Flex yoga mat"
        ]
      }
    ]
  }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  job = client.applications.jobs.create(
      application_id="<application-id>",
      inputs=[
          {
              "id": "Product descriptions",
              "value": [
                  "Terra running shoe",
                  "Aqua swim goggles",
                  "Flex yoga mat"
              ]
          }
      ],
  )
  print(f"Created job: {job.id}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const job = await client.applications.jobs.create(
    "<application-id>",
    {
      inputs: [
        {
          id: "Product descriptions",
          value: [
            "Terra running shoe",
            "Aqua swim goggles",
            "Flex yoga mat"
          ]
        }
      ]
    }
  );
  console.log(`Created job: ${job.id}`);
  ```
</CodeGroup>

### Check job status

Use the job ID from the creation response to check the status of your job and see the results.

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.writer.com/v1/applications/jobs/<job-id>' \
  -H "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  job_status = client.applications.jobs.retrieve("<job-id>")
  print(f"Job status: {job_status.status}")
  if job_status.status == "completed":
      print(f"Job results: {job_status.data.suggestion}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const jobStatus = await client.applications.jobs.retrieve("<job-id>");
  console.log(`Job status: ${jobStatus.status}`);
  if (jobStatus.status === "completed") {
    console.log(`Job results: ${jobStatus.data.suggestion}`);
  }
  ```
</CodeGroup>

The response includes the current status. If the job has completed, the results are in the `data.suggestion` field, which has the same structure as the [no-code agents API](/home/applications#response-format).

```json  theme={null}
{
    "id": "123-456-789",
    "status": "completed",
    "application_id": "2932402-23429023894-234234234",
    "created_at": "2025-02-10T18:18:09.501223Z",
    "completed_at": "2025-02-10T18:18:14.470324Z",
    "data": {
        "title": "Social post",
        "suggestion": "# Social post\nImage: A photo of a person running in a pair of Terra running shoes.\n\nCaption:\n\nIntroducing the all-new Terra running shoe, designed to take you further than ever before. With its innovative cushioning system and durable outsole, the Terra is perfect for runners of all levels.\n\nWhether you're hitting the trails or pounding the pavement, the Terra will keep you comfortable and supported mile after mile. So what are you waiting for? Lace up a pair of Terras and start your journey today!\n\n#TerraRunningShoe #RunFurther #NeverStopExploring #GetOutside"
    },
    "error": null
}
```

### List all jobs

You can retrieve all jobs for an application to monitor batch processing:

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.writer.com/v1/applications/<application-id>/jobs' \
  -H "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  jobs = client.applications.jobs.list(
      application_id="<application-id>"
  )
  for job in jobs.result:
      print(f"Job {job.id}: {job.status}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const jobs = await client.applications.jobs.list(
    "<application-id>"
  );
  jobs.result.forEach(job => {
    console.log(`Job ${job.id}: ${job.status}`);
  });
  ```
</CodeGroup>

### Retry failed jobs

If a job fails, you can retry it using the retry endpoint:

<CodeGroup>
  ```bash cURL theme={null}
  curl 'https://api.writer.com/v1/applications/jobs/<failed-job-id>/retry' \
  -X POST \
  -H "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  retry_response = client.applications.jobs.retry("<failed-job-id>")
  print(f"Retried job: {retry_response.id}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const retryResponse = await client.applications.jobs.retry("<failed-job-id>");
  console.log(`Retried job: ${retryResponse.id}`);
  ```
</CodeGroup>

## Next steps

By following this guide, you can use the async Applications API to handle large-scale tasks.

Next, learn how to enhance your no-code agents with [Knowledge Graph](/home/knowledge-graph), our tool for RAG.
