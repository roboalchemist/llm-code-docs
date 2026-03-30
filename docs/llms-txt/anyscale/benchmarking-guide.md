# Source: https://docs.anyscale.com/llm/serving/benchmarking/benchmarking-guide.md

# Benchmarking with Ray Serve LLM

[View Markdown](/llm/serving/benchmarking/benchmarking-guide.md)

# Benchmarking with Ray Serve LLM

When serving large language models (LLMs) in production, understanding how your deployment performs under load is critical. Benchmarking helps you measure throughput and latency so you can tune your system for both cost-efficiency and user experience. For detailed explanations of these metrics, see [Understand LLM latency and throughput metrics](/llm/serving/benchmarking/metrics.md).

This guide shows you how to benchmark LLMs deployed with Ray Serve LLM using the [built-in benchmarking tool from vLLM](https://docs.vllm.ai/en/stable/cli/bench/serve/). For additional context, examples, and advanced benchmarking workflows, see the [vLLM benchmark guide](https://docs.vllm.ai/en/stable/contributing/benchmarks/).

## Benchmark a deployment[​](#benchmark-a-deployment "Direct link to Benchmark a deployment")

You can simulate traffic against your deployed model and produce standardized performance metrics, allowing you to quickly evaluate how well your deployment handles different workloads.

The benchmarking tool works by:

* Sending prompts to your deployed model endpoint at a configurable rate and concurrency.
* Collecting responses and recording statistics such as throughput (req/s, tokens/s) and latency (TTFT, TPOT, ITL).
* Summarizing results in a standardized report you can compare across runs.

Use this benchmarking tool when you want to test how your deployment performs under realistic serving conditions, including request concurrency, traffic shaping, and end-to-end latency as experienced by clients.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Deploy your model and install vLLM with benchmarking tools:

```
pip install "vllm>=0.11.1"
```

See [Deploy LLMs](https://console.anyscale.com/template-preview/deployment-serve-llm) for examples on how to deploy models using Ray Serve LLM and Anyscale services.

note

To measure on a single replica, deploy with autoscaling turned off. Otherwise, autoscaling may launch additional replicas and skew the results.

```
# Example with the python sdk
llm_config = LLMConfig(
    ...,
    deployment_config=dict(
        autoscaling_config=dict(
            num_replicas=1 # Set to 1 replica only
        )
    ),
)
```

For guidance on benchmarking with autoscaling enabled, see [Benchmark with Ray Serve autoscaling](#benchmark-with-ray-serve-auto-scaling).

### Configure and run a benchmark[​](#configure-and-run-a-benchmark "Direct link to Configure and run a benchmark")

To benchmark your Ray Serve LLM deployment, you need to provide several parameters and set the appropriate tokens:

* `--model`: Hugging Face model ID. Must match the `model_source` field in your Ray Serve LLM config.
* `--served-model-name`: Name exposed by your deployment. Must match the `model_id` field in your Ray Serve LLM config.
* `--base-url`: Your service endpoint URL *without a trailing slash*.
* `export OPENAI_API_KEY`: Optional: Authentication token if your Anyscale service requires it.
* `export HF_TOKEN`: Optional: Hugging Face token when using gated models.

tip

If these parameters don't match, the benchmark fails to connect or download the right tokenizer to compute metrics.

For example, if your Ray Serve LLM config looks like this:

```
applications:
- args:
    llm_configs:
      - model_id: my-llama-3.1-8b
        model_source: meta-llama/Llama-3.1-8B-Instruct
```

And your service endpoint is:

```
Endpoint: https://my-service-abcd1234.anyscaleuserdata.com # Or http://127.0.0.1:8000 for local deployments
Authentication Token: XYZ
```

If applicable, set your service authentication token and Hugging Face token, then run the benchmark:

```
export OPENAI_API_KEY="XYZ"  # If authentication is required
export HF_TOKEN="<YOUR-HF-TOKEN>"  # For gated models like Meta's Llama 3 models

vllm bench serve \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --served-model-name my-llama-3.1-8b \
  --base-url https://my-service-abcd1234.anyscaleuserdata.com \ # no trailing slash
  ...
```

The benchmark returns a summary of the metrics collected:

```
============ Serving Benchmark Result ============
Successful requests:                     851       
Benchmark duration (s):                  622.99    
Total input tokens:                      869049    
Total generated tokens:                  104230    
Request throughput (req/s):              1.37      
Output token throughput (tok/s):         167.30    
Total Token throughput (tok/s):          1562.26   
---------------Time to First Token----------------
Mean TTFT (ms):                          297324.84 
Median TTFT (ms):                        298166.31 
P99 TTFT (ms):                           590867.00 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          160.37    
Median TPOT (ms):                        143.00    
P99 TPOT (ms):                           643.71    
---------------Inter-token Latency----------------
Mean ITL (ms):                           148.81    
Median ITL (ms):                         100.39    
P99 ITL (ms):                            694.74    
==================================================
```

For details on how to read the report output, see [Understand the report output](#understand-the-report-output).

### Advanced configuration[​](#advanced-configuration "Direct link to Advanced configuration")

Beyond the required parameters, you can customize many aspects of your benchmark such as workload patterns, traffic patterns, token lengths, dataset selection, and results logging. You can also define Service Level Objectives for goodput tracking and use custom datasets with your own prompts.

For detailed parameter descriptions, default values, and configuration examples, see the [vLLM benchmark CLI reference](https://docs.vllm.ai/en/stable/cli/bench/serve/) and the [vLLM benchmark guide](https://docs.vllm.ai/en/stable/contributing/benchmarks/).

## Understand the report output[​](#understand-the-report-output "Direct link to Understand the report output")

Each benchmarking run produces a report that summarizes how your model performed under the given load. See [Configure and run a benchmark](#configure-and-run-a-benchmark) for an example output. The results generally fall into three main categories:

* *Run summary*
  <br />
  <!-- -->
  Number of successful requests, total benchmark duration, and total input/output tokens processed.
* *Throughput metrics*
  <br />
  <!-- -->
  Requests per second and token throughput including input, output, or total tokens. These indicate overall system capacity. Results also include goodput metrics if set with `--goodput`.
* *Latency metrics*
  <br />
  <!-- -->
  Key measurements such as *TTFT*, *TPOT*, and *ITL*, which capture responsiveness and smoothness of token generation.

> For precise definitions and details of each metric, see [Understand LLM latency and throughput metrics](/llm/serving/benchmarking/metrics.md).

### Interpret results[​](#interpret-results "Direct link to Interpret results")

* *Throughput vs. Latency*
  <br />
  <!-- -->
  If your goal is capacity planning, such as determining how many tokens per second your cluster can serve, you should focus on throughput metrics. If instead you aim to optimize user experience, such as reducing how long it takes for the first token to appear, then you should focus on latency metrics instead.
* *High TTFT* (Time to First Token)
  <br />
  <!-- -->
  Often suggests prefill bottlenecks (long inputs, inefficient batching, queuing latency, or insufficient GPU resources).
* *High ITL* (Inter-Token Latency)
  <br />
  <!-- -->
  Indicates delays between tokens, which can make streaming responses feel choppy. Common causes include aggressive batching, scheduler contention, inter-node latency, memory pressure, or insufficient KV cache due to a large batch size.

tip

Balance throughput and latency based on your use case. A system with high throughput but poor latency may hurt interactivity, while a system tuned only for latency may not scale well under load.

> For tuning strategies, see[](/llm/serving/performance-optimization.md)

## Benchmark LoRA deployments[​](#benchmark-lora-deployments "Direct link to Benchmark LoRA deployments")

First, deploy your service. For details on how to serve a multi-LoRA deployment using Ray Serve LLM or Anyscale services, see [Deploy multi-LoRA adapters on LLMs](/llm/serving/multi-lora.md).

If you’ve deployed your model with multiple adapters, use the `--lora-modules` flag with a space-separated list of adapter names you'd like to benchmark. Otherwise, by default, the benchmarking tool doesn't use any adapters.

```
vllm bench serve \
  ...
  --lora-modules adapter_name1 adapter_name2 adapter_name3
```

note

The adapter names must match the directory structure you defined in the cloud storage where you stored the adapter weights. See [Deploy multi-LoRA adapters on LLMs: Prepare LoRA adapter checkpoints](/llm/serving/multi-lora.md#prepare-lora-adapter-checkpoints) for more information.

To measure their combined performance, the benchmarking script simulates traffic across multiple adapters by randomly picking one of the specified adapters for each request.

## Benchmark with Ray Serve auto-scaling[​](#benchmark-with-ray-serve-auto-scaling "Direct link to Benchmark with Ray Serve auto-scaling")

Benchmark with the [Ray Serve autoscaler](https://docs.ray.io/en/latest/serve/autoscaling-guide.html) enabled to validate scale-out behavior, steady-state latency, and cost under realistic load.

For setup and tuning, see the [Advanced autoscaling guide](https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html), and consult [Tune parameters for LLMs on Anyscale services: Ray Serve autoscaling configuration](/llm/serving/parameter-tuning.md#ray-serve-autoscaling-configuration) for joint vLLM engine & Ray Serve auto-scaler recommendations.

## Benchmark on custom data[​](#benchmark-on-custom-data "Direct link to Benchmark on custom data")

You can benchmark with your own prompts instead of a built-in dataset.

Create a `.jsonl` file where each line is a JSON object containing a "prompt" field:

```
{"prompt": "Summarize the key points of the following text: <text here>."}
{"prompt": "What is the capital of France?"}
```

Set `--dataset-name` to `"custom"` and point to your .jsonl file with `--dataset-path`:

```
vllm bench serve \
  --dataset-name custom \
  --dataset-path ./datasets/custom_prompts.jsonl \
  ...
```

Helpful options:

* `--custom-output-len`: Max output tokens per request. Defaults to `256`.
* `--custom-skip-chat-template`: Don't apply the model's chat template to prompts. Defaults to `false`.

For examples of benchmarking with different dataset types including ShareGPT, Sonnet, and specialized datasets for testing features such as prefix caching or structured outputs, see the [vLLM benchmark examples](https://docs.vllm.ai/en/stable/contributing/benchmarks/#examples).

## Apply best practices[​](#apply-best-practices "Direct link to Apply best practices")

Follow these best practices when benchmarking your Ray Serve LLM deployment to ensure reliable and meaningful results:

### Warm up the system[​](#warm-up-the-system "Direct link to Warm up the system")

When benchmarking complex inference systems, consider running a short warm-up phase with `--num-warmups` before collecting measurements to avoid skew from initial model load times or cache misses.

### Run multiple trials[​](#run-multiple-trials "Direct link to Run multiple trials")

Repeat benchmarks and average the results to reduce noise from transient variability.

### Test different request rates and concurrency levels[​](#test-different-request-rates-and-concurrency-levels "Direct link to Test different request rates and concurrency levels")

Run `vllm bench serve` with various values of `--request-rate` and `--max-concurrency` to explore both low-load and high-load scenarios.

### Record your environment details[​](#record-your-environment-details "Direct link to Record your environment details")

Capture GPU type, number of replicas, and software versions to ensure results are reproducible.

### Handle variability in token outputs[​](#handle-variability-in-token-outputs "Direct link to Handle variability in token outputs")

For consistent runs, fix input and output lengths and set `--ignore-eos` to ensure all outputs are the same length. Benchmark on the [random dataset](https://docs.vllm.ai/en/stable/cli/bench/serve.html#random-dataset-options) for precise control over input and output token counts.

### Disable automatic prefix caching[​](#disable-automatic-prefix-caching "Direct link to Disable automatic prefix caching")

Caching can boost throughput and reduce latency depending on the prompt mix used in the benchmark. For a fair baseline, turn off [automatic prefix caching (APC)](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/) in your vLLM engine by setting `enable_prefix_caching=False` prior to deployment. Use `engine_kwargs` in your Ray Serve LLM config to forward engine parameters.

For example, using the Python SDK:

```
llm_config = LLMConfig(
    ...
    engine_kwargs=dict(enable_prefix_caching=False),
)
```

If your production traffic shares prefixes such as template-based prompts or RAG queries and you want to emulate that environment, keep automatic prefix caching enabled, which is the default, and run a benchmark on a prefix-sharing dataset. vLLM provides a ready-made [prefix-repetition dataset](https://docs.vllm.ai/en/stable/cli/bench/serve/#prefix-repetition-dataset-options) for this purpose. For a complete example of benchmarking with prefix caching, see the [vLLM prefix caching benchmark guide](https://docs.vllm.ai/en/stable/contributing/benchmarks/#prefix-caching-benchmark).

note

Ray Serve LLM includes a prefix cache-aware router. Enable it in your deployment to benchmark prefix-shared workloads. For details, see [Ray Serve: Reduce LLM Inference Latency by 60% with Custom Request Routing](https://www.anyscale.com/blog/ray-serve-faster-first-token-custom-routing).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

This section lists the most common failures you'll hit when benchmarking Ray Serve LLM with vLLM and how to fix them. Set `VLLM_LOGGING_LEVEL=DEBUG` to enable verbose logs for troubleshooting.

### `Waiting for endpoint to become up` with Anyscale services[​](#waiting-for-endpoint-to-become-up-with-anyscale-services "Direct link to waiting-for-endpoint-to-become-up-with-anyscale-services")

The message likely means there are issues sending requests to the service. Set the `OPENAI_API_KEY` environment variable to your Anyscale service authentication key and verify that `--base-url` points to your service endpoint with no trailing slash at the end

```
export OPENAI_API_KEY=<YOUR-AUTHENTICATION-KEY-HERE>
...
vllm bench serve ... --base-url <MY-SERVICE-ENDPOINT> # no trailing slash at the end
```

### `Cannot access gated repo`[​](#cannot-access-gated-repo "Direct link to cannot-access-gated-repo")

vLLM uses the model's tokenizer to count output tokens for latency metrics such as ITL and TPOT. If you use a gated model such as Meta's Llama 3, provide your Hugging Face token so the benchmarking tool can download the tokenizer:

```
export HF_TOKEN="<YOUR_HUGGING_FACE_TOKEN>"
```
