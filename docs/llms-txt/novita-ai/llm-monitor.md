# Source: https://novita.ai/docs/guides/llm-monitor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Monitoring

> Description of your new file.

Novita AI provides comprehensive monitoring metrics for the usage of large language model (LLM) APIs. These metrics help you gain deep insights into the availability and performance of your LLM API requests.

You can view the monitoring metrics on the [LLM Monitoring Page](https://novita.ai/models-console/llm-metrics).

## Metric Descriptions

<Note>
  All metrics are broken down by **model** and sampled at the **minute level**. However, depending on your selected time interval, samples may not be shown for every minute. In such cases, values will be averaged across the selected time range.
</Note>

* **Requests Per Minute (RPM)**

Displays the number of API requests sent per minute. This helps you understand usage patterns and the level of API concurrency.

* **Request Success Rate**

Shows the percentage of successful API responses per minute (non-5xx status codes), reflecting the API's availability.

* **Average Token Count per Request**

Displays the average number of input and output tokens per request per minute, which helps you monitor token consumption patterns.

* **End-to-End (E2E) Latency**

Shows the total time required for the model to generate a full response in each request per minute. Metrics include the 99th percentile, 95th percentile, and average latency.

* **Time to First Token (TTFT)**

<Note>
  Only tracked for streaming requests where stream=true.
</Note>

Displays the time it takes to process the prompt and generate the first output token in each request per minute. Includes the 99th percentile, 95th percentile, and average latency.

* **Time Per Output Token (TPOT)**

<Note>
  Only tracked for streaming requests where stream=true.
</Note>

Displays the average time between consecutive output tokens in each request per minute. Includes the 99th percentile, 95th percentile, and average latency.


Built with [Mintlify](https://mintlify.com).