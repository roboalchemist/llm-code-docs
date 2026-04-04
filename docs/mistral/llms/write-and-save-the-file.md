# Write and save the file
with open('batch_results.jsonl', 'wb') as f:
    f.write(output_file_stream.read())
```

  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript


const outputFileStream = await client.files.download({ fileId: retrievedJob.outputFile });

// Write the stream to a file
const writeStream = fs.createWriteStream('batch_results.jsonl');
outputFileStream.pipeTo(new WritableStream({
    write(chunk) {
      writeStream.write(chunk);
    },
    close() {
      writeStream.end();
    }
}));
```

  </TabItem>
  <TabItem value="curl" label="curl">

```bash
curl 'https://api.mistral.ai/v1/files/<uuid>/content' \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
```

  </TabItem>
</Tabs>

## List batch jobs
You can view a list of your batch jobs and filter them by various criteria, including:

- Status: `QUEUED`,
`RUNNING`, `SUCCESS`, `FAILED`, `TIMEOUT_EXCEEDED`, `CANCELLATION_REQUESTED` and `CANCELLED`
- Metadata: custom metadata key and value for the batch

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
list_job = client.batch.jobs.list(
    status="RUNNING",
    metadata={"job_type": "testing"}
)
```

  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript
const listJob = await client.batch.jobs.list({
    status: "RUNNING",
    metadata: {
        jobType: "testing"
    }
});
```

  </TabItem>
  <TabItem value="curl" label="curl">

```bash
curl 'https://api.mistral.ai/v1/batch/jobs?status=RUNNING&job_type=testing'\
--header 'x-api-key: $MISTRAL_API_KEY'
```

  </TabItem>
</Tabs>


## Request the cancellation of a batch job

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
canceled_job = client.batch.jobs.cancel(job_id=created_job.id)
```

  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript
const canceledJob = await mistral.batch.jobs.cancel({
  jobId: createdJob.id,
});
```

  </TabItem>
  <TabItem value="curl" label="curl">

```bash
curl -X POST https://api.mistral.ai/v1/batch/jobs/<jobid>/cancel \
--header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>
</Tabs>

## An end-to-end example

<details>
<summary><b>Example</b></summary>

```python


from io import BytesIO


from mistralai import File, Mistral


def create_client():
    """
    Create a Mistral client using the API key from environment variables.

    Returns:
        Mistral: An instance of the Mistral client.
    """
    return Mistral(api_key=os.environ["MISTRAL_API_KEY"])

def generate_random_string(start, end):
    """
    Generate a random string of variable length.

    Args:
        start (int): Minimum length of the string.
        end (int): Maximum length of the string.

    Returns:
        str: A randomly generated string.
    """
    length = random.randrange(start, end)
    return ' '.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

def print_stats(batch_job):
    """
    Print the statistics of the batch job.

    Args:
        batch_job: The batch job object containing job statistics.
    """
    print(f"Total requests: {batch_job.total_requests}")
    print(f"Failed requests: {batch_job.failed_requests}")
    print(f"Successful requests: {batch_job.succeeded_requests}")
    print(
        f"Percent done: {round((batch_job.succeeded_requests + batch_job.failed_requests) / batch_job.total_requests, 4) * 100}")


def create_input_file(client, num_samples):
    """
    Create an input file for the batch job.

    Args:
        client (Mistral): The Mistral client instance.
        num_samples (int): Number of samples to generate.

    Returns:
        File: The uploaded input file object.
    """
    buffer = BytesIO()
    for idx in range(num_samples):
        request = {
            "custom_id": str(idx),
            "body": {
                "max_tokens": random.randint(10, 1000),
                "messages": [{"role": "user", "content": generate_random_string(100, 5000)}]
            }
        }
        buffer.write(json.dumps(request).encode("utf-8"))
        buffer.write("\n".encode("utf-8"))
    return client.files.upload(file=File(file_name="file.jsonl", content=buffer.getvalue()), purpose="batch")


def run_batch_job(client, input_file, model):
    """
    Run a batch job using the provided input file and model.

    Args:
        client (Mistral): The Mistral client instance.
        input_file (File): The input file object.
        model (str): The model to use for the batch job.

    Returns:
        BatchJob: The completed batch job object.
    """
    batch_job = client.batch.jobs.create(
        input_files=[input_file.id],
        model=model,
        endpoint="/v1/chat/completions",
        metadata={"job_type": "testing"}
    )

    while batch_job.status in ["QUEUED", "RUNNING"]:
        batch_job = client.batch.jobs.get(job_id=batch_job.id)
        print_stats(batch_job)
        time.sleep(1)

    print(f"Batch job {batch_job.id} completed with status: {batch_job.status}")
    return batch_job


def download_file(client, file_id, output_path):
    """
    Download a file from the Mistral server.

    Args:
        client (Mistral): The Mistral client instance.
        file_id (str): The ID of the file to download.
        output_path (str): The path where the file will be saved.
    """
    if file_id is not None:
        print(f"Downloading file to {output_path}")
        output_file = client.files.download(file_id=file_id)
        with open(output_path, "w") as f:
            for chunk in output_file.stream:
                f.write(chunk.decode("utf-8"))
        print(f"Downloaded file to {output_path}")


def main(num_samples, success_path, error_path, model):
    """
    Main function to run the batch job.

    Args:
        num_samples (int): Number of samples to process.
        success_path (str): Path to save successful outputs.
        error_path (str): Path to save error outputs.
        model (str): Model name to use.
    """
    client = create_client()
    input_file = create_input_file(client, num_samples)
    print(f"Created input file {input_file}")

    batch_job = run_batch_job(client, input_file, model)
    print(f"Job duration: {batch_job.completed_at - batch_job.created_at} seconds")
    download_file(client, batch_job.error_file, error_path)
    download_file(client, batch_job.output_file, success_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Mistral AI batch job")
    parser.add_argument("--num_samples", type=int, default=100, help="Number of samples to process")
    parser.add_argument("--success_path", type=str, default="output.jsonl", help="Path to save successful outputs")
    parser.add_argument("--error_path", type=str, default="error.jsonl", help="Path to save error outputs")
    parser.add_argument("--model", type=str, default="codestral-latest", help="Model name to use")

    args = parser.parse_args()

    main(args.num_samples, args.success_path, args.error_path, args.model)
```
</details>

## FAQ

### Is the batch API available for all models?
Yes, batch API is available for all models including user fine-tuned models.

### Does the batch API affect pricing?
We offer a 50% discount on batch API. Learn more about our [pricing](https://mistral.ai/pricing#api-pricing).

### Does the batch API affect rate limits?
No

### What's the max number of requests in a batch?
Currently, there is a maximum limit of 1 million pending requests per workspace. This means you cannot submit a job with more than 1 million requests. Additionally, you cannot submit two jobs with 600,000 requests each at the same time. You would need to wait until the first job has processed at least 200,000 requests, reducing its pending count to 400,000. At that point, the new job with 600,000 requests would fit within the limit.

### What's the max number of batch jobs one can create?
Currently, there is no maximum limit.

### How long does the batch API take to process?
Processing speeds may be adjusted based on current demand and the volume of your request. Your batch results will only be accessible once the entire batch processing is complete.

Users can set `timeout_hours` when creating a job, which specifies the number of hours after which the job should expire. It defaults to 24 hours and should be lower than 7 days. A batch will expire if processing does not complete within the specified timeout.

### Can I view batch results from my workspace?
Yes, batches are specific to a workspace. You can see all batches and their results that were created within the workspace associated with your API key.

### Will batch results ever expire?
No, the results do not expire at this time.

### Can batches exceed the spend limit?
Yes, due to high throughput and concurrent processing, batches may slightly exceed your workspace's configured spend limit.


[Citations and References]
Source: https://docs.mistral.ai/docs/capabilities/citations_and_references

Citations enable models to ground their responses and provide references, making them a powerful feature for Retrieval-Augmented Generation (RAG) and agentic applications. This feature allows the model to provide the source of the information extracted from a document or chunk of data from a tool call.

Our models have been deeply trained to ground on documents and provide sources, with a built-in feature to extract references and citations.

## Code Example

To provide documents to the model, you can include the sources as a function call response.  
Below is an example of references, in this case from Wikipedia, using tool calls.

<details>
<summary><b>References Example</b></summary>
```json
{
  "0": {
    "url": "https://en.wikipedia.org/wiki/2024_Nobel_Peace_Prize",
    "title": "2024 Nobel Peace Prize",
    "snippets": [
      [
        "The 2024 Nobel Peace Prize, an international peace prize established according to Alfred Nobel's will, was awarded to Nihon Hidankyo (the Japan Confederation of A- and H-Bomb Sufferers Organizations), for their activism against nuclear weapons, assisted by victim/survivors (known as Hibakusha) of the atomic bombings of Hiroshima and Nagasaki in 1945.",
        "They will receive the prize at a ceremony on 10 December 2024 at Oslo, Norway."
      ]
    ],
    "description": null,
    "date": "2024-11-26T17:39:55.057454",
    "source": "wikipedia"
  },
  "1": {
    "url": "https://en.wikipedia.org/wiki/Climate_Change",
    "title": "Climate Change",
    "snippets": [
      [
        "Present-day climate change includes both global warming—the ongoing increase in global average temperature—and its wider effects on Earth’s climate system. Climate change in a broader sense also includes previous long-term changes to Earth's climate. The current rise in global temperatures is driven by human activities, especially fossil fuel burning since the Industrial Revolution. Fossil fuel use, deforestation, and some agricultural and industrial practices release greenhouse gases. These gases absorb some of the heat that the Earth radiates after it warms from sunlight, warming the lower atmosphere. Carbon dioxide, the primary gas driving global warming, has increased in concentration by about 50% since the pre-industrial era to levels not seen for millions of years."
      ]
    ],
    "description": null,
    "date": "2024-11-26T17:39:55.057454",
    "source": "wikipedia"
  },
  "2": {
    "url": "https://en.wikipedia.org/wiki/Artificial_Intelligence",
    "title": "Artificial Intelligence",
    "snippets": [
      [
        "Artificial intelligence (AI) refers to the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals. Such machines may be called AIs."
      ]
    ],
    "description": null,
    "date": "2024-11-26T17:39:55.057454",
    "source": "wikipedia"
  }
}
```
</details>

### Initialize Client

```python

from mistralai import Mistral, ToolMessage


api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
```

### Define the Tool
In this case, we will create a `get_information` tool that will return the references mentioned previously.

```python
get_information_tool = {
    "type": "function",
    "function": {
        "name": "get_information",
        "description": "Get information from external source.",
        "parameters": {}
    },
}

def get_information():
    return json.dumps(references)
```

### Set Up Chat History

```python
chat_history = [
    {
        "role": "system",
        "content": "Answer the user by providing references to the source of the information."
    },
    {
        "role": "user",
        "content": "Who won the Nobel Prize in 2024?"
    }
]
```

### Make the Initial Chat Request

```python
chat_response = client.chat.complete(
    model=model,
    messages=chat_history,
    tools=[get_information_tool],
)

if hasattr(chat_response.choices[0].message, 'tool_calls'):
    tool_call = chat_response.choices[0].message.tool_calls[0]
    chat_history.append(chat_response.choices[0].message)
    print(tool_call)
else:
    print("No tool call found in the response")
```

Output:
```
function=FunctionCall(name='get_information', arguments='{}') id='F4HiRgdZp' type=None index=0
```

### Handle Tool Call and Append Result

```python
result = get_information()

tool_call_result = ToolMessage(
    content=result,
    tool_call_id=tool_call.id,
    name=tool_call.function.name,
)