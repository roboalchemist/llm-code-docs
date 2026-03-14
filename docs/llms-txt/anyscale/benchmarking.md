# Source: https://docs.anyscale.com/llm/serving/benchmarking.md

# Benchmarking

[View Markdown](/llm/serving/benchmarking.md)

# Benchmarking

When you deploy LLMs to production, understanding how they perform under real-world conditions is critical for delivering responsive user experiences while managing costs effectively.

Ray Serve LLM integrates with vLLM's comprehensive benchmarking tools, making it straightforward to measure your deployment's throughput and latency. You can simulate realistic traffic patterns, test different configurations, and collect standardized metrics, all without building custom testing infrastructure. On Anyscale, you get additional benefits such as built-in Grafana dashboards for real-time monitoring and the ability to quickly scale your deployments for performance testing.

This section helps you understand the key performance metrics that matter for LLMs and shows you how to benchmark your Ray Serve LLM deployments effectively.

## Understand metrics[​](#understand-metrics "Direct link to Understand metrics")

Learn about the key performance metrics for LLMs, including latency (TTFT, ITL, TPOT, E2E), throughput (TPS, RPS), and goodput. Understanding these metrics helps you identify bottlenecks and make informed optimization decisions. See [Understand LLM latency and throughput metrics](/llm/serving/benchmarking/metrics.md).

## Benchmark your deployment[​](#benchmark-your-deployment "Direct link to Benchmark your deployment")

Use vLLM's benchmarking tools to measure your deployment's performance under realistic serving conditions. This guide shows you how to run benchmarks, configure workloads, interpret results, and test scenarios such as LoRA deployments and autoscaling. See [Benchmarking with Ray Serve LLM](/llm/serving/benchmarking/benchmarking-guide.md).

## Reference benchmarks[​](#reference-benchmarks "Direct link to Reference benchmarks")

For published benchmark data on Ray Serve LLM performance, including replica startup latency and throughput measurements, see [Ray Serve LLM Benchmarks](https://docs.ray.io/en/latest/serve/llm/benchmarks.html).
