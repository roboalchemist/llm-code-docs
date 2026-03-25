<!-- Source: https://docs.verda.com/containers/batching-and-streaming.md -->

# Batching and Streaming

## Batching

In the scaling section, you can control the number of concurrent requests. While most diffusion-based models support only one request at a time, Language Models (LLMs) can efficiently handle multiple concurrent requests.

By default, the number of concurrent requests is set to 1, with a maximum of 100 concurrent requests per replica.

Modern LLM engines are optimized for batching requests, with minimal performance impact. Taking advantage of batching can significantly improve throughput.

Our benchmarks using [text-generation-inference](https://github.com/huggingface/text-generation-inference) demonstrate that token throughput can increase up to 20x with batching, while maintaining reasonable latency.

Below is a benchmark table showing median processing times for different batch sizes. While this data is from an older LLM, the pattern remains consistent across different models.

Note: Output was limited to 100 tokens per request.

| Batch Size | Total time (ms) | Tokens produced |
| ---------- | --------------- | --------------- |
| 1          | 1776            | 100             |
| 2          | 1981            | 200             |
| 4          | 2067            | 400             |
| 8          | 3767            | 800             |
| 16         | 4431            | 1600            |
| 32         | 4942            | 3200            |

The results show that batch sizes of 4 concurrent requests have minimal impact on latency, making them ideal for real-time applications.

For batch processing jobs, maximum efficiency (in tokens per $/€) is achieved with larger batch sizes (32 or more concurrent requests, up to 100 if supported). Note that your specific model's token limits and inference engine capabilities may restrict the maximum number of concurrent requests.

## Streaming

For LLM models, we support streaming for real-time applications. Streaming is not recommended for batch jobs.

Streaming works when the inference server supports Server-Sent Events (SSE). We have tested and support [text-generation-inference](https://github.com/huggingface/text-generation-inference) and [vllm](https://github.com/vllm-project/vllm).

To enable streaming, you need to set the SSE standard headers in the request. Receiving these headers will instruct TGI and VLLM to stream the response.

```http
Accept: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

Depending on your code used to call the API, you may need to set additional options. Below is an example of how to call the API using Python and the `requests` library, which requires the `stream=True` option:

```python
import requests
import json
import sys
import os

def generate_text(prompt):
    url = "https://containers.datacrunch.io/vllm-deepseek/v1/completions"

    payload = {
    "model": "deepseek-ai/deepseek-llm-7b-chat",
    "prompt": prompt,
    "max_tokens": 200,
    "temperature": 0.7,
    "stream": True
    }

    # Get token from environment variable - this is a your Inference API key you can get from cloud.datacrunch.io in the 'keys' section
    token = os.getenv('DATACRUNCH_TOKEN')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/event-stream',
        'Authorization': f'Bearer {token}',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }

    try:
        # Make POST request to the API with stream=True
        response = requests.post(url, json=payload, headers=headers, stream=True)
        response.raise_for_status()

        full_text = ""
        for line in response.iter_lines():

            if line:
                line = line.decode('utf-8')

                if line.startswith('data:'):
                    data = line[5:]  # Remove 'data: ' prefix
                    if data == '[DONE]':
                        break
                    try:
                        event_data = json.loads(data)
                        token_text = event_data['choices'][0]['text']

                        full_text += token_text
                        # Print token immediately to show progress
                        print(token_text, end='', flush=True)
                    except json.JSONDecodeError:
                        print("xxx")
                        continue

        print()
        return full_text

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}", file=sys.stderr)
        return None

def main():

    input_data = {
        "prompt": "Write a long story about a robot learning to paint."
    }

    result = generate_text(input_data['prompt'])

    if result:
        print("\nFull response:")
        print(json.dumps({'response': result}, indent=2))
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
```
