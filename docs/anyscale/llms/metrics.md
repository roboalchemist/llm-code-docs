# Source: https://docs.anyscale.com/monitoring/metrics.md

# Source: https://docs.anyscale.com/llm/serving/benchmarking/metrics.md

# Understand LLM latency and throughput metrics

[View Markdown](/llm/serving/benchmarking/metrics.md)

# Understand LLM latency and throughput metrics

When you evaluate the performance of a Large Language Model (LLM), it's essential to consider not only the quality of its outputs but also its latency and throughput. These metrics are critical for understanding how efficiently and responsively a model can operate in production environments. Together, they provide a comprehensive view of system performance. To measure these metrics under realistic serving conditions, see [Benchmarking with Ray Serve LLM](/llm/serving/benchmarking/benchmarking-guide.md).

Depending on your use case and workload characteristics, some metrics may be more important than others. For example, interactive applications such as chatbots or coding assistants benefit most from low [time to first token (TTFT)](#time-to-first-token-ttft) and [inter-token latency (ITL)](#inter-token-latency-itl-and-time-per-output-token-tpot) to maintain a responsive feel. In contrast, large-scale batch processing or data generation pipelines might prioritize high [tokens per second (TPS)](#tokens-per-second-tps-or-token-throughput) or [requests per second (RPS)](#requests-per-second-rps) to maximize throughput and cost efficiency.

## Time to first token (TTFT)[​](#time-to-first-token-ttft "Direct link to Time to first token (TTFT)")

*Time to first token (TTFT)* refers to the time elapsed between submitting a prompt and receiving the first token of the model's response.

### Why TTFT matters[​](#why-ttft-matters "Direct link to Why TTFT matters")

TTFT is a key contributor to perceived responsiveness. A low TTFT makes the model feel fast and interactive, which is especially important in chat-based or real-time applications. Conversely, a high TTFT can create a sense of lag and degrade the user experience—even if the rest of the response is fast.

### What influences TTFT[​](#what-influences-ttft "Direct link to What influences TTFT")

Several factors can impact TTFT, including:

* **Prompt length**: Longer prompts typically result in longer TTFT because the model must first process the entire input before generating any output. During this phase, the model builds a *key-value (KV) cache*, which acts as its short-term memory for the session.
* **System load**: When the server is under heavy usage, it may queue incoming requests. This queuing delay adds to the TTFT and can vary depending on infrastructure, autoscaling behavior, and request prioritization.
* **Prefill step**: The prefill phase involves running the model over the entire input prompt to populate the KV cache. This step is compute-intensive and directly determines how quickly the model can begin generating the first token. See [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md).

## End-to-end latency[​](#end-to-end-latency "Direct link to End-to-end latency")

*End-to-end (E2E) latency* measures the total time from when the server receives a prompt to when it finishes sending the full response. It captures the entire duration of the interaction for a single query.

At a high level, end-to-end latency of a single request consists of two phases:

```
End-to-End Latency = Time to First Token + Total Generation Time
```

### Why end-to-end latency matters[​](#why-end-to-end-latency-matters "Direct link to Why end-to-end latency matters")

E2E latency reflects the complete waiting time experienced by the user. While TTFT indicates how quickly the model begins responding, E2E latency shows how long it takes to deliver the entire output. It's especially important for use cases that require full responses before taking further action, such as summarization, code generation, or batch inference.

### What influences E2E latency[​](#what-influences-e2e-latency "Direct link to What influences E2E latency")

E2E latency includes both the initial processing, or prefill phase, and the subsequent token-by-token generation, or decoding phase. You can decrease your E2E latency by optimizing for your [time to first token (TTFT)](#time-to-first-token-ttft) and your [inter-token latency (ITL)](#inter-token-latency-itl-and-time-per-output-token-tpot).

## Inter-token latency (ITL) and time per output token (TPOT)[​](#inter-token-latency-itl-and-time-per-output-token-tpot "Direct link to Inter-token latency (ITL) and time per output token (TPOT)")

Both *ITL* and *TPOT* describe how fast tokens come after generation starts. They ignore TTFT and focus on the "steady stream" instead.

For a single request, ITLs are the small gaps between tokens, while TPOT is simply the average of those gaps:

TPOT (1 request)=Avg(ITL)=#Output Tokens−1E2E latency−TTFT​

Across many requests, vLLM reports them differently: **average TPOT** is the simple mean of each request's TPOT (all requests weighted equally), while **average ITL** is token-weighted (all tokens weighted equally). For N requests:

Avg TPOT (N requests)=NTPOT1​+TPOT2​+⋯+TPOTN​​ Avg ITL (N requests)=#Output Tokens across requestsSum of all ITLs across requests​

note

The distinction between TPOT and ITL varies across the literature, and some sources treat them as equivalent. Since Ray Serve LLM uses vLLM as its backend, this guide adopts the definitions used in the vLLM benchmarking tool.

For example:

* Request A: 100 tokens at \~10 ms per token → TPOT ≈ 10 ms
* Request B: 2 tokens at \~50 ms per token → TPOT ≈ 50 ms
* **Avg TPOT** = (10 + 50) / 2 = **30 ms** (treats A and B equally)
* **Avg ITL** ≈ (100×10 + 2×50) / (100 + 2) = **\~10.8 ms** (weights by tokens)

tip

For simplicity, the example assumes a constant ITL for all tokens within a request. In practice, vLLM accurately sums each individual ITL per token and aggregates them for reporting.

### Why TPOT and ITL matter[​](#why-tpot-and-itl-matter "Direct link to Why TPOT and ITL matter")

TPOT, and its token-weighted counterpart ITL, capture the smoothness and speed of generation. Low, consistent values give a fluid real-time feel, while high or variable values make output appear in bursts, degrading chat or streaming UX.

### Which metric to use[​](#which-metric-to-use "Direct link to Which metric to use")

* Use **average TPOT** to compare per-request behavior when each request is equally important.
* Use **average ITL** to estimate the system's steady streaming speed across mixed-length traffic.

### What influences TPOT or ITL[​](#what-influences-tpot-or-itl "Direct link to What influences TPOT or ITL")

You can influence TPOT or ITL by tuning the decoding step. After the first token, the model generates tokens one at a time using the KV cache. This phase is memory-bound and may slow down if large prefills share the batch, competing for GPU compute and extending the model's forward pass. See [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md) for more information.

## Tokens per second (TPS) or token throughput[​](#tokens-per-second-tps-or-token-throughput "Direct link to Tokens per second (TPS) or token throughput")

*TPS* measures throughput, or how many output tokens the system generates each second. There are two important variants:

* **System TPS (overall throughput)**: The total number of tokens produced per second across **all concurrent users**. As load increases, system TPS rises until it reaches the infrastructure's maximum capacity.

  This metric reflects the raw processing capability of your deployment. If your system handles multiple requests concurrently, you can define your system TPS as:

  TPS=Tlast​−Tfirst​#Output Tokens​

  where Tfirst​ is the timestamp of the first request sent, and Tlast​ is the timestamp of the last response of the last request received.

* **User TPS**: The throughput a **single user** experiences. It's closely tied to **inter-token latency (ITL)**, because `TPS per User ≈ 1 / ITL` when the output sequence length is large. As concurrency increases, user TPS typically drops because the engine shares GPU and compute resources.

### Why TPS matters[​](#why-tps-matters "Direct link to Why TPS matters")

System TPS is a critical metric for capacity planning and cost forecasting, as it reflects the total processing capability of your deployment.

User TPS, on the other hand, directly impacts the perceived responsiveness for an individual user, making it an important measure of end-user experience.

### What influences TPS[​](#what-influences-tps "Direct link to What influences TPS")

Several factors influence both system-wide and per-user TPS, and there's often a trade-off between the two. Larger models have longer forward passes, reducing the number of tokens generated per second for both metrics. [Scaling infrastructure](#scale-infrastructure-to-improve-latency-and-throughput) can increase system TPS by handling more concurrent requests. See [inter-token latency (ITL)](#inter-token-latency-itl-and-time-per-output-token-tpot) for additional details on factors affecting user TPS.

## Requests per second (RPS)[​](#requests-per-second-rps "Direct link to Requests per second (RPS)")

*RPS* measures how many user prompts the system can complete each second. It reflects the system's ability to handle concurrent workloads and is especially important in applications with many users sending short, frequent queries.

RPS=Total Time in SecondsTotal Completed Requests​

### Why RPS matters[​](#why-rps-matters "Direct link to Why RPS matters")

RPS is a direct indicator of system capacity. A higher RPS means you can serve more users simultaneously without queuing delays. For workloads dominated by short interactions, such as chatbots, search queries, or API endpoints, RPS is often the most important performance metric for meeting demand.

### What influences RPS[​](#what-influences-rps "Direct link to What influences RPS")

* **Prompt and output length**: Shorter requests complete faster, increasing RPS; longer ones occupy resources longer, lowering it.
* **Concurrency and scheduling**: Higher concurrency can raise RPS by keeping the GPU busy, but excessive load may increase TTFT, ITL, and E2E latency.
* **Batching parameters**: Higher `max_num_seqs` batches more requests together, improving RPS at high load. Larger `max_num_batched_tokens` may favor TPS over RPS by prioritizing token throughput instead of request completion speed.

## Goodput[​](#goodput "Direct link to Goodput")

*Goodput* measures the percentage of requests that meet your defined Service Level Objectives (SLOs). While throughput metrics such as TPS and RPS tell you how much work the system is doing, goodput tells you how much of that work meets your quality standards.

Goodput=Total Requests#Requests Meeting All SLOs​×100%

You define goodput by setting latency thresholds for one or more metrics. For example, you might require that requests have a TTFT under 500ms, a TPOT under 15ms, and an E2E latency under 2 seconds. Goodput then reports what fraction of requests satisfy all these requirements.

Goodput bridges the gap between raw performance numbers and actual user satisfaction. A system might achieve high RPS or TPS, but if many requests violate latency SLOs, users experience poor service quality. This metric is especially valuable for SLA compliance, capacity planning while maintaining quality standards, and identifying when optimizations that increase raw throughput come at the cost of latency and user experience. As system load increases, latency typically degrades, causing goodput to drop even as raw throughput continues to rise.

## Understand percentiles (p50, p95, p99)[​](#understand-percentiles-p50-p95-p99 "Direct link to Understand percentiles (p50, p95, p99)")

Just looking at the average latency can be misleading and hide a wide range of experiences where a few very slow responses mask many fast ones. This is where percentiles come in and help you understand the experience for not just the "typical" user, but also the "unlucky" ones.

* **p50 (the median)**: This is the typical experience. 50% of users have a latency this fast or faster.
* **p95**: This is the experience for the "unlucky" 5%. It's a common metric for setting service level agreements (SLAs), as it focuses on eliminating all but the most extreme outlier cases.
* **p99**: This represents a near worst-case scenario. 99% of users have a better experience than this. If your p99 latency meets your requirements, your system is very consistent.

By tracking p95 or p99 latency, you ensure that almost everyone using your service has a reliable and acceptably fast experience, not just the "average" user.

## Scale infrastructure to improve latency and throughput[​](#scale-infrastructure-to-improve-latency-and-throughput "Direct link to Scale infrastructure to improve latency and throughput")

Several infrastructure-level factors influence all latency and throughput metrics, regardless of whether you're optimizing for TTFT, ITL, TPS, or RPS. Addressing these shared factors ensures you improve system performance holistically rather than in isolation.

* **Hardware performance**: Faster GPUs (for example, A100, H100) and optimized inference kernels reduce per-token computation time, improving every latency metric and boosting both TPS and RPS. When sharding models across multiple GPUs or nodes, choose hardware with high-speed interconnects such as NVLink to minimize communication overhead.
* **Cluster size and replication**: Increasing the number of replicas and GPUs/nodes per replica expands total compute capacity, raising system TPS and RPS and helping maintain consistent user TPS under heavy load.

## Monitor with the Ray Serve LLM dashboard[​](#monitor-ray-serve-llm-dashboard "Direct link to Monitor with the Ray Serve LLM dashboard")

Ray Serve LLM ships with an LLM-specific Grafana dashboard that provides real-time visibility into key performance metrics. This helps you diagnose bottlenecks, validate optimizations, and monitor production workloads.

To enable it on Ray versions before 2.52.0, add the `log_engine_metrics` field to your **Serve LLM config**:

```
applications:
- args:
    llm_configs:
        ...
        log_engine_metrics: true
```

note

Starting with `ray>=2.52.0`, Ray enables `log_engine_metrics` by default.

You can access the dashboard with the following steps:

1. Navigate to your **Workspace** or **Service** page.
2. Open the **Metrics** tab.
3. Expand **"View on Grafana"**.
4. Select **"Serve LLM Dashboard"**.

The dashboard includes a range of metrics, such as:

* **Token throughput (TPS)**: Total tokens generated per second.
* **Time to first token (TTFT)**: Initial latency before the first token appears.
* **Time per output token (TPOT)**: Average time between tokens after the first.
* **End-to-end request latency**: Full request duration from submission to final token.
* **Request prefill and decode time**: Breakdown of time spent in prefill versus decode phases.
* **Peak TPS per model**: Highest observed throughput for each deployed model.
* Additional engine-level metrics for deeper performance analysis.

This built-in dashboard helps you connect the metrics in this guide to real operational data, enabling data-driven tuning of your Ray Serve LLM deployment. For measuring these metrics under controlled load conditions, see [Benchmarking with Ray Serve LLM](/llm/serving/benchmarking/benchmarking-guide.md).

## Summary[​](#summary "Direct link to Summary")

In this guide, you learned about the key latency and throughput metrics for LLMs, including TTFT, ITL/TPOT, E2E latency, TPS, RPS, and goodput. You learned why each metric matters, what factors influence them, and how to monitor and optimize these metrics in Ray Serve LLM for different workloads.
