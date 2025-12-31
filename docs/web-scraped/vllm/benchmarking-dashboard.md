# Source: https://docs.vllm.ai/en/stable/benchmarking/dashboard/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/benchmarking/dashboard.md "Edit this page")

# Performance Dashboard[¶](#performance-dashboard "Permanent link")

The performance dashboard is used to confirm whether new changes improve/degrade performance under various workloads. It is updated by triggering benchmark runs on every commit with both the `perf-benchmarks` and `ready` labels, and when a PR is merged into vLLM.

The results are automatically published to the public [vLLM Performance Dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm).

## Manually Trigger the benchmark[¶](#manually-trigger-the-benchmark "Permanent link")

Use [vllm-ci-test-repo images](https://gallery.ecr.aws/q9t5s3a7/vllm-ci-test-repo) with vLLM benchmark suite. For CPU environment, please use the image with \"-cpu\" postfix.

Here is an example for docker run command for CPU.

    docker run -it --entrypoint /bin/bash -v /data/huggingface:/root/.cache/huggingface  -e HF_TOKEN=''  --shm-size=16g --name vllm-cpu-ci  public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:1da94e673c257373280026f75ceb4effac80e892-cpu

Then, run below command inside the docker instance.

    bash .buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh

When run, benchmark script generates results under **benchmark/results** folder, along with the benchmark_results.md and benchmark_results.json.

### Runtime environment variables[¶](#runtime-environment-variables "Permanent link")

-   `ON_CPU`: set the value to \'1\' on Intel® Xeon® Processors. Default value is 0.
-   `SERVING_JSON`: JSON file to use for the serving tests. Default value is empty string (use default file).
-   `LATENCY_JSON`: JSON file to use for the latency tests. Default value is empty string (use default file).
-   `THROUGHPUT_JSON`: JSON file to use for the throughout tests. Default value is empty string (use default file).
-   `REMOTE_HOST`: IP for the remote vLLM service to benchmark. Default value is empty string.
-   `REMOTE_PORT`: Port for the remote vLLM service to benchmark. Default value is empty string.

For more results visualization, check the [visualizing the results](https://github.com/intel-ai-tce/vllm/blob/more_cpu_models/.buildkite/nightly-benchmarks/README.md#visualizing-the-results).

More information on the performance benchmarks and their parameters can be found in [Benchmark README](https://github.com/intel-ai-tce/vllm/blob/more_cpu_models/.buildkite/nightly-benchmarks/README.md) and [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] performance benchmark description](https://github.com/vllm-project/vllm/blob/main/.buildkite/performance-benchmarks/performance-benchmarks-descriptions.md).

## Continuous Benchmarking[¶](#continuous-benchmarking "Permanent link")

The continuous benchmarking provides automated performance monitoring for vLLM across different models and GPU devices. This helps track vLLM\'s performance characteristics over time and identify any performance regressions or improvements.

### How It Works[¶](#how-it-works "Permanent link")

The continuous benchmarking is triggered via a [GitHub workflow CI](https://github.com/pytorch/pytorch-integration-testing/actions/workflows/vllm-benchmark.yml) in the PyTorch infrastructure repository, which runs automatically every 4 hours. The workflow executes three types of performance tests:

-   **Serving tests**: Measure request handling and API performance
-   **Throughput tests**: Evaluate token generation rates
-   **Latency tests**: Assess response time characteristics

### Benchmark Configuration[¶](#benchmark-configuration "Permanent link")

The benchmarking currently runs on a predefined set of models configured in the [vllm-benchmarks directory](https://github.com/pytorch/pytorch-integration-testing/tree/main/vllm-benchmarks/benchmarks). To add new models for benchmarking:

1.  Navigate to the appropriate GPU directory in the benchmarks configuration
2.  Add your model specifications to the corresponding configuration files
3.  The new models will be included in the next scheduled benchmark run

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 28, 2025] ]