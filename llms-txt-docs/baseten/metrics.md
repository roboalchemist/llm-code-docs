# Source: https://docs.baseten.co/observability/metrics.md

# Metrics

> Understand the load and performance of your model

The Metrics tab in the model dashboard provides deployment-specific insights into model load and performance. Use the dropdowns to filter by environment or deployment and time range.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a81bbd59a02719c6814e62fdbfa89ec3" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/observability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=15a3fb2106b5f51cd50b261131541f01 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1aa2af207e9f007781838fbd8ca63f50 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=90b0499c358c033b78985f2e08386e2e 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e6dfb73381b1ac4f70a7299f473c2fe7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=537db025cbccafe7f54dbe0d99c736fe 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=daf4644abc87786401d3959d0f05d7d7 2500w" />

## Inference volume

Tracks the request rate over time, segmented by HTTP status codes:

* `2xx`: 🟢 Successful requests
* `4xx`: 🟡 Client errors
* `5xx`: 🔴 Server errors (includes model prediction exceptions)

<Note>
  Note that for non-HTTP models and Chains (WebSockets and gRPC), the status codes will
  reflect the status codes for those protocols.
</Note>

***

## Response time

Measured at different percentiles (p50, p90, p95, p99):

* **End-to-end response time:** Includes cold starts, queuing, and inference (excludes client-side latency). Reflects real-world performance.
* **Inference time:** Covers only model execution, including pre/post-processing. Useful for optimizing single-replica performance.
* **Time to first byte:** Measures the time-to-first-byte time distribution, including any queueing and routing time. A proxy for TTFT.

***

## Request and response size

Measured at different percentiles (p50, p90, p95, p99):

* **Request size:** Tracks the request size distribution. A proxy for input tokens.
* **Response size:** Tracks the response size distribution. A proxy for generated tokens.

***

## Replicas

Tracks the number of **active** and **starting** replicas:

* **Starting:** Waiting for resources or loading the model.
* **Active:** Ready to serve requests.
* For development deployments, a replica is considered active while running the live reload server.

***

## CPU usage and memory

Displays resource utilization across replicas. Metrics are averaged and may not capture short spikes.

### Considerations:

* **High CPU/memory usage**: May degrade performance—consider upgrading to a larger instance type.
* **Low CPU/memory usage**: Possible overprovisioning—switch to a smaller instance to reduce costs.

***

## GPU usage and memory

Shows GPU utilization across replicas.

* **GPU usage**: Percentage of time a kernel function occupies the GPU.
* **GPU memory**: Total memory used.

### Considerations:

* **High GPU load**: Can slow inference—check response time metrics.
* **High memory usage**: May cause out-of-memory failures.
* **Low utilization**: May indicate overprovisioning—consider a smaller GPU.

***

## Async Queue Metrics

* **Time in Async Queue**: Time spent in the async queue before execution (p50, p90, p95, p99).
* **Async Queue Size**: Number of queued async requests.

### Considerations:

* Large queue size indicates requests are queued faster than they are processed.
* To improve async throughput, increase the max replicas or adjust autoscaling concurrency.
